"""Offline contract tests. No live model, external tool or production token used."""
from __future__ import annotations

import asyncio
import copy
from types import SimpleNamespace

import pytest

from zombie_fruitstack_capture import (
    CaptureError, HostCapture, PrivateJSONLSink, audit_host_events, digest, digest_text,
)

KEYS = {"peachme": b"peach-test-only-secret-001",
        "cherryme": b"cherry-test-only-secret-002",
        "plumme": b"plum-test-only-secret-003"}
CANARY = "ZOMBIE-CANARY-7F3A"


def actual_peach_result(*, status="CALLED", outcome="AUTONOMOUS", result=None,
                        args=None, work_ref="w-1", tool="google_research"):
    """Fixture matches PeachMe ToolGateway.invoke's nested receipt shape."""
    args = args if args is not None else {"objective": "voltage"}
    decision = {"outcome": outcome, "reasons": [], "controls": {},
                "authority": "peachme.tool_registry"}
    receipt = {"receipt_id": "receipt-123", "work_ref": work_ref,
               "server": "google-research-peer", "tool": tool,
               "status": status, "decision": decision,
               "arguments_sha256": digest(args),
               "result_sha256": digest(result) if status == "CALLED" else None,
               "prev_hash": "0" * 64, "hash": "a" * 64}
    return {"status": status, "decision": decision, "receipt": receipt,
            "result": result if status == "CALLED" else None, "error": None}


def collector():
    events = []
    return HostCapture("trace-1", "w-1", keys=KEYS,
                       event_sink=events.append), events


def sample_source():
    excerpt = "The voltage is 120V."
    return SimpleNamespace(
        source_ref="https://test.example/voltage",
        excerpt=excerpt, excerpt_sha256=digest_text(excerpt),
        retrieval_receipt_id="receipt-123",
    )


def get_peachme_event(capture, *, args=None, result=None):
    args = args if args is not None else {"objective": "voltage"}
    result = result if result is not None else {"new_sources": []}
    raw = actual_peach_result(args=args, result=result)
    return capture.observe_peachme(raw, server="google-research-peer",
                                   tool="google_research", arguments=args,
                                   work_ref="w-1")


def test_real_shape_capture_transformation_client_submission():
    capture, events = collector()
    peach = get_peachme_event(capture)
    cherry = capture.observe_cherryme(sample_source(), peach)
    observed = []

    async def send(payload):
        observed.append(copy.deepcopy(payload))
        return {"answer": "120V"}

    model_payload = {"messages": [{"role": "user", "content": CANARY + " 120V"}]}
    result, model_event = asyncio.run(capture.submit_model(
        sender=send, payload=model_payload,
        source_event_ids=[cherry], model_id="provider-model-staging",
    ))
    report = audit_host_events(events, KEYS)
    assert result == {"answer": "120V"}
    assert observed == [model_payload]
    assert model_event == "trace-1:3"
    assert report["event_counts"] == {
        "tool_return": 1, "source_admitted": 1, "model_client_submit": 1,
    }
    assert report["canary_in_submitted_client_payload"] == 1
    assert report["provider_received_or_processed"] == "NOT_ATTESTED"
    assert events[1]["excerpt_sha256"] != events[0]["tool_result_sha256"]


def test_observation_never_stores_raw_prompts_queries_results_or_urls():
    capture, events = collector()
    peach = get_peachme_event(capture)
    cherry = capture.observe_cherryme(sample_source(), peach)
    asyncio.run(capture.submit_model(
        sender=lambda _: "ok",
        payload={"messages": [{"content": CANARY, "role": "user"}]},
        source_event_ids=[cherry], model_id="staging",
    ))
    representation = repr(events)
    assert "The voltage is" not in representation
    assert "https://test.example" not in representation
    assert CANARY not in representation
    assert "new_sources" not in representation
    assert "voltage" not in events[0]


def test_peachme_receipt_result_tampering_is_rejected():
    capture, events = collector()
    raw = actual_peach_result(result={"ok": True})
    raw["result"] = {"ok": False}
    with pytest.raises(CaptureError, match="result digest"):
        capture.observe_peachme(raw, server="google-research-peer",
                                tool="google_research",
                                arguments={"objective": "voltage"}, work_ref="w-1")
    assert events == []


def test_peachme_policy_and_binding_mismatch_rejected():
    capture, events = collector()
    raw = actual_peach_result(result={"ok": True})
    raw["receipt"]["work_ref"] = "someone-else"
    with pytest.raises(CaptureError, match="different request"):
        capture.observe_peachme(raw, server="google-research-peer",
                                tool="google_research",
                                arguments={"objective": "voltage"}, work_ref="w-1")
    raw = actual_peach_result(status="REFUSED", outcome="AUTONOMOUS")
    with pytest.raises(CaptureError, match="REFUSED"):
        capture.observe_peachme(raw, server="google-research-peer",
                                tool="google_research",
                                arguments={"objective": "voltage"}, work_ref="w-1")
    assert events == []


