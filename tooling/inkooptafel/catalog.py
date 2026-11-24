"""Load and validate the YAML catalogues in data/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"
SCHEMA_DIR = DATA_DIR / "schemas"

CATALOGUES = {
    "classification": "classification.yaml",
    "patterns": "patterns.yaml",
    "sources": "sources.yaml",
}


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_schema(name: str) -> dict:
    with (SCHEMA_DIR / f"{name}.schema.json").open(encoding="utf-8") as fh:
        return json.load(fh)


def validate(name: str, data: Any) -> list[str]:
    """Return a list of readable schema errors (empty when valid)."""
    validator = Draft202012Validator(load_schema(name))
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
    return [f"{'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}" for e in errors]


def load(name: str, path: Path | None = None) -> Any:
    """Load a catalogue by name and raise ValueError if it does not match its schema."""
    data = load_yaml(path or DATA_DIR / CATALOGUES[name])
    errors = validate(name, data)
    if errors:
        raise ValueError(f"{name} is invalid:\n  " + "\n  ".join(errors))
    return data


def axis_values(classification: dict, axis_id: str) -> list[str]:
    for axis in classification["axes"]:
        if axis["id"] == axis_id:
            return [v["id"] for v in axis["values"]]
    raise KeyError(f"Unknown axis: {axis_id}")
