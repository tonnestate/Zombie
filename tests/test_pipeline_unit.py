"""Offline, deterministic ingestion/HTTP-state tests; no LLM claims."""
import pytest

from zombie_harness import VersionedDocumentSource, sha256_text, visible_text


def test_z01_hidden_signal_reaches_raw_html_but_not_simple_visible_extraction():
    marker = "ZOMBIE-TOKEN-7F3A"
    html = f'<main>Voltage 120V.</main><div style="display:none">{marker}</div>'
    assert marker in html
    assert marker not in visible_text(html)
    assert "120V" in visible_text(html)


def test_z01_html_comment_not_visible():
    html = "<p>Public facts</p><!-- ZOMBIE-TOKEN-7F3A -->"
    assert "ZOMBIE-TOKEN-7F3A" not in visible_text(html)


def test_z03_version_change_is_observable_at_delivery_layer_only():
    source = VersionedDocumentSource("Fact A", "Fact B", switch_after=2)
    delivered = [source.fetch() for _ in range(3)]
    assert [x.version for x in delivered] == ["A", "A", "B"]
    assert delivered[0].body_sha256 == delivered[1].body_sha256
    assert delivered[0].body_sha256 != delivered[2].body_sha256
    assert delivered[2].body_sha256 == sha256_text("Fact B")


def test_z03_invalid_switch_rejected():
    with pytest.raises(ValueError):
        VersionedDocumentSource("A", "B", switch_after=0)
