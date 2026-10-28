# Design decisions: how to write the document that proposes or records a design decision

Question: how should design documents, RFCs and architecture decision records be written, so a reader can judge a proposal before it is adopted and later recover why the system is as it is.

Steps: [protocol](protocol.md) · [sources](sources.md) · [frame](frame.md) · [review](review.md) · [state of the art](state-of-the-art.md) · [position](position.md) · [against](against.md) · [baseline](baseline.md) · [bibliography](../bibliography.md)

This is a multivocal literature review (Garousi 2019) by one reviewer, searched on 2026-10-28.

- It covers published research and public practice.
- It scores 46 grey sources out of 20 (31 from the web, 15 threads from Q/A sites); 8 fall below the threshold of 10 and are used as examples only.
- It is not a standard, a new result, or a claim to the state of the art.
- A number read only in an abstract or summary is marked "(secondary)".

## Claims

| Claim | Grade | Where |
|---|---|---|
| Research on documenting architectural decisions is mostly approaches and tools; 83% of 144 papers propose one and 4% use experiments (counts not checked against the paper) | measured, descriptive (systematic mapping, 2002-2012; abstract read) | review.md 0 |
| Grey sources on documenting decisions concentrate on ADR templates: 12 of 19 | measured, descriptive, one review (a master's thesis) | review.md 0 |
| Practitioners value design rationale and report barriers to documenting it | measured, descriptive (81 survey answers; 25 interviews) | review.md 3 |
| Cost of capture is the long-named barrier to rationale | supported with caveat (argument and retrospective, not a trial) | review.md 1 |
| Documented rationale raised decision effectiveness after a requirements change, with no efficiency gain, in one lab experiment | measured, one study, 50 students | review.md 4 |
| Decision viewpoints made four student teams more systematic in weighing options, and did not help with requirements | measured, small | review.md 4 |
| The value of rationale depends on its intended use | measured, one experiment (secondary) | review.md 4 |
| Nygard's five-part record scored above MADR 2024 on a weighted writer-side score | measured, preprint, 33 undergraduates | review.md 4 |
| ADRs in open source are tried more than kept; about half of repositories hold one to five | measured, descriptive (secondary) | review.md 5 |
| About 63% of 5,800 ADRs were opened already accepted | measured, descriptive (secondary) | review.md 5 |
| Go proposals are declined most often for feasibility, obsolescence, use cases and principles, not document form | measured, descriptive, preprint, one project | review.md 5 |
| Proposal templates share motivation, design, alternatives and drawbacks | convention, adopted (descriptive comparison) | state-of-the-art.md |
| Keep rejected alternatives with their reasons; keep accepted records immutable | convention, untested | position.md |
| A proposal that opens with the decision asked for helps the reviewer | convention, untested (a hypothesis to test) | baseline.md |

## Named baseline

- Record: Nygard 2011 (title, status, context, decision, consequences).
- Proposal: PEP 12 (Goodger 2002) with PEP 1 (Warsaw 2000).
- Comparison: reader tasks "judge before adoption" and "recover why", crossover design, effect sizes (baseline.md).

## General principles linked, not reviewed again

- [Overview first](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/overview-first.md)
- [One mode per document](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/one-mode-per-document.md)
- [Define before use](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/define-before-use.md)
