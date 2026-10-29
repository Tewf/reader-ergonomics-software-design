# Review

This file reads the literature on designing an algorithm and on stating what it must do, in strands. The strands are existing reviews, design, specification, evidence of effect, readability, practice, engineering, and models as implementers.

The mark "(secondary)" flags a number read in an abstract or a summary and not in the paper. The mark "title only" means the paper was located and not read. Grey scores are in [sources](sources.md), and a source scoring under 10 of 20 is named "example only".

## 0. Existing reviews

- Liu 2024 (read in part: abstract, method, section 5): a systematic review of studies on teaching algorithm design to undergraduates; preprint.
  - It searched the ACM Digital Library up to 2023-08 and kept 94 papers.
  - 38 of the 88 papers with quantitative data use statistical tests; 17 report controlled trials.
  - Greedy algorithms have 8 of the 94 papers.
  - It does not review design techniques as a taxonomy; it tags papers by topic.
- Zhumagambetov 2021: systematic review of teaching formal methods; by its title and abstract it catalogues obstacles and strategies reported by teachers (abstract only, as summarised by a search page).
- Okumus 2025 (abstract read): systematic mapping of contract-based design for dependable systems; 1,221 studies found, 288 analysed.
- Beg 2025 (abstract read): a short survey of 35 papers on using models to write formal specifications from requirements.
- ter Beek 2022: guidelines for empirical studies of formal methods; its abstract says such studies are scarce (secondary).
- Woodcock 2009 and Garavel 2020 are surveys of practice (strand 5).
- Hatcliff 2012 (abstract read) surveys behavioural interface specification languages with a focus on automatic program verification.
- Huisman 2020 (abstract read) asks why formal methods still miss industrial practice and stresses human aspects.
- Gleirscher 2019 (abstract read) summarises strengths and weaknesses of formal methods and sets an agenda for assuring robots and autonomous systems.
- Robins 2003: a narrative review of learning programming; a search summary says its deficits concern problem solving, design and turning a design into a program (secondary).
- No systematic review compared planning strategies or specification styles on correctness outcomes; the nearest are the ones above.
- How this review differs: it joins design, specification and the model as implementer, keeps adoption apart from measured effect, and scores grey sources on 20 criteria.

## 1. Design techniques and problem solving (Q1, Q2)

- Polya 1945 (book not opened): the general heuristics of problem solving; the Q/A sites send learners to it for formal methods too (CS 2012a, example only).
- Levitin 1999 (full text read): names five shortcomings of the usual flat list of techniques. They are mixed levels of generality, divide and decrease not told apart, brute force and transformation missing, no special cases, and classical algorithms left unclassified. It puts four general techniques at the top (brute force, divide-and-conquer, decrease-and-conquer, transform-and-conquer), chosen by a test of generality, and argues from examples, with no data.
  - Levitin 2000 (read) is a magazine article that restates the argument and cites the 1999 paper. It lists five shortcomings of the usual flat list: unequal generality, brute force and transform-and-conquer missing, divide-and-conquer not told from decrease-and-conquer, no hierarchy, and many classic algorithms unclassified.
  - Its level one is brute force, divide-and-conquer, decrease-and-conquer and transform-and-conquer; its level two is local search (greedy, iterative improvement), dynamic programming and state-space-tree methods.
  - It argues from examples and intuition and reports no data.
  - The terms technique, strategy, paradigm and pattern name one category, according to a single answer (CS 2020b, example only).
- Textbooks name their techniques in their chapter lists: Kleinberg 2005 promises "a range of design and analysis techniques" (publisher page); Skiena 2020 has a part called Practical Algorithm Design (publisher page; neither book opened).
- No study that tests whether a taxonomy of design techniques is sound, complete or predictive was found (this search, strings F1 to F2, G4).
- Liu 2024 section 5.1 reports what students do:
  - they under-use recursion and reduction after an algorithms course, and lean on greedy methods even against counterexamples (reading of Ginat 2003 and others; title only for the cited studies);
  - abstraction ability correlated with performance in the algorithms course and in no other of ten courses (reading of Bennedsen 2008, title only).
