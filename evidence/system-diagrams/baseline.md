# Baseline: what the diagram rules are compared against

This file names the baseline a proposed rule on system diagrams must beat, and how the two would be compared.

## Named baselines

| Baseline | Why |
|---|---|
| A. UML component and deployment diagrams drawn to OMG 2017 | the standard, most studied (Budgen 2011) |
| B. C4 container diagrams drawn to the C4 notation rules, with a key | the practitioner reference (Brown 2026b), industrial use reported by Jongeling 2025 |
| C. Unstructured boxes and lines (no key, no types) | what Baltes 2014 found most common |

The comparison is B against A and C on the same system.

## How a comparison would be measured

| Element | Choice | Instrument from |
|---|---|---|
| Reader task | answer structural questions: who calls whom, what contains what, what is on which node, path from X to Y | Störrle 2011 question catalogue of ten questions; Ware 2002 path finding |
| Accuracy | right answers out of ten | Störrle 2011, 2016b |
| Time | seconds per answer and per right answer | Störrle 2011 |
| Rating | clarity and quality, 0 to 10 | Störrle 2011 |
| Description match | free description of the system scored against the author's text | Nicacio 2022 |
| Gaze | fixations and visual effort on relevant elements | Sharif 2010, Santos 2018 |
| Size control | element count and layout-flaw count | Störrle 2016b |
| Layout control | good versus bad compound layout | Störrle 2011 |
| Readers | novices and experts apart | Störrle 2014 |
| Key | the same diagram with and without a key | no instrument found; Santos 2018 only varied symbols |

## Checklist for a diagram in this repository

1. A title with type and scope; a key (Brown 2026b, Brown 2026d; IcePanel 2023).
2. Each element has a type; each container a technology (Brown 2026b).
3. One-way arrows, each labelled with intent and protocol (Brown 2026b; Microsoft 2023 for data flows).
4. Layout flaws few (at most 15 to 20) and flaw rate at most 0.5; a centre of about 44 to 65 elements, depending on the data set, fewer for novices (Störrle 2016b, measured).
5. Compound layout: group related elements, keep paths straight, few crossings (Störrle 2011, Ware 2002).
6. Colour used for kind, consistent, legible in grayscale, never the only signal (Brown 2026b; Fuchsia 2025; GitLab 2026).
7. Source as text next to the picture so the two change together; accept limited layout control (GitHub 2022, Jongeling 2025; adoption only).
8. Legible at 700 px width, with text contrast of 4.5:1 and alt text (AWS 2026b; Fuchsia 2025).

- Items 4 and 5 are measured, on one group's data.
- Items 1 to 3, 6 to 8 are convention, untested; the C4, IcePanel, Fuchsia and GitLab pages behind them score below 10 of 20, so they are examples of practice, not support.
- Item 8's contrast figure rests on AWS 2026b (12.5 of 20) and the 4.5:1 floor of the reader-ergonomics standard.
