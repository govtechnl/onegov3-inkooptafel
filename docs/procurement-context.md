# Procurement context: what you should know

> *You do not need to be a procurement lawyer to compete. But knowing where the walls and doors are will save you from building a tool that produces requirements nobody can use.*

This page summarises the context. It is **not legal advice**. Ask a mentor with procurement or legal expertise, or check the original sources.

## Requirements and award criteria

In a tender, the buyer works with a **programme of requirements** (*programma van eisen*, PvE) inside the tender documents (*bestek*):

- **Requirements** (*eisen*) are knock-out: an offer that does not meet them is excluded.
- **Award criteria** (*gunningscriteria*) are scored: offers that pass the requirements are compared on them.

Your tool should label each output as one or the other. A sovereignty minimum (such as a minimum SEAL level) is typically a requirement; how far a supplier goes beyond it can be an award criterion. The EU Cloud Sovereignty Framework works in exactly this way (see [sovereignty-levels.md](sovereignty-levels.md)).

## Proportionality

Dutch procurement law requires requirements to be proportionate to the contract. In practice: every requirement should be explainable from the nature of the system, the data and the risks. That is why an advice per classification outcome is more defensible than "maximum sovereignty for everything".

Design consequences for your tool:

- Show **why** a requirement applies (toets outcome, level, source).
- Prefer requirements that describe an **outcome or guarantee** (for example: data and control not subject to non-European extraterritorial law) over requirements that name a technology or a supplier.
- Flag when a combination of requirements may sharply narrow the market, so the buyer can make a conscious choice.

## There is more room than buyers often think

At the Unconference Digitale Autonomie (May 2026), the Dutch competition authority ACM stressed that governments often have more legal room to set market conditions than they think, as long as they do not distort competition unnecessarily. In July 2026, five Dutch regulators (ACM, AFM, AP, DNB and RDI) recommended that governments explicitly weigh digital autonomy when procuring IT. Sources: [Dutch IT Channel, 3 July 2026](https://www.dutchitchannel.nl/news/754870/digitale-autonomie-leeft-bij-overheid), [RDI: De route naar digitale autonomie](https://www.rdi.nl/documenten/2026/07/10/de-route-naar-digitale-autonomie).

## Existing building blocks to align with

- **GIBIT**, the municipal IT purchasing conditions (VNG).
- **VNG cloud tender template** (programme of requirements for PaaS and IaaS).
- **IBD Proportioneel Leveranciers- en Contractmanagement (PLC).**
- **EU Cloud Sovereignty Framework**, as used by the European Commission in its own cloud procurement.

Links are in [sources.md](sources.md).

## Things that make a jury nervous

- Requirements that exclude suppliers by name or by country of origin without a legal basis.
- Requirements copied from a law without saying which article they come from.
- A tool that presents its output as a legal conclusion rather than an advice to a buyer.
