# Baseline: what a rule for architecture descriptions is compared against

This file names the baseline a proposed rule on architecture descriptions must beat, and how the two would be compared.

## The named baseline

**A Views and Beyond style structured description**, as written for Ernst 2023: nine standard headers, lists, three diagrams, about 800 words for a 10 kSLOC system.

- Why this one: it is the only structured format with a published controlled comparison and a public replication package.
- It is also 42010 shaped: views, a roadmap, mappings between views, rationale.
- Practice comparators, not baselines for measurement: the arc42 (Starke 2026) twelve sections, the C4 four levels, the ARCHITECTURE.md codemap (matklad 2021).
- The multivocal search (protocol.md) found no controlled comparison of any of these, so the baseline is unchanged.
- A candidate second arm: a task excerpt cut from the full description (Rost 2016), since Rost 2013 found task-specific content the readers' wish.

## How a comparison would be measured

| Element | Choice | Source of the instrument |
|---|---|---|
| Reader | a newcomer to the system; a reviewer and an operator need new instruments (none found) | Ernst 2023 |
| Task | four questions from remembering to creating, 75 minutes, a system of about 10 kSLOC | Ernst 2023 (Bloom levels I to VI) |
| Outcome | answer quality on a four-point ordinal scale, coded by raters | Ernst 2023 |
| Control | prior familiarity with the code, recorded and used as a covariate or a stratum | Ernst 2023 (dominant factor) |
| Retrieval | time and correctness on look-up questions about the architecture | de Graaf 2016 (efficiency, effectiveness) |
| Perception | Likert items on navigability, consistency, vision, usefulness for coding | Ernst 2023, items SE1 to SE8 |
| Persistence | share of the description still true after a set of changes | Migliorini 2024 (updates), Rost 2013 (up to date) |

A result is read against the published null: a rule is worth keeping only if it beats the baseline on an outcome the baseline did not move.

## Crosswalk: reader question to template section

A reading by this review, not a quotation from any source.

| Reader question | 42010 | Views and Beyond | Rozanski | arc42 | C4 | ARCHITECTURE.md |
|---|---|---|---|---|---|---|
| Who is this for, what do they care about | stakeholders, concerns | roadmap | stakeholders per viewpoint | 1 Introduction and Goals | none | overview of the problem |
| What is around it | chosen by viewpoint | not fixed | Context | 3 Context and Scope | level 1 system | overview |
| What are the parts | views | module views | Functional | 5 Building Block View | containers, components | codemap |
| How does it run | views | component-and-connector views | Concurrency | 6 Runtime View | dynamic diagram | none |
| Where does it run | views | allocation views | Deployment, Operational | 7 Deployment View | deployment diagram | none |
| What holds everywhere | correspondences | mappings between views | perspectives | 8 Crosscutting Concepts | none | cross-cutting concerns, invariants |
| Why this shape | rationale | rationale | none | 9 Decisions | none | see design-decisions review |
| What is risky | none | none | perspectives | 10, 11 Quality, Risks | none | none |
| What do the words mean | none | glossary | none | 12 Glossary | none | none |

## Checklist for one description

Each item names its source and grade; all are convention, untested unless marked.

1. The first lines say who the description serves and which tasks it answers (42010 stakeholders; Rost 2013, task wish).
2. The first page gives the purpose, the users and what the system touches (Dagenais 2010, supported with caveat; C4 level 1; arc42 3).
3. A map of the parts follows, one line each, answering where a thing lives and what a given thing does (matklad 2021).
4. Invariants and boundaries are stated, including things that must be absent (matklad 2021).
5. Runtime and deployment are separate sections, so an operator reaches them without reading the rest (arc42 6, 7; Kruchten 1995).
6. Cross-cutting concepts are written once and linked from the parts (one place per fact, linked in the README).
7. Stable facts come first and carry the most weight; detail that changes sits in code or a linked page (Lethbridge 2003, supported with caveat).
8. Parts are named by code names a reader can search, not by links that go stale (matklad 2021).
9. Terms are defined before use and listed once (arc42 12; define before use).
10. Each view answers one family of questions, and views are mapped to each other (42010; Rozanski 2011).
11. The description states its date and how it is kept current (Rost 2013, Migliorini 2024).
12. Rationale is a pointer to the decision records, not repeated here (design-decisions review).
