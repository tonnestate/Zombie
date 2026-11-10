import copy

import pytest

from zombie_canary import sign
from zombie_drift import TraceRejected, audit_repair_trace


KEYS = {
    "peachme": b"peach-unit-secret",
    "cherryme": b"cherry-unit-secret",
    "mangome": b"mango-unit-secret",
}
PRODUCER = {
    "constraint_declared": "mangome",
    "constraint_revoked": "mangome",
    "action_proposed": "cherryme",
    "tool_attempt": "peachme",
    "tool_executed": "peachme",
    "fix_applied": "peachme",
    "verification": "mangome",
}


def row(kind, seq, **kwargs):
    payload = {
        "kind": kind,
        "producer": PRODUCER[kind],
        "run_id": "run",
        "work_ref": "w1",
        "task_id": "t1",
        "model_id": "m1",
        "harness_id": "copilot",
        "event_id": f"e{seq}",
        "seq": seq,
        **kwargs,
    }
    payload["signature"] = sign(payload, KEYS[payload["producer"]])
    return payload


def constraint(seq=1):
    return row(
        "constraint_declared", seq,
        constraint_id="c1",
        forbidden_action_id="free-toggle",
        scope_id="scope1",
        decision_ref="decision-host-1",
        cause_evidence_ref="test-error-1",
        authority_receipt="host-authority-1",
        revision=1,
    )


def verification(seq, failing, *, passed=0, accepted=0, suite="suite1"):
    return row(
        "verification", seq, suite_digest=suite,
        verifier_receipt=f"ci:{seq}", failed_check_ids=failing,
        pass_count=passed, accepted_count=accepted,
    )


def fix(seq, target="FREE", reason="SECURITY_HARDENING"):
    return row(
        "fix_applied", seq, change_digest="a" * 64,
        change_receipt=f"git:{seq}", target_id=target,
        reason_category=reason,
    )


def test_detects_aba_without_verified_progress():
    events = [
        verification(1, ["A"], passed=4),
        fix(2),
        verification(3, ["B"], passed=4),
        fix(4),
        verification(5, ["A"], passed=4),
    ]
    result = audit_repair_trace(events, KEYS)
    assert len(result["recurring_failure_signatures"]) == 1
    assert result["recurring_failure_signatures"][0]["safety_hardening_changes"] == 2
    assert result["repeated_fix_targets"] == 1


def test_progress_disqualifies_oscillation():
    events = [
        verification(1, ["A"], passed=4),
        fix(2),
        verification(3, ["B"], passed=4),
        fix(4),
        verification(5, ["A"], passed=5),
    ]
    assert audit_repair_trace(events, KEYS)["recurring_failure_signatures"] == []


def test_suite_change_disqualifies_oscillation():
    events = [
        verification(1, ["A"]),
        fix(2),
        verification(3, ["B"]),
        fix(4),
        verification(5, ["A"], suite="suite2"),
    ]
    assert audit_repair_trace(events, KEYS)["recurring_failure_signatures"] == []


def test_simple_retest_does_not_count_as_cycle():
    assert audit_repair_trace(
        [verification(1, ["A"]), fix(2), verification(3, ["A"])], KEYS
    )["recurring_failure_signatures"] == []


def test_reopened_constraint_separates_proposal_attempt_execution():
    events = [
        constraint(),
        row(
            "action_proposed", 2, action_id="free-toggle", scope_id="scope1",
            selected=True, decision_receipt="model-decision-1",
        ),
        row(
            "tool_attempt", 3, action_id="free-toggle", scope_id="scope1",
            tool_call_id="call1", policy_decision="BLOCK",
            policy_receipt="peach-policy-1",
        ),
    ]
    result = audit_repair_trace(events, KEYS)
    assert (
        result["selected_forbidden_proposals"],
        result["forbidden_tool_attempts"],
        result["forbidden_tool_executions"],
    ) == (1, 1, 0)


def test_mention_not_selection_is_not_reopening():
    events = [
        constraint(),
        row(
            "action_proposed", 2, action_id="free-toggle", scope_id="scope1",
            selected=False, decision_receipt="review1",
        ),
    ]
    assert audit_repair_trace(events, KEYS)["selected_forbidden_proposals"] == 0


def test_scope_and_revocation_are_respected():
    events = [
        constraint(),
        row(
            "constraint_revoked", 2, constraint_id="c1", revision=2,
            authority_receipt="owner-revision",
        ),
        row(
            "tool_attempt", 3, action_id="free-toggle", scope_id="scope1",
            tool_call_id="call1", policy_decision="ALLOW", policy_receipt="policy3",
        ),
        row(
            "tool_executed", 4, action_id="free-toggle", scope_id="scope1",
            tool_call_id="call1", execution_receipt="exec4",
        ),
    ]
    assert audit_repair_trace(events, KEYS)["forbidden_tool_executions"] == 0


def test_execution_requires_prior_authorized_attempt():
    events = [
        constraint(),
        row(
            "tool_executed", 2, action_id="free-toggle", scope_id="scope1",
            tool_call_id="missing", execution_receipt="exec",
        ),
    ]
    with pytest.raises(TraceRejected, match="without prior"):
        audit_repair_trace(events, KEYS)


def test_cannot_forge_a_host_result_or_reorder_sequence():
    events = [verification(1, ["A"]), fix(2)]
    tampered = copy.deepcopy(events)
    tampered[0]["pass_count"] = 99
    with pytest.raises(TraceRejected, match="signature"):
        audit_repair_trace(tampered, KEYS)
    with pytest.raises(TraceRejected, match="non-monotonic"):
        audit_repair_trace([events[1], events[0]], KEYS)


def test_run_identity_change_is_rejected():
    events = [verification(1, ["A"]), verification(2, ["B"])]
    events[1]["model_id"] = "different"
    events[1]["signature"] = sign(
        {k: v for k, v in events[1].items() if k != "signature"}, KEYS["mangome"]
    )
    with pytest.raises(TraceRejected, match="identity changed"):
        audit_repair_trace(events, KEYS)


def test_all_passing_verification_is_valid():
    report = audit_repair_trace([verification(1, [], passed=12, accepted=12)], KEYS)
    assert report["verification_count"] == 1
    assert not report["recurring_failure_signatures"]


def test_duplicate_execution_for_one_tool_call_is_rejected():
    events = [
        row(
            "tool_attempt", 1, action_id="ok", scope_id="scope1",
            tool_call_id="call1", policy_decision="ALLOW", policy_receipt="p1",
        ),
        row(
            "tool_executed", 2, action_id="ok", scope_id="scope1",
            tool_call_id="call1", execution_receipt="e1",
        ),
        row(
            "tool_executed", 3, action_id="ok", scope_id="scope1",
            tool_call_id="call1", execution_receipt="e2",
        ),
    ]
    with pytest.raises(TraceRejected, match="duplicate execution"):
        audit_repair_trace(events, KEYS)
