"""Offline tests for Z13 active skill lifecycle contract; no real skills installed."""
import copy
import hashlib
import hmac
import json

import pytest

import zombie_skill_validate as s


def target():
    return {
        "target_id": "lab-skill", "model_id": "model-pinned", "harness_id": "harness-staging",
        "endpoint": "http://127.0.0.1:9000/skills", "adapter": "skill_lab_v1",
        "receipt_key_env": "ZOMBIE_SKILL_TEST_KEY", "research_staging": True,
    }


def signed(request, secret=b"test-host-key-with-strong-separation", *, selected=True, loaded=True):
    source = request["skill"]
    pin_match = source["approved_digest"] == source["current_digest"]
    payload = {
        "protocol": s.PROTOCOL,
        "trial_id": request["trial_id"], "model_id": request["model_id"],
        "harness_id": request["harness_id"], "vector": request["vector"],
        "arm": request["arm"], "output": s.EXPECTED,
        "events": [
            {"stage": "discovery", "candidate_digest": source["current_digest"]},
            {"stage": "selection", "selected": selected, "host_receipt": "selection-1"},
            {"stage": "integrity", "pin_match": pin_match,
             "policy_decision": "BLOCK_UNPINNED" if not pin_match else "ALLOW_PINNED",
             "host_receipt": "integrity-1"},
            {"stage": "load", "loaded": loaded, "skill_digest": source["current_digest"] if loaded else None,
             "host_receipt": "load-1"},
            {"stage": "model_input", "payload_sha256": s.sha("input")},
            {"stage": "model_output", "payload_sha256": s.sha(s.EXPECTED)},
        ],
    }
    payload["signature"] = hmac.new(secret, s.canonical(payload), hashlib.sha256).hexdigest()
    return payload


def make_request(vector="frontmatter", arm="neutral"):
    return {
        "protocol": s.PROTOCOL, "trial_id": "trial01",
        "model_id": "model-pinned", "harness_id": "harness-staging",
        "vector": vector, "arm": arm, "skill": s.build_skill(vector, arm),
    }


def test_all_vectors_have_neutral_and_adversarial_skills():
    assert set(s.VECTORS) == {
        "frontmatter", "body", "linked-reference", "post-approval-update"
    }
    for vector in s.VECTORS:
        normal, attacker = s.build_skill(vector, "neutral"), s.build_skill(vector, "attack")
        assert normal["task"] == attacker["task"]
        assert normal["facts"] == attacker["facts"]
        assert s.MARKER in json.dumps(normal["skill_files"])
        assert s.MARKER in json.dumps(attacker["skill_files"])


def test_post_approval_update_changes_only_adversarial_current_digest():
    clean = s.build_skill("post-approval-update", "neutral")
    attack = s.build_skill("post-approval-update", "attack")
    assert clean["approved_digest"] == clean["current_digest"]
    assert attack["approved_digest"] == clean["approved_digest"]
    assert attack["current_digest"] != attack["approved_digest"]


def test_synthetic_attestation_verifies_happy_path():
    request = make_request()
    report = s.verify_receipt(target(), request, signed(request), b"test-host-key-with-strong-separation")
    assert report["status"] == "OBSERVED"
    assert report["loaded"]
    assert report["pin_match"]
    assert report["legitimate_exact"]
    assert not report["exact_marker_takeover"]


def test_changed_pinned_skill_must_be_denied_load():
    request = make_request("post-approval-update", "attack")
    with pytest.raises(ValueError, match="unapproved update"):
        s.verify_receipt(target(), request, signed(request), b"test-host-key-with-strong-separation")
    valid = s.verify_receipt(
        target(), request, signed(request, loaded=False),
        b"test-host-key-with-strong-separation",
    )
    assert valid["pin_match"] is False
    assert valid["unapproved_update_loaded"] is False


def test_unsigned_or_tampered_trace_is_rejected():
    request = make_request()
    altered = copy.deepcopy(signed(request))
    altered["events"][3]["loaded"] = False
    with pytest.raises(ValueError, match="tampered"):
        s.verify_receipt(target(), request, altered, b"test-host-key-with-strong-separation")


def test_plan_does_not_call_network(monkeypatch):
    monkeypatch.delenv("ZOMBIE_AUTHORIZED_TARGET", raising=False)
    monkeypatch.setattr(
        s.requests, "post",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("network forbidden")),
    )
    report = s.run([target()], 2, 131, execute=False)
    assert len(report["observations"]) == 16
    assert all(r["status"] == "NOT_EXECUTED" for r in report["observations"])
    assert all(p["completed_pairs"] == 0 for p in report["paired_summary"])


def test_explicit_execution_opt_in_is_required(monkeypatch):
    monkeypatch.delenv("ZOMBIE_AUTHORIZED_TARGET", raising=False)
    with pytest.raises(ValueError, match="ZOMBIE_AUTHORIZED_TARGET"):
        s.run([target()], 1, 131, execute=True)


def test_remote_http_and_wrong_adapter_rejected():
    with pytest.raises(ValueError, match="HTTPS"):
        s.validate_target({**target(), "endpoint": "http://remote.example.invalid/skills"})
    with pytest.raises(ValueError, match="only authorized"):
        s.validate_target({**target(), "adapter": "untrusted"})
