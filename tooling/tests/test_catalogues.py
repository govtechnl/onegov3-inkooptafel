"""Checks that keep the starter data consistent. CI runs these on every push and PR."""

from __future__ import annotations

from pathlib import Path

import pytest

from inkooptafel import catalog

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


@pytest.mark.parametrize("name", sorted(catalog.CATALOGUES))
def test_catalogue_matches_schema(name):
    data = catalog.load_yaml(catalog.DATA_DIR / catalog.CATALOGUES[name])
    assert catalog.validate(name, data) == []


def test_examples_match_schemas():
    assert catalog.validate("assessment", catalog.load_yaml(EXAMPLES / "assessment-example.yaml")) == []
    assert catalog.validate("rules", catalog.load_yaml(EXAMPLES / "example-rules.yaml")) == []


def test_source_ids_unique():
    ids = [s["id"] for s in catalog.load("sources")["sources"]]
    assert len(ids) == len(set(ids))


def test_toets_question_ids_unique_and_complete():
    biv = catalog.load("toets")["biv"]
    expected = [("beschikbaarheid", "B", 7), ("integriteit", "I", 7), ("vertrouwelijkheid", "V", 8)]
    for key, prefix, n in expected:
        ids = [q["id"] for q in biv[key]["questions"]]
        assert ids == [f"{prefix}{i}" for i in range(1, n + 1)]


def test_v_decision_rules_only_reference_known_questions():
    v = catalog.load("toets")["biv"]["vertrouwelijkheid"]
    known = {q["id"] for q in v["questions"]}
    for rule in v["decision_rules"]:
        for key in ("if_any_yes", "if_all_no", "and_yes"):
            assert set(rule.get(key, [])) <= known


def test_example_rules_point_to_known_sources():
    known = {s["id"] for s in catalog.load("sources")["sources"]}
    for rule in catalog.load_yaml(EXAMPLES / "example-rules.yaml")["rules"]:
        for req in rule.get("requirements", []):
            assert req["source"] in known, f"{req['id']}: unknown source {req['source']!r}"


def test_bio2_advice_covers_every_score():
    biv = catalog.load("toets")["biv"]
    for block in ("beschikbaarheid", "integriteit"):
        assert set(biv[block]["bio2_advice"]) == {1, 2, 3, 4, 5}
