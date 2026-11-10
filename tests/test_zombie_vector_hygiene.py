"""Static numerical regression suite; no model loading or activation hooks."""
import copy
import math

import pytest

import zombie_vector_hygiene as z


def sample(vectors=None, **overrides):
    if vectors is None:
        vectors = [[1.0, 0.0], [0.0, 1.0]]
    p = {
        "protocol": z.PROTOCOL,
        "model_id": "cloud-lab-model",
        "model_version": "sha-pinned-version",
        "harness_id": "lab-harness",
        "checkpoint_sha256": "a" * 64,
        "coordinate_basis_id": "same-layer-and-order",
        "tensor_layout_sha256": "b" * 64,
        "intervention_kind": "activation_delta",
        "accumulation": "same_state_additive",
        "repairs": [
            {"repair_id": f"repair-{i+1}", "artifact_receipt": f"host-{i+1}", "vector": v}
            for i, v in enumerate(vectors)
        ],
    }
    p.update(overrides)
    return p


def test_orthogonal_repairs_have_no_geometric_cross_term():
    report = z.analyze(sample())
    assert report["analysis_mode"] == "OFFLINE_VECTOR_GEOMETRY"
    assert report["steps"][1]["cumulative_energy_ratio"] == pytest.approx(1)
    assert report["steps"][1]["max_abs_pairwise_cosine"] == pytest.approx(0)
    assert report["steps"][1]["cancellation_fraction"] == pytest.approx(1 - math.sqrt(2) / 2)


def test_aligned_repairs_accumulate_constructively():
    report = z.analyze(sample([[1., 0.]] * 10))
    assert report["repair_count"] == 10
    assert report["steps"][9]["cumulative_norm"] == pytest.approx(10)
    assert report["steps"][9]["cumulative_energy_ratio"] == pytest.approx(10)
    assert report["steps"][9]["max_abs_pairwise_cosine"] == pytest.approx(1)
    assert report["steps"][9]["cancellation_fraction"] == pytest.approx(0)
    assert report["assertions"]["safety"] == "NOT_EVALUATED"


def test_opposite_vectors_cancel_even_though_both_are_nonzero():
    report = z.analyze(sample([[1., 0.], [-1., 0.], [1., 0.]]))
    assert report["steps"][1]["cumulative_norm"] == 0
    assert report["steps"][1]["cumulative_energy_ratio"] == 0
    assert report["steps"][1]["cancellation_fraction"] == 1
    assert report["steps"][1]["alignment_with_previous_sum"] == pytest.approx(-1)
    assert report["steps"][2]["alignment_with_previous_sum"] is None


def test_no_raw_vectors_or_prompts_in_report():
    report = z.analyze(sample([[3., 4.]]))
    assert "vector" not in str(report["steps"][0].keys())
    assert "3.0, 4.0" not in str(report)
    assert report["steps"][0]["vector_sha256"]
    assert report["steps"][0]["guardrail_effect"] == "NOT_MEASURED"


@pytest.mark.parametrize("changes", [
    {"accumulation": "independent_requests"},
    {"intervention_kind": "api_prompt"},
    {"coordinate_basis_id": ""},
    {"checkpoint_sha256": "invalid"},
    {"repairs": []},
    {"repairs": [{"repair_id": "a", "artifact_receipt": "a", "vector": [0., 0.]}]},
    {"repairs": [{"repair_id": "a", "artifact_receipt": "a", "vector": [1., 2.]},
                 {"repair_id": "b", "artifact_receipt": "b", "vector": [1., 2., 3.]}]},
    {"repairs": [{"repair_id": "a", "artifact_receipt": "a", "vector": [1., 2.]},
                 {"repair_id": "a", "artifact_receipt": "b", "vector": [1., 2.]}]},
    {"repairs": [{"repair_id": "a", "artifact_receipt": "a", "vector": [float('nan'), 2.]}]},
    {"repairs": [{"repair_id": "a", "artifact_receipt": "a", "vector": [True, 2.]}]},
    {"repairs": [{"repair_id": f"v{i}", "artifact_receipt": "host", "vector": [1., 2.]}
                 for i in range(11)]},
])
def test_uncomparable_or_invalid_vector_evidence_rejected(changes):
    with pytest.raises(z.VectorEvidenceError):
        z.analyze(sample(**changes))


def test_deterministic_inputs_and_outputs_for_paired_model_analysis():
    p = sample([[1., 1.], [2., -1.]])
    assert z.analyze(p) == z.analyze(copy.deepcopy(p))
    assert z.analyze(p)["steps"][1]["vector_sha256"] != z.analyze(p)["steps"][0]["vector_sha256"]
