# Judging criteria

How the expert jury, with expertise in digital autonomy, procurement and open-source development, weighs submissions. Four levels: **Must**, **Should**, **Should not**, **Could**.

A submission that fails any Must criterion is not a valid submission, regardless of how well it scores on the rest.

## ✅ Must: minimum requirements for a valid submission

| # | Criterion | How the jury checks |
|---|---|---|
| M1 | Working tool that produces a focused requirement set from a SEAL level and the scope of a procurement | Live demo or recording on at least two cases of different scope; the sets differ where the scope differs |
| M2 | Every selected requirement traceable to a public source | Source id or link per requirement |
| M3 | A reason for every requirement left out | The buyer can see why a requirement is not in the set |
| M4 | Selection rules explicit in code or configuration | Rules readable without the UI; no decision hidden in a prompt |
| M5 | Code and rules open source | Public repository, linked in Alkemio, under an OSI-approved licence (code) and CC BY 4.0 / CC0 (rules, docs) |

## ⭐ Should: distinguishing qualities

| # | Criterion | What it looks like |
|---|---|---|
| S1 | Works for different kinds of procurement | Demonstrated on the supplied cases in `cases/`, not tuned to one |
| S2 | Usable by non-technical users | A buyer or information manager gets through the question flow in about five minutes |
| S3 | Coverage against the DACC library | The jury compares your set for a case with the DACC requirement library: relevant requirements found, irrelevant ones left out |
| S4 | Aligned with existing frameworks and minimum requirements | Requirements fit GIBIT, the VNG cloud guidance or the EU Cloud Sovereignty Framework, and respect the floor from law and regulation |
| S5 | Library and rules maintainable separately from the interface | Changing a data file changes the outcome; tests show what changed |

## ⚠ Should not: pitfalls to avoid

| # | Pitfall | Why it weakens or disqualifies |
|---|---|---|
| X1 | A language model decides the SEAL level, the classification or the selection | Violates M4; not testable, not explainable. Using a model to find candidate requirements in sources is fine |
| X2 | Requirements that exclude suppliers without proportionate justification | Conflicts with procurement law; unusable in a real tender |
| X3 | Showing every requirement for a level | That is what tools do today; it leaves the selection to the buyer |
| X4 | "Autonomy washing" | Labelling everything as high risk, or adopting supplier claims without checking them |
| X5 | Non-reproducible or non-open code or rules | Violates M5; the jury cannot verify the method |

## ✨ Could: bonus for outstanding submissions

| # | Bonus | Evidence |
|---|---|---|
| C1 | Open-source viability | Indicators of contributor-community size and diversity for an open-source alternative, from public data |
| C2 | Link to the DACC maturity model | Process-level outcome connected to system-level classification |
| C3 | Usable by several organisations at once | For example a shared classification of common application families, supporting joint procurement |
| C4 | Translation from the classificatietoets to the DACC matrix | Process criticality and BIV mapped to criticality K1-K4 and data classification D1-D4, with the choices made explicit (they do not map one to one) |

## How judging works

Musts are pass or fail. Teams pitch per challenge in a first round (10 December, 14:00-15:00), a technical jury reviews every submission in Alkemio, and the best team per challenge goes to the final, where the grand jury scores six criteria from 1 to 5. See [EVENT.md](../EVENT.md#how-judging-works).
