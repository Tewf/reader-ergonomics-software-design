# Frame: the problem and its names

This file states, in one sentence, the problem of presenting an algorithm, then the names the field and its practitioners use, and the name of the method used to review it.

## The problem in one sentence

Decide which notation presents an algorithm so that a reader can follow it, implement it, or check it, and under which conditions.

## Names for the same things

| Thing | Field name | Practitioner name |
|---|---|---|
| Informal algorithm text | **pseudocode**, pseudo-code | "the algorithm", algorithm box, reference language, command set |
| Constrained code-like text for designs | **program design language** (PDL), Caine and Gordon 1975 | structured English, design language |
| Drawn control flow | **flowchart**, structured flowchart, **Nassi-Shneiderman diagram**, **control structure diagram** (CSD) | flow diagram, activity diagram |
| Design by successive detail | **stepwise refinement**, Wirth 1971 | top-down design, pseudocode programming process (PPP, McConnell 2004) |
| Code and prose woven together | **literate programming**, Knuth 1984 | notebook, tutorial code |
| Machine-checkable design text | **formal specification**, **TLA+**, **PlusCal** | executable specification, model |
| Real code as the description | executable pseudocode | "Python is pseudocode", "write Python, not pseudocode" (Davis 2023) |
| Exam-board notation | reference language, pseudocode guide | exam reference language |

## Related fields that use other words

- Program comprehension: **code comprehension experiment**, tracing, beacons, programming plans.
- Notation design: **cognitive dimensions of notations**, visual against textual programming, **cognitive fit**.
- Documentation formats: **software documentation format**, symbology and spatial arrangement.
- Reproducibility: **method documentation**, ambiguity, underspecification.
- Machine learning: **pseudocode-to-code** and **code-to-pseudocode** generation.

## Reader tasks used as outcomes

| Task | Typical measure |
|---|---|
| Trace (forward, backward) | time, errors |
| Implement | correctness, time, errors |
| Find a bug | time to find and fix |
| Answer comprehension questions | accuracy, time, confidence |
| Compose an algorithm | proportion that works |

## Method: a multivocal literature review

- This review is a **multivocal literature review** (MLR, Garousi 2019): formal literature and **grey literature** (material not published through journals or conferences) in one pool.
- Grey tiers: tier 1 = books, theses, standards-like and government documents, technical reports; tier 2 = wikis, course handouts, package pages, Q/A; tier 3 = blogs, e-mails, tweets.
- Each grey source is scored out of 20; see [protocol](protocol.md) and [sources](sources.md).

## Search terms for existing reviews

- Academic: systematic literature review, mapping study, survey, multivocal review, combined with pseudocode, algorithm representation, program comprehension, visual against textual programming, pseudocode-to-code.
- Acronyms: SLR, SMS, MLR.
- Authors: Wyrich, Waddel, Noone, Ulate-Caballero.
- Result: the existing reviews are in review.md strand 0.

## Search terms tried, three ways

- Academic: pseudocode comprehension; flowchart against pseudocode; program design language; algorithm representation; documentation format.
- Acronym: PDL, NS diagram, CSD, SPoC, TLA+, ERL.
- Author: Shneiderman, Ramsey, Scanlan, Curtis, Boehm-Davis, Green, Petre, Knuth, Wirth, Oda, Kulal, Newcombe, Cormen.
- Practice: exam board names (AQA, OCR, Cambridge International, College Board, Pearson Edexcel), CTAN package names, TeX FAQ, course handouts, Wikipedia, Rosetta Code.
- Terms that returned nothing relevant: "pseudocode ambiguity developers", "reproducing algorithms from pseudocode"; the query was wrong, since the field files this under reproducibility.
