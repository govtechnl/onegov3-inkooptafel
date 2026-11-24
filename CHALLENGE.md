# Challenge Brief | Van classificatie naar inkooptafel

> **OneGov #3** · Challenge 2 · DACC & VNG Realisatie · 9-10 December 2026 · The Hague Tech, Den Haag
>
> *Is this system business-critical? What data does it hold? And what should you then require from your supplier? You build the tool that answers that in five minutes.*
>
> **Challenge owners:** Jacco Brouwer (VNG Realisatie), Thijs Turel (DACC / AMS Institute)
> **Contact:** [hack@govtechnl.nl](mailto:hack@govtechnl.nl)

This is an English working translation of the Dutch challenge brief. The authoritative version is the Dutch brief on Alkemio.

---

## Background

Digital autonomy is high on the Dutch government agenda. In December 2025 the cabinet presented its vision on digital autonomy and sovereignty for government (*Visie Digitale autonomie en soevereiniteit van de overheid*). Municipalities align with it through the VNG position paper, and in July 2026 five Dutch regulators (ACM, AFM, AP, DNB and RDI) called on government bodies to weigh digital autonomy explicitly when buying IT.

So there is plenty of policy. But it disappears at the procurement table, because nobody can make it concrete. A buyer who tenders a new system has to decide how much autonomy that system needs, and what they may require from a supplier without breaching procurement law.

The answer is not "everything maximally sovereign". Not every system needs the same level of autonomy: a staff rostering tool is different from the population register. That is why there is a classification model: combine the **business criticality** of a system with the **sensitivity of its data**, and you know how much weight the system carries. The translation from there to a sovereignty level does not exist yet. That is where teams come in.

The Digital Autonomy Competence Centre (DACC) is a collaboration of, among others, AMS Institute, VNG, Digicampus, the Ministry of the Interior (BZK), TU Delft and the City of Amsterdam. It develops instruments that show what does and does not work towards digital autonomy, such as the *Volwassenheidsmodel Digitale Autonomie* for primary processes. This challenge takes that work to the level of the individual system and the individual tender, together with VNG Realisatie.

## Problem statement

Buyers and information managers who want to weigh autonomy all hit the same walls:

- Policy on digital autonomy is abstract. A tender needs testable requirements and award criteria.
- There is no shared, fast way to decide which sovereignty level a specific system needs. A uniformly high level is unaffordable and often not proportionate.
- Classification (what is critical?) and procurement (what do we ask for?) are separate worlds. The outcome of one does not flow into the other.
- Buyers often do not know how much room procurement law gives them. Fearing objections, they leave autonomy out.

## The challenge

> *How do we turn a classification model for digital autonomy into a tool that buyers and information managers can use tomorrow: classify a system, advise a well-founded sovereignty level, and get requirements that go straight into the tender documents?*

You turn the model's rules into working code (rules-as-code), design a smart question flow around it and demonstrate the whole on a real procurement case. The tool goes through three steps:

| Step | What happens |
|---|---|
| **01 Classify** | A smart question flow places a system in a few minutes. How business-critical is it? How sensitive is the data? Does it touch a critical process on the IBD list? Outcome: a pattern. See [`docs/classification-model.md`](docs/classification-model.md). |
| **02 Advise a level** | You translate the pattern into a well-founded sovereignty level. This part does not exist yet. Which minimum requirements apply anyway under law and regulation? Why, traceable to the source? What is proportionate? |
| **03 Get requirements** | The buyer gets requirements, award criteria and example wording that go straight into the tender. Exportable (e.g. `.docx` or `.md`), demonstrated on a real case. |

## Guiding questions

1. How do you turn the classification model into explicit, testable decision rules, so every outcome can be explained?
2. Which questions must a non-technical user answer to reach a reliable classification in a few minutes?
3. Which sovereignty level fits a pattern, and which minimum requirements from law and regulation (such as NORA and the Cyberbeveiligingswet) form the floor? How do you translate that into requirements and award criteria that are proportionate and fit procurement law?
4. How do you keep the model separate from the tool, so the rules can be updated when policy or frameworks change?

## Personas

Two example personas. See [`docs/personas.md`](docs/personas.md).

- **Sanne**, ICT procurement adviser at a mid-sized municipality: *"I don't want to know what autonomy is. I want to know what I'm allowed to require."*
- **Ahmed**, information manager at a municipality: *"Not everything has to be sovereign. But I have to be able to explain why one thing is and the other isn't."*

## Who we are looking for

Developers, UX designers, procurement and contract specialists, information security officers and lawyers who want to build something tangible. The strongest teams combine someone who writes code with someone who knows what a tender looks like from the inside.

## Starting point: open source and open rules

