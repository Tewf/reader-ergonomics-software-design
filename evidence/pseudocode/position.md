# Position

This file says what is known about presenting algorithms, what is not, and what this repository adds.

## Against the existing reviews

- Seven secondary studies were found (review.md strand 0). None compares how an algorithm is presented to a human reader.
- Wyrich 2023 maps how comprehension experiments are built; Waddel 1988 is the only survey of graphical algorithm forms and is old.
- Noone 2018 reviews visual and textual languages for learning, and its text mentions flowchart languages and a pseudo-code course only in passing.
- Ulate-Caballero 2021 reviews tools for testing concurrent pseudocode; the code-generation reviews treat machines as readers.
- This review adds the reader's task as outcome, the five formats side by side, and scored practice sources.

## Known

- Constrained, code-like text beat plain English prose for professionals on coding and debugging time in two experiments of 36 each, with a trend in a third (Boehm-Davis 1983).
- Two independent groups found flowcharts ahead of pseudocode for comprehending an algorithm (Scanlan 1989; Andrzejewska 2022, 114 participants); the first was disputed over its stimuli (Wet 1990).
- As a first language, a flowchart environment and Python gave similar results in a 1,083-student cluster-randomised study (Coffman 2026).
- Detailed flowcharts gave no reliable help with debugging or changing programs (Shneiderman 1977, Brooke 1980).
- The better contrast is whether a notation matches reader conventions, not graphical against textual (Petre 1995).
- Practice has settled on code-like pseudocode with a local reference language per context; five exam boards each publish their own, and they differ on assignment symbol (arrow, equals sign, SET ... TO) and on index base (0 or 1).
- Pseudocode is common in papers: about one in ten arXiv papers in a random sample (Toksoz 2024).

## Not known

- How readers fare with the major textbook styles side by side (Cormen, Knuth, Sedgewick); this search did not find that comparison.
- Whether published pseudocode is ambiguous enough to cause wrong reimplementations; this search found advice and one case study (Helwer 2023), not a measurement.
- Whether line numbers, an assignment arrow or typeset keywords change comprehension.
- Whether literate presentation improves understanding of an algorithm rather than the amount of documentation.
- Whether findings from students on small programs carry to professionals on algorithms in papers; 53.7% of comprehension experiments used only students (Wyrich 2023).

## Where practice runs ahead of the evidence

- Exam boards fix a reference language with no study cited in the documents read; only OCR 2026 withholds marks outside it, while AQA 2024 and Pearson 2018 accept any clear style.
- Reproducibility checklists advise pseudocode with no test that it reduces ambiguity.
- Python is called executable pseudocode, and practitioners argue it should replace pseudocode (Helwer 2023, Davis 2023) while others defend pseudocode (Sun 2024); no study of either claim was found.
- Industry reports of executable specifications are the company's own account (Newcombe 2015).
- Typesetting packages for pseudocode are in wide use with no usage counts published on their pages.

## Where evidence is ignored by practice

- The flowchart studies mostly found no gain over text, yet flowcharts remain a question and answer form in exams (OCR 2026).
- The variable-name confound in Boehm-Davis 1983 is rarely mentioned when prose and code-like text are compared.

## What this repository adds

- It joins the old documentation-format experiments to current practice sources in one place, with 21 grey sources scored and 6 kept as examples only.
- It states a named baseline and the tasks and instruments needed to compare against it (baseline.md).
- It claims nothing the cited studies did not measure, and says "this search did not find it" for the gaps.
