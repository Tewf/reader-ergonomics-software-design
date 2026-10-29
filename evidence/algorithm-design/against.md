# Against

This file collects the evidence against specifying and planning before coding, the controversies, and the replications. A source scored under 10 of 20 is named "example only". "(secondary)" marks a number read in an abstract or a summary.

## Specifications cost more than they return, for most software

- Practitioner essay (Wayne 2019, 12.5 of 20): proofs demand expertise, tools improved mostly through solvers, and for most software partial verification is more economical; its figures are quoted from other sources.
- SESE 2018e (top answer, 21 votes): resource and budget constraints decide, and formal development usually costs much more.
- SESE 2010h: one answer calls formal methods "absolutely useless" beyond the trivial, after a course on Alloy; another says plain English and diagrams work better. Both are anecdotes.
- Woodcock 2009: a respondent found the costly step was annotating code with pre and postconditions; others reported a long specification phase.
- Müller 2002 (secondary summary): in one of two experiments, effort tended to be higher with assertions.

## The effect is small, observed rather than controlled

- Casalnuovo 2015: the authors call the assertion effect small; the design is observational and cannot rule out that careful developers write both asserts and fewer bugs.
- Kochhar 2017 (secondary): the replication on Java found the same direction and the same smallness; a replication that agrees is not a controlled test.
- Polikarpova 2013 (secondary): the largest effect (twice as many bugs) is from the authors' own method on data structures, not on algorithms people write.
- Woodcock 2009: the authors say the invitation drew satisfied users; the 92% is not a rate for all projects.
- Pfleeger 1997 (read once in an author's copy, not re-reached) studied an air traffic control system. It found no quantitative evidence that formally designed code was of higher quality than informal code, and no significant difference between formal methods. The benefit came through simpler, testable components. Static inspection and unit testing were still needed.
- Sobel 2002 (secondary, as described by Berry 2003): the formal group passed all six tests against 45.5% of the control teams. Berry 2003 (read) answers that students volunteered for the formal curriculum, assignment was not random, confounds were not excluded and the test set was small. The authors' reply says the comment misunderstands the experiment (Sobel 2003, summary only).
- Rafique 2013 (secondary): for tests as specification, the meta-analysis summary shows a small quality gain and inconclusive productivity.

## People find the notations hard

- Finney 1996 (secondary): trained students did very poorly in a small reading experiment.
- Gleirscher 2020 (secondary): intent to use rose, ease of use was rated negatively.
- Kaufman 2026: programmers judge incorrect assertions at 49%, with unchanged confidence, and natural-language explanations gave no overall benefit; a low-quality explanation lowered accuracy.
- SO 2009e (top answer, 38 votes): contracts often cannot be stated conveniently, or checked with current tools.

## Contracts are not adopted as the literature expects

- Dietrich 2017: contracts in Java are used less than expected, with large differences between projects, and some contract use points to unsafe subtyping.
- SESE 2012l and SO 2009f: mainstream languages lack support; the accepted route is assertions and libraries.
- Neatu 2026: a standards paper asks whether contracts are ready for C++26 and offers deferral; the paper says it does not argue against contracts as a concept.

## Plans and specifications for a model: results with limits

- Jin 2025 (independent): naive zero-shot chain of thought can lower accuracy; the gain depends on language type system and model size.
- Jiang 2023b and Li 2023b: the largest gains (25.4% and 13.79%, both relative) are the method authors' own, on function-level benchmarks.
- Lahiri 2022 and Fakhoury 2024: the gains are with an idealised proxy for the user, and the follow-up's abstract (45.97%), text (45.73%) and table (about 33 points) disagree.
- Sun 2023: the checker had zero false acceptances on a small hand-made set; that is not a rate on real code.
- Thoughtworks 2025: the spec-driven workflows are elaborate and opinionated, the spec files can be hard to review, and handwriting detailed rules for a model may not scale (radar page, read).
- Spec Kit 2026 and Kiro 2026 report no effect (example only, both under 10).

## Experiments on algorithms are hard to repeat

- Collberg 2016 (secondary): 32.3% of 402 papers backed by code built within 30 minutes.
- Hooker 1995 (read) argues, without data, that competitive testing of heuristics makes fair comparison hard and tells which algorithm is faster but not why. Hooker 1994 (title only; the PDF is an unreadable scan) is not used for any claim.

## Planning before coding is not always better

- SESE 2011l: the top answer calls the extreme of writing the whole program on paper first a bad idea; the second answer defends starting to code.
- SESE 2011m: no specification in natural language is free of ambiguity, and a formal one is not either.
- The Q/A sites hold no study; each answer is an opinion or an experience.

## What the evidence against does not say

- None of it shows that a pre and postcondition costs more than it saves for the algorithms in the question; none measured that either way.
- None shows a plan or a specification harms a model at equal length, except the naive chain of thought in Jin 2025.