- Programming plans: Soloway 1986 (abstract read) says teaching problem solving through programming needs a revised introductory curriculum.
  - Spohrer 1985 (machine summary; secondary) gives a descriptive theory of buggy novice programs and a bug categorisation by goals and plans.
  - Soloway 1984 is reviewed in the pseudocode topic.
- Fisler 2014 applied the rainfall problem, a test of plan composition, to over 200 solutions from five courses; functional-first students did better than in earlier work (secondary).
- The design recipe: Felleisen 2004 states a curriculum built on it; the textbook preface lists six steps and offers only teaching experience as support (HtDP 2026, read).
- Loksa 2016 (abstract read): explicit teaching of a six-stage problem solving process, with prompts, raised productivity, independence, self-efficacy, metacognitive awareness and growth mindset in 48 high school students across two summer camps.
- Wirth 1971 and Dijkstra 1975 tie design to derivation: [pseudocode](../pseudocode/frame.md) covers the first; strand 2 the second.

## 2. Stating intended behaviour (Q3)

- Hoare 1969 gives the triple: a precondition, a statement, a postcondition.
- Dijkstra 1975 derives programs from their postconditions with guarded commands.
- Gries 1981 and Back 1998 develop derivation and the refinement calculus (books not opened; DOIs resolve to the books).
- Kourie 2012 describes **correctness by construction**: the specification comes first and the program grows with its proof (book not opened).
- Furia 2014 classifies loop invariants over a range of fundamental algorithms (abstract; secondary); invariants derive from postconditions by recurring patterns, and the study calls for high-level specifications.
- Meyer 1992 puts the triple into the language as a contract: preconditions, postconditions and class invariants checked at run time.
- Abrial 2010 (book not opened) and Jackson 2002 give model-based notations: Event-B and Alloy; Hatcliff 2012 surveys interface specification languages (strand 0).
- Claessen 2000 turns a property into a test run on random inputs; MacIver 2019 does the same for Python.
- Nothing in this strand compares the styles on a measured outcome; each is an argument or a tool.

## 3. Do specifications help, and at what cost (Q4)

- Casalnuovo 2015 (read: abstract and introduction): of the 100 most popular C and C++ projects on a code host, 69 held more than a minimal number of assertions, and 4.6% of methods had one.
  - Methods with asserts had significantly fewer defects; the authors call the effect small.
  - The design is observational; developer skill is not controlled.
