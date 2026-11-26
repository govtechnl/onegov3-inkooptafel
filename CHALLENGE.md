# Challenge Brief | Van beleid naar inkooptafel

> **OneGov #3** · Challenge 2 · DACC & VNG Realisatie · 9-10 December 2026 · The Hague Tech, Den Haag
>
> *Is this system business-critical? What data does it hold? And which requirements does this procurement really need? You build the tool that answers that in five minutes.*
>
> **Challenge owners:** Jacco Brouwer (VNG Realisatie), Thijs Turèl (DACC / AMS Institute)
> **Contact:** [hack@govtechnl.nl](mailto:hack@govtechnl.nl)

This is an English working translation of the Dutch challenge brief. The authoritative version is the Dutch brief on Alkemio.

---

## Background

Digital autonomy is high on the Dutch government agenda. In December 2025 the cabinet presented its vision on digital autonomy and sovereignty for government (*Visie Digitale autonomie en soevereiniteit van de overheid*). Municipalities align with it through the VNG position paper, and in July 2026 five Dutch regulators (ACM, AFM, AP, DNB and RDI) called on government bodies to weigh digital autonomy explicitly when buying IT.

So there is plenty of policy. But it disappears at the procurement table, because nobody can make it concrete. A buyer who tenders a new system has to decide how much autonomy that system needs, and what they may require from a supplier without breaching procurement law.

The answer is not "everything maximally sovereign". Not every system needs the same level of autonomy: a staff rostering tool is different from the population register. That is why instruments exist to classify a system. The *classificatietoets*, in use in a pilot in Amsterdam, takes a process down to its critical data and scores **process criticality** and **availability, integrity and confidentiality (BIV)**. The DACC's procurement-requirements tool uses a matrix of **criticality** and **data classification** to arrive at an indicative SEAL level.

After that, it stops being useful. Today's tool shows the buyer **every** requirement for the chosen level, and the buyer has to strike out what does not fit. A small procurement for a single module, on a high SEAL level, does not need the full list. That is where teams come in.

The Digital Autonomy Competence Centre (DACC) is a collaboration of, among others, AMS Institute, VNG, Digicampus, the Ministry of the Interior (BZK), TU Delft and the City of Amsterdam. It develops instruments that show what does and does not work towards digital autonomy, such as the *Volwassenheidsmodel Digitale Autonomie* for primary processes. This challenge takes that work to the level of the individual system and the individual tender, together with VNG Realisatie.

## Problem statement

Buyers and information managers who want to weigh autonomy all hit the same walls:

- Policy on digital autonomy is abstract. A tender needs testable requirements and award criteria.
- There is no shared, fast way to decide which sovereignty level a specific system needs. A uniformly high level is unaffordable and often not proportionate.
- Classification (what is critical?) and procurement (what do we ask for?) are separate worlds. The outcome of one does not flow into the other.
- Buyers often do not know how much room procurement law gives them. Fearing objections, they leave autonomy out.

## The challenge

> *How do we give a buyer the requirements that fit their procurement: matched not only to the SEAL level, but also to what is actually being bought, with an explanation for every requirement that is left out?*

You build the step after the SEAL level: a tool that, from the level and the scope of the procurement, assembles a focused requirement set from public sources, and demonstrates it on several procurement cases. The tool goes through three steps:

| Step | What happens |
|---|---|
| **01 Classify** | Short. Use the classificatietoets ([`docs/classification-model.md`](docs/classification-model.md)) or the two axes of the DACC matrix: criticality and data classification. Outcome: a profile. |
| **02 SEAL level** | The indicative SEAL level comes from the DACC matrix. You do not have to invent this step. |
| **03 Focused requirement set (the core)** | From the SEAL level **and** the scope of the procurement, the tool assembles the requirements and award criteria that fit, from public sources, each traceable to its source. For every requirement it leaves out, it says why. Exportable (e.g. `.docx` or `.md`) and demonstrated on several cases. See [`docs/requirements.md`](docs/requirements.md). |

## Guiding questions

1. Which facts about a procurement decide whether a requirement applies? Think of personal data, highly classified data, who operates the service, cloud or on-premise, AI.
2. How do you build a requirement library from public sources such as the EU Cloud Sovereignty Framework, the VNG cloud guidance, GIBIT and PIANOo, while keeping every requirement traceable?
3. Which minimum requirements from law and regulation (such as the AVG and the Cyberbeveiligingswet) always form the floor, whatever the scope?
4. How do you explain to a buyer why a requirement is left out, so they can defend that choice in a tender?
5. How do you keep the library and the selection rules separate from the tool, so they can be updated when policy or frameworks change?

## Personas

Two example personas. See [`docs/personas.md`](docs/personas.md).

- **Sanne**, ICT procurement adviser at a mid-sized municipality: *"I don't want to know what autonomy is. I want to know what I'm allowed to require."*
- **Ahmed**, information manager at a municipality: *"Not everything has to be sovereign. But I have to be able to explain why one thing is and the other isn't."*

## Who we are looking for

Developers, UX designers, procurement and contract specialists, information security officers and lawyers who want to build something tangible. The strongest teams combine someone who writes code with someone who knows what a tender looks like from the inside.

## Starting point: open source and open rules

