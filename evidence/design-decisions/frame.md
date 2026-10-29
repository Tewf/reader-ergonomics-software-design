# Frame: the problem and its names

This file states the problem of proposing and recording decisions, in one sentence. It then gives the names that research and practice use for the problem.

## The problem in one sentence

Decide how to write the document that proposes a design decision and the document that records it. A reviewer must be able to judge the proposal before adoption; a later maintainer must be able to recover why the system is as it is.

## What the field calls it

- **Design rationale (DR)**: the reasons behind design decisions (Lee 1997; Dutoit 2006).
- **Design rationale systems**: tools and notations that capture DR, such as IBIS and QOC (Regli 2000; MacLean 1991).
- **Rationale management**: the software-engineering name for capture, storage and use of DR (Dutoit 2006).
- **Architectural design decision (ADD, AD)**: a decision treated as a first-class entity (Jansen 2005; Tyree 2005).
- **Knowledge vaporization**: decisions disappearing into the architecture because they are not recorded (Jansen 2005).
- **Architectural knowledge management (AKM)**: the research programme that absorbed DR (Capilla 2016).
- **Decision documentation** and **decision viewpoint**: the architecture-description view of the same thing (van Heesch 2012).
- **Design space analysis**: questions, options and criteria laid out as a space (MacLean 1991).

## What practitioners call it

- **ADR**: architecture decision record, from Nygard 2011; also **decision log** for the collection.
- **Design doc**: the pre-implementation document at Google (Ubl 2020).
- **RFC**: request for comments, from the IETF (IETF 2014), reused by Rust, HashiCorp 2026, Uber and others.
- **RFD**: request for discussion (Oxide RFD 1, Frazelle 2026).
- **PEP** and **KEP**: Python and Kubernetes enhancement proposals (PEP 1, Warsaw 2000; KEP template, Kubernetes 2026).
- **PR/FAQ** and **six-pager**: Amazon's narrative formats (Amazon 2021).
- **Y-statement**: a one-sentence decision record (Zdun 2013).
- **Lightweight decision record**, **architecture decision log** and **decision register** are further names for the same artefact (Runde 2018; GDS 2026).
- **Improvement proposal** (Kafka KIP) and **evolution proposal** (Swift) are the proposal names outside the examples above (Swift 2026).
- The words differ more than the content: most of these have context, a decision, alternatives and consequences.

## The method named

- This review is a **multivocal literature review (MLR)**: it pools formal literature with **grey literature**, defined below (Garousi 2019). [protocol](protocol.md) states the searches; [sources](sources.md) lists the pool.
- **Grey literature** is material not controlled by commercial publishers. Garousi 2019 sorts it into tiers by how much control the outlet exerts:
  - tier 1, high control: books, magazines, theses, government and standards documents, white papers;
  - tier 2, moderate: presentations, videos, project documentation, Q/A and wiki pages;
  - tier 3, low: blogs, emails, tweets.
- The nearest earlier work is also an MLR (Harhio 2022); review.md strand 0 says how this one differs.

## Two moments, two readers

| Moment | Reader | Reader task | Document, in practice |
|---|---|---|---|
| Before adoption | reviewer, approver | judge: is the problem real, is the design sound, were alternatives weighed | design doc, RFC, proposal, enhancement proposal |
| After adoption | maintainer, newcomer, later architect | recover: why this, what else was considered, what changes if a constraint moves | decision record, accepted RFC, log of decisions |

- One decision often appears in both documents; the first is a proposal, the second a record.
- Some processes merge them: a proposal is merged and then kept as the record (Rust RFCs, PEPs).
- Others keep them apart: an ADR is written once the team has decided, or moves from Proposed to Accepted (GDS 2026; AWS 2026c, example only).

## Search terms tried, three ways

- Academic: design rationale, rationale management, architectural knowledge management, architecture decision documentation, design space analysis.
- Acronym: DR, AKM, ADD, ADR, IBIS, QOC, MADR, PEP, KEP, RFC, RFD.
- Author: Lee, Kunz, Rittel, MacLean, Conklin, Dutoit, Burge, Tyree, Jansen, Tang, Falessi, Zimmermann, Zdun, Weinreich, Buchgeher, Nygard.
- For existing reviews (Garousi Guideline 2): systematic review, systematic mapping study, semi-systematic literature study, multivocal literature review, literature overview; with architectural decisions, architecture decision records, decision documentation, design rationale; authors Tofan, Razavian, Tang, Harhio.
- Zero-result queries (for example "Rust RFC empirical study") meant the words were wrong; the process-mining studies are filed under PEP and Go proposals.

## Not reviewed here

- Whether a decision was good (a design-quality question, out of scope for this repository).
- The architecture description as a whole and its views ([architecture-descriptions](../architecture-descriptions/frame.md), where the term and architectural knowledge are defined).
- Diagram notation (review "system-diagrams").
- Findings that are general reading principles are linked, not reviewed again: [overview first](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/overview-first.md), [one mode per document](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/one-mode-per-document.md), [define before use](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/define-before-use.md), [given before new](https://github.com/Tewf/reader-ergonomics/blob/master/principles/sentence/given-before-new.md).
