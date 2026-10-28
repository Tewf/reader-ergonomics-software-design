# Design decisions: how to write the document that proposes or records a design decision

Question: how should design documents, RFCs and architecture decision records be written, so a reader can judge a proposal before it is adopted and later recover why the system is as it is.

Steps: [frame](frame.md) · [review](review.md) · [state of the art](state-of-the-art.md) · [position](position.md) · [against](against.md) · [baseline](baseline.md) · [bibliography](../bibliography.md)

This is an informal reading of published research and public practice. It is not a standard, a new result, or a claim to the state of the art. A number read only in an abstract or summary is marked "(secondary)".

## Claims

| Claim | Grade | Where |
|---|---|---|
| Practitioners value design rationale and report barriers to documenting it | measured, descriptive (81 survey answers; 25 interviews) | review.md 3 |
| Cost of capture is the long-named barrier to rationale | supported with caveat (argument and retrospective, not a trial) | review.md 1 |
| Documented rationale raised decision effectiveness after a requirements change, with no efficiency gain, in one lab experiment | measured, one study, 50 students | review.md 4 |
| The value of rationale depends on its intended use | measured, one experiment (secondary) | review.md 4 |
| Nygard's five-part record scored above MADR 2024 on a weighted writer-side score | measured, preprint, 33 undergraduates | review.md 4 |
| ADRs in open source are tried more than kept; about half of repositories hold one to five | measured, descriptive (secondary) | review.md 5 |
| About 63% of 5,800 ADRs were opened already accepted | measured, descriptive (secondary) | review.md 5 |
| Go proposals are declined for feasibility, use cases and principles, not document form | measured, descriptive, preprint, one project | review.md 5 |
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
