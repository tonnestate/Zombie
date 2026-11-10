"""Project ZOMBIE: isolated IPI test harness components (not an agent)."""
from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import urlsplit

import requests


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


_VOID_TAGS = frozenset({"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"})


class _VisibleHTML(HTMLParser):
    """Deliberately limited HTML text extractor for pipeline unit tests."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden: list[bool] = []
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in _VOID_TAGS:
            # Void elements have no end tag: never shift visibility frames.
            return
        a = dict(attrs)
        style = "".join((a.get("style") or "").lower().split())
        invisible = (
            tag in {"script", "style", "template", "noscript"}
            or "hidden" in a
            or "display:none" in style
            or "visibility:hidden" in style
            or a.get("aria-hidden") == "true"
        )
        self.hidden.append(invisible or (self.hidden[-1] if self.hidden else False))

    def handle_startendtag(self, tag, attrs):
        # Void tags may be self-closing; do not retain their hidden state.
        pass

    def handle_endtag(self, tag):
        if tag in _VOID_TAGS:
            return
        if self.hidden:
            self.hidden.pop()

    def handle_data(self, data):
        if not any(self.hidden):
            self.parts.append(data)


def visible_text(html: str) -> str:
    """Toy extractor: NOT a browser-equivalent DOM/visibility implementation."""
    parser = _VisibleHTML()
    parser.feed(html)
    return " ".join(" ".join(parser.parts).split())


@dataclass(frozen=True)
class DocumentDelivery:
    request_number: int
    version: str
    body: str
    body_sha256: str


class VersionedDocumentSource:
    """Deterministic stand-in for a lab-owned server; no agent identification."""

    def __init__(self, a: str, b: str, switch_after: int):
        if switch_after < 1:
            raise ValueError("switch_after must be positive")
        self.a = a
        self.b = b
        self.switch_after = switch_after
        self.calls = 0

    def fetch(self) -> DocumentDelivery:
        self.calls += 1
        version = "A" if self.calls <= self.switch_after else "B"
        body = self.a if version == "A" else self.b
        return DocumentDelivery(self.calls, version, body, sha256_text(body))


def authorized_endpoint() -> str | None:
    """Never contact a real agent implicitly; require explicit opt-in."""
    url = os.environ.get("AGENT_ENDPOINT", "").strip()
    if not url:
        return None
    if os.environ.get("ZOMBIE_AUTHORIZED_TARGET") != "YES":
        raise RuntimeError("Set ZOMBIE_AUTHORIZED_TARGET=YES for an authorized staging target")
    parsed = urlsplit(url)
    if parsed.scheme not in {"https", "http"} or not parsed.hostname:
        raise ValueError("AGENT_ENDPOINT must be a valid HTTP(S) URL")
    if parsed.scheme != "https" and parsed.hostname not in {"localhost", "127.0.0.1", "::1"}:
        raise ValueError("Remote targets require HTTPS")
    if parsed.username or parsed.password or parsed.fragment:
        raise ValueError("Credentials or fragments in AGENT_ENDPOINT are prohibited")
    return url


def call_agent(task: str, retrieved_content: str) -> dict:
    url = authorized_endpoint()
    if url is None:
        raise RuntimeError("No AGENT_ENDPOINT configured: remote IPI tests must SKIP")
    key = os.environ.get("AGENT_API_KEY", "")
    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = f"Bearer {key}"
    response = requests.post(
        url,
        json={"task": task, "retrieved_content": retrieved_content},
        headers=headers,
        timeout=(5, 30),
        allow_redirects=False,
    )
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict) or not isinstance(data.get("response"), str):
        raise ValueError("Agent endpoint must return a JSON object with string 'response'")
    return data


def diagnostic(result: object) -> dict:
    """Report only structure and hashes, never raw prompts or private agent output."""
    if isinstance(result, dict):
        return {
            "response_sha256": sha256_text(str(result.get("response", ""))),
            "response_chars": len(str(result.get("response", ""))),
            "tool_audit_available": isinstance(result.get("tool_calls"), list),
            "tool_call_count": len(result["tool_calls"]) if isinstance(result.get("tool_calls"), list) else None,
        }
    return {"result_type": type(result).__name__}
