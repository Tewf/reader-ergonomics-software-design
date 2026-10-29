# Frame: the problem and its names

This file states, in one sentence, the problem of designing a running system before building it, then the names research and practice give to its parts. The review is a multivocal literature review after Garousi 2019: see the [evidence method](../README.md#method) and the [protocol](protocol.md).

## The problem in one sentence

Decide how the services, data stores, networks and machines of a running system are designed before they are built, so that the system meets its load, reliability and consistency goals. Then find out which of the principles used for this have been tested.

## What the field calls it

- **Computer system design**: the older research name; its principles are stated as hints and arguments (Lampson 1983; Saltzer 1984).
- **Distributed systems design**: design of systems whose parts fail independently and talk over a network (Kleppmann 2017, not opened).
- **Consistency model**: a contract on what a read may return after writes; Viotti 2016 counts more than 50 of them (abstract).
- **CAP theorem** and **PACELC**: the trade-off between consistency, availability and partition tolerance, with latency added (Gilbert 2002; Brewer 2012; Abadi 2012).
- **Fallacies of distributed computing**: false assumptions such as "the network is reliable" (Bailis 2014; Azure Patterns 2026 lists them).
- **Failure study** and **outage study**: counting what went wrong in production (Yuan 2014; Alquraan 2018; Gunawi 2016).
- **Site reliability engineering (SRE)**: operations treated as an engineering discipline (Beyer 2016).
- **API usability** and **API design**: the interface between services or to a library (Myers 2016; Rauf 2019).
- **Systems engineering**: the discipline with an architecture definition and a design definition process (ISO 2023b, not opened; Nuseibeh 2001).
- **Design-level formal methods** and **lightweight formal methods**: a precise model of the design, checked before code exists (Newcombe 2015; Bogli 2024).
- **Deterministic simulation** and **fault injection**: testing a design or system under controlled failure (Alquraan 2018; Jepsen 2026).

## What practitioners call it

- **System design**: the word of interview books and primers (Primer 2026).
- **Scalability**, **high availability** and **back-of-the-envelope estimation**: the three topics those books teach first (Primer 2026; SESE 2018p).
- **Well-architected**: a vendor's checklist of pillars (AWS 2026p).
- **Cloud design patterns**: named solutions such as Retry, Saga, Sharding (Azure Patterns 2026).
- **API guidelines** and **API improvement proposals (AIP)**: company rule sets for service interfaces (Google AIP 2025; Zalando 2026; Microsoft API 2026).
- **Postmortem**: the written account of an outage (Beyer 2016).
- **Chaos engineering**: injecting failure in production on purpose (Owotogbe 2025; SESE 2013q).

## Search terms tried, three ways

- Academic: computer system design, distributed systems design, consistency models, failure analysis, API usability, design definition.
- Acronym: CAP, PACELC, SRE, TLA+, MLR, SLR.
- Author: Lampson, Saltzer, Brewer, Gilbert, Abadi, Gunawi, Yuan, Alquraan, Myers, Stylos, Newcombe, Kleppmann.
- For existing reviews (Garousi Guideline 2): systematic review, mapping study, multivocal review, survey, with each term above.
- Zero or junk results (a cloud-outage systematic review query returned energy and agriculture papers) meant the words were wrong; they were rephrased.

## Not reviewed here

- Module decomposition, styles, tactics and architecture evaluation: [architecture-design](../architecture-design/frame.md).
- Specification languages in general, contracts and pre and postconditions: [algorithm-design](../algorithm-design/frame.md).
- How an architecture is documented: [architecture-descriptions](../architecture-descriptions/frame.md); how a decision is recorded: [design-decisions](../design-decisions/frame.md); how a diagram is drawn: [system-diagrams](../system-diagrams/frame.md).
- General reading principles are linked, not reviewed again: [overview first](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/overview-first.md), [define before use](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/define-before-use.md), [worked examples with subgoals](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/worked-examples-with-subgoals.md).