def test_refused_gateway_cannot_become_source():
    capture, events = collector()
    raw = actual_peach_result(status="REFUSED", outcome="BLOCKED")
    gateway = capture.observe_peachme(raw, server="google-research-peer",
                                      tool="google_research",
                                      arguments={"objective": "voltage"}, work_ref="w-1")
    assert gateway.status == "REFUSED"
    with pytest.raises(CaptureError, match="successful"):
        capture.observe_cherryme(sample_source(), gateway)
    assert len(events) == 1


def test_source_retrieval_receipt_and_excerpt_digest_cannot_change():
    capture, _ = collector()
    gateway = get_peachme_event(capture)
    source = sample_source()
    source.retrieval_receipt_id = "fake"
    with pytest.raises(CaptureError, match="receipt mismatch"):
        capture.observe_cherryme(source, gateway)
    source = sample_source()
    source.excerpt = "Modified"
    with pytest.raises(CaptureError, match="digest mismatch"):
        capture.observe_cherryme(source, gateway)


def test_cannot_submit_model_without_valid_source_handoff():
    capture, _ = collector()
    with pytest.raises(CaptureError, match="requires observed"):
        asyncio.run(capture.submit_model(
            sender=lambda x: x, payload={"messages": ["something"]},
            source_event_ids=[], model_id="staging",
        ))


def test_signature_tampering_and_parent_rewriting_fail_closed():
    capture, events = collector()
    gateway = get_peachme_event(capture)
    capture.observe_cherryme(sample_source(), gateway)
    changed = copy.deepcopy(events)
    changed[1]["excerpt_sha256"] = "f" * 64
    with pytest.raises(CaptureError, match="signature"):
        audit_host_events(changed, KEYS)
    changed = copy.deepcopy(events)
    changed[1]["parent_event_ids"] = ["unknown"]
    with pytest.raises(CaptureError, match="signature"):
        audit_host_events(changed, KEYS)


def test_wrapped_async_peachme_invocation_observes_actual_return():
    capture, events = collector()

    class Peaches:
        async def invoke(self, server, tool, arguments, work_ref):
            return actual_peach_result(result={"ok": True}, args=arguments,
                                       work_ref=work_ref, tool=tool)

    answer, evidence = asyncio.run(capture.invoke_peachme(
        Peaches(), server="google-research-peer",
        tool="google_research", arguments={"objective": "voltage"},
        work_ref="w-1",
    ))
    assert answer["status"] == "CALLED"
    assert evidence.receipt_id == "receipt-123"
    assert audit_host_events(events, KEYS)["event_counts"]["tool_return"] == 1


def test_capture_fails_closed_if_host_sink_fails():
    def fail_sink(_):
        raise RuntimeError("audit storage unavailable")
    capture = HostCapture("trace", "w-1", keys=KEYS, event_sink=fail_sink)
    with pytest.raises(RuntimeError, match="audit storage unavailable"):
        get_peachme_event(capture)


def test_model_client_error_is_recorded_without_forging_submission_success():
    capture, events = collector()
    gateway = get_peachme_event(capture)
    source = capture.observe_cherryme(sample_source(), gateway)

    def client_error(_):
        raise RuntimeError("provider failure")

    with pytest.raises(RuntimeError, match="provider failure"):
        asyncio.run(capture.submit_model(
            sender=client_error, payload={"messages": []},
            source_event_ids=[source], model_id="staging",
        ))
    report = audit_host_events(events, KEYS)
    assert report["event_counts"]["model_client_submit"] == 1
    assert report["canary_in_submitted_client_payload"] == 0
    assert events[-1]["client_status"] == "CLIENT_ERROR"


def test_model_payload_mutation_prevents_attested_success():
    capture, events = collector()
    gateway = get_peachme_event(capture)
    source = capture.observe_cherryme(sample_source(), gateway)

    def mutating_client(payload):
        payload["messages"].append({"role": "system", "content": "changed"})
        return "ok"

    with pytest.raises(CaptureError, match="mutated input"):
        asyncio.run(capture.submit_model(
            sender=mutating_client, payload={"messages": []},
            source_event_ids=[source], model_id="staging",
        ))
    assert len(events) == 2


def test_host_keys_required_and_distinct():
    with pytest.raises(CaptureError, match="keys must be distinct"):
        HostCapture("trace", "w-1",
                    keys={name: b"repeated-16-byte-key" for name in KEYS},
                    event_sink=lambda _: None)



def test_private_jsonl_sink_persists_real_signed_evidence(tmp_path):
    import json
    import stat

    destination = tmp_path / "research-private.jsonl"
    capture = HostCapture("trace", "w-1", keys=KEYS, event_sink=PrivateJSONLSink(destination))
    get_peachme_event(capture)
    mode = stat.S_IMODE(destination.stat().st_mode)
    assert mode & 0o077 == 0
    loaded = [json.loads(line) for line in destination.read_text("utf-8").splitlines()]
    assert len(loaded) == 1
    assert audit_host_events(loaded, KEYS)["event_counts"]["tool_return"] == 1


def test_private_sink_rejects_existing_public_permissions(tmp_path):
    import os
    destination = tmp_path / "worldreadable.jsonl"
    destination.write_text("", encoding="utf-8")
    os.chmod(destination, 0o644)
    capture = HostCapture("trace", "w-1", keys=KEYS, event_sink=PrivateJSONLSink(destination))
    with pytest.raises(CaptureError, match="private regular file"):
        get_peachme_event(capture)
