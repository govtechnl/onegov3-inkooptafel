"""Render a programme-of-requirements (PvE) fragment for one pattern as Markdown.

Every requirement is printed with the source it comes from, so the output stays
traceable when an inkoper pastes it into a bestek.

Example:
    python -m inkooptafel.pve P03
    python -m inkooptafel.pve P03 --patterns examples/example-patterns.yaml
"""

from __future__ import annotations

import argparse
from pathlib import Path

from . import catalog

TYPE_LABEL = {"eis": "Eis", "gunningscriterium": "Gunningscriterium"}


def render(pattern_id: str, patterns_path: Path | None = None) -> str:
    patterns = {p["id"]: p for p in catalog.load("patterns", patterns_path)["patterns"]}
    sources = {s["id"]: s for s in catalog.load("sources")["sources"]}
    if pattern_id not in patterns:
        raise KeyError(f"Unknown pattern id: {pattern_id}")
    p = patterns[pattern_id]

    lines = [
        f"## Soevereiniteitseisen, patroon {p['id']}",
        "",
        f"- **Kritikaliteit:** {p['kritikaliteit']}",
        f"- **Gegevensclassificatie:** {p['gegevensclassificatie']}",
        f"- **Geadviseerd niveau:** {p['sovereignty_level'] or 'nog niet bepaald'}",
    ]
    if p["rationale"]:
        lines.append(f"- **Onderbouwing:** {p['rationale']}")
    lines.append("")

    if not p["requirements"]:
        lines.append("_Voor dit patroon zijn nog geen eisen vastgelegd._")
        return "\n".join(lines) + "\n"

    lines += ["| # | Type | Eis | Bron |", "|---|---|---|---|"]
    for r in p["requirements"]:
        src = sources.get(r["source"], {"name": f"onbekende bron '{r['source']}'"})
        name = f"[{src['name']}]({src['url']})" if src.get("url") else src["name"]
        lines.append(f"| {r['id']} | {TYPE_LABEL[r['type']]} | {r['text']} | {name} |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pattern_id")
    parser.add_argument("--patterns", type=Path, default=None)
    args = parser.parse_args(argv)
    print(render(args.pattern_id, args.patterns), end="")


if __name__ == "__main__":
    main()
