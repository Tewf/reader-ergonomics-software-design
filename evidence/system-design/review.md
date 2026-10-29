# Review

This file reads the literature on designing a running system before it is built.
The strands are existing reviews, principles, trade-offs, failure studies, estimation, interfaces, checking, standards, interview books, Q/A sites and models as implementers.

A number read in an abstract or a summary, and not in the paper, carries "(secondary)". Grey scores are in [sources](sources.md); a source under 10 of 20 would be named "example only", and none fell under 10. Works not reachable are named "located only".

## 0. Existing reviews

- No review of the whole topic was found. Viotti 2016 surveys more than 50 consistency notions; Li 2013p surveys public cloud outage reports (abstracts).
- Rauf 2019: systematic mapping of API usability evaluation, 47 primary studies (abstract).
- Machini 2024: mapping of web API usability; 96 metrics, about 40% on learnability, about 14% tied to web APIs; 18 studies (secondary).
- Bogli 2024 (full text read): 290 papers in the first pool, 16 high-affinity ones. 81% of those used TLA+ in early design. It opens by citing another work for the scarce adoption of formal methods in industry.
- Multivocal reviews: Owotogbe 2025 on chaos engineering, 96 sources; Costa 2025 on SRE, 28 studies, 11 formal and 17 grey.

## 1. Principles of computer system design (Q1)

- Lampson 1983 (read) gives hints drawn from systems the author built; he claims no originality.
- Lampson 2020 (abstract and contents read) recasts them as goals (STEADY) and techniques (AID).
- Saltzer 1984 (read): a function placed low in a system is justified only as a performance gain when the ends must implement it anyway.
- All three argue from examples; none reports a test of a principle.
- Grade: convention, untested.

## 2. Consistency and availability (Q2)

- Brewer 2000 (slides) stated the conjecture; Gilbert 2002 proves it in the asynchronous network model (abstract).
- Brewer 2012 (read): 2 of 3 misleads, partitions are rare, and the choice varies by operation and data.
  - He proposes three steps: detect a partition, enter a partition mode, recover.
  - Examples: ATM withdrawal caps in partition mode; shopping carts merged as a union.
- Kleppmann 2015: Fox and Brewer and Gilbert and Lynch define availability and consistency differently; partition tolerance is a system assumption, not a property.
  - He proposes a delay-sensitivity framework instead.
- Abadi 2012: during a partition, availability against consistency; otherwise latency against consistency (PACELC).
- Bailis 2012 (read): a model fitted to two LinkedIn latency profiles predicts 99.9% consistent reads after 1.85 ms (flash disks) or 45.5 ms (spinning disks), with N=3 and R=W=1. Yammer's profile gives 1,364 ms at the same setting. These are Monte Carlo predictions, not measured staleness.
  - The model matched an instrumented Cassandra with an error of 0.28% on average; the delays there were injected, not production.
- Grade: theory for the theorem; measured, descriptive for staleness; convention for design advice.

## 3. What failure studies say designs get wrong (Q3)

- Yuan 2014: 198 failures sampled from 17,216 reports of five systems; 48 catastrophic (Table 1).
  - 92% of catastrophic failures came from incorrect handling of non-fatal errors (Finding 10).
  - 58% were catchable by simple tests of error handling: 35% trivial patterns (Finding 11) plus 23% (Finding 12).
  - 77% of failures need more than one input event (Finding 1); 98% manifest on three nodes or fewer (Finding 3).
- Alquraan 2018: 136 failures from 25 systems, all tied to network partitions.
  - 80% catastrophic (Finding 1); 90% silent (Finding 2); 21% leave a lasting error after healing.
  - Of the 88 failures taken from issue trackers, 47% (41) needed a redesigned mechanism (Finding 11), and design flaws took 2.5 times longer to fix than implementation bugs (205 against 81 days, mean).
  - 83% reproduce on three nodes; 93% could be reproduced by fault injection (Findings 12 and 13).
  - The authors say design reviews would have avoided most; they did not test a review.
- Gunawi 2016 (read): 597 outages of 32 services from 1,247 public reports, 2009 to 2015.
  - Shares of known causes: upgrades 16%, network 15%, bugs 15%, configuration 10%. 59% were full outages (secondary: an author copy read once and not re-reached; the population of the 59% is to be checked in the paper).
  - Only 40% of reports reveal a root cause and 24% a fix.
- Gunawi 2014: 3,655 vital issues of 21,399 in six cloud systems. Gunawi 2018: 101 fail-slow hardware reports from 12 institutions. Liu 2019: bugs are a major cause of Azure incidents. Huang 2017: gray failure, no counts (abstracts).
- Bailis 2014: the companion post says evidence on partitions is scarce; the article was not reached.
- Grade: measured, descriptive.

## 4. Capacity and load estimation before building (Q4)

- This search found no controlled study of how accurate estimates made before building turn out to be.
- Dean 2013 (read) gives arithmetic a designer can use: if each of 100 servers is slow one time in 100, 63% of requests wait for one slow server.
  - A measured table from a Google service: 99th percentile of 10 ms for one random leaf, 140 ms for all leaves.
  - Hedged requests cut the 99.9th percentile of a 1,000-key read from 1,800 ms to 74 ms for 2% more requests.
- Practice teaches estimation by hand (Primer 2026; SESE 2018p).
- Grade: convention, untested for estimation; measured for the latency example (one service).

## 5. Interfaces between services (Q5)

