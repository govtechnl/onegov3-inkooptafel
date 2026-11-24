"""From a toets profile to sovereignty advice and a programme-of-requirements (PvE) fragment.

This is the part of the challenge that does not exist yet. The engine is deliberately
simple: teams write the rules (data/schemas/rules.schema.json); this module only
evaluates them, combines the outcome and renders it with a source per requirement.

Example (illustrative rules, not advice):
    python -m inkooptafel.advies examples/assessment-example.yaml --rules examples/example-rules.yaml
"""

from __future__ import annotations

import argparse
from pathlib import Path

from . import catalog, toets

SEAL_ORDER = ["SEAL-0", "SEAL-1", "SEAL-2", "SEAL-3", "SEAL-4"]
TYPE_LABEL = {"eis": "Eis", "gunningscriterium": "Gunningscriterium"}


def matches(when: dict, p: dict) -> bool:
    if "proceskritikaliteit_in" in when and p["proceskritikaliteit"] not in when["proceskritikaliteit_in"]:
        return False
    if "b_min" in when and (p["B"] is None or p["B"] < when["b_min"]):
        return False
    if "i_min" in when and (p["I"] is None or p["I"] < when["i_min"]):
        return False
    if "v_in" in when and p["V"] not in when["v_in"]:
        return False
    if "leveranciersafhankelijk" in when and p["leveranciersafhankelijk"] != when["leveranciersafhankelijk"]:
        return False
    return True


def advise(p: dict, rules: dict) -> dict:
    """Evaluate all rules. Returns matched rule ids, the combined SEAL minimum per
    objective (highest wins) and the de-duplicated requirements."""
    matched = [r for r in rules["rules"] if matches(r["when"], p)]
    sovereignty: dict[str, str] = {}
    for r in matched:
        for obj, level in r.get("sovereignty", {}).items():
            current = sovereignty.get(obj)
            if current is None or SEAL_ORDER.index(level) > SEAL_ORDER.index(current):
                sovereignty[obj] = level
    requirements, seen = [], set()
    for r in matched:
        for req in r.get("requirements", []):
            if req["id"] not in seen:
                seen.add(req["id"])
                requirements.append({**req, "rule": r["id"]})
    return {
        "matched": [{"id": r["id"], "rationale": r["rationale"]} for r in matched],
        "sovereignty": dict(sorted(sovereignty.items())),
        "requirements": requirements,
    }


def render(p: dict, advice: dict, sources: dict | None = None) -> str:
    sources = sources or {s["id"]: s for s in catalog.load("sources")["sources"]}
    lines = ["## Soevereiniteitsadvies", "", toets.format_profile(p), ""]
    if not advice["matched"]:
        lines.append("_Geen regels van toepassing op dit profiel._")
        return "\n".join(lines) + "\n"

    lines += ["### Waarom", ""]
    lines += [f"- **{m['id']}**: {m['rationale']}" for m in advice["matched"]]
    if advice["sovereignty"]:
        lines += ["", "### Minimaal SEAL-niveau per doel", "", "| Doel | Minimum |", "|---|---|"]
        lines += [f"| {k} | {v} |" for k, v in advice["sovereignty"].items()]
    if advice["requirements"]:
        lines += ["", "### Eisen en gunningscriteria", "", "| # | Type | Tekst | Bron | Regel |",
                  "|---|---|---|---|---|"]
        for r in advice["requirements"]:
            src = sources.get(r["source"], {"name": f"onbekende bron '{r['source']}'"})
            name = f"[{src['name']}]({src['url']})" if src.get("url") else src["name"]
            lines.append(f"| {r['id']} | {TYPE_LABEL[r['type']]} | {r['text']} | {name} | {r['rule']} |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("assessment", type=Path)
    parser.add_argument("--rules", type=Path, required=True)
    args = parser.parse_args(argv)
    p = toets.profile(catalog.load_file("assessment", args.assessment))
    rules = catalog.load_file("rules", args.rules)
    print(render(p, advise(p, rules)), end="")


if __name__ == "__main__":
    main()
