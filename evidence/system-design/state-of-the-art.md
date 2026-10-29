# State of the art, per sub-question

Each sub-question has two records, kept apart: the **most adopted** practice (what people use) and the **best evidence** (what a study measured). Upper bounds stay separate from lower bounds; the first says what has been achieved, the second what is impossible.

| Sub-question | Most adopted | Best evidence | Measured how |
|---|---|---|---|
| Q1 Principles of system design | Lampson 1983 hints; end-to-end argument (Saltzer 1984) | none found that tests a principle | argument and experience only |
| Q2 Consistency and availability | binary CP or AP framing (Primer 2026) | Brewer 2012 and Kleppmann 2015 (arguments on the framing); Bailis 2012 (staleness) | argument; model fitted to production latencies of two firms |
| Q3 What designs get wrong | postmortem practice (Beyer 2016); Jepsen 2026 | Yuan 2014; Alquraan 2018; Gunawi 2016 | 198 and 136 failures, read and partly reproduced; 597 outages from public reports |
| Q4 Capacity and load estimation | back-of-the-envelope in primers (Primer 2026) | Dean 2013 (fan-out arithmetic and one measured table); no study of estimate accuracy | arithmetic; one Google service |
| Q5 Interfaces between services | company rule sets (Google AIP 2025; Zalando 2026; Microsoft API 2026) | Stylos 2007 (30 programmers, user study); Piccioni 2013 (25); Murphy 2018; Kotstein 2021; Rauf 2019 | user studies on library APIs; 24 interviews; 8-expert Delphi; mapping of 47 studies |
| Q6 Checking a design before building | design review; TLA+ at AWS (Newcombe 2015); simulation (Zhou 2021) | Newcombe 2015 and Bornholt 2021 (owners' reports, with counts); Bogli 2024 (review) | experience, no control; 16 industrial papers |
| Q7 Systems engineering standards | ISO 2023b (15288); INCOSE 2023 (not opened) | Elm 2012 | survey with statistical links |
| Q8 Interview books and primers | Primer 2026: 376k stars | none: no study compares them with research | counts of stars only |
| Models as implementer | none | Cheng 2026 (benchmark, no results in abstract); Sahu 2026 | benchmark design; argument with a tool |

## Lower bounds, upper bounds

- Lower bound: no web service can have consistency, availability and partition tolerance together, proved in the asynchronous network model (Gilbert 2002, abstract); Kleppmann 2015 shows the result depends on its definitions.
- Lower bound, practical: latency is traded against consistency even without a partition (Abadi 2012, PACELC).
- Best case in two modelled profiles: in Dynamo-style quorums fitted to LinkedIn latencies (N=3, R=W=1), 99.9% of reads were predicted consistent after 1.85 ms to 45.5 ms (Bailis 2012). This is one configuration, not a bound.
- Upper bound: 93% of partition failures studied could be reproduced by fault injection (Alquraan 2018, Finding 13).

## Adoption counts, descriptive, taken 2026-10-29

| Count | Value | Caveat |
|---|---|---|
| Stars of the system design primer | 375,957 | created 2017-02-26; last push 2026-09-15 |
| Forks of the primer | 59k | page figure, rounded |
| Stars of the Microsoft REST guidelines | 23.3k | page figure, rounded |
| Jepsen analyses listed | 51 entries for 39 systems | 2013-05-18 to 2026-10-20; counted by the page reader |
| Azure cloud design patterns | 44 | counted in the catalog table |
| Stars of another primer (ByteByteGo 2023) | 90,808 | repository count only; not read |

## Reading the table

- Most adopted and best evidence are different holders on every row where both exist.
- Where the research record is empty (Q1, Q4, Q8), this search found nothing; that is not proof nothing exists.
