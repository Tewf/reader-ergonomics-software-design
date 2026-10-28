# Pseudocode: how to present an algorithm to a reader

Question: how should an algorithm be presented (pseudocode, flowchart, structured English, program design language, literate program, executable specification, real code) so the reader understands it and can implement or verify it.

Steps: [frame](frame.md) · [review](review.md) · [state of the art](state-of-the-art.md) · [position](position.md) · [against](against.md) · [baseline](baseline.md) · [bibliography](../bibliography.md)

Related general principles (not reviewed again here):

- [Draw relations](https://github.com/Tewf/reader-ergonomics/blob/master/principles/page/draw-relations.md)
- [Define before use](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/define-before-use.md)
- [Names predict content](https://github.com/Tewf/reader-ergonomics/blob/master/principles/collection/names-predict-content.md)
- [Worked examples with subgoals](https://github.com/Tewf/reader-ergonomics/blob/master/principles/document/worked-examples-with-subgoals.md)
- [Figure next to its text](https://github.com/Tewf/reader-ergonomics/blob/master/principles/page/figure-next-to-its-text.md)
- Identifier names: the [psycholinguistics review](https://github.com/Tewf/reader-ergonomics/tree/master/evidence/psycholinguistics) covers the code-readability studies.
- Readers that are models: the [LLM readers review](https://github.com/Tewf/reader-ergonomics/tree/master/evidence/llm-readers).

## Claims

| Claim | Grade | Where |
|---|---|---|
| Detailed flowcharts gave no reliable gain over text for writing, reading, debugging or changing programs | measured, old and small tasks | review.md 1 |
| Code-like constrained text (PDL) beat plain English prose for tracing, coding and debugging by professionals; part of the gap was variable naming | measured | review.md 1 |
| PDL designs were more detailed than flowchart designs; comprehension of equivalent designs did not differ | measured, abstract read only (secondary) | review.md 1 |
| Structured flowcharts beat pseudocode in one author's comprehension and preference experiments; the stimuli were disputed | measured, contested | review.md 1, against.md |
| Visual against textual is the wrong contrast: the notation must match the conventions readers expect | supported with caveat | review.md 2 |
| The comparison literature is thin: 95 code comprehension experiments in 40 years, over half with students only, one replication | measured, descriptive | review.md 2 |
| Three of the four exam boards checked define their own reference language; pseudocode has no common standard | measured, descriptive | review.md 4 |
| About one arXiv paper in ten has pseudocode (1991-2023 sample) | measured, descriptive | review.md 5 |
| Reproducibility guidance asks for pseudocode to reduce ambiguity; no study tested that it does | convention, untested | review.md 5 |
| An executable specification found bugs that prose and pseudocode designs hid (one company, self-reported) | convention, untested | review.md 6 |
| Literate programming raised the amount of documentation in one course; no comprehension experiment was found | supported with caveat | review.md 7 |
| Indentation as an aid has mixed evidence: one replication failed, one trial found a large effect on reading time | supported with caveat | review.md 2 |
