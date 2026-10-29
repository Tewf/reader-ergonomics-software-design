# Against: controversies, null results, where practice contradicts the evidence

This file lists the evidence against the principles of the review, and the places where the evidence disagrees with what practice teaches. No failed replication was found; no study was replicated in this search.

## Against the binary reading of CAP

- Brewer 2012 says the 2 of 3 reading is misleading: partitions are rare and the choice varies per operation.
- The primer states that "you can only support two" of three guarantees, then asks for a CP or AP choice (Primer 2026).
- Kleppmann 2015 adds that the formal definitions of availability and consistency differ from the original ones, and that partition tolerance is an assumption of the system model.
- A 100-vote answer on a Q/A site says the same as Brewer 2012 (SO 2012p), below a 688-vote answer that does not.
- SO 2012r and SO 2016p show the same system sits at different positions by configuration.
- Grade: the disagreement is real; no study measures which reading helps a designer.

## Against design as the main source of failure

- Yuan 2014: 92% of catastrophic failures came from error handling, and 35% from trivial patterns; the authors say simple testing would have caught most.
- Alquraan 2018 finds the opposite for partitions: 47% of the 88 issue-tracker failures needed a redesigned mechanism.
- Both are descriptive studies of open-source systems; the sampling and limits are in section 2 of Yuan 2014 and in the discussion of Alquraan 2018.
- The two do not conflict: error handling and partition handling are different failure classes.

## Against rules for their own sake

- Kotstein 2021: of 82 REST rules, 28 were rated high importance, 17 medium and 37 low (abstract). 45 of 82 were rated at least medium, so a guideline holds many rules experts rate low, but not a majority.
- Murphy 2017: 32 company guidelines differ on some topics (secondary).
- Stylos 2007 (read): with 30 programmers, the design choice the authors expected to help did not (a user study, no statistical test).
- Zalando 2026 and Microsoft API 2026 are long rule sets; neither reports a test of its rules.

## Against injecting failure as a requirement

- SESE 2013q (60-vote answer): design proper bad-path handling and test it; a requirement to crash at random makes real crashes unfilable as bugs.
- Chaos engineering has a multivocal review (Owotogbe 2025; title only).

## Against verified systems being correct

- Fonseca 2017: 16 bugs in three formally verified distributed systems (abstract); verification does not remove the need to test the assumptions.

## Against owner reports

- Newcombe 2015 reports the owner's success with TLA+; there is no control group and no outside replication found.
- Bornholt 2021 reports its owner's 16 prevented issues; two experts worked nine months full time to start.
- Bogli 2024 finds only 16 high-affinity industrial TLA+ papers after screening 290, and opens by citing another work for the scarce adoption of formal methods in industry.
- AWS 2026p reports its own framework; the claim of hundreds of thousands of architectures is the owner's.
- Alquraan 2018 says design reviews would have avoided most failures; the study did not run reviews.

## Against designing from a vague problem

- SESE 2022p: do not expect a precise design from a vague description; ask better questions.
- SESE 2011p: an interview design question tests how you clarify requirements, not a memorised answer.
- Primer 2026 teaches the same first step: outline use cases, constraints and assumptions.

## Where practice contradicts or ignores evidence

- The primer has no mention of outages, postmortems, Jepsen, chaos or TLA+ in its README (one match was a company name).
- Yuan 2014, Alquraan 2018, Gunawi, Lampson, Saltzer and Brewer are not named in the primer; the check was a text search of its README, not of its linked pages.
- Practice mostly does not contradict the studies; it is silent on them.
