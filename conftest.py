"""Sanitized pytest-html diagnostics; never persist secrets or raw model context."""
from __future__ import annotations

import os
import subprocess
from urllib.parse import urlsplit

import pytest


def _git(*args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", *args], text=True, stderr=subprocess.DEVNULL, timeout=2
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return "unavailable"


def _safe_target() -> str:
    url = os.environ.get("AGENT_ENDPOINT") or "not configured (offline only)"
    parsed = urlsplit(url)
    if not parsed.hostname:
        return url if url == "not configured (offline only)" else "configured (invalid URL)"
    # No path, query, userinfo or tokens in reports.
    return f"{parsed.scheme}://{parsed.hostname}"


def pytest_configure(config):
    config.addinivalue_line("markers", "remote: calls explicitly authorized remote staging endpoint")
    try:
        from pytest_metadata.plugin import metadata_key
        meta = config.stash[metadata_key]
        meta.pop("Packages", None)
        meta.pop("Plugins", None)
        meta["Target"] = _safe_target()
        meta["Model"] = os.environ.get("AGENT_MODEL_VERSION") or "NOT_PROVIDED"
        meta["Git Branch"] = _git("rev-parse", "--abbrev-ref", "HEAD")
        meta["Git Commit"] = _git("rev-parse", "--short=12", "HEAD")
        meta["Evidence"] = "offline unit tests and opt-in remote output checks; not a security certification"
    except ImportError:
        pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    metadata = getattr(item, "zombie_diagnostics", None)
    if not isinstance(metadata, dict):
        return
    try:
        import pytest_html
    except ImportError:
        return
    extras = list(getattr(report, "extras", []))
    extras.append(pytest_html.extras.json(metadata, name="Redacted diagnostic hashes"))
    report.extras = extras
