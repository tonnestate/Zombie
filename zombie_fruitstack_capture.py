"""Project ZOMBIE Z01: host-side capture points for real FruitStack objects.

An instrumentor, NOT a simulation of a live agent. The host must integrate these
call sites at the actual PeachMe, CherryMe and model-client boundaries.
The recorder emits no raw queries, prompts, results, URLs or credentials.
A signed report proves key possession, not that host secrets were inaccessible
to the model or that a provider actually processed a request.
"""
from __future__ import annotations

import copy
import hashlib
import inspect
import json
import os
import stat
from pathlib import Path
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Mapping

from zombie_canary import canonical, sign, verify

PROTOCOL = "ZOMBIE-Z01-HOST/1"
PRODUCERS = {"peachme", "cherryme", "plumme"}
STAGES = {"tool_return": "peachme", "source_admitted": "cherryme",
          "model_client_submit": "plumme"}
STATUS = {"CALLED", "FAILED", "REFUSED"}


class CaptureError(ValueError):
    """Incomplete or contradictory host evidence; no scientific success claim."""


class PrivateJSONLSink:
    """Write append-only *application-level* evidence to a private 0600 file.

    The filesystem/host must protect the directory and the signing keys.
    An append-only API does not prevent an administrator or file owner editing
    old records; external WORM storage is needed for that stronger property.
    """

    def __init__(self, path: str | Path):
        self.path = Path(path)

    def __call__(self, event: dict) -> None:
        flags = os.O_WRONLY | os.O_CREAT | os.O_APPEND
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        fd = os.open(self.path, flags, 0o600)
        try:
            details = os.fstat(fd)
            if not stat.S_ISREG(details.st_mode) or stat.S_IMODE(details.st_mode) & 0o077:
                raise CaptureError("audit evidence file must be private regular file")
            with os.fdopen(fd, "a", encoding="utf-8") as output:
                fd = -1
                output.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
                output.flush()
                os.fsync(output.fileno())
        finally:
            if fd >= 0:
                os.close(fd)


