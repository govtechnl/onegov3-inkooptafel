# Classification model: the classificatietoets

> **Beta.** The classificatietoets is a beta version that is still being developed. Expect it to change after the hackathon.

The **classificatietoets** (process and data classification, steps 0 to 4) is one of the options for step 01 of this challenge. It was developed by Suzanne Kaufmann (Data Governance Lead, Gemeente Amsterdam) and others, and is used in a pilot in Amsterdam. It builds on BIO2 and takes the assessment from the process down to the critical data that process needs. The questions for availability (B) and integrity (I) largely follow the baseline classification questionnaire of the IBD (VNG).

Suzanne Kaufmann is at the hackathon on both days as content expert for the toets. Ask her how a question is meant.

Machine-readable version: [`data/toets.yaml`](../data/toets.yaml). Code: [`tooling/inkooptafel/toets.py`](../tooling/inkooptafel/toets.py).

## Five steps: from broad to targeted

| Step | Name | What you do | Output |
|---|---|---|---|
| 0 | Proces en dienst | Determine importance and the impact of failure | Scoped process, process owner, **proceskritikaliteit**, provisional **BIV** of the process |
| 1 | Activiteiten | Map the work and dependencies, in the order the work happens | Activities A1, A2, ... |
| 2 | Kritieke data | Choose the critical data sets and the critical data elements (fields) | Data sets D1, D2, ... and elements D1.1, D1.2, ... |
| 3 | Bron en taken | Record the official source, systems and responsible teams | Source, systems and teams per critical data set |
| 4 | BIV en afspraken | Assess each critical data element on B, I and V | B, I and V per element, and agreements on management, quality and suppliers |

Only critical data and the most important data elements go through to step 4. That way protection, quality controls, recovery agreements and **supplier requirements** focus on the data with the highest risk.

## The building blocks

### Proceskritikaliteit (step 0)

| Value | When |
|---|---|
| Kritiek | Formally designated as critical, or serious consequences after 72 hours of failure and no reliable fallback |
| Kern | Important municipal task; consequences of failure can be absorbed temporarily |
| Ondersteunend | Mainly supports steering, planning or management; the main task can continue for now |
| Onbekend | Consequences still unclear; the process owner has this investigated |

GEMMA helps to type the process; the criticality decides how much attention it gets.

### BIV (step 0 for the process, step 4 per critical data element)

- **B, beschikbaarheid (availability):** seven questions (B1 to B7), each mapped to a score of 1 to 5. A shorter acceptable outage or recovery time means a higher score.
- **I, integriteit (integrity):** seven questions (I1 to I7), each scored 1 to 5.
- **V, vertrouwelijkheid (confidentiality):** eight yes/no questions (V1 to V8) and decision rules that give **Openbaar**, **Vertrouwelijk** or **Geheim**.

Rules that matter for your code:

- For B and I the final score is the **highest** score. **Never add up, never average.**
- B, I and V remain **separate** classifications.
- Personal data are in principle at least Vertrouwelijk, but do not automatically get the highest level.
- "Weet ik niet" means: find out. Do not guess.
- The process outcome from step 0 is context for step 4, not something to copy.

### From outcome to agreements

The toets ends with what to discuss and record. For this challenge the last row is the important one:

| What needs attention | Discuss and record |
|---|---|
| High availability score | Management: back-up, recovery, emergency access, continuity, recovery time |
| High integrity score | Quality: controls, standards, corrections, source agreements |
| High confidentiality or a sensitive signal | Management and security: access, logging, masking, control |
| Critical data and data elements | Management: risk, protection, resources, who monitors progress |
| **Dependency on a supplier or platform** | **Supplier and autonomy: storage location, access, export, transfer, recovery, exit and possibly a SEAL assessment** |

## What is missing, and where you come in

The toets tells you **what** is critical and **how** sensitive it is. It does **not** say which sovereignty level or which supplier requirements follow. The toets is explicit about this:

> The SEAL level does not follow automatically from the BIV score; the assessment is about the concrete service being procured.

That is the core of the challenge:

1. Turn the toets into a usable tool: a question flow that produces a **profile** (proceskritikaliteit, B, I, V, supplier dependency).
2. Design **rules** that go from that profile, plus what you know about the service being procured, to an advised sovereignty level (for example a SEAL minimum per objective). See [sovereignty-levels.md](sovereignty-levels.md).
3. Use minimum requirements from law and regulation as the floor. See [sources.md](sources.md).
4. Produce requirements and award criteria for the programme of requirements (PvE). See [procurement-context.md](procurement-context.md).

## Design choices you will have to make

- **Process or data element?** The toets classifies both. Which one drives the supplier requirements of a tender, and how do you combine several data elements in one service?
- **Kern versus Ondersteunend** is a judgement of the process owner. Support that judgement; do not replace it.
- **What does "high" mean?** The toets says "hoge score" without a threshold. If your rules use one (for example B of 4 or more), state it and test it.
- **Beyond BIV.** SEAL concerns the service: jurisdiction, operations, supply chain, exit. Which extra questions about the service does your tool ask?

## The earlier simplified view

Before the toets was available, the challenge used a simplified matrix from the VNG *Uitvoeringsstrategie Cloud* work: business-critical or not, times five data classes (openbaar, door wet- en regelgeving gebonden, persoonsgegevens, bijzondere persoonsgegevens, staatsgeheimen), giving ten patterns linked to mitigating measures from the Handreiking Cloud. You may use it as a quick entry or a sanity check.

If you think the toets is wrong or incomplete, say so in your pitch or open an issue. Do not change `data/toets.yaml` silently.
