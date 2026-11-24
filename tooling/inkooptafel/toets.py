"""The classificatietoets as code: from answers to a toets profile.

A profile is the outcome of the questionnaire for one process or data element:
proceskritikaliteit, a B score, an I score and a V level. Everything here follows
the rules in data/toets.yaml:

- B and I: the final score is the highest score of the questions. Never add, never average.
- V: decision rules (Geheim > Vertrouwelijk > Openbaar); "weet ik niet" that could change
  the outcome gives "onbekend" (find out, do not guess).
- Proceskritikaliteit: only decided automatically where the questionnaire is explicit;
  otherwise the process owner's judgement ("oordeel") is required.

The SEAL level does NOT follow from this profile. That step is the challenge; see advies.py.

Example:
    python -m inkooptafel.toets examples/assessment-example.yaml
"""

from __future__ import annotations

import argparse
from pathlib import Path

from . import catalog

NEEDS_JUDGEMENT = "beoordeling-nodig"


def proceskritikaliteit(answers: dict) -> tuple[str, str]:
    """Return (value, reason). Explicit 'oordeel' of the process owner wins."""
    if "oordeel" in answers:
        return answers["oordeel"], "oordeel proceseigenaar"
    if answers.get("formeel_kritiek"):
        return "kritiek", "formeel als kritiek aangewezen"
    gevolg = answers.get("gevolg_72u", "onbekend")
    nood = answers.get("noodoplossing", "onbekend")
    if gevolg in {"ernstig", "zeer-ernstig"} and nood == "nee":
        return "kritiek", f"gevolg bij 72 uur uitval {gevolg} en geen noodoplossing"
    if gevolg == "onbekend" or nood == "onbekend":
        return "onbekend", "gevolg of noodoplossing onbekend: laten uitzoeken"
    # Kern versus Ondersteunend is a judgement in the questionnaire, not a rule.
    return NEEDS_JUDGEMENT, "kern of ondersteunend: oordeel van de proceseigenaar nodig"


def score_beschikbaarheid(answers: dict, toets: dict | None = None) -> tuple[int | None, list[str]]:
    """Highest score over the answered B questions, plus the question(s) that decided it."""
    toets = toets or catalog.load("toets")
    questions = {q["id"]: q for q in toets["biv"]["beschikbaarheid"]["questions"]}
    scores: dict[str, int] = {}
    for qid, choice in answers.items():
        if qid not in questions:
            raise ValueError(f"Unknown B question: {qid}")
        choices = questions[qid]["choices"]
        if choice not in choices:
            raise ValueError(f"{qid}: choice must be one of {list(choices)}, got {choice!r}")
        scores[qid] = choices[choice]
    return _max(scores)


def score_integriteit(answers: dict, toets: dict | None = None) -> tuple[int | None, list[str]]:
    """Highest score over the answered I questions (each already on the 1-5 scale)."""
    toets = toets or catalog.load("toets")
    known = {q["id"] for q in toets["biv"]["integriteit"]["questions"]}
    for qid in answers:
        if qid not in known:
            raise ValueError(f"Unknown I question: {qid}")
    return _max(dict(answers))


def vertrouwelijkheid(answers: dict, toets: dict | None = None) -> tuple[str, list[str]]:
    """Apply the V decision rules from data/toets.yaml. Returns (level, deciding questions)."""
    toets = toets or catalog.load("toets")
    rules = {r["level"]: r for r in toets["biv"]["vertrouwelijkheid"]["decision_rules"]}
    yes = {q for q, a in answers.items() if a == "ja"}
    unknown = {q for q, a in answers.items() if a == "weet-ik-niet"}

    geheim_q = set(rules["geheim"]["if_any_yes"])
    if yes & geheim_q:
        return "geheim", sorted(yes & geheim_q)
    if unknown & geheim_q:
        return "onbekend", sorted(unknown & geheim_q)

    vertr_q = set(rules["vertrouwelijk"]["if_any_yes"])
    if yes & vertr_q:
        return "vertrouwelijk", sorted(yes & vertr_q)
    if unknown & vertr_q:
        return "onbekend", sorted(unknown & vertr_q)

    open_rule = rules["openbaar"]
    all_no = all(answers.get(q) == "nee" for q in open_rule["if_all_no"])
    confirmed = all(answers.get(q) == "ja" for q in open_rule["and_yes"])
    if all_no and confirmed:
        return "openbaar", list(open_rule["and_yes"])
    return "onbekend", ["niet alle vragen beantwoord of openbaarheid niet gecontroleerd (V8)"]


def profile(assessment: dict, toets: dict | None = None) -> dict:
    """Turn a full assessment (see data/schemas/assessment.schema.json) into a profile."""
    toets = toets or catalog.load("toets")
    a = assessment["assessment"]
    kritikaliteit, k_reason = proceskritikaliteit(a.get("proceskritikaliteit", {}))
    b, b_from = score_beschikbaarheid(a.get("beschikbaarheid", {}), toets)
    i, i_from = score_integriteit(a.get("integriteit", {}), toets)
    v, v_from = vertrouwelijkheid(a.get("vertrouwelijkheid", {}), toets)
    return {
        "object": a["object"],
        "level": a["level"],
        "proceskritikaliteit": kritikaliteit,
        "proceskritikaliteit_reden": k_reason,
        "B": b,
        "B_bepaald_door": b_from,
        "I": i,
        "I_bepaald_door": i_from,
        "V": v,
        "V_bepaald_door": v_from,
        "leveranciersafhankelijk": a.get("leveranciersafhankelijk", False),
    }


def _max(scores: dict[str, int]) -> tuple[int | None, list[str]]:
    if not scores:
        return None, []
    top = max(scores.values())
    return top, sorted(q for q, s in scores.items() if s == top)


def format_profile(p: dict) -> str:
    def s(x):
        return "onbekend (niet beantwoord)" if x is None else f"{x} / 5"

    return "\n".join([
        f"Object: {p['object']} ({p['level']})",
        f"Proceskritikaliteit: {p['proceskritikaliteit']} ({p['proceskritikaliteit_reden']})",
        f"B: {s(p['B'])}  bepaald door {', '.join(p['B_bepaald_door']) or '-'}",
        f"I: {s(p['I'])}  bepaald door {', '.join(p['I_bepaald_door']) or '-'}",
        f"V: {p['V']}  bepaald door {', '.join(p['V_bepaald_door']) or '-'}",
        f"Afhankelijk van leverancier of platform: {'ja' if p['leveranciersafhankelijk'] else 'nee'}",
    ])


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("assessment", type=Path, help="YAML file with answers")
    args = parser.parse_args(argv)
    assessment = catalog.load_file("assessment", args.assessment)
    print(format_profile(profile(assessment)))


if __name__ == "__main__":
    main()
