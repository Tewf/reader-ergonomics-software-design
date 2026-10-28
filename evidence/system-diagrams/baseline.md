# Baseline: what the diagram rules are compared against

This file names the baseline a proposed rule on system diagrams must beat, and how the two would be compared.

## Named baselines

| Baseline | Why |
|---|---|
| A. UML component and deployment diagrams drawn to OMG 2017 | the standard, most studied (Budgen 2011) |
| B. C4 container diagrams drawn to the C4 notation rules, with a key | the practitioner reference |
| C. Unstructured boxes and lines (no key, no types) | what Baltes 2014 found most common |

The comparison is B against A and C on the same system.

## How a comparison would be measured

| Element | Choice | Instrument from |
|---|---|---|
| Reader task | answer structural questions: who calls whom, what contains what, what is on which node, path from X to Y | Störrle 2011 question catalogue of ten questions; Ware 2002 path finding |
| Accuracy | right answers out of ten | Störrle 2011, 2014 |
| Time | seconds per answer and per right answer | Störrle 2011 |
| Rating | clarity and quality, 0 to 10 | Störrle 2011 |
| Gaze | fixations and visual effort on relevant elements | Sharif 2010 |
| Size control | number of elements, 20 to 60 | Störrle 2014 |
| Layout control | good versus bad compound layout | Störrle 2011 |
| Readers | novices and experts apart | Störrle 2014 |

## Checklist for a diagram in this repository

1. A title with type and scope; a key (C4 model, Brown 2026b).
2. Each element has a type; each container a technology (C4 model).
3. One-way arrows, each labelled with intent and protocol (C4 model).
4. About 60 elements at most, fewer for novices (Störrle 2014, measured).
5. Compound layout: group related elements, keep paths straight, few crossings (Störrle 2011, Ware 2002).
6. Colour used for kind, consistent, legible in grayscale (C4 model).
7. Source as text next to the picture so the two change together (GitHub 2022; adoption only).
8. Legible at 700 px width (AWS 2026b, secondary).

Items 1 to 3, 6 to 8 are convention, untested; items 4 and 5 are measured.
