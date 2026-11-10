"""Persist verified ZOMBIE security reports beside PlumMe state, outside quality feedback."""
from __future__ import annotations

import hashlib
import json
import os
import stat
from pathlib import Path

from zombie_independent_verifier import canonical, verify_report


class IntegrationError(ValueError):
    pass


class PlumMeSecurityResults:
    """Separate durable security-results stream; never feeds cognitive utility or route health."""

    def __init__(self, state_dir: str | Path):
        self.path = Path(state_dir) / "zombie_security_results.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def accept(self, report: dict, verifier_key: bytes, *, fence=None, lease_id: str | None = None) -> dict:
        if not verify_report(report, verifier_key):
            raise IntegrationError("invalid verifier signature")
        model = report.get("model_identity")
        if not isinstance(report.get("run_id"), str) or not report["run_id"] or not isinstance(model, dict):
            raise IntegrationError("missing run/model identity")
        if report.get("assessment_status") not in {"VERIFIED", "VERIFIED_FAILURE"}:
            raise IntegrationError("assessment is not complete")
        if (fence is None) != (lease_id is None):
            raise IntegrationError("lease fence and lease id must be supplied together")
        row = {"run_id": report["run_id"], "report_id": report["report_id"],
               "model_identity": model, "assessment_status": report["assessment_status"],
               "report": report, "report_sha256": hashlib.sha256(canonical(report)).hexdigest()}
        encoded = canonical(row) + b"\n"
        flags = os.O_WRONLY | os.O_CREAT | os.O_APPEND
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        fd = os.open(self.path, flags, 0o600)
        try:
            info = os.fstat(fd)
            if not stat.S_ISREG(info.st_mode) or stat.S_IMODE(info.st_mode) & 0o077:
                raise IntegrationError("security-results file must be a private regular file")
            with os.fdopen(fd, "ab") as stream:
                fd = -1
                stream.write(encoded)
                stream.flush()
                os.fsync(stream.fileno())
        finally:
            if fd >= 0:
                os.close(fd)
        if fence is not None:
            fence.settle(lease_id, "DONE", report["report_id"])
        return {"run_id": row["run_id"], "report_id": row["report_id"],
                "report_sha256": row["report_sha256"], "path": str(self.path)}

    def read(self, run_id: str) -> dict:
        if not self.path.exists():
            raise KeyError(run_id)
        found = None
        with self.path.open(encoding="utf-8") as stream:
            for line in stream:
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise IntegrationError("corrupt security-results stream") from exc
                if row.get("run_id") == run_id:
                    if found is not None and found != row:
                        raise IntegrationError("conflicting reports for run")
                    found = row
        if found is None:
            raise KeyError(run_id)
        if hashlib.sha256(canonical(found["report"])).hexdigest() != found.get("report_sha256"):
            raise IntegrationError("stored report digest mismatch")
        return found
