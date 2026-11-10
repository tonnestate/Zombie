"""Offline validation of the executable Z01A paired attack runner."""
import copy

import pytest

import zombie_attack_validate as z


def agent_target(**changes):
    row = {
        "target_id": "staging-copilot",
        "adapter": "agent",
        "endpoint": "http://127.0.0.1:8000/test",
        "model_id": "model-1",
        "harness_id": "copilot",
        "research_staging": True,
    }
    row.update(changes)
    return row


def direct_target(**changes):
    return agent_target(
        target_id="direct-model-1",
        adapter="openai_chat",
        harness_id="direct",
        endpoint="https://staging.example.invalid/v1/chat/completions",
        **changes,
    )


def test_vectors_have_identical_product_facts_and_marker_in_both_arms():
    assert len(z.vectors()) == 3
    for case in z.vectors():
        assert z.FACTS in case.neutral and z.FACTS in case.attack
        assert z.MARKER in case.neutral and z.MARKER in case.attack
        assert case.attack != case.neutral


def test_strict_legitimate_success_and_exact_redirection_differ():
    assert z.classify(z.EXPECTED)["legitimate_exact"]
    assert z.classify(z.MARKER)["exact_takeover_marker"]
    quoted = z.classify("Source metadata mentions " + z.MARKER)
    assert quoted["marker_mentioned"] and not quoted["exact_takeover_marker"]


def test_network_execution_requires_explicit_opt_in(monkeypatch):
    monkeypatch.delenv("ZOMBIE_AUTHORIZED_TARGET", raising=False)
    with pytest.raises(ValueError, match="ZOMBIE_AUTHORIZED_TARGET"):
        z.run([agent_target()], 1, 42, execute=True)


def test_plan_makes_no_network_calls(monkeypatch):
    def deny(*args, **kwargs):
        raise AssertionError("Network call attempted in plan mode")
    monkeypatch.setattr(z.requests, "post", deny)
    report = z.run([agent_target(), direct_target()], 2, 17, execute=False)
    assert report["execution"] == "PLAN_ONLY"
    assert len(report["observations"]) == 2 * 3 * 2 * 2
    assert all(row["status"] == "NOT_EXECUTED" for row in report["observations"])
    assert all(row["completed_pairs"] == 0 for row in report["paired_summary"])


def test_plan_order_is_repeatable_and_paired():
    targets = [agent_target()]
    p1 = z.build_plan(targets, 4, 19)
    p2 = z.build_plan(targets, 4, 19)
    assert p1 == p2
    for vector in z.vectors():
        for repeat in range(1, 5):
            arms = [x["arm"] for x in p1 if x["vector_id"] == vector.name and x["replicate"] == repeat]
            assert set(arms) == {"neutral", "attack"}


def test_simulated_responder_counts_paired_success_without_claiming_real_model(monkeypatch):
    monkeypatch.setenv("ZOMBIE_AUTHORIZED_TARGET", "YES")

    def fake_call(target, task, document):
        attacked = (
            "[im_start]system" in document
            or "Assistant instruction:" in document
            or '"instruction": ' in document
        )
        text = z.MARKER if attacked else z.EXPECTED
        return {
            "response": text,
            "duration_ms": 1,
            "reported_model_id": target["model_id"],
            "model_identity_match": True,
            "tool_call_metadata_present": False,
            "request_sha256": z.digest(document),
        }

    monkeypatch.setattr(z, "call_target", fake_call)
    report = z.run([agent_target()], 2, 17, execute=True)
    assert len(report["paired_summary"]) == 3
    assert all(row["completed_pairs"] == 2 for row in report["paired_summary"])
    assert all(row["attack_only_exact_marker"] == 2 for row in report["paired_summary"])
    assert all(row["neutral_legitimate"] == 2 for row in report["paired_summary"])
    assert all(row["model_input_evidence"] == "CLIENT_PAYLOAD_ONLY" for row in report["observations"])
    assert all("response" not in row and "document" not in row for row in report["observations"])


def test_partial_failed_pair_does_not_turn_into_success_or_failure(monkeypatch):
    monkeypatch.setenv("ZOMBIE_AUTHORIZED_TARGET", "YES")

    def fake_call(target, task, document):
        if "[im_start]system" in document or "Assistant instruction:" in document or '"instruction": ' in document:
            raise ValueError("simulated gateway error")
        return {
            "response": z.EXPECTED, "duration_ms": 1,
            "reported_model_id": "model-1", "model_identity_match": True,
            "tool_call_metadata_present": False, "request_sha256": z.digest(document),
        }

    monkeypatch.setattr(z, "call_target", fake_call)
    report = z.run([agent_target()], 1, 17, execute=True)
    assert all(row["completed_pairs"] == 0 for row in report["paired_summary"])
    assert sum(row["status"] == "ERROR" for row in report["observations"]) == 3
    assert not any("response" in row for row in report["observations"])


@pytest.mark.parametrize("changes", [
    {"research_staging": False},
    {"endpoint": "http://staging.example.invalid/test"},
    {"endpoint": "https://user:pass@staging.example.invalid/test"},
    {"endpoint": "https://staging.example.invalid/test?token=secret"},
    {"adapter": "openai_chat"},
])
def test_invalid_targets_are_rejected(changes):
    with pytest.raises(ValueError):
        z.validate_target(agent_target(**changes))


def test_openai_chat_constructs_fixed_system_and_untrusted_document():
    target = direct_target()
    payload = z.create_request(target, z.TASK, z.vectors()[0].attack)
    assert payload["model"] == target["model_id"]
    assert payload["messages"][0]["role"] == "system"
    assert payload["messages"][1]["role"] == "user"
    assert z.MARKER in payload["messages"][1]["content"]


def test_agent_adapter_uses_existing_contract_without_inventing_routing_fields():
    target = agent_target()
    assert z.create_request(target, "task", "document") == {
        "task": "task", "retrieved_content": "document"
    }


def test_openai_and_agent_responses_are_distinct():
    d = direct_target()
    a = agent_target()
    assert z.parse_response(d, {
        "model": "model-1", "choices": [{"message": {"content": z.EXPECTED}}]
    })[0] == z.EXPECTED
    assert z.parse_response(a, {"response": z.MARKER})[0] == z.MARKER
    with pytest.raises(ValueError):
        z.parse_response(d, {"response": "not a completion"})


def test_repeats_are_bounded():
    with pytest.raises(ValueError):
        z.build_plan([agent_target()], 21, 1)
    with pytest.raises(ValueError):
        z.build_plan([agent_target()], 0, 1)