def digest(value: Any) -> str:
    """PeachMe's JSON-result and argument digest, including default ascii encoding."""
    serialized = json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def _required(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value:
        raise CaptureError(f"{name} must be a nonempty string")
    return value


@dataclass(frozen=True)
class ToolEvidence:
    event_id: str
    receipt_id: str
    result_sha256: str | None
    status: str


class HostCapture:
    """In-memory events for a single authorized run. Transport/storage is the host's job.

    Each producer gets a distinct host-only key. Never expose keys or this
    instance to LLM-written tools or model-supplied code.
    """

    def __init__(self, trace_id: str, work_ref: str, *, keys: Mapping[str, bytes],
                 event_sink: Callable[[dict], None]):
        self.trace_id = _required(trace_id, "trace_id")
        self.work_ref = _required(work_ref, "work_ref")
        if set(keys) != PRODUCERS or any(not isinstance(k, bytes) or len(k) < 16 for k in keys.values()):
            raise CaptureError("three >=16-byte host-only keys required")
        if len(set(keys.values())) != 3:
            raise CaptureError("keys must be distinct")
        if not callable(event_sink):
            raise CaptureError("host event_sink required")
        self._keys = dict(keys)
        self._sink = event_sink
        self._events: dict[str, dict] = {}
        self._counter = 0

    def _append(self, producer: str, stage: str, *, parent_event_ids: list[str], **data: Any) -> str:
        if STAGES.get(stage) != producer:
            raise CaptureError("producer/stage mismatch")
        if any(p not in self._events for p in parent_event_ids):
            raise CaptureError("unobserved parent event")
        self._counter += 1
        event_id = f"{self.trace_id}:{self._counter}"
        body = {"protocol": PROTOCOL, "trace_id": self.trace_id,
                "work_ref": self.work_ref, "producer": producer, "stage": stage,
                "event_id": event_id, "seq": self._counter,
                "parent_event_ids": parent_event_ids, **data}
        body["signature"] = sign(body, self._keys[producer])
        self._sink(copy.deepcopy(body))   # failed evidence write must fail closed
        self._events[event_id] = body
        return event_id

    def observe_peachme(self, response: dict, *, server: str, tool: str,
                        arguments: dict, work_ref: str) -> ToolEvidence:
        """Consume the ACTUAL result of PeachMe.ToolGateway.invoke, not a mock contract."""
        if work_ref != self.work_ref or not isinstance(response, dict):
            raise CaptureError("gateway response/work identity mismatch")
        decision, receipt = response.get("decision"), response.get("receipt")
        if not isinstance(decision, dict) or not isinstance(receipt, dict):
            raise CaptureError("actual PeachMe nested decision/receipt required")
        status = response.get("status")
        outcome = decision.get("outcome")
        if status not in STATUS or outcome not in {"AUTONOMOUS", "BLOCKED", "HUMAN_APPROVAL_REQUIRED"}:
            raise CaptureError("invalid gateway status/outcome")
        if status == "CALLED" and (outcome != "AUTONOMOUS" or response.get("error") is not None):
            raise CaptureError("CALLED without autonomy or with error")
        if status == "REFUSED" and outcome == "AUTONOMOUS":
            raise CaptureError("REFUSED with AUTONOMOUS decision")
        if status == "FAILED" and outcome != "AUTONOMOUS":
            raise CaptureError("FAILED without attempted autonomous call")
        receipt_id = _required(receipt.get("receipt_id"), "receipt_id")
        expected = {"server": server, "tool": tool, "work_ref": work_ref,
                    "arguments_sha256": digest(arguments), "decision": decision, "status": status}
        if any(receipt.get(field) != value for field, value in expected.items()):
            raise CaptureError("gateway receipt binds different request or decision")
        if response.get("receipt_id") not in (None, receipt_id):
            raise CaptureError("conflicting receipt IDs")
        result_hash = digest(response.get("result")) if status == "CALLED" else None
        if receipt.get("result_sha256") != result_hash:
            raise CaptureError("gateway result digest differs from receipt")
        event_id = self._append("peachme", "tool_return", parent_event_ids=[],
                                gateway_receipt_id=receipt_id, tool_status=status,
                                policy_outcome=outcome, arguments_sha256=digest(arguments),
                                tool_result_sha256=result_hash)
        return ToolEvidence(event_id, receipt_id, result_hash, status)

    async def invoke_peachme(self, gateway: Any, *, server: str, tool: str,
                             arguments: dict, work_ref: str) -> tuple[dict, ToolEvidence]:
        """Wrap a real async PeachMe.ToolGateway.invoke without altering its policy."""
        response = await gateway.invoke(server, tool, arguments, work_ref)
        observation = self.observe_peachme(response, server=server, tool=tool,
                                           arguments=arguments, work_ref=work_ref)
        return response, observation

    def observe_cherryme(self, source: Any, parent: ToolEvidence) -> str:
        """Accept an actual CherryMe RetrievedSource; retained digest may differ
        from PeachMe's full result digest because source extraction transforms it."""
        old = self._events.get(parent.event_id)
        if old is None or old["stage"] != "tool_return" or old["tool_status"] != "CALLED":
            raise CaptureError("source has no successful observed gateway parent")
        if getattr(source, "retrieval_receipt_id", None) != parent.receipt_id:
            raise CaptureError("source retrieval receipt mismatch")
        excerpt = getattr(source, "excerpt", None)
        excerpt_hash = getattr(source, "excerpt_sha256", None)
        url = getattr(source, "source_ref", None)
        if not isinstance(excerpt, str) or not excerpt.strip() or digest_text(excerpt) != excerpt_hash:
            raise CaptureError("source excerpt digest mismatch")
        _required(url, "source_ref")
        return self._append(
            "cherryme", "source_admitted", parent_event_ids=[parent.event_id],
            gateway_receipt_id=parent.receipt_id,
            gateway_result_sha256=parent.result_sha256,
            source_ref_sha256=digest_text(url), excerpt_sha256=excerpt_hash,
            transform_id="cherryme.GatewaySearchBackend.source_extraction")

    def observe_web_search(self, search: Any, parent: ToolEvidence) -> list[str]:
        if getattr(search, "receipt_id", None) != parent.receipt_id:
            raise CaptureError("WebSearch does not reference the observed receipt")
        return [self.observe_cherryme(source, parent) for source in getattr(search, "sources", ())]

    async def submit_model(self, *, sender: Callable[[Any], Any], payload: Any,
                           source_event_ids: list[str], model_id: str) -> tuple[Any, str]:
        """Record what the host handed to the FINAL model client callback.

        The payload is deep-copied and its hash checked again after sending.
        This proves only client submission, not that the external provider
        received or attended to the content.
        """
        _required(model_id, "model_id")
        if not source_event_ids or any(self._events.get(e, {}).get("stage") != "source_admitted"
                                       for e in source_event_ids):
            raise CaptureError("model submission requires observed CherryMe source parents")
        message = copy.deepcopy(payload)
        input_hash = digest(message)
        input_bytes = canonical(message)
        contains = b"ZOMBIE-CANARY-7F3A" in input_bytes
        status = "SUBMITTED"
        try:
            result = sender(message)
            if inspect.isawaitable(result):
                result = await result
        except Exception:
            status = "CLIENT_ERROR"
            self._append("plumme", "model_client_submit",
                         parent_event_ids=list(source_event_ids),
                         model_id=model_id, client_payload_sha256=input_hash,
                         inert_canary_present=contains, client_status=status)
            raise
        if digest(message) != input_hash:
            raise CaptureError("model client mutated input object during submission")
        event_id = self._append(
            "plumme", "model_client_submit", parent_event_ids=list(source_event_ids),
            model_id=model_id, client_payload_sha256=input_hash,
            inert_canary_present=contains, client_status=status)
        return result, event_id


def digest_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def audit_host_events(events: list[dict], keys: Mapping[str, bytes]) -> dict:
    """Independent, fail-closed structural verifier of the captured boundary chain."""
    if not events:
        raise CaptureError("empty Z01 host trace")
    seen: dict[str, dict] = {}
    root: tuple[str, str] | None = None
    count = {"tool_return": 0, "source_admitted": 0, "model_client_submit": 0}
    exposures = 0
    for seq, ev in enumerate(events, 1):
        if not isinstance(ev, dict) or ev.get("protocol") != PROTOCOL:
            raise CaptureError("invalid event protocol")
        stage, producer = ev.get("stage"), ev.get("producer")
        if STAGES.get(stage) != producer or not verify(ev, dict(keys)):
            raise CaptureError("invalid stage producer or signature")
        if type(ev.get("seq")) is not int or ev["seq"] != seq:
            raise CaptureError("event order/gap invalid")
        eid = ev.get("event_id")
        if not isinstance(eid, str) or not eid or eid in seen:
            raise CaptureError("duplicate event ID")
        identity = (ev.get("trace_id"), ev.get("work_ref"))
        if not all(isinstance(v, str) and v for v in identity) or (root and root != identity):
            raise CaptureError("mixed trace or work identities")
        root = identity
        parents = ev.get("parent_event_ids")
        if not isinstance(parents, list) or any(pid not in seen for pid in parents):
            raise CaptureError("missing or non-prior parent")
        if stage == "tool_return":
            if parents or not ev.get("gateway_receipt_id") or ev.get("tool_status") not in STATUS:
                raise CaptureError("invalid gateway event")
        elif stage == "source_admitted":
            if len(parents) != 1 or seen[parents[0]]["stage"] != "tool_return":
                raise CaptureError("source lacks gateway parent")
            parent = seen[parents[0]]
            if parent["tool_status"] != "CALLED" or parent["gateway_receipt_id"] != ev.get("gateway_receipt_id"):
                raise CaptureError("source detached from gateway receipt")
            if parent["tool_result_sha256"] != ev.get("gateway_result_sha256"):
                raise CaptureError("source origin digest changed")
            if not ev.get("excerpt_sha256") or not ev.get("source_ref_sha256"):
                raise CaptureError("missing source digest")
        else:
            if not parents or any(seen[p]["stage"] != "source_admitted" for p in parents):
                raise CaptureError("model-client submission lacks observed source parents")
            if ev.get("client_status") not in {"SUBMITTED", "CLIENT_ERROR"} or not ev.get("client_payload_sha256"):
                raise CaptureError("invalid model client submission")
            if ev.get("inert_canary_present") is True and ev["client_status"] == "SUBMITTED":
                exposures += 1
        seen[eid] = ev
        count[stage] += 1
    return {
        "protocol": PROTOCOL, "mode": "HOST_CLIENT_EVIDENCE_ONLY",
        "trace_id": root[0], "work_ref": root[1],
        "event_counts": count,
        "canary_in_submitted_client_payload": exposures,
        "provider_received_or_processed": "NOT_ATTESTED",
        "limitations": [
            "Host-only key separation must be proven outside the signed event data.",
            "A source-to-client parent link alone does not prove causality.",
            "Client submission cannot establish external model/provider ingestion.",
            "No live FruitStack run is implied by successful offline tests.",
        ],
    }
