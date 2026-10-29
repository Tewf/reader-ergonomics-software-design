# Evidence

One literature review per topic, in the steps reader-ergonomics uses for its own
[evidence](https://github.com/Tewf/reader-ergonomics/tree/40cd9fb3ed21a01a8913788edc46ade9562a797d/evidence): frame, review, state of the art, position, the
case against, baseline. Every work cited is listed once in the [bibliography](bibliography.md).

| Topic | Question |
|---|---|
| [architecture-descriptions](architecture-descriptions/) | how a description of a system's architecture is organised so a reader finds what they need |
| [design-decisions](design-decisions/) | how design documents, RFCs and decision records are written so a reader can judge a proposal and later recover why |
| [pseudocode](pseudocode/) | how an algorithm is presented so a reader understands it and can implement or verify it |
| [system-diagrams](system-diagrams/) | how diagrams of a system are drawn so a reader extracts the right structure quickly and correctly |
| [architecture-design](architecture-design/) | how the structure of one system is chosen before it is built, so it meets its quality goals and stays cheap to change |
| [system-design](system-design/) | how a running system across machines is designed before it is built, so it meets its load, reliability and consistency goals |
| [algorithm-design](algorithm-design/) | how an algorithm is designed and its behaviour specified before it is coded, so an implementer, a person or a model, builds it correctly |

The first four are about documents that describe a system; the last three are about designing it, at the abstract layer
just before the code.

## Method

Each topic is a **multivocal literature review** built to a written protocol after Garousi 2019. The review pools research and **grey literature** (standards, company practice, templates, practitioner books and sites). Two files in each topic make the review checkable and rerunnable:

| File | What it holds |
|---|---|
| `protocol.md` | why grey literature is included, the questions, every search string with its date and count, the stopping rule, the selection criteria |
| `sources.md` | every included source, how it was found, and its quality: the evidence grade for research, a score out of 20 for grey literature |

Grey literature is included when a topic answers yes to any of the seven questions of Garousi 2019, Table 4; each
protocol answers them in its section 1.

A grey source is scored on Garousi's 20 criteria, in eight groups. The `sources.md` tables abbreviate the groups with letters:

- A: authority (of 4)
- M: methodology (6)
- O: objectivity (4)
- D: date (1)
- P: position among related sources (1)
- N: novelty (2)
- I: impact (1)
- T: outlet tier (1)

A grey source below 10 of 20 may illustrate what practice does, but it never supports a claim.

Outlet tier scores 1, 0.5 or 0. Tier 1 is a book, magazine, thesis, standard, committee paper or vendor guidance page; tier 2 is a talk, repository, project, wiki or Q/A page; tier 3 is a blog.

For each source a review extracts its kind, year, claim, evidence and any number, then answers its questions in prose; each claim points to a row of `sources.md`.

Limits every review shares: search engines personalise and drift, so a repeat gives other counts; Semantic Scholar and arXiv counts match words, not phrases; a source read by abstract only is marked so in `sources.md`.

How a number was read is marked beside it. "(secondary)" means only an abstract or another work's summary was read. The
three design reviews also write "abstract read" when the paper's own abstract was read, and "located only" when nothing
beyond the title and venue was reached; such a work supports no claim.

Each review keeps the form most used in practice apart from the best tested one; practice counts as evidence only
where a study measured its effect.

**Second rater.** A second rater re-scored, blind, every fifth grey source of the four document reviews of this
repository and the three of its sibling (38 of 175):

- inclusion: the raters agreed for 89.5% of the sample, Cohen's kappa 0.46, unstable at this size (bootstrap 0.00 to 0.87);
- totals: intraclass correlation ICC(A,1) 0.62, mean absolute difference 2.05 of 20, the second rater 1.8 points higher;
- four sources moved from below 10 to above it, and each stays an example of practice;
- the raters differed most on novelty, methodology and objectivity;
- outlet tier was not scored blind, and the first rater kept only the eight subtotals.

The same was done on 2026-10-29 for the three design reviews (15 of 70 grey sources):

- inclusion: the raters agreed for 86.7% of the sample; kappa is not informative, since the first rater included all 15;
- totals: ICC(A,1) 0.71 (bootstrap 0.37 to 0.88), mean absolute difference 1.20 of 20, the second rater 0.4 points lower;
- two sources fell below 10 for the second rater (AWS 2026d, SO 2009f), and each is kept as an example of practice only;
- the raters differed most on impact and objectivity.

## Audit

Every DOI was resolved against Crossref when the reviews were written. On 2026-10-28 every numeric line of the four
reviews was checked against its primary source (173 lines: 124 correct, 21 imprecise, 17 unverifiable, 8 repeats, 3
wrong). Every wrong, imprecise or unverifiable line was corrected, narrowed or marked. Claims without a number
were not audited this way. 

On 2026-10-28, the claims the audit could not verify were checked against the full texts through the university's access (17 claims: 11 correct, 2 imprecise, 2 partly confirmed, 2 still unverifiable).

On 2026-10-29 the three design reviews were audited the same way, each by an agent other than its writer (168 lines:
112 correct, 15 imprecise, 14 unverifiable, 26 repeats, 1 wrong). The wrong line reversed its source and was rewritten;
every imprecise line was corrected, and every unverifiable one is marked.

The same night, the 14 claims left unverified or read second-hand were taken to the full texts through the
university's access:

- 6 were read: 5 correct, and 1 imprecise (a share of impacts reported as a share of outages), now corrected;
- 1 is in a journal outside the access;
- 7 sit behind a publisher's bot check that was not bypassed; they stay marked.
