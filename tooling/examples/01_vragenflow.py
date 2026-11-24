"""Minimal question flow: from a few yes/no questions to a pattern and a PvE fragment.

One possible design, not the prescribed one. It makes two choices you may want to
challenge in your own solution:

1. Criticality is asked as a single question, informed by the IBD list of
   critical processes.
2. Data classification takes the most sensitive class that applies
   ("highest class wins").

Run:
    python examples/01_vragenflow.py
    python examples/01_vragenflow.py --patterns examples/example-patterns.yaml
"""

from __future__ import annotations

import argparse
from pathlib import Path

from inkooptafel import classify, pve

# Most sensitive first: the first "ja" decides the class.
DATA_QUESTIONS = [
    ("staatsgeheimen", "Verwerkt het systeem staatsgeheimen?"),
    ("bijzondere-persoonsgegevens", "Verwerkt het systeem bijzondere persoonsgegevens (bijv. gezondheid)?"),
    ("persoonsgegevens", "Verwerkt het systeem persoonsgegevens?"),
    ("wettelijk-gebonden", "Gelden er wettelijke regels voor de gegevens (bijv. archief, geheimhouding)?"),
]


def decide(critical: bool, data_answers: dict[str, bool]) -> tuple[str, str]:
    """Turn answers into the two axis values. Pure function, easy to test."""
    kritikaliteit = "bedrijfskritiek" if critical else "niet-kritiek"
    for value, _question in DATA_QUESTIONS:
        if data_answers.get(value):
            return kritikaliteit, value
    return kritikaliteit, "openbaar"


def ask(question: str) -> bool:
    while True:
        answer = input(f"{question} [j/n] ").strip().lower()
        if answer in {"j", "ja", "y", "yes"}:
            return True
        if answer in {"n", "nee", "no"}:
            return False
        print("Antwoord met j of n.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Minimal classification question flow")
    parser.add_argument("--patterns", type=Path, default=None)
    args = parser.parse_args()

    critical = ask("Ondersteunt het systeem een kritiek proces (zie de IBD-lijst)?")
    data_answers: dict[str, bool] = {}
    for value, question in DATA_QUESTIONS:
        data_answers[value] = ask(question)
        if data_answers[value]:
            break

    kritikaliteit, gegevens = decide(critical, data_answers)
    pattern = classify.classify(kritikaliteit, gegevens, args.patterns)
    print()
    print(pve.render(pattern["id"], args.patterns))


if __name__ == "__main__":
    main()
