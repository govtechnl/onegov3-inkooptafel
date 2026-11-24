"""Map a system's answers on both axes to a classification pattern.

This is the deterministic core every team can build on: no AI, no interpretation,
just a lookup that can be read and tested.

Example:
    python -m inkooptafel.classify --kritikaliteit bedrijfskritiek \
        --gegevens persoonsgegevens
"""

from __future__ import annotations

import argparse
from pathlib import Path

from . import catalog


def classify(kritikaliteit: str, gegevensclassificatie: str, patterns_path: Path | None = None) -> dict:
    """Return the pattern that matches the two axis values.

    Raises ValueError for unknown values, so a tool never silently guesses.
    """
    classification = catalog.load("classification")
    allowed_k = catalog.axis_values(classification, "kritikaliteit")
    allowed_g = catalog.axis_values(classification, "gegevensclassificatie")
    if kritikaliteit not in allowed_k:
        raise ValueError(f"kritikaliteit must be one of {allowed_k}, got {kritikaliteit!r}")
    if gegevensclassificatie not in allowed_g:
        raise ValueError(
            f"gegevensclassificatie must be one of {allowed_g}, got {gegevensclassificatie!r}"
        )

    patterns = catalog.load("patterns", patterns_path)["patterns"]
    for pattern in patterns:
        if (
            pattern["kritikaliteit"] == kritikaliteit
            and pattern["gegevensclassificatie"] == gegevensclassificatie
        ):
            return pattern
    raise LookupError(f"No pattern for ({kritikaliteit}, {gegevensclassificatie})")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--kritikaliteit", required=True)
    parser.add_argument("--gegevens", required=True, dest="gegevensclassificatie")
    parser.add_argument("--patterns", type=Path, default=None, help="Alternative patterns file")
    args = parser.parse_args(argv)

    pattern = classify(args.kritikaliteit, args.gegevensclassificatie, args.patterns)
    level = pattern["sovereignty_level"] or "nog niet bepaald"
    print(f"Patroon {pattern['id']}: {pattern['kritikaliteit']} x {pattern['gegevensclassificatie']}")
    print(f"Geadviseerd soevereiniteitsniveau: {level}")
    print(f"Aantal eisen: {len(pattern['requirements'])}")


if __name__ == "__main__":
    main()
