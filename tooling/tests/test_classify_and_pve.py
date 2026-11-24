from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

from inkooptafel import classify, pve

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


def _load_vragenflow():
    spec = importlib.util.spec_from_file_location("vragenflow", EXAMPLES / "01_vragenflow.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_classify_returns_matching_pattern():
    p = classify.classify("bedrijfskritiek", "persoonsgegevens")
    assert p["kritikaliteit"] == "bedrijfskritiek"
    assert p["gegevensclassificatie"] == "persoonsgegevens"


def test_classify_rejects_unknown_values():
    with pytest.raises(ValueError):
        classify.classify("heel-kritiek", "openbaar")
    with pytest.raises(ValueError):
        classify.classify("bedrijfskritiek", "geheim")


def test_pve_without_requirements_says_so():
    p = classify.classify("niet-kritiek", "openbaar")
    out = pve.render(p["id"])
    assert "nog geen eisen" in out


def test_pve_example_lists_requirements_with_sources():
    out = pve.render("P03", EXAMPLES / "example-patterns.yaml")
    assert "P03-R1" in out
    assert "Gunningscriterium" in out


@pytest.mark.parametrize(
    "critical, answers, expected",
    [
        (True, {}, ("bedrijfskritiek", "openbaar")),
        (False, {"persoonsgegevens": True}, ("niet-kritiek", "persoonsgegevens")),
        (True, {"persoonsgegevens": True, "staatsgeheimen": True}, ("bedrijfskritiek", "staatsgeheimen")),
    ],
)
def test_vragenflow_highest_class_wins(critical, answers, expected):
    assert _load_vragenflow().decide(critical, answers) == expected
