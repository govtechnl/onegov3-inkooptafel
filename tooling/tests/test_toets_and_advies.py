from __future__ import annotations

from pathlib import Path

import pytest

from inkooptafel import advies, catalog, toets

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
ALL_NO = {f"V{i}": "nee" for i in range(1, 8)}


# --- Beschikbaarheid and integriteit: highest score wins, never an average ----------------

def test_b_takes_highest_not_average():
    score, decided_by = toets.score_beschikbaarheid({"B1": "meer-dan-twee-weken", "B3": "max-4-werkuren"})
    assert score == 5
    assert decided_by == ["B3"]


def test_b_rejects_unknown_choice():
    with pytest.raises(ValueError):
        toets.score_beschikbaarheid({"B1": "maand"})


def test_i_takes_highest():
    assert toets.score_integriteit({"I1": 2, "I2": 4, "I6": 1}) == (4, ["I2"])


def test_unanswered_gives_none():
    assert toets.score_integriteit({}) == (None, [])


# --- Vertrouwelijkheid decision rules ------------------------------------------------------

@pytest.mark.parametrize(
    "answers, expected",
    [
        ({**ALL_NO, "V8": "ja"}, "openbaar"),
        ({**ALL_NO, "V8": "nee"}, "onbekend"),
        ({**ALL_NO, "V5": "ja"}, "vertrouwelijk"),
        ({**ALL_NO, "V5": "ja", "V3": "ja"}, "geheim"),
        ({**ALL_NO, "V5": "ja", "V1": "weet-ik-niet"}, "onbekend"),
        ({**ALL_NO, "V7": "ja", "V8": "ja"}, "geheim"),
    ],
)
def test_v_rules(answers, expected):
    assert toets.vertrouwelijkheid(answers)[0] == expected


# --- Proceskritikaliteit -------------------------------------------------------------------

@pytest.mark.parametrize(
    "answers, expected",
    [
        ({"formeel_kritiek": True}, "kritiek"),
        ({"gevolg_72u": "ernstig", "noodoplossing": "nee"}, "kritiek"),
        ({"gevolg_72u": "onbekend", "noodoplossing": "ja"}, "onbekend"),
        ({"gevolg_72u": "merkbaar", "noodoplossing": "ja"}, toets.NEEDS_JUDGEMENT),
        ({"gevolg_72u": "merkbaar", "noodoplossing": "ja", "oordeel": "ondersteunend"}, "ondersteunend"),
    ],
)
def test_proceskritikaliteit(answers, expected):
    assert toets.proceskritikaliteit(answers)[0] == expected


# --- Example end-to-end -------------------------------------------------------------------

def _example_profile():
    return toets.profile(catalog.load_file("assessment", EXAMPLES / "assessment-example.yaml"))


def test_example_profile():
    p = _example_profile()
    assert (p["proceskritikaliteit"], p["B"], p["I"], p["V"]) == ("kern", 4, 3, "vertrouwelijk")


def test_advice_combines_highest_seal_and_dedups():
    p = _example_profile()
    rules = catalog.load_file("rules", EXAMPLES / "example-rules.yaml")
    advice = advies.advise(p, rules)
    matched = [m["id"] for m in advice["matched"]]
    assert matched == ["VB-PERSOONSGEGEVENS", "VB-LEVERANCIER", "VB-HOGE-BESCHIKBAARHEID"]
    assert advice["sovereignty"]["SOV-4"] == "SEAL-3"
    ids = [r["id"] for r in advice["requirements"]]
    assert len(ids) == len(set(ids))


def test_render_lists_sources():
    p = _example_profile()
    rules = catalog.load_file("rules", EXAMPLES / "example-rules.yaml")
    out = advies.render(p, advies.advise(p, rules))
    assert "Gunningscriterium" in out
    assert "Algemene verordening gegevensbescherming" in out
