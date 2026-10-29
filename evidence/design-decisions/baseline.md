# Baseline: what the rules are compared against

This file names the baseline that a proposed rule on design documents and decision records must beat. It also says how the two would be compared.

## The named baselines

| Document | Baseline | Why this one |
|---|---|---|
| Decision record (after adoption) | Nygard 2011: title, status, context, decision, consequences | most used in open source (Buchgeher 2023, secondary); the only template with a controlled comparison (Nogueira 2026) |
| Proposal (before adoption) | PEP 12 (Goodger 2002) with PEP 1 (Warsaw 2000): abstract, motivation, specification, rationale, backwards compatibility, rejected ideas, open issues | a long-running proposal process with a public archive of 746 files and two process-mining studies (Keertipati 2016; Sharma 2022) |

- The choice is confirmed from the grey side: 12 of 19 grey sources in Harhio 2022 concern ADR templates. The baseline sources score Nygard 2011 13.5, Warsaw 2000 15 and Goodger 2002 12 of 20 (sources.md).
- Go proposals (Go 2026b) and Swift proposals (Swift 2026) are further proposal processes with a public archive; they were not made baselines because no template comparison with them exists.
- Rust RFC template (Rust 2026b) and KEP template (Kubernetes 2026) are the second baselines for a proposal; both are compared with PEP 12 section by section (state-of-the-art.md).
- MADR 2024 is the richer record baseline: it adds drivers, considered options, and pros and cons per option.
- The academic anchor is Falessi 2010 (rationale documentation against none) for what a record is for.

## Candidate variant to test

- A proposal that opens with the decision asked for, its status and what the reviewer must decide.
- Every option, including the rejected ones, carries its consequences and the reason it lost.
- Proposal and record are two linked documents, each of one mode.
- These are hypotheses, graded **convention, untested**.

## How a comparison would be measured

| Reader task | Outcome | Instrument | Prior study to borrow from |
|---|---|---|---|
| Judge before adoption | share of seeded flaws found; time to verdict | proposals with a fixed list of planted flaws (a missing option, an unstated consequence, a constraint contradicted) | seeded-defect inspection experiments (Basili 1996; Aurum 2002 for the literature) |
| Recover why, after a gap | share of correct answers to fixed questions: why this option, what lost and why, what breaks if a constraint moves | questions answered from the record alone, a week or more after reading | Falessi 2010 (decisions under changed requirements); Karsenty 1996 (rationale documents, result not read) |
| Cost to the writer | time to write; effort felt | same decision written under each template | Nogueira 2026 (FS2: time and perceived objectivity) |

- Design: crossover with counterbalanced order and a one-week gap, as in Nogueira 2026.
- Effect sizes: Cliff's delta and probability of superiority, as in Nogueira 2026.
- Subjects: reviewers with practice reading designs; students are a threat to generalisation (Falessi 2010).
- Reader-side outcomes are the gap this baseline exposes: Nogueira 2026 scores the writer.

## A checklist for a document in the baseline's own terms

Per record, from Nygard 2011:

1. A short noun phrase as the title, numbered in sequence.
2. Status is present and current; a superseded record stays in place and is marked.
3. Context states the situation the decision responds to.
4. Decision is written in full sentences, active voice.
5. Consequences list all effects, positive and negative.
6. One or two pages.

Per proposal, from PEP 1 and PEP 12:

1. A motivation that says why the present state cannot solve the problem.
2. A specification of the syntax and semantics of the change.
3. A rationale that says why this design and not another.
4. A backwards compatibility section and a security implications section.
5. Rejected ideas with their reasons.
6. Open issues left for discussion.

A rule may be rejected deliberately; the rejection is written where a reviewer looks for the missing section.
