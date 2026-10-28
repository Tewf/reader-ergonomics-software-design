# Position

This file says what is known about presenting algorithms, what is not, and what this repository adds.

## Known

- Constrained, code-like text beat plain English prose for professionals in four experiments (Boehm-Davis 1983).
- The flowchart advantage, where found, is contested and tied to the stimulus (Scanlan 1989 and its comments).
- Detailed flowcharts gave no reliable help with debugging or changing programs (Shneiderman 1977, Brooke 1980).
- The better contrast is whether a notation matches reader conventions, not graphical against textual (Petre 1995).
- Practice has settled on code-like pseudocode with a local reference language per context (exam boards, textbooks).
- Pseudocode is common in papers: about one in ten arXiv papers in a random sample (Toksoz 2024).

## Not known

- How readers fare with the major textbook styles side by side (Cormen, Knuth, Sedgewick); this search did not find that comparison.
- Whether published pseudocode is ambiguous enough to cause wrong reimplementations; this search found advice and one case study (Helwer 2023), not a measurement.
- Whether line numbers, an assignment arrow or typeset keywords change comprehension.
- Whether literate presentation improves understanding of an algorithm rather than the amount of documentation.
- Whether findings from students on small programs carry to professionals on algorithms in papers; 53.7% of comprehension experiments used only students (Wyrich 2023).

## Where practice runs ahead of the evidence

- Exam boards fix a reference language and penalise answers outside it, with no study cited in the documents read.
- Reproducibility checklists advise pseudocode with no test that it reduces ambiguity.
- Python is called executable pseudocode in practice; no study of that claim was found.
- Industry reports of executable specifications are the company's own account (Newcombe 2015).
- Typesetting packages for pseudocode are in wide use with no usage counts published on their pages.

## Where evidence is ignored by practice

- The flowchart studies mostly found no gain over text, yet flowcharts remain a question and answer form in exams (OCR 2026).
- The variable-name confound in Boehm-Davis 1983 is rarely mentioned when prose and code-like text are compared.

## What this repository adds

- It joins the old documentation-format experiments to current practice sources in one place.
- It states a named baseline and the tasks and instruments needed to compare against it (baseline.md).
- It claims nothing the cited studies did not measure, and says "this search did not find it" for the gaps.
