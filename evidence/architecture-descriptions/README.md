# Architecture descriptions: how to organise the description of a system's architecture for its reader

Question: how should a description of a software system's architecture be organised (views, levels of abstraction, sections, entry points)? The reader may be a new team member, a reviewer or an operator; each must find what they need and build a correct model of the system.

| Steps | [frame](frame.md) | [review](review.md) | [state of the art](state-of-the-art.md) | [position](position.md) | [against](against.md) | [baseline](baseline.md) | [protocol](protocol.md) | [sources](sources.md) | [bibliography](../bibliography.md) |
|---|---|---|---|---|---|---|---|---|---|

Method: a multivocal literature review (Garousi 2019), 92 sources: 51 formal, 41 grey of which 8 score below 10 of 20 (examples of practice only). The grey sources include 21 threads from Q/A sites.

## Scope

- The object is the document and its reader, not the quality of the architecture it describes.
- Sibling reviews cover the notation and layout of diagrams (system-diagrams) and decision records, design documents and RFCs (design-decisions).
- General findings are linked, not repeated: [documentation](https://github.com/Tewf/reader-ergonomics/tree/7a76cc6a86b7a5c1e451e4416534d113abd0f594/evidence/documentation), [file structure and architecture recovery](https://github.com/Tewf/reader-ergonomics/tree/7a76cc6a86b7a5c1e451e4416534d113abd0f594/evidence/file-structure), and the principles [overview first](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/document/overview-first.md), [one mode per document](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/document/one-mode-per-document.md), [define before use](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/document/define-before-use.md) and [draw relations](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/page/draw-relations.md).

## Claims

Grades: **measured**, **supported with caveat**, **convention, untested**; an adoption count is **measured, descriptive**.

| Claim | Grade | Where |
|---|---|---|
| Developers report architecture documentation as outdated, inconsistent in form and not fitted to their task (147 industrial respondents) | measured, descriptive (self-report) | review.md 3 |
| Abstract, high-level documentation is trusted more and stays useful when detail goes stale | supported with caveat | review.md 3 |
| Newcomers want the architecture early, to see where a task fits in the whole | supported with caveat | review.md 3 |
| Structured (Views and Beyond) against essay format: no significant effect on newcomers' architecture-understanding scores; prior familiarity with the code dominated (65 students, one system) | measured, one study | review.md 4 |
| Publishing an architecture document in a large open-source project had ambiguous measured effects; peripheral members still needed it | supported with caveat (one case) | review.md 4 |
| Organising architectural knowledge by readers' questions goes with better retrieval | supported with caveat (two case studies, correlation) | review.md 4 |
| Open-source projects rarely document architecture (108 of 2,000); the views found are informal, single and mostly never updated | measured, descriptive | review.md 5 |
| Nineteen reviews of the field exist; none takes the organisation of a description for its reader as its subject | supported with caveat (abstracts read) | review.md 0 |
| Splitting a description by concern may serve developers with one task badly; a task excerpt was proposed and later validated | convention, with a later validation (secondary) | review.md 4 |
| Text against diagram descriptions: no overall difference in an earlier experiment (those who mostly used text scored better), as with structured against essay | measured, two experiments (one secondary) | review.md 4 |
| Standards organise a description by stakeholder concerns, viewpoints and views | convention, untested | review.md 2 |
| arc42 (12 sections, Starke 2026), C4 (4 levels) and ARCHITECTURE.md (a map of the code) are the practice templates; this search found no comparative trial of them; the arc42 site scores 9.5 of 20 and is an example of practice | convention, untested | review.md 6, sources.md |
| About 7 in 10 agent context files carry an architecture section; two test settings found repository overviews did not help coding agents | measured, descriptive; measured (two settings) | review.md 6 |