- Kochhar 2017: a partial replication on Java projects found a small yet significant relation (185 projects, 20 million lines; secondary).
- Müller 2002: two controlled experiments of programming with assertions; effort moved both ways and programs were slightly more reliable (summary of the abstract, no numbers; secondary).
- Polikarpova 2013: testing against strong specifications found twice as many bugs as standard contracts, at a reasonable cost in annotation and run time (abstract; secondary; the authors' own method on data structure libraries).
- Estler 2014 (abstract read on the preprint): in 21 projects in Eiffel, C# and Java, over 7,700 revisions, contracts are stable compared to implementations.
- Woodcock 2009 (read, section 3): in 62 industrial projects, quality was reported higher in 92% of cases and lower in none.
  - Three times as many projects reported shorter time as longer; five times as many, among those with a view, reported lower cost.
  - The authors warn that the open invitation biased the sample toward satisfied users.
  - One respondent said the costly step was annotating code with pre and postconditions.
- Pfleeger 1997 (read once in an author's preprint copy, whose address was not recorded): code and fault records of an air traffic control system of almost 200,000 lines. They fall in four design types (VDM, finite state machines, VDM with CCS, informal). The audit could not reach a copy, and the IEEE text is closed.
  - It found no quantitative evidence that formally designed code was of higher quality than informally designed code, and no significant difference between the formal methods.
  - Formal specification gave simple, independent components that were easy to unit test; static analysis found latent faults in the delivered code.
  - The authors conclude that specification, static inspection and thorough unit testing are all needed; the system is one product, an observational case study.
- Sobel 2002 (findings as described in Berry 2003; secondary): a quasi-experiment on an elevator simulation. The 6 teams of the formal methods group passed all six tests, against 45.5% of 11 control teams. The students had volunteered for the formal curriculum.
- Berry 2003 (read): a published comment on Sobel 2002; assignment to groups was voluntary and not random, confounds were not excluded, and six test cases are a small sample. The authors' reply (Sobel 2003, summary only) says the faults come from a misunderstanding.
- Rafique 2013 (adjacent): a meta-analysis of test-driven development; a search summary reports a small gain in quality and inconclusive productivity (secondary, no numbers).
- No controlled experiment that compared a pre and postcondition specification with none, at equal effort, on algorithms people write, was found in the strings run.

## 4. Are formal notations readable (Q5)

- Finney 1996: students trained in discrete mathematics and in Z did very poorly in a small reading experiment (repository abstract; no sample size seen; secondary).
- Gleirscher 2020 (abstract read on the preprint): of 216 respondents, intent to apply formal methods rose, and ease of use was rated negatively.
- Kaufman 2026 (abstract read, preprint): 86 programmers judged generated assertions; accuracy was 74% on correct ones and 49% on incorrect ones, with equal confidence (odds ratio 2.94).
  - Natural-language explanations gave no overall benefit; a low-quality explanation lowered accuracy while confidence rose.
- Reading studies of notation in general are in [pseudocode](../pseudocode/review.md); none there tests a pre and postcondition.

## 5. Practice (Q6)

- Surveys of practitioners:
  - Garavel 2020 (read in an open copy) sent 170 invitations and received 130 responses (76%) to 30 questions, and compiled 111 position statements.
  - Of those responses, 62.3% answered that designing trustworthy systems without formal methods is probably or definitely not possible.
  - Snook 2001 (machine summary; secondary) interviewed formal methods users on effects and pragmatic issues.
  - Gleirscher 2020 (N = 216) and Woodcock 2009 (62 projects) are in strands 3 and 4.
- Contracts in the wild:
  - Dietrich 2017 (abstract read): 25 techniques catalogued; in the 200 most popular Maven Central projects (351,034 KLOC) contracts are used less than expected, with large differences between projects.
  - Estler 2014: above 33% of program elements carry contracts in most of 21 contract-equipped projects (preprint abstract).
- Property-based testing:
  - Goldstein 2024 (abstract read): 30 interviews at one trading firm; strengths are complex code and confidence beyond conventional tests, weaknesses are the effort of writing properties and generators.
  - Hypothesis, the Python library: 9,114 stars and 52,744,281 downloads in the last month, read on 2026-10-29 (Hypothesis 2026, scored 11 of 20 for these counts only).
  - Bornholt 2021 is a system design practice at a cloud provider; it is reviewed in the [system-design topic](../system-design/frame.md), not here.
- A production engine specified and verified in Dafny: a team of Amazon authors reports four years of work, a threefold speed gain and differential testing against 10^15 production samples. The source is Chakarov 2025 (abstract and text read), the owner reporting on itself. The TLA+ side of AWS is system design (Newcombe 2015, other topic).
- Standards committee: contracts reached the C++26 working draft in 2025 and a paper of 2026-03 asks whether they are ready to ship (Neatu 2026, read).
- A practitioner essay asks why formal methods are not used and answers with cost, difficulty of proof and social barriers; its figures are quoted from other sources (Wayne 2019).

## 6. Algorithm engineering and experiments (Q7)

- Sanders 2009 (machine summary; secondary): algorithm theory, with its modelling, design and analysis, is an ingredient of algorithm engineering, not a competing approach.
- Johnson 2002 (machine summary; secondary): an informal discussion of issues in analysing algorithms by experiment, from more than a decade of experience; McGeoch 2012 is the book (publisher listing only).
- Müller-Hannemann 2010 (an edited volume on bridging theory and practice) and Hooker 1994 and 1995 (an empirical science of algorithms; testing heuristics) are known by title only.
- Collberg 2016: of 402 papers backed by code, 32.3% could be obtained and built within 30 minutes (a summary of the 2013 technical report; secondary; the article may differ).

## 7. Designing for a model as implementer (Q8)

Benchmarks measure the pass rate on small function-level problems, usually with the authors' own method; vendor pages are in strand 5.

- Planning:
  - Jiang 2023 (abstract; code-davinci-002 on HumanEval and other function-level benchmarks): self-planning raised Pass@1 by up to 25.4% (relative) against direct generation and up to 11.9% against chain of thought.
  - Li 2023 (Table 2): structured chain of thought beat chain of thought by up to 13.79% relative in Pass@1 (ChatGPT on HumanEval, 53.29 to 60.64, or 7.35 points).
  - Jin 2025 (abstract; independent): five prompting paradigms, six Python benchmarks, a 12-language benchmark and six models from 7B to 480B parameters.
    - Its text reports 5 to 12% on average. Its Table 3 gives 2.5 to 4.4 points over zero-shot generation, averaged over six models (about 5 to 9% relative), and -0.6 to +11.9 points per model.
    - Naive zero-shot chain of thought could lower accuracy.
  - Zhang 2023 (abstract): a planning algorithm for the decoding step, not a written plan (adjacent).
- Tests and intent as specification:
  - Lahiri 2022 and Fakhoury 2024: asking the user a few test questions raised Pass@1 within 5 simulated interactions with an idealised user. Lahiri 2022 reports 22.5 to 37.7 points on MBPP and 24.8 to 54.0 on HumanEval with Codex. Fakhoury 2024 reports 45.97% in its abstract, while its text says 45.73% and its Table IV implies about 33 points over seven models. A user study of 15 programmers found fewer wrong judgements of generated code (abstract).
  - Mathews 2024 (abstract): adding test cases to the prompt led to higher success on two benchmarks.
  - Murr 2023 (abstract): 104 problems, four prompt styles, four models; results not read.
- Formal specification and verification:
  - Misu 2024 (Table 1; GPT-4, five attempts): on 178 problems, a verified method with a strong specification came out for 58% with a chain of thought plus retrieval prompt. It came out for 19% with no context and 10% with a signature. Counting any verified method, the shares were 64%, 58% and 53%.
  - Loughridge 2024 (text): on 782 programs, Claude 3 Opus restored the missing verification hints for 67.8%, with up to ten attempts that return the verifier's error. The task fills in hints and does not write the specification.
  - Sun 2023 (abstract): consistency checks among code, docstring and annotations accepted correct instances at up to 87% and no adversarial incorrect ones, on a small hand-made set.
  - Endres 2023 (abstract): defines the task of turning intent into postconditions, with metrics of correctness and discriminative power.
  - Lahiri 2024 and Li 2025 (abstracts): a metric for intent formalization in verification-aware languages; Dafny as an intermediate language the user never sees.
  - Kaufman 2026: people judge incorrect assertions poorly (strand 4).
- Surveys: Jiang 2024 (abstract read) is a systematic review of language models for code generation, with a taxonomy and an empirical comparison; Beg 2025 is above.
- Spec-driven development, as practice: Thoughtworks 2025, Spec Kit 2026 (143,670 stars) and Kiro 2026 describe requirements, design and task files given to an assistant; none of the three pages reports an effect. Piskala 2026 is a practitioner guide on a preprint server (abstract only).

## 8. Q/A sites

16 threads read on 2026-10-29 from three sites (Software Engineering 9, Stack Overflow 4, Computer Science 3), scored in [sources](sources.md). Two score below 10 and are examples only.

- Contracts: the caller meets the precondition (SESE 2011q); mainstream languages lack support, and JML, .NET Code Contracts and ACSL are the named routes (SESE 2012l, SO 2009f).
- Contracts against tests: contracts often cannot be stated or checked conveniently (SO 2009e); they cut the tests needed (SO 2008d); both serve as oracles (SESE 2013d).
- Formal methods at work: answers split between useless beyond the trivial and plain English with diagrams (SESE 2010h); cost is the barrier (SESE 2018e).
- Plan before coding: write a spec first, not the whole program (SESE 2011l); a spec marks when work is done (SESE 2011n); no specification is fully unambiguous (SESE 2011m).
- Properties as tests: SESE 2015g; a case on Hirschberg's algorithm (SO 2015a).
- A first-hand account of Dijkstra's formal curriculum at one university (CS 2016a).
