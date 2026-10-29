# Position: what is known, what is not, what this repository adds

This file separates "nobody has done this" from "this search did not find it". Every "none found" below is a statement about this search, run on 2026-10-29 by one reviewer.

## Known

- Production failures of distributed systems are mostly simple to reproduce: 98% manifest on three nodes or fewer (Yuan 2014, Finding 3) and 83% of partition failures on three (Alquraan 2018, Finding 12).
- Most catastrophic failures in the sample came from error handling (92%, Yuan 2014); most partition failures were silent (90%, Alquraan 2018).
- The consistency literature is large and ordered: more than 50 notions (Viotti 2016, abstract); the CAP result depends on its definitions (Kleppmann 2015).
- API usability has user studies and a mapping of 47 studies (Rauf 2019).
- A precise model of a design can be checked before code exists, by owners' reports (Newcombe 2015; Hackett 2023); lightweight models cost 13% of a code base in one case (Bornholt 2021).

## Not known

- Whether any principle of computer system design (a hint, the end-to-end argument) improves a design when tested; none found (Q1).
- How accurate estimates made before building turn out to be; none found (Q4).
- Whether design review finds the partition flaws the authors say it would; the claim was not tested (Alquraan 2018).
- Whether an interview primer improves a design; no study (Q8).
- Whether a model can implement a service from a written design; no measurement found (review.md 11).
- The content of three works not reached: Ellis 2007, Nuseibeh 2001 and Brooker 2025.

## Where practice runs ahead of the evidence

- Primers: 376k stars for a study guide whose CAP section the later literature calls misleading (Primer 2026; Brewer 2012; Kleppmann 2015).
- Interface guidelines: three large company rule sets, with no test of their rules found; the controlled studies concern library APIs (Stylos 2007), and experts rated 37 of 82 REST rules low (Kotstein 2021).
- Vendor frameworks: a six-pillar checklist adopted by customers, tested by its owner's claim only (AWS 2026p).
- TLA+ at AWS: one owner reports success; reviews of industrial use exist (Bogli 2024) but no controlled comparison.

## Where evidence is ignored by practice

- The failure studies are absent from the primer README (text search); their finding that simple error-handling tests would have caught most catastrophic failures is not taught (Yuan 2014).
- Brewer 2012 is not named in the primer README, which states the binary reading.
- Practice mostly does not contradict the evidence; it does not cite it.

## What this repository adds

- A review of the topic as a whole, with practice beside research, graded; no earlier review spanning these eight questions was found.
- A boundary: this topic reviews systems, the sibling topics review documents about them.
- A question none of the studies asks: how a design for a running system should be written down so a reader finds its load, failure and consistency assumptions.
- A baseline and a proposal to compare against (baseline.md); it is not run.
