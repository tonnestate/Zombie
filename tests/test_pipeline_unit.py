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


def test_z01_void_inside_hidden_element_keeps_later_visible_text():
    html = '<div style="display:none">SECRET<img src=x></div><p>VISIBLE-FACT</p>'
    result = visible_text(html)
    assert result == "VISIBLE-FACT"
    assert "SECRET" not in result


def test_z01_voids_outside_hidden_regions_do_not_corrupt_visibility():
    html = '<p>VISIBLE-A<br><img src=x><input value="META"></p><div hidden>HIDDEN-MARKER</div><p>VISIBLE-B</p>'
    result = visible_text(html)
    assert result == "VISIBLE-A VISIBLE-B"
    assert "HIDDEN-MARKER" not in result


def test_z01_orphan_void_endtag_does_not_pop_hidden_region():
    html = '<div hidden>SECRET</br>ALSO-SECRET</div><p>VISIBLE</p>'
    result = visible_text(html)
    assert result == "VISIBLE"
