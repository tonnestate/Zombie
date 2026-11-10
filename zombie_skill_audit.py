"""Project ZOMBIE: read-only static triage of untrusted agent skill packages.

Findings are *indicators*, not proof of malicious intent or runtime compromise.
Never imports, downloads, installs, or executes files in the scanned directory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

MAX_FILES = 200
MAX_SINGLE_FILE_BYTES = 512_000
MAX_TOTAL_BYTES = 5_000_000

CHECKS = (
    ("role_spoofing", "HIGH", r"(?:\[im_start\]\s*system|<system(?:\s|>)|\[SYSTEM[-_ ]MESSAGE\]|ignore\s+(?:all\s+)?(?:prior|previous|user|developer|system)\s+(?:instructions|requests)|override\s+(?:the\s+)?(?:system|developer)\s+instructions)"),
    ("concealment_instruction", "HIGH", r"(?:do\s+not\s+(?:tell|inform|notify|reveal|disclose)\s+(?:the\s+)?user|hide\s+(?:this|the\s+action|the\s+change)\s+from\s+(?:the\s+)?user|without\s+the\s+user(?:'s)?\s+(?:knowledge|consent))"),
    ("credential_exposure_instruction", "CRITICAL", r"(?:\b(?:api[_ -]?key|secret|password|access[_ -]?token|\.env|private[_ -]?key|credentials)\b.{0,90}\b(?:send|post|upload|transmit|export|email)\b|\b(?:send|post|upload|transmit|email)\b.{0,90}\b(?:api[_ -]?key|secret|password|access[_ -]?token|credentials)\b)"),
    ("remote_script_execution", "CRITICAL", r"(?:\b(?:curl|wget)\b[^\n|]{0,250}\|\s*(?:sudo\s+)?(?:bash|sh)\b|\b(?:Invoke-Expression|iex)\b.{0,180}(?:DownloadString|Invoke-WebRequest|iwr)\b)"),
    ("authority_escalation", "HIGH", r"(?:treat\s+.{0,70}\s+as\s+(?:system|developer|trusted)\s+(?:instructions|authority)|bypass\s+(?:the\s+)?(?:policy|approval|sandbox|permissions)|grant\s+(?:yourself|the\s+agent)\s+(?:admin|root))"),
    ("privileged_system_change", "HIGH", r"(?:\b(?:sudo\s+)?(?:crontab|systemctl|schtasks)\b|\b(?:chmod\s+777|setenforce\s+0)\b)"),
)
COMPILED = tuple((label, severity, re.compile(pattern, re.IGNORECASE)) for label, severity, pattern in CHECKS)
EXTRAS = {".md", ".txt", ".py", ".js", ".ts", ".sh", ".ps1", ".json", ".yaml", ".yml", ".toml", ".cfg", ".ini"}
SKILL_FILES = {"SKILL.md", "skill.md"}


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _finding(path: str, line: int | None, indicator: str, severity: str, evidence: str, **extra) -> dict:
    # Never store raw matches; skill text may itself contain credentials.
    return {"path": path, "line": line, "indicator": indicator, "severity": severity,
            "evidence_sha256": _sha(evidence.encode("utf-8")), **extra}


def audit_skill(root: Path, *, approved_manifest: dict[str, str] | None = None) -> dict:
    root = root.resolve(strict=True)
    if not root.is_dir() or not any((root / p).is_file() for p in SKILL_FILES):
        raise ValueError("Target must be a skill directory containing SKILL.md")
    if approved_manifest is not None:
        if not isinstance(approved_manifest, dict) or not all(
            isinstance(k, str) and k and not k.startswith("/") and ".." not in Path(k).parts
            and isinstance(v, str) and re.fullmatch(r"[a-f0-9]{64}", v)
            for k, v in approved_manifest.items()
        ):
            raise ValueError("Approved manifest must map safe relative paths to SHA-256 digests")
    findings, scanned, digests = [], [], {}
    total = 0
    count = 0
    paths = sorted(root.rglob("*"))
    for file in paths:
        rel = file.relative_to(root).as_posix()
        if file.is_symlink():
            findings.append(_finding(rel, None, "symlink_requires_review", "HIGH", rel))
            continue
        if not file.is_file():
            continue
        count += 1
        if count > MAX_FILES:
            raise ValueError("Skill exceeds file scan limit")
        size = file.stat().st_size
        total += size
        if total > MAX_TOTAL_BYTES:
            raise ValueError("Skill exceeds total byte scan limit")
        if size > MAX_SINGLE_FILE_BYTES:
            findings.append(_finding(rel, None, "oversized_unscanned_file", "HIGH", str(size)))
            scanned.append({"path": rel, "bytes": size, "status": "NOT_SCANNED_TOO_LARGE"})
            continue
        data = file.read_bytes()
        digests[rel] = _sha(data)
        if (file.suffix.lower() not in EXTRAS and file.name not in SKILL_FILES
                and file.name.lower() not in {"license", "copying", "notice", "authors"}):
            scanned.append({"path": rel, "bytes": len(data), "status": "NON_TEXT_REVIEW_REQUIRED"})
            findings.append(_finding(rel, None, "non_text_payload", "REVIEW", rel))
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            findings.append(_finding(rel, None, "non_utf8_content", "REVIEW", rel))
            scanned.append({"path": rel, "bytes": len(data), "status": "NON_UTF8_REVIEW_REQUIRED"})
            continue
        scanned.append({"path": rel, "bytes": len(data), "status": "SCANNED"})
        is_license = file.name.lower() in {"license", "license.md", "license.txt", "copying", "copying.md"}
        for line_no, line in enumerate(text.splitlines(), 1):
            for label, severity, pattern in COMPILED:
                if pattern.search(line):
                    findings.append(_finding(rel, line_no, label, severity, line))
                    if is_license and label in {"role_spoofing", "concealment_instruction", "authority_escalation"}:
                        findings.append(_finding(rel, line_no, "license_as_agent_instructions", "HIGH", line))
            if any(
                ord(char) in (0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF)
                or 0x202A <= ord(char) <= 0x202E
                or 0x2066 <= ord(char) <= 0x2069
                for char in line
            ):
                findings.append(_finding(rel, line_no, "invisible_unicode_control", "REVIEW", line))
    if approved_manifest is not None:
        for rel in sorted(set(approved_manifest) | set(digests)):
            if rel not in digests:
                findings.append(_finding(rel, None, "approved_file_missing", "HIGH", rel))
            elif rel not in approved_manifest:
                findings.append(_finding(rel, None, "file_added_after_approval", "HIGH", rel))
            elif approved_manifest[rel] != digests[rel]:
                findings.append(_finding(rel, None, "approved_digest_changed", "HIGH", rel))
    return {
        "protocol": "ZOMBIE-SKILL-TRIAGE/1",
        "classification": "REVIEW_REQUIRED" if findings else "NO_MATCHING_STATIC_INDICATORS",
        "malicious_intent_proven": False,
        "files_seen": count,
        "files": scanned,
        "manifest": digests,
        "findings": findings,
        "limitations": [
            "Regex indicators are neither proof of intent nor exhaustive detection.",
            "Quoted training examples and benign documentation may trigger false positives.",
            "Non-text contents, archives, dependencies and runtime behavior are not analyzed.",
            "A manifest comparison is meaningful only when the baseline was approved independently.",
            "This scanner never executes scripts or loads a skill into a real agent.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only static skill triage; no code execution")
    parser.add_argument("skill_directory", type=Path)
    parser.add_argument("--approved-manifest", type=Path)
    parser.add_argument("--report", type=Path, default=Path("zombie-skill-audit.json"))
    args = parser.parse_args()
    try:
        trusted = None
        if args.approved_manifest:
            payload = json.loads(args.approved_manifest.read_text("utf-8"))
            trusted = payload["manifest"] if isinstance(payload, dict) and "manifest" in payload else payload
        report = audit_skill(args.skill_directory, approved_manifest=trusted)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        parser.exit(2, f"Skill audit refused: {exc}\n")
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print(f"{report['classification']}: {len(report['findings'])} indicators, "
          f"{report['files_seen']} files assessed; details in {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
