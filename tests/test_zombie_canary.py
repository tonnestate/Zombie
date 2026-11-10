from zombie_canary import CANARY, audit, sign

KEYS = {"peachme": b"test-key-peach", "cherryme": b"test-key-cherry", "mangome": b"test-key-mango"}


def event(producer, stage, event_id, **kwargs):
    item = {
        "producer": producer, "stage": stage, "event_id": event_id,
        "trace_id": "synthetic-run-001", "canary_id": CANARY,
        "source_receipt": "synthetic-receipt-001", "content_sha256": "a" * 64,
        **kwargs,
    }
    item["signature"] = sign(item, KEYS[producer])
    return item


def test_unsigned_host_claim_is_not_trusted():
    unsigned = event("cherryme", "verification", "v1", independent_verifier_receipt="mock-verifier", verdict="SUPPORTED")
    unsigned["trust_class"] = "verified"  # signature cannot survive modification
    report = audit([unsigned], KEYS)
    assert report["accepted_events"] == 0
    assert "untrusted signature" in report["faults"][0]


def test_canary_preserves_source_lineage_but_does_not_claim_memory():
    records = [
        event("peachme", "gateway_result", "g1"),
        event("cherryme", "source_received", "c1", parent_event_id="g1"),
        event("cherryme", "candidate", "c2", parent_event_id="c1"),
    ]
    report = audit(records, KEYS)
    assert report["accepted_events"] == 3
    assert report["matrix"]["cherryme"]["later_reuse"] == "FEHLT"
    assert report["matrix"]["cherryme"]["trust_class"] == "FEHLT"
    assert not report["faults"]


def test_promotion_without_independent_verification_is_rejected():
    report = audit([event("cherryme", "verification", "v1", verdict="SUPPORTED")], KEYS)
    assert report["rejected_events"] == 1
    assert "independent verifier" in report["faults"][0]


def test_cross_session_memory_requires_write_and_refetch_evidence():
    records = [
        event("cherryme", "memory_write", "w1", memory_id="mem-001", write_policy_receipt="policy-001", session_id="s1"),
        event("cherryme", "memory_reuse", "r1", memory_id="mem-001", read_receipt="read-001", session_id="s2"),
    ]
    report = audit(records, KEYS)
    assert report["matrix"]["cherryme"]["later_reuse"] == "TEILWEISE"
    records[1] = event("cherryme", "memory_reuse", "r1", memory_id="mem-001", read_receipt="read-001", session_id="s2", no_refetch_evidence="network-audit-1", context_reset_evidence="reset-1")
    report = audit(records, KEYS)
    assert report["matrix"]["cherryme"]["later_reuse"] == "VORHANDEN"


def test_provenance_cannot_be_changed_across_handoff():
    records = [
        event("peachme", "gateway_result", "g1"),
        event("cherryme", "source_received", "c1", parent_event_id="g1", content_sha256="b" * 64),
    ]
    result = audit(records, KEYS)
    assert result["rejected_events"] == 1
    assert "provenance changed" in result["faults"][0]
