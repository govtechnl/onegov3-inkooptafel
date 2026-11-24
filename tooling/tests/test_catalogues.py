"""Checks that keep the starter data consistent. CI runs these on every push and PR."""

from __future__ import annotations

import itertools
from pathlib import Path

import pytest

from inkooptafel import catalog

EXAMPLE_PATTERNS = Path(__file__).resolve().parents[1] / "examples" / "example-patterns.yaml"


@pytest.mark.parametrize("name", sorted(catalog.CATALOGUES))
def test_catalogue_matches_schema(name):
    data = catalog.load_yaml(catalog.DATA_DIR / catalog.CATALOGUES[name])
    assert catalog.validate(name, data) == []


def test_example_patterns_match_schema():
    assert catalog.validate("patterns", catalog.load_yaml(EXAMPLE_PATTERNS)) == []


def test_source_ids_unique():
    ids = [s["id"] for s in catalog.load("sources")["sources"]]
    assert len(ids) == len(set(ids))


@pytest.mark.parametrize("path", [None, EXAMPLE_PATTERNS])
def test_patterns_cover_every_combination_once(path):
    classification = catalog.load("classification")
    expected = set(
        itertools.product(
            catalog.axis_values(classification, "kritikaliteit"),
            catalog.axis_values(classification, "gegevensclassificatie"),
        )
    )
    patterns = catalog.load("patterns", path)["patterns"]
    combos = [(p["kritikaliteit"], p["gegevensclassificatie"]) for p in patterns]
    assert len(combos) == len(set(combos)), "a combination appears more than once"
    assert set(combos) == expected
    ids = [p["id"] for p in patterns]
    assert len(ids) == len(set(ids)), "pattern ids must be unique"


@pytest.mark.parametrize("path", [None, EXAMPLE_PATTERNS])
def test_every_requirement_points_to_a_known_source(path):
    known = {s["id"] for s in catalog.load("sources")["sources"]}
    for pattern in catalog.load("patterns", path)["patterns"]:
        for req in pattern["requirements"]:
            assert req["source"] in known, f"{req['id']}: unknown source {req['source']!r}"
