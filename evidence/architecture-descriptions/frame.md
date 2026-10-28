# Frame: the problem and its names

This file states, in one sentence, the problem of describing an architecture, then lists what research and practice call its parts. The review is a **multivocal literature review** (MLR, Garousi 2019): formal and grey literature together, see [protocol](protocol.md). The grey sources (defined in the [design-decisions frame](../design-decisions/frame.md)) fall in three tiers by outlet control: books and standards, then project sites and panels, then blogs.

## The problem in one sentence

Decide how the written account of a system's architecture is divided (views, levels, sections) and entered (first page, reading order). A reader with a stated task should find the answer and end with a correct model of the system.

## What the field calls it

| Our phrase | Field name |
|---|---|
| the document | **architecture description** (AD, ISO/IEC/IEEE 42010), **software architecture documentation** (SAD) |
| the parts | **views** and **viewpoints**; **view types** (Views and Beyond); structures (Soni 1995) |
| the readers | **stakeholders** with **concerns** (42010); **newcomers**, **architects**, **developers** in empirical work |
| the content | **architectural knowledge** (AK), **architecture knowledge management** (AKM) |
| finding things | **architectural knowledge retrieval**, **architectural information search** |
| the first days | **onboarding**, **project landscape** (Dagenais 2010), **architecture explanation** (Rukmono 2026) |
| the prose form | **essay-style document** (ESD, Robillard 2016) against a **systematic** or **catalogue** format |

## What practitioners call it

- **ARCHITECTURE.md** and its **codemap** (matklad 2021).
- The **arc42 (Starke 2026)** template and its twelve sections.
- The **C4 model (Brown 2026a)**: system context, containers, components, code.
- **Docs as code**, **docs-like-code** (Backstage 2020), **developer portal**.
- The big picture and the system overview (a wish in Rost 2013).
- The **architecture section** of agent context files (AGENTS.md, CLAUDE.md).

## Definitions used here

- **Architecture** in 42010: what is fundamental to a system in its environment, namely its elements, their relationships and the principles of its design and evolution (ISO 2022).
- An architecture can exist unwritten; the **description** is the written artefact, and the map is not the territory (ISO 2022).
- **View**: a representation of one or more structural aspects of an architecture that addresses concerns of stakeholders (Rozanski 2011).
- **Viewpoint**: the conventions for building one kind of view (Rozanski 2011).
- Perry 1992 framed architecture as elements, form and rationale; the primary text was not re-read for this review.

## Out of scope here

- Diagram notation and layout: review system-diagrams.
- Decision records, design documents, RFCs: review design-decisions.
- Pseudocode.
- How good the architecture is: another object.

## Search terms tried, three ways

- Academic: architecture documentation, architectural views, architecture knowledge retrieval, newcomer onboarding.
- Acronym: AD, SAD, AK, AKM, V&B, ESD, ADL, SLR, MSR, SMS, MLR.
- For existing reviews: systematic literature review, systematic mapping study, multivocal literature review, tertiary study, each with architecture documentation, architecture description, architectural knowledge, docs as code, onboarding.
- Author: Clements, Kruchten, Rozanski, Hilliard, Rost, Malavolta, de Graaf, Ernst, Robillard, Kazman, Dagenais, Lethbridge, Brown, Starke.
- A search for a count of repositories with an ARCHITECTURE.md found no study; a platform code-search count was not stable, so none is reported.
