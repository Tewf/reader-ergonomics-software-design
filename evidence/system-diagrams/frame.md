# Frame: the problem and its names

This file states the problem in one sentence, lists what research and practice call its parts, and names the review method.

## The problem in one sentence

Decide how to draw a diagram of a software system. The reader must answer structural questions quickly and without error: what talks to what, what is inside what, what runs where, in which order.

## Method

- A **multivocal literature review (MLR)**: a systematic review of formal literature plus **grey literature**, done to Garousi 2019. The searches are in [protocol](protocol.md) and the pool in [sources](sources.md).
- Grey literature here comes in three tiers by outlet control:
  - tier 1: standards and books (OMG 2017);
  - tier 2: company and project documentation, wikis, talks, repository pages (Microsoft 2026 icons, OWASP 2026);
  - tier 3: blogs (IcePanel 2023, GitHub 2022).

## Names for the same thing

| Source | Names |
|---|---|
| Notation theory | **visual notation**, **cognitive effectiveness**, **visual syntax**, **Physics of Notations (PoN)**, **cognitive dimensions of notations (CDN)** |
| Empirical software engineering | **UML comprehension**, **diagram layout quality**, **diagram size**, **model understanding**, **model understandability** |
| Graph drawing | **graph aesthetics**, edge crossings, bends, symmetry, continuity |
| Standards | **UML 2.5**, **SysML**, component, deployment, sequence and class diagram |
| Software visualisation | **software architecture visualization**, software visualization evaluation |
| Practitioners | **boxes and lines**, **architecture diagram**, **C4 model (Brown 2026b)** (context, container, component, code), **DFD** (data-flow diagram), **threat-model DFD**, **diagrams as code** |
| Cloud vendors | **architecture icons**, reference architecture diagram |

## Differences in meaning

- Researchers study UML nearly alone; practitioners often draw informal boxes and lines (Baltes 2014).
- "Layout" means a graph-drawing metric to one field and a human arrangement by grouping to another (Störrle 2011).
- "Diagram" in practice may be an image, a whiteboard sketch or text rendered by a tool.
- "Understandability" has no shared definition across studies (Houy 2012, secondary).

## Search terms tried, three ways

- Academic: visual notation, UML comprehension, layout quality, architecture diagram readability, dataflow diagram experiment.
- Acronym: PoN, CDN, UML, SysML, DFD, STRIDE, C4.
- Author: Moody, Green, Blackwell, Petre, Budgen, Störrle, Purchase, Ware, Sharif, Koning, Baltes, Hebig.
- For existing reviews: systematic review, systematic literature review, mapping study, MLR, multivocal, each with UML, diagram, architecture visualization, model comprehension and eye tracking.
