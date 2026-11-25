# Judging criteria

How the expert jury, with expertise in digital autonomy, procurement and open-source development, weighs submissions. Four levels: **Must**, **Should**, **Should not**, **Could**.

A submission that fails any Must criterion is not a valid submission, regardless of how well it scores on the rest.

## ✅ Must: minimum requirements for a valid submission

| # | Criterion | How the jury checks |
|---|---|---|
| M1 | Working tool that classifies a process and its critical data on process criticality and BIV, based on the supplied toets | Live demo or recording; the outcome follows the rules in `data/toets.yaml` |
| M2 | For each outcome an advised sovereignty level, with a traceable justification | Rationale linked to the toets and to sources |
| M3 | Output a buyer can use in tender documents | Requirements and/or award criteria, labelled as such |
| M4 | Decision rules explicit in code or configuration | Rules readable without the UI; no decision hidden in a prompt |
| M5 | Code and rules open source | Public repository, linked in Alkemio, under an OSI-approved licence (code) and CC BY 4.0 / CC0 (rules, docs) |

## ⭐ Should: distinguishing qualities

| # | Criterion | What it looks like |
|---|---|---|
| S1 | Traceability | The user sees which answers led to the classification and which source each requirement comes from |
| S2 | Usable by non-technical users | A buyer or information manager gets through the question flow in about five minutes |
| S3 | Demonstrated on a supplied case | Worked example from `cases/` in your repository and your Alkemio submission |
| S4 | Aligned with existing frameworks and minimum requirements | Requirements fit GIBIT, the VNG cloud template or the EU Cloud Sovereignty Framework, and respect the floor from law and regulation |
| S5 | Rules maintainable separately from the interface | Changing a data file changes the outcome; tests show what changed |

## ⚠ Should not: pitfalls to avoid

| # | Pitfall | Why it weakens or disqualifies |
|---|---|---|
| X1 | An LLM interprets legal texts and decides the classification | Violates M4; not testable, not explainable |
| X2 | Requirements that exclude suppliers without proportionate justification | Conflicts with procurement law; unusable in a real tender |
| X3 | "Autonomy washing" | Labelling everything as high risk, or adopting supplier claims without checking them |
| X4 | Non-reproducible or non-open code or rules | Violates M5; the jury cannot verify the method |

## ✨ Could: bonus for outstanding submissions

| # | Bonus | Evidence |
|---|---|---|
| C1 | Open-source viability | Indicators of contributor-community size and diversity for an open-source alternative, from public data |
| C2 | Link to the DACC maturity model | Process-level outcome connected to system-level classification |
| C3 | Usable by several organisations at once | For example a shared classification of common application families, supporting joint procurement |

## How judging works

Musts are pass or fail. Teams pitch per challenge in a first round (10 December, 14:00-15:00), a technical jury reviews every submission in Alkemio, and the best team per challenge goes to the final, where the grand jury scores six criteria from 1 to 5. See [EVENT.md](../EVENT.md#how-judging-works).
