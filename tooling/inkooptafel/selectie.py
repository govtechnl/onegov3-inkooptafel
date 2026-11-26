"""From a SEAL level and a procurement scope to a focused requirement set.

Step 03 of the challenge. Showing every requirement for a SEAL level is what tools do
today; the buyer then has to strike out what does not fit. This module keeps only the
requirements whose scope conditions hold, and says for every requirement it leaves out
why. The library format is data/schemas/requirements.schema.json; the scope format is
data/schemas/scope.schema.json.

Example (illustrative library, not advice):
    python -m inkooptafel.selectie examples/scope-example.yaml --library examples/example-requirements.yaml
"""

from __future__ import annotations

import argparse
from pathlib import Path

from . import catalog


def check(req: dict, seal: str, scope: dict) -> str | None:
    """Return None if the requirement applies, otherwise the reason it is left out."""
    if seal not in req["levels"]:
        return f"not part of {seal} (levels: {', '.join(req['levels'])})"
    for flag, wanted in (req.get("applies_when") or {}).items():
        if flag not in scope:
            return f"scope does not say whether '{flag}' holds"
        if scope[flag] != wanted:
            return f"applies only when '{flag}' is {str(wanted).lower()}"
    return None


def select(scope_doc: dict, library: dict) -> tuple[list[dict], list[tuple[dict, str]]]:
    """Split the library into (selected, [(left_out, reason), ...])."""
    seal, scope = scope_doc["seal"], scope_doc["scope"]
    selected, left_out = [], []
    for req in library["requirements"]:
        reason = check(req, seal, scope)
        if reason is None:
            selected.append(req)
        else:
            left_out.append((req, reason))
    return selected, left_out


def unknown_sources(library: dict) -> list[str]:
    known = {s["id"] for s in catalog.load("sources")["sources"]}
    return sorted({r["source"] for r in library["requirements"]} - known)


def render(scope_doc: dict, selected: list[dict], left_out: list[tuple[dict, str]]) -> str:
    lines = [f"# {scope_doc.get('name', 'Selection')}", "", f"SEAL level: {scope_doc['seal']}", ""]
    lines.append(f"## Selected ({len(selected)})")
    for r in selected:
        lines.append(f"- [{r['id']}] ({r['type']}) {r['text']}  _source: {r['source']}_")
    lines += ["", f"## Left out ({len(left_out)})"]
    for r, reason in left_out:
        lines.append(f"- [{r['id']}] {reason}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("scope", type=Path, help="YAML file in the format of scope.schema.json")
    ap.add_argument("--library", type=Path, required=True, help="requirements.schema.json format")
    args = ap.parse_args(argv)
    scope_doc = catalog.load_file("scope", args.scope)
    library = catalog.load_file("requirements", args.library)
    missing = unknown_sources(library)
    if missing:
        raise SystemExit(f"Unknown source ids (not in data/sources.yaml): {', '.join(missing)}")
    print(render(scope_doc, *select(scope_doc, library)))


if __name__ == "__main__":
    main()