**Model and cases.** The challenge owners supply the classification model, an overview of relevant law and regulation, the IBD list of critical processes for municipalities and one or more anonymised procurement cases through this repository. What is already here is listed in the [README](README.md#whats-in-here).

**Software.** You are free in your technical approach: a decision-rule engine, a declarative rule format (YAML or JSON) or an existing rules-as-code framework. AI may help with explanation or the question flow, but the classification itself must be testable. All code and rules are released open source after the hackathon. See [`docs/rules-as-code.md`](docs/rules-as-code.md).

## Technical framing

- **Rules-as-code.** Decision rules are explicit in code or configuration and can be read and tested without the interface. Ship a few test cases that show the rules do what the model prescribes.
- **Traceability.** Every classification, measure and requirement points to its source: the model, a framework (such as GIBIT or the EU Cloud Sovereignty Framework) or legislation. See [`docs/sources.md`](docs/sources.md).
- **Sovereignty levels.** The classification model does not yet give a sovereignty level. Teams advise which level fits a pattern and justify it. The SEAL scale from the EU Cloud Sovereignty Framework (SEAL-0, no sovereignty, to SEAL-4, full digital sovereignty) can serve as a reference. Minimum requirements from law and regulation form the floor. See [`docs/sovereignty-levels.md`](docs/sovereignty-levels.md).
- **Proportionality.** Requirements must be in proportion to the classification. A tool that excludes suppliers without justification does not help the buyer. See [`docs/procurement-context.md`](docs/procurement-context.md).
- **Open source.** All code, rules and documentation are published open source after the hackathon.

## Judging criteria

Teams are judged by an expert jury with expertise in digital autonomy, procurement and open-source development. Full table: [`docs/judging-criteria.md`](docs/judging-criteria.md).

### ✅ Must

- A working tool that classifies a system on business criticality and data sensitivity, based on the supplied classification model.
- Per pattern, the tool advises a sovereignty level, with a justification traceable to the model and the sources.
- The tool produces requirements or criteria a buyer can use in tender documents.
- Decision rules are explicit in code or configuration (rules-as-code), not hidden in a prompt.
- Code and rules are published open source, for example via GitHub.

### ⭐ Should

- Every outcome is traceable: the user sees why a system falls in a pattern and which source a requirement comes from.
- The question flow is usable by a buyer or information manager without a technical background, in about five minutes.
- The whole is demonstrated on one of the supplied procurement cases.
- Requirements align with existing frameworks such as GIBIT, the VNG cloud tender template or the EU Cloud Sovereignty Framework, and take minimum requirements from law and regulation into account.
- The model can be maintained separately from the interface, so rules can be updated without rebuilding the tool.

### ⚠ Should not

- An LLM that interprets legal texts and thereby decides the classification itself. AI may help, but the decision rules must be testable.
- Requirements that exclude suppliers without proportionate justification and thereby conflict with procurement law.
- "Autonomy washing": a tool that labels everything as high risk or adopts supplier claims without checking them.
- Code or rules that are not reproducible or not available open source.

### ✨ Could (bonus)

- **Open-source viability:** the tool helps assess whether an open-source alternative is and stays reliable and viable, for example through the size and diversity of its contributor community (active contributors, spread across organisations and countries, activity over time).
- The tool links to the DACC *Volwassenheidsmodel Digitale Autonomie*, so process level and system level connect.
- The output can be used by several organisations at once, for example for joint procurement.

## Deliverables

- A working tool (web app, CLI or similar) that classifies, advises a sovereignty level and generates requirements.
- The decision rules as separate, readable configuration or code, with test cases.
- A worked example of at least one procurement case: classification, advised level and the requirements the tool produces.
- The source code, published open source via GitHub.
- A pitch (max. 3 minutes) and a pitch deck (max. 10 slides).

## Submission

Submissions go through **Alkemio**, the central submission and review platform for OneGov. The link to the challenge space follows.

Each team submits, via Alkemio:

1. A **link to the team's Pull Request** on this repository, one PR per team (see [CONTRIBUTING.md](CONTRIBUTING.md)).
2. The **worked procurement case** (classification, advised level, requirements).
3. The **pitch deck** (max. 10 slides, PDF or link).

The Alkemio submission is what the jury scores during the hackathon. The Pull Request is still required: it is leading for the post-hackathon review.

## Why join

- Results are published on [digitale-autonomie.nl](https://digitale-autonomie.nl) and the DACC uses them as input for further development of its procurement model. You work on something that goes further than a demo in a drawer.
- You build with developers, designers and administrators from municipalities, central government and the open-source community.
- You work directly with the challenge owners from the DACC and VNG Realisatie on a question that is on the table right now.
- Everything you make is open source and carries your name.
- Every tender in which autonomy counts concretely is a step away from irreversible dependency.

## Disclaimer

The tools and rules produced during this hackathon are published as open source. Use in real tenders depends on further substantive and legal review by the challenge owners. This challenge is an innovation exercise; outcomes are not legal advice.

Challenge owners: Jacco Brouwer (VNG Realisatie) · Thijs Turel (DACC / AMS Institute) · Questions: [hack@govtechnl.nl](mailto:hack@govtechnl.nl)
