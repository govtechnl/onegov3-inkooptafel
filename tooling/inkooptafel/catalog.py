"""Load and validate the YAML files in data/ and team files against data/schemas/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"
SCHEMA_DIR = DATA_DIR / "schemas"

# Catalogues shipped with the repo: name -> file in data/
CATALOGUES = {
    "toets": "toets.yaml",
    "sources": "sources.yaml",
}


def load_yaml(path: Path) -> Any:
    with Path(path).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_schema(schema: str) -> dict:
    with (SCHEMA_DIR / f"{schema}.schema.json").open(encoding="utf-8") as fh:
        return json.load(fh)


def validate(schema: str, data: Any) -> list[str]:
    """Return readable schema errors (empty list when valid)."""
    validator = Draft202012Validator(load_schema(schema))
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
    return [f"{'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}" for e in errors]


def load_file(schema: str, path: Path) -> Any:
    """Load any YAML file and raise ValueError if it does not match the schema."""
    data = load_yaml(path)
    errors = validate(schema, data)
    if errors:
        raise ValueError(f"{path} does not match {schema}.schema.json:\n  " + "\n  ".join(errors))
    return data


def load(name: str) -> Any:
    """Load a catalogue shipped in data/ by name ('toets' or 'sources')."""
    return load_file(name, DATA_DIR / CATALOGUES[name])
