# Evidence

One literature review per topic, in the steps reader-ergonomics uses for its own
[evidence](https://github.com/Tewf/reader-ergonomics/tree/master/evidence): frame, review, state of the art, position, the
case against, baseline. Every work cited is listed once in the [bibliography](bibliography.md).

| Topic | Question |
|---|---|
| [architecture-descriptions](architecture-descriptions/) | how a description of a system's architecture is organised so a reader finds what they need |
| [design-decisions](design-decisions/) | how design documents, RFCs and decision records are written so a reader can judge a proposal and later recover why |
| [pseudocode](pseudocode/) | how an algorithm is presented so a reader understands it and can implement or verify it |
| [system-diagrams](system-diagrams/) | how diagrams of a system are drawn so a reader extracts the right structure quickly and correctly |

## Method

Each topic is a **multivocal literature review**: research and **grey literature** (standards, company
practice, templates, practitioner books and sites) in one review, built to a written protocol after
Garousi 2019. Two files in each topic make the review checkable and rerunnable:

| File | What it holds |
|---|---|
| `protocol.md` | why grey literature is included, the questions, every search string with its date and count, the stopping rule, the selection criteria |
| `sources.md` | every included source, how it was found, and its quality: the evidence grade for research, a score out of 20 for grey literature |

A grey source is scored on Garousi's 20 criteria, in eight groups. The `sources.md` tables abbreviate them: A authority
(of 4), M methodology (6), O objectivity (4), D date (1), P position among related sources (1), N novelty (2), I impact
(1), T outlet tier (1). Below 10 of 20 it may illustrate what practice does, but it never supports a claim.

Each review keeps the form most used in practice apart from the best tested one; practice counts as evidence only
where a study measured its effect.

**Second rater.** A second rater re-scored, blind, every fifth grey source of the seven reviews in this repository
and its sibling (38 of 175):

- inclusion: the raters agreed for 89.5% of the sample, Cohen's kappa 0.46, unstable at this size (bootstrap 0.00 to 0.87);
- totals: intraclass correlation ICC(A,1) 0.62, mean absolute difference 2.05 of 20, the second rater 1.8 points higher;
- four sources moved from below 10 to above it, and each stays an example of practice;
- the raters differed most on novelty, methodology and objectivity;
- outlet tier was not scored blind, and the first rater kept only the eight subtotals.

## Audit

Every DOI was resolved against Crossref when the reviews were written. On 2026-10-28 every numeric line of the four
reviews was checked against its primary source (173 lines: 124 correct, 21 imprecise, 17 unverifiable, 8 repeats, 3
wrong). Every wrong, imprecise or unverifiable line was corrected, narrowed or marked. Claims without a number
were not audited this way.
