# Case: Hosting en Technisch Applicatiebeheer (HenT), gemeente Amsterdam

> Public tender, not anonymised. Source: TenderNed, prior information notice TN-534511 (7 September 2025), [tenderned.nl/aankondigingen/overzicht/391737](https://www.tenderned.nl/aankondigingen/overzicht/391737). Year: 2025. Internal reference AICT2024-0184.
>
> Worked out from the public notice by GovTechNL as a starter case. The challenge owners may add or replace cases.

## The system or service

Outsourced hosting and technical application management (TAB) for the City of Amsterdam, in one lot:

- **Project services:** project management, design, build, testing, implementation, migration and changes.
- **Management services:** technical application management and ITSM processes (change, release, incident, problem, configuration, logging, audits, reporting).
- **Application services:** stacks, integration and middleware, databases, management tooling.
- **Infrastructure services:** virtual and physical servers, storage, cloud integration, backup and recovery. Co-location is optional.

The supplier first takes over **126 applications** from the current HenT contract, migrating them under the municipality's direction, then onboards new applications and decommissions old ones. Innovation is in scope, including AI, digital autonomy, quantum computing and post-quantum cryptography.

## The data

The notice does not list the applications. Because it covers a large part of the municipality's application landscape, it will include applications with personal data and, likely, special categories of personal data. The notice mentions "sensitive information" that should be hosted on-premise in the supplier's data centre.

## Criticality

The service hosts and manages the municipality's business applications, so an outage affects many processes at once, some of which will be on the IBD list of critical processes. The supplier has to meet agreed requirements for availability, integrity, confidentiality and performance, connect to the municipality's Generic Security Service and risk management process, provide Single Sign-On for all applications, and publish applications on the public internet with appropriate measures.

## Current situation

An existing HenT contract with an external supplier (no name in the notice). New contract from 23 February 2026, 5 years plus four optional extensions of 2 years (13 years in total). Estimated value EUR 153.4 million excluding VAT, about EUR 11.8 million a year. Performance location: the Netherlands.

## What was asked in the tender

- **Sovereignty:** on-premise sovereign hosting in the supplier's data centre for sensitive information; the supplier must be able to move cloud and SaaS applications from a hyperscaler back to a hosting environment. The municipality is also looking at the national government cloud (Rijkscloud).
- **No hard sovereignty requirements yet:** the notice says policy and technology are not mature enough, so it sketches wishes and frameworks and aligns the tender with the municipality's Digital Autonomy track.
- **Frameworks:** ITIL, the city's enterprise architecture (Stedelijke Enterprise Architectuur), the municipality's security and risk frameworks.
- **Award criteria:** quality 60 points (service catalogue with pay-per-use, vision and roadmap, operating model, migration approach), sustainability 10 points, price 30 points. Social return: at least 2% of the contract value.
- **Exit:** the notice does not describe an exit or end-of-contract transition.

## Questions for teams

- The notice deliberately sets no hard sovereignty requirements. What would your tool advise for a contract like this, and how do you deal with 126 applications that each have their own profile?
- Which applications or application groups would you classify first, and what SEAL minimum per sovereignty objective follows for the hosting layer as a whole?
- The notice has no exit clause. Which exit and transfer requirements would your tool add, and from which source (for example `handreiking-exit`, `vng-bestek-cloud` or `gibit`)?
- How do "move back from a hyperscaler" and "on-premise for sensitive information" translate into testable requirements or award criteria that stay proportionate?