- Controlled or observational user studies exist, mostly on library APIs:
  - Stylos 2007 (read): a comparative user study, by the authors' own account aimed at trends rather than statistics, with 30 professional programmers. Against the authors' hypothesis they preferred and were more effective with parameterless constructors.
  - Ellis 2007: factory against constructor; located only, and Myers 2016 reports that avoiding the factory pattern improves usability (secondary).
  - Stylos 2008: 2.4 to 11.2 times faster when a method sat on the expected class (read in Myers 2016, secondary).
  - Piccioni 2013 (read): 25 programmers on one persistence library; names and relations between types were hard; no comparison condition.
- Bloch 2006 is an influential talk on API design (title and venue only).
- Myers 2016 (read): few empirical studies of API design patterns exist; design guidelines from experienced designers are large and sometimes contradictory.
- Murphy 2018: 24 designers from 7 companies learned design on the job (abstract). Murphy 2017: 32 company REST guidelines differ on some topics (secondary).
- Kotstein 2021: 8 experts rated 82 REST rules; 28 high, 17 medium, 37 low importance (abstract).
- Grade: supported with caveat for Stylos 2007 (a user study with no statistical test) and for Stylos 2008 and Ellis 2007 (reported in Myers 2016, design and sample unknown). All concern library APIs, not network services. The rest are measured, descriptive.

## 6. Checking a design before building (Q6)

- Newcombe 2015 (owner's report, preprint read): precise designs found bugs that testing missed.
  - Seven teams used TLA+; engineers learned it in 2 to 3 weeks; DynamoDB had 3 bugs, some needing traces of 35 steps.
  - Engineers design the happy case first; the model forces them to ask what must go right when things fail.
- Bornholt 2021 (read): executable reference models, 1% of the code, plus property tests and model checking on 40,000 lines of Rust.
  - 16 issues prevented from reaching production; checks are 13% of the code base; 18% of harness lines were last edited by non-experts.
  - Two experts worked full time for nine months to start.
- Zhou 2021 (read): the real database runs in a deterministic simulation with fault injection; it cannot find performance issues.
- Hackett 2023: a small TLA+ model of Cosmos DB exposed two documentation issues; Cirstea 2024 and Tang 2024 check code against TLA+ specifications (abstracts); Brooker 2025 is located only.
- ter Beek 2024 surveys formal methods in industry, from requirements to runtime monitoring (abstract).
- Alquraan 2018 proposes design review for partitions, and fault injection with a test framework.
- Grade: convention, untested; each owner reports its own success.

## 7. Systems engineering standards (Q7)

- ISO 2023b (ISO 15288), edition 2, sets architecture definition (6.4.4) and design definition (6.4.5) processes (publisher listing, secondary).
- ISO 2019 (ISO 42020) sets architecture processes; INCOSE 2023 elaborates 15288 (listings; none opened); Nuseibeh 2001 is located only.
- Elm 2012: a survey found strong statistical links between systems engineering practices and project performance (abstract).
- Grade: convention, untested for the standards; supported with caveat for the survey.

## 8. Interview books and primers (Q8)

- Primer 2026 holds 376k stars and teaches four steps: use cases and constraints, a high-level design, core components, scaling.
- SESE 2011p, SO 2014p and SESE 2022p show learners asking how, and answers saying to clarify requirements first.

## 9. Practice

| Who | Since | Form | Evidence of use |
|---|---|---|---|
| Primer 2026 | 2017-02-26 | study guide and interview prep | 376k stars, 59k forks (2026-10-29) |
| AWS 2026p | undated | six pillars of cloud design | owner's claim: hundreds of thousands of architectures |
| Azure Patterns 2026 | updated 2026 | 44 cloud design patterns, each mapped to pillars | owner's catalog |
| Google AIP 2025 | 2018-08-20 | proposals with states Draft to Approved | owner's process |
| Zalando 2026 | undated | MUST, SHOULD, MAY rules plus a linter | owner's rule set |
| Microsoft API 2026 | undated | REST guidelines | 23.3k stars |
| Beyer 2016 | 2016 | blameless postmortems, written after set triggers | owner's account |
| Jepsen 2026 | 2013-05-18 | independent tests of databases under faults | 51 analyses of 39 systems, to 2026-10-20 |

## 10. Q/A sites

Fourteen threads from 380 returned (strings SY1 to SY18; [protocol](protocol.md)). Practitioner opinion, no data.

- Q2: the top thread on CAP asks what A and P mean (SO 2012p, 688-vote answer).
  - A second answer (100 votes) calls the 2 of 3 reading misleading, as Brewer 2012 does.
  - SO 2012r and SO 2016p say a system's position depends on configuration.
- SO 2012q explains eventual consistency by analogy; SESE 2017p shows the hard part: an email cannot be undone; SESE 2013p: scaling is BASE against ACID, not SQL against NoSQL.
- Q3: SESE 2013q (60-vote answer) says design for bad paths and test them.
- Q4: SESE 2018p says to ask for operational expectations before estimating; SESE 2016p: how much availability is wanted decides the cost.
- Q5: SESE 2014p shows PATCH idempotence depends on the patch format; SESE 2015p shows latency decides many small against few large calls.

## 11. Designing for a model as implementer

- Cheng 2026: a benchmark of eleven real systems where a model writes a TLA+ model; scored on syntax, running, conformance and invariants (abstract; no results in it).
- Sahu 2026: models gave plausible network designs that missed constraints and showed stickiness to familiar patterns (abstract; no numbers).
- Planning before code (Jiang 2023) belongs to [algorithm-design](../algorithm-design/review.md).
- This search found no measurement of a model implementing a service from a written system design; a vendor benchmark page was located and not read.
