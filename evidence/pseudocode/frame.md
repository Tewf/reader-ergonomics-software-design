# Frame: the problem and its names

This file states, in one sentence, the problem of presenting an algorithm, then the names the field and its practitioners use.

## The problem in one sentence

Decide which notation presents an algorithm so that a reader can follow it, implement it, or check it, and under which conditions.

## Names for the same things

| Thing | Field name | Practitioner name |
|---|---|---|
| Informal algorithm text | **pseudocode**, pseudo-code | "the algorithm", algorithm box, reference language |
| Constrained code-like text for designs | **program design language** (PDL), Caine and Gordon 1975 | structured English, design language |
| Drawn control flow | **flowchart**, structured flowchart, **Nassi-Shneiderman diagram**, **control structure diagram** (CSD) | flow diagram, activity diagram |
| Design by successive detail | **stepwise refinement**, Wirth 1971 | top-down design |
| Code and prose woven together | **literate programming**, Knuth 1984 | notebook, tutorial code |
| Machine-checkable design text | **formal specification**, **TLA+**, **PlusCal** | executable specification, model |
| Real code as the description | executable pseudocode | "Python is pseudocode" |
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

## Search terms tried, three ways

- Academic: pseudocode comprehension; flowchart against pseudocode; program design language; algorithm representation; documentation format.
- Acronym: PDL, NS diagram, CSD, SPoC, TLA+, ERL.
- Author: Shneiderman, Ramsey, Scanlan, Curtis, Boehm-Davis, Green, Petre, Knuth, Wirth, Oda, Kulal, Newcombe, Cormen.
- Practice: exam board names (AQA, OCR, Cambridge International, College Board), CTAN package names, Wikipedia, Rosetta Code.
- Terms that returned nothing relevant: "pseudocode ambiguity developers", "reproducing algorithms from pseudocode"; the query was wrong, since the field files this under reproducibility.
