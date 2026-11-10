"""ZOMBIE: geometric hygiene of sequential repair deltas.

Offline, read-only analysis. Never executes a model, installs an adapter or
modifies a checkpoint. Vector geometry does NOT establish model safety, task
improvement or even a real deployed intervention.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

PROTOCOL = "ZOMBIE-VECTOR-HYGIENE/1"
KINDS = {"activation_delta", "effective_weight_delta"}
MAX_REPAIRS = 10
MAX_DIMENSIONS = 16384


class VectorEvidenceError(ValueError):
    pass


def _hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"),
                   ensure_ascii=False, allow_nan=False).encode("utf-8")
    ).hexdigest()


def _nonempty(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise VectorEvidenceError(f"missing {field}")
    return value


def _vector(values: object, dimension: int | None) -> tuple[float, ...]:
    if not isinstance(values, list) or not 1 <= len(values) <= MAX_DIMENSIONS:
        raise VectorEvidenceError("vector must be a bounded list of finite numbers")
    if dimension is not None and len(values) != dimension:
        raise VectorEvidenceError("different vector coordinate dimensions")
    if any(type(x) not in (int, float) or not math.isfinite(x) for x in values):
        raise VectorEvidenceError("non-finite or non-numeric coordinate")
    v = tuple(float(x) for x in values)
    norm = math.hypot(*v)
    if not 1e-100 <= norm <= 1e100:
        raise VectorEvidenceError("zero or numerically unbounded repair delta")
    return v


def _dot(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    return math.fsum(x * y for x, y in zip(a, b))


def analyze(payload: dict) -> dict:
    if not isinstance(payload, dict) or payload.get("protocol") != PROTOCOL:
        raise VectorEvidenceError("incorrect protocol")
    for field in ("model_id", "model_version", "harness_id", "checkpoint_sha256",
                  "coordinate_basis_id", "tensor_layout_sha256", "intervention_kind"):
        _nonempty(payload.get(field), field)
    for field in ("checkpoint_sha256", "tensor_layout_sha256"):
        value = payload[field]
        if len(value) != 64 or any(ch not in "0123456789abcdef" for ch in value):
            raise VectorEvidenceError(f"invalid {field}")
    if payload["intervention_kind"] not in KINDS:
        raise VectorEvidenceError("no comparable coordinate representation specified")
    if payload.get("accumulation") != "same_state_additive":
        raise VectorEvidenceError(
            "only genuinely superposed comparable deltas can be analyzed as cumulative"
        )
    repairs = payload.get("repairs")
    if not isinstance(repairs, list) or not 1 <= len(repairs) <= MAX_REPAIRS:
        raise VectorEvidenceError("require 1..10 repair vectors")
    seen = set()
    vectors = []
    ids = []
    dim = None
    for entry in repairs:
        if not isinstance(entry, dict):
            raise VectorEvidenceError("repair entry must be object")
        ident = _nonempty(entry.get("repair_id"), "repair_id")
        _nonempty(entry.get("artifact_receipt"), "artifact_receipt")
        if ident in seen:
            raise VectorEvidenceError("duplicate repair identity")
        seen.add(ident)
        v = _vector(entry.get("vector"), dim)
        dim = len(v)
        vectors.append(v)
        ids.append(ident)

    norms = [math.hypot(*v) for v in vectors]
    cumulative = [0.0] * dim
    sum_sq = 0.0
    sum_norm = 0.0
    steps = []
    for index, (rid, delta, norm) in enumerate(zip(ids, vectors, norms)):
        previous = tuple(cumulative)
        sum_sq += norm ** 2
        sum_norm += norm
        cumulative = [a + b for a, b in zip(cumulative, delta)]
        cum_norm = math.hypot(*cumulative)
        previous_norm = math.hypot(*previous)
        pairwise = []
        for j in range(index):
            prev = vectors[j]
            similarity = _dot(prev, delta) / (norms[j] * norm)
            pairwise.append(max(-1.0, min(1.0, similarity)))
        align = (
            max(-1.0, min(1.0, _dot(previous, delta) / (previous_norm * norm)))
            if previous_norm > 0 else None
        )
        # Geometric energy: 1 if deltas are pairwise orthogonal,
        # >1 for constructive overlap, <1 for cancelling overlap.
        energy_ratio = cum_norm ** 2 / sum_sq
        # Orthogonal vectors have energy_ratio=1, so no destructive cross-term.
        # Path inefficiency can still be positive even for orthogonal vectors.
        destructive_interference = max(0.0, 1.0 - energy_ratio)
        path_inefficiency = max(0.0, 1.0 - cum_norm / sum_norm)
        steps.append({
            "repair_index": index + 1, "repair_id": rid,
            "vector_sha256": _hash(list(delta)),
            "delta_norm": norm,
            "cumulative_norm": cum_norm,
            "cumulative_energy_ratio": energy_ratio,
            "destructive_interference_fraction": destructive_interference,
            "path_inefficiency": path_inefficiency,
            "max_abs_pairwise_cosine": max((abs(x) for x in pairwise), default=None),
            "mean_abs_pairwise_cosine": (
                math.fsum(abs(x) for x in pairwise) / len(pairwise)
                if pairwise else None
            ),
            "alignment_with_previous_sum": align,
            "nonlinearity_observed": "NOT_MEASURED",
            "guardrail_effect": "NOT_MEASURED",
        })
    return {
        "protocol": PROTOCOL, "analysis_mode": "OFFLINE_VECTOR_GEOMETRY",
        "model_id": payload["model_id"], "model_version": payload["model_version"],
        "harness_id": payload["harness_id"], "checkpoint_sha256": payload["checkpoint_sha256"],
        "coordinate_basis_id": payload["coordinate_basis_id"],
        "tensor_layout_sha256": payload["tensor_layout_sha256"],
        "intervention_kind": payload["intervention_kind"], "repair_count": len(repairs),
        "steps": steps,
        "assertions": {
            "real_model_activation": "NOT_ATTESTED",
            "safety": "NOT_EVALUATED",
            "rollback": "NOT_EVALUATED",
            "capability_retention": "NOT_EVALUATED",
        },
        "limitations": [
            "Only comparable, same-state additive deltas are accepted; sequential independent API calls are not cumulative.",
            "Static dot products cannot establish nonlinear downstream generation effects.",
            "A high cosine, destructive energy cross-term or path inefficiency is not proof of maliciousness or compromised guardrails.",
            "Adapter matrices need reconstruction into a common effective weight delta; flattened LoRA A/B separately are not comparable.",
            "Host-based guardrail, task, skill and capability tests and true rollback must be measured separately.",
            "Numerical observations require preregistered thresholds and a proper null distribution for inferential claims.",
        ],
    }


def main() -> int:
    cli = argparse.ArgumentParser(description="Offline geometric ZOMBIE repair vector hygiene")
    cli.add_argument("input", type=Path, help="private JSON with precomputed comparable repair deltas")
    cli.add_argument("--report", type=Path, default=Path("zombie-vector-hygiene-report.json"))
    args = cli.parse_args()
    try:
        p = json.loads(args.input.read_text("utf-8"))
        report = analyze(p)
    except (ValueError, OSError, OverflowError) as error:
        cli.exit(2, f"Vector evidence rejected: {error}\n")
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", "utf-8")
    print(f"Vector geometry computed for {report['repair_count']} deltas; "
          "no safety or cognitive-boost claim made")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
