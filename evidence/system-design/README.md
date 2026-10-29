# System design: how a running system is designed before it is built

Question: how is a running system (services, data stores, networks and machines) designed before it is built? The system should meet its load, reliability and consistency goals. The review asks what the evidence says about the principles used.

| Steps | [frame](frame.md) | [review](review.md) | [state of the art](state-of-the-art.md) | [position](position.md) | [against](against.md) | [baseline](baseline.md) | [protocol](protocol.md) | [sources](sources.md) | [bibliography](../bibliography.md) |
|---|---|---|---|---|---|---|---|---|---|

Method: after Garousi 2019, a multivocal literature review by one reviewer; the shared rules are in the [evidence method](../README.md#method). The search ran on 2026-10-29, and a second pass the same day read open copies and ran snowballing.

- Its scope is published research and public practice.
- It scores 23 grey sources out of 20 (9 from the web, 14 threads from Q/A sites); none falls below the threshold of 10.
- It holds 48 formal sources, 7 of them reviews.
  - 7 are known by title and venue only, and 4 by a summary (secondary).
  - The rest were read at least to the abstract.
  - 10 were read in full text, and Newcombe 2015 in its preprint.
- It claims to be neither a standard, nor a new result, nor the state of the art.
- The mark "(secondary)" goes on a number read only in an abstract or a summary.
- Counts from OpenAlex are missing; its queries are in `openalex.tsv`.

## Claims

| Claim | Grade | Where |
|---|---|---|
| Principles of computer system design (Lampson's hints, the end-to-end argument) are argued from the authors' experience; no test of one was found | convention, untested (both read) | review.md 1 |
| In a model fitted to two production latency profiles of one firm (LinkedIn, N=3, R=W=1), 99.9% consistent reads were predicted after 1.85 ms (flash) or 45.5 ms (disk); a second firm's profile gave 1,364 ms | measured, descriptive (full text read; model checked on one instrumented cluster with injected delays) | review.md 2 |
| Brewer's own article calls the "2 of 3" reading misleading; Kleppmann finds the definitions of C and A differ between the two formal sources | argument, supported with caveat (both read) | review.md 2; against.md |
| 92% of 48 catastrophic failures in five systems came from incorrect handling of non-fatal errors; 58% were catchable by simple tests | measured, descriptive (full text; 198 failures) | review.md 3 |
| 80% of 136 partition failures were catastrophic and 90% silent; 47% of the 88 taken from issue trackers needed a redesigned mechanism | measured, descriptive (full text; 25 systems) | review.md 3 |
| Design flaws took 2.5 times longer to fix than implementation bugs, in the 88 issue-tracker partition failures | measured, descriptive (full text, with the authors' caveat on timing) | review.md 3 |
| Of 597 outages in 32 services, upgrades (16%), network (15%), bugs (15%) and configuration (10%) led the known causes; 40% of reports revealed a root cause (355 of 597 unknown) | measured, descriptive (full text, Table 3; public reports only) | review.md 3 |
| With 100 servers each slow 1 time in 100, 63% of requests meet a slow one; hedged requests cut a 99.9th percentile from 1,800 to 74 ms for 2% more requests | arithmetic, and measured on one Google benchmark | review.md 4 |
| Thirty programmers did better with parameterless constructors, against the authors' hypothesis | supported with caveat: a user study with no statistical test, library API (full text read) | review.md 5 |
| Experts rated 28 of 82 REST rules high, 17 medium and 37 low in importance | measured, descriptive (8 experts, abstract) | review.md 5 |
| Designers of APIs learn on the job and have little training (24 designers, 7 companies) | measured, descriptive (abstract) | review.md 5 |
| TLA+ found bugs in AWS designs; engineers learned it in 2 to 3 weeks | convention, untested (the owner's report) | review.md 6 |
| Lightweight models at 1% of the code, with property tests, prevented 16 issues from reaching production in one S3 storage node | convention, untested (the owner's report, full text read) | review.md 6 |
| No controlled study of estimation before building was found | gap, not a result | review.md 4 |
| A system design primer holds 376k stars and never names the failure studies | measured, descriptive (counts and a text search) | state-of-the-art.md; against.md |

## Named baseline

- Checklist: Lampson 1983 with its 2020 revision, or the six-pillar well-architected framework (AWS 2026p).
- Check: Newcombe 2015.
- Comparison: a seeded-flaw reader task, crossover, not run (baseline.md).

## General principles linked, not reviewed again

- [Overview first](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/principles/document/overview-first.md)
- [Define before use](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/principles/document/define-before-use.md)
- [Worked examples with subgoals](https://github.com/Tewf/reader-ergonomics/blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/principles/document/worked-examples-with-subgoals.md)

## Neighbouring topics

- Module decomposition and styles: [architecture-design](../architecture-design/README.md).
- Specifications and contracts: [algorithm-design](../algorithm-design/README.md).
- Recording decisions: [design-decisions](../design-decisions/README.md).
