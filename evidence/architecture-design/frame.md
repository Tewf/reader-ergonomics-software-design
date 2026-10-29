# Frame: the problem and its names

This file states, in one sentence, the problem of choosing the structure of a software system, then the names research and practice give to it and to its parts.

## The problem in one sentence

Choose how one software system is divided into parts and how the parts depend on each other, before it is built, so that it meets its quality goals and stays cheap to change.

## What the field calls it

| Our phrase | Field name |
|---|---|
| choosing the structure | **software architecture design**, **architecting** (Hofmeister 2007; Bass 2021) |
| a method for it | **attribute-driven design (ADD)**, driven by quality goals (Cervantes 2016) |
| the quality goals | **quality attributes**, written as scenarios; the standard list is ISO/IEC 25010 (ISO 2023c) |
| a way to reach a goal | **architectural tactic**, a design decision made to affect one quality attribute (as the field states it; Bass 2021, book not opened) |
| the shape chosen | **architectural style** or **pattern**, a family of architectures that share characteristics and constrain elements and relations (Microsoft 2025); the seminal catalogue of styles is Shaw 1996 (book, not opened) |
| the principle of division | **information hiding**: a module hides a decision likely to change behind an interface (Parnas 1972; as the field states it, the paper was not re-read) |
| the measures of division | **coupling** (dependence between modules) and **cohesion** (how focused one module is) (Stevens 1974; SESE 2012k) |
| the dependency matrix | **design structure matrix (DSM)**, **design rule space** (Baldwin 2000; Xiao 2014) |
| checking before building | **architecture evaluation**: SAAM, **ATAM** (Kazman 2000; Babar 2004) |
| structure decays | **architecture erosion**, **degradation**, **decay**, **smells** (de Silva 2012; Li 2022; Le 2018) |
| the cost of decay | **architectural technical debt (ATD)**: big design decisions that later hinder progress (Verdecchia 2021) |
| structure and the team | **Conway's law**, the **mirroring hypothesis** (Conway 1968; Colfer 2016) |
| how much to decide early | **up-front design**, **agile architecture** (Abrahamsson 2010; Waterman 2015) |
| how architects think | **design reasoning**, **satisficing**, **naturalistic** against **rational** decision making, **cognitive bias** (Tang 2015; Zannier 2007; Mohanani 2020) |
| whether team and structure fit | **socio-technical congruence**: the fit between the coordination a task needs and the coordination done (Cataldo 2008) |
| where debt sits | **architecture root**, **hotspot**, **design rule space** (Kazman 2015; Mo 2015) |

## What practitioners call it

- **Microservices**, **monolith**, **modular monolith**, **majestic monolith** (Lewis 2014; Fowler 2015; SESE 2020c).
- **Domain-driven design (DDD)**: organise software around a model of the business domain (Evans 2003, book not opened); a service holds one **bounded context** (Microsoft 2025).
- **Evolutionary architecture** and **architectural fitness function**: an automated check that a characteristic still holds (Ford 2017; ThoughtWorks 2017).
- **Inverse Conway maneuver** and **team topologies**: shape the teams to get the structure wanted (ThoughtWorks 2014; Skelton 2025).
- **Well-architected framework** and **architecture styles guide**: vendor checklists by pillar (AWS 2026d; Microsoft 2025).
- **Loosely coupled teams**, the delivery-performance name for loose coupling (DORA 2025).
- **Deep modules**: a small interface over much function (Ousterhout 2021; book not opened).
- The words differ more than the content: "service", "module", "component" and "package" overlap (SESE 2020c).

## The method named

- This review is a multivocal literature review after Garousi 2019, described in the [evidence method](../README.md#method). The [protocol](protocol.md) states the searches and [sources](sources.md) the pool.
- Grey tiers: tier 1 high outlet control (books, standards, reports); tier 2 moderate (project pages, Q/A sites); tier 3 low (blogs).

## Questions

- Q1 to Q11 are listed in [protocol](protocol.md), section 2.
- Q10 is the strand "designing for a model as implementer"; Q11 is how architects reason.

## Search terms tried, three ways

- Academic: design reasoning, socio-technical congruence, architecture roots, software architecture design, architecting, attribute-driven design, architectural tactics, information hiding, design structure matrix, architecture evaluation, architecture erosion, architectural technical debt, mirroring hypothesis, microservices granularity.
- Acronym: ADD, QAS, ATAM, SAAM, DSM, ATD, DDD, SLR, SMS, MLR.
- Author: Tang, Razavian, Cataldo, Cai, Parnas, Constantine, Baldwin, MacCormack, Colfer, Kazman, Kruchten, Hofmeister, Prechelt, Budgen, Waterman, Nagappan, Taibi, Fowler, Ford.
- Zero-result queries ("big design up front", "architectural debt" as a title on Q/A sites) meant the words were wrong; the field says "up-front architecture" and "architectural technical debt".

## Boundaries: one place per fact

| Neighbour topic | What stays there |
|---|---|
| [architecture-descriptions](../architecture-descriptions/frame.md) | documenting an architecture: views, arc42, C4 |
| [design-decisions](../design-decisions/frame.md) | decision records, design docs, RFCs, rationale; Tofan 2014 |
| system-design | data, consistency, replication, failure, capacity, APIs between services, checking a design before building (Newcombe 2015) |
| algorithm-design | design techniques, specification, function-level planning for code generation |

- The general reading principles are linked, not reviewed again: [overview first](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/principles/document/overview-first.md), [define before use](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/principles/document/define-before-use.md).
- Out of scope: whether a particular system is well designed; code-level design rules (naming, functions); programming languages.