**Toets, demo and cases.** This repository holds the classificatietoets, an overview of relevant law and regulation, procurement cases of different scope in [`cases/`](cases/), and a starter format for a requirement library and a scope. A demo of the DACC procurement-requirements tool, without its requirements, follows. What is already here is listed in the [README](README.md#whats-in-here).

**Not shared.** The DACC's own requirement library is not shared with teams: it contains strategically sensitive material. The challenge owners use it as a checklist for the jury. Some other material is shared with registered teams on Alkemio only. Do not put material that is shared on Alkemio only into your repository, your prompts or your pitch deck.

**Software.** You are free in your technical approach: a decision-rule engine, a declarative rule format (YAML or JSON) or an existing rules-as-code framework. A language model may help you find and extract candidate requirements from public sources, as long as every requirement keeps its source. The SEAL level, the classification and the selection must be explicit and testable. All code and rules are released open source after the hackathon. See [`docs/rules-as-code.md`](docs/rules-as-code.md).

## Technical framing

- **Rules-as-code.** Decision rules are explicit in code or configuration and can be read and tested without the interface. Ship a few test cases that show the rules do what the model prescribes.
- **Traceability.** Every classification, measure and requirement points to its source: the toets, a framework (such as GIBIT or the EU Cloud Sovereignty Framework) or legislation. See [`docs/sources.md`](docs/sources.md).
- **Sovereignty levels.** The toets itself does not give a sovereignty level. The DACC matrix gives an indicative SEAL level; use it as the input to step 03. The SEAL scale comes from the EU Cloud Sovereignty Framework (SEAL-0 to SEAL-4). Minimum requirements from law and regulation form the floor. See [`docs/sovereignty-levels.md`](docs/sovereignty-levels.md).
- **Scope-based selection.** Two procurements on the same SEAL level can need very different requirement sets. The selection depends on explicit facts about the procurement, and every requirement left out has a reason. See [`docs/requirements.md`](docs/requirements.md).
- **Proportionality.** Requirements must be in proportion to the classification. A tool that excludes suppliers without justification does not help the buyer. See [`docs/procurement-context.md`](docs/procurement-context.md).
- **Open source.** All code, rules and documentation are published open source after the hackathon.

## Judging criteria

Teams are judged by an expert jury with expertise in digital autonomy, procurement and open-source development. Full table: [`docs/judging-criteria.md`](docs/judging-criteria.md).

### ✅ Must

- A working tool that, from a SEAL level and the scope of a procurement, produces a focused requirement set instead of the full list for that level.
- Every selected requirement is traceable to a public source.
- For every requirement left out, the tool says why.
- The selection rules are explicit in code or configuration, not hidden in a prompt.
- Code and rules are published open source, for example via GitHub.

### ⭐ Should

- The tool is demonstrated on the supplied procurement cases and works for different kinds of procurement, not for one case only.
- The question flow is usable by a buyer or information manager without a technical background, in about five minutes.
- Requirements align with existing frameworks such as GIBIT, the VNG cloud guidance or the EU Cloud Sovereignty Framework, and respect minimum requirements from law and regulation.
- The requirement library and the selection rules can be maintained separately from the interface.

### ⚠ Should not

- A language model that decides the SEAL level, the classification or the selection itself. It may help find requirements in sources, but the decisions must be testable.
- Showing every requirement for a level and leaving the selection to the buyer: that is what tools do today.
- Requirements that exclude suppliers without proportionate justification and thereby conflict with procurement law.
- "Autonomy washing": a tool that labels everything as high risk or adopts supplier claims without checking them.
- Code or rules that are not reproducible or not available open source.

### ✨ Could (bonus)

- **Open-source viability:** the tool helps assess whether an open-source alternative is and stays reliable and viable, for example through the size and diversity of its contributor community (active contributors, spread across organisations and countries, activity over time).
- A translation from the classificatietoets (process criticality, BIV) to the axes of the DACC matrix (criticality K1-K4, data classification D1-D4). They do not map one to one.
- The tool links to the DACC *Volwassenheidsmodel Digitale Autonomie*, so process level and system level connect.
- The output can be used by several organisations at once, for example for joint procurement.

## Deliverables

- A working tool (web app, CLI or similar) that produces a focused requirement set from a SEAL level and the scope of a procurement.
- The requirement library and the selection rules as separate, readable configuration or code, with test cases.
- Worked examples of at least two procurement cases of different scope: SEAL level, scope, the selected requirements and the reasons for what was left out.
- The source code, published open source via GitHub.
- A pitch (max. 3 minutes) and a pitch deck (max. 10 slides).

## Submission

Submissions go through [Alkemio](https://alkem.io/onegov-hackathon), the central submission and review platform for OneGov.

**Deadline: Thursday 10 December 2026, 14:00.**

Each team submits, via Alkemio:

1. A **link to your public repository** (your fork of this repository, or your own), with an open source licence and a README that says how to run your work.
2. The **worked procurement cases** (SEAL level, scope, selected requirements and reasons for what was left out).
3. The **pitch deck** (max. 10 slides, PDF or link).

The Alkemio submission is your submission: the jury scores what is in Alkemio. A Pull Request into this repository is welcome but optional.

## Why join

- Results are published on [digitale-autonomie.nl](https://digitale-autonomie.nl) and the DACC uses them as input for further development of its procurement model. You work on something that goes further than a demo in a drawer.
- You build with developers, designers and administrators from municipalities, central government and the open-source community.
- You work directly with the challenge owners from the DACC and VNG Realisatie on a question that is on the table right now.
- Everything you make is open source and carries your name.
- Every tender in which autonomy counts concretely is a step away from irreversible dependency.

## Disclaimer

The tools and rules produced during this hackathon are published as open source. Use in real tenders depends on further substantive and legal review by the challenge owners. This challenge is an innovation exercise; outcomes are not legal advice.

Challenge owners: Jacco Brouwer (VNG Realisatie) · Thijs Turèl (DACC / AMS Institute) · Questions: [hack@govtechnl.nl](mailto:hack@govtechnl.nl)
