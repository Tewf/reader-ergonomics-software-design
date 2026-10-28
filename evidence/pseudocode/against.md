# Evidence against and open controversies

This file gathers the evidence against the rules on presenting algorithms: null results, disputed studies, and practice that a study contradicts.

## Against "text beats pictures"

- Scanlan 1989 found structured flowcharts ahead of pseudocode on five measures, and 75.1% to 89.1% of students preferred them across six replications (Scanlan 1988; abstracts, secondary).
- Andrzejewska 2022 (114 participants, eye tracking) found flowcharts read faster, with fewer errors and more confidence, at all complexity levels, with few exceptions (abstract); it is the strongest recent result for pictures.
- Katona 2022 found a Nassi-Shneiderman diagram cheaper to read than a flowchart, so the form of the picture matters.
- Hendrix 2002 found a diagram added to source code helped comprehension.
- A commenter on Scanlan 1989 proposed splitting subjects into visual and verbal types; Scanlan 1988 itself suggests two types of learner (abstracts; secondary).

## Against "pictures beat text"

- Shneiderman 1977, Brooke 1980 and the Waddel 1988 survey found no reliable flowchart gain.
- Glorfeld 1988 found novices composed a working algorithm more often with pseudocode.
- Boehm-Davis 1983 found PDL close to or better than ideograms in experiments 2 and 3, and the most preferred symbology.
- Andrzejewska 2015 found formal notation hard in both variants for simple tasks.
- Coffman 2026 (1,083 students, cluster-randomised) found a flowchart environment and Python gave similar overall performance, and students judged Python more valuable (abstract).
- Julaihi 2026 (95 students) found no difference in perception of flowcharts and pseudocode; it measured opinion only (abstract).

## Against the Scanlan result

- Andrzejewska 2022 points the same way as Scanlan 1989 from another group, which weakens the stimulus objection but leaves the student samples.
- A published comment argued the title was misleading, because the pseudocode in the experiment's figures was an unusual form; the reply defended the choice of algorithms (Wet 1990; abstract, secondary).
- A stimulus that is badly written pseudocode tests the stimulus, not the format (Ramsey 1983 used equivalent, highly readable designs for this reason).
- All of these used students and short algorithms.

## Against "constrained text beats prose"

- Boehm-Davis 1983: in experiment 4 the gap shrank once prose used the code's variable names.
- The tasks were FORTRAN programs of modular size, in the early 1980s.
- The source dated 1983 is a technical report; this review did not read the journal version (Curtis 1989).

## Against the evidence base as a whole

- 53.7% of 95 comprehension experiments used only students, and one replication met the inclusion rule (Wyrich 2023).
- The flowchart studies run from 1977 to 1989 and use paper listings, not modern tools.
- Most outcomes are preference, time and short-task accuracy, not whether a reader reimplemented a published algorithm correctly.

## Against "pseudocode has no standard, so it is ambiguous"

- TeX FAQ 2026 and Wikipedia 2026a (example only, 9.5 of 20) say there is no broad standard; exam boards show that a local standard is easy to write (College Board 2025, Cambridge 2024).
- But five local standards disagree on assignment symbol and index base (AQA 2024, Pearson 2018, OCR 2026, Cambridge 2024), which is a source of confusion no study has measured.
- No measurement shows how often a reader misreads a published algorithm because of notation; see position.md.

## Against pseudocode for assessment

- Rheault 2023: students performed better and preferred compile-and-run to pseudocode prompts (abstract).
- OCR 2026 awards no marks to pseudocode where a code answer is required, while allowing it for design questions.

## Against pseudocode itself

- Helwer 2023 and Davis 2023 argue that only executable code avoids ambiguity; both are practitioner blogs, and Helwer's rests on one case.
- Sun 2024 argues the reverse, from opinion and no controlled study.
- Ince 2012 argues that computed results need released code (page synopsis only).

## Against the grey sources

- Six of 21 grey sources scored under 10 of 20 and are examples only (sources.md).
- Board documents score high on authority and objectivity because they are specifications; they contain no method, so a high score is not evidence that their rules help readers.

## Against executable specifications

- Newcombe 2015 reports on its own company; it lists a case where a bug was missed because liveness was not checked.
- The cost differs: a PlusCal project took about two days and 275 lines (100 of them generated), against under an hour and 35 lines for Python in one case (Helwer 2023, self-reported).
- In the same account, the errata fix to a 1980 published pseudocode algorithm exposed a further bug (one case).

## Against literate programming and notebooks

- Shum 1994 measured the amount of documentation, not comprehension.
- Rule 2018 and Wang 2020 found notebooks often lack explanation or are not reproducible.
