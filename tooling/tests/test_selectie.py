from __future__ import annotations

from pathlib import Path

from inkooptafel import catalog, selectie

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


def lib():
    return catalog.load_file("requirements", EXAMPLES / "example-requirements.yaml")


def ids(reqs):
    return {r["id"] for r in reqs}


def test_example_files_are_valid():
    catalog.load_file("scope", EXAMPLES / "scope-example.yaml")
    assert selectie.unknown_sources(lib()) == []


def test_level_filter():
    doc = {"seal": "SEAL-1", "scope": {"leverancier_beheert_dienst": True}}
    selected, _ = selectie.select(doc, lib())
    assert ids(selected) == {"VB-EXIT"}


def test_small_scope_gets_fewer_requirements_on_same_level():
    full = {"seal": "SEAL-3", "scope": {"persoonsgegevens": True, "hooggerubriceerd": True,
                                         "leverancier_beheert_dienst": True, "cloud": True, "ai": True}}
    licence_only = {"seal": "SEAL-3", "scope": {"persoonsgegevens": True, "hooggerubriceerd": True,
                                                 "leverancier_beheert_dienst": False, "cloud": False,
                                                 "ai": False}}
    big, _ = selectie.select(full, lib())
    small, _ = selectie.select(licence_only, lib())
    assert ids(small) < ids(big)


def test_every_left_out_requirement_has_a_reason():
    doc = catalog.load_file("scope", EXAMPLES / "scope-example.yaml")
    selected, left_out = selectie.select(doc, lib())
    assert len(selected) + len(left_out) == len(lib()["requirements"])
    assert all(reason for _, reason in left_out)


def test_unknown_flag_is_left_out_with_reason():
    doc = {"seal": "SEAL-3", "scope": {}}
    _, left_out = selectie.select(doc, lib())
    reasons = dict((r["id"], why) for r, why in left_out)
    assert "does not say" in reasons["VB-SLEUTELS"]
