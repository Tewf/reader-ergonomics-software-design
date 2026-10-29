# System diagrams: how to draw a software system so the reader gets the structure

Question: how should diagrams of a software system be drawn so that a reader extracts the right structure quickly and correctly? The diagrams are component and container, deployment, sequence, data-flow, and class diagrams used as documentation. This is a multivocal literature review: formal and grey literature, to Garousi 2019.

Steps: [frame](frame.md) · [protocol](protocol.md) · [review](review.md) · [sources](sources.md) · [state of the art](state-of-the-art.md) · [position](position.md) · [against](against.md) · [baseline](baseline.md) · [bibliography](../bibliography.md)

General principles are not reviewed again here: [draw relations](https://github.com/Tewf/reader-ergonomics/blob/master/principles/page/draw-relations.md) and [figure next to its text](https://github.com/Tewf/reader-ergonomics/blob/master/principles/page/figure-next-to-its-text.md). Which views a description contains belongs to the review "architecture-descriptions".

## Claims

| Claim | Grade | Where |
|---|---|---|
| Good layout (many heuristics together) raises clarity ratings and speeds correct answers; accuracy gains are small | measured, one research group | review.md 2 |
| Diagram size and layout flaws correlate negatively with performance; flaws weigh more (r = -0.419 against -0.270); novices suffer more | measured, one research group, re-analysed data | review.md 2 |
| The centre size differs by data set (44, 49 and 65 elements in three sets), so the size limit is not a threshold | measured, one research group | review.md 2 |
| Single graph-drawing aesthetics (crossings, bends) carry less weight on UML than on abstract graphs | supported with caveat | review.md 3 |
| UML documentation helps complex maintenance tasks, with no time saving | measured | review.md 2 |
| Design-level UML models help code comprehension; analysis-level ones may hurt | measured (secondary) | review.md 2 |
| Visual notations should follow cognitive principles (Physics of Notations); its applications are rarely verified and it is hard to apply objectively | convention | review.md 1 |
| A clearer symbol set gave no accuracy or speed gain when a key was present | measured, 57 novices, one study | review.md 1 |
| Practitioners draw mostly informal diagrams, with some UML elements | measured, descriptive | review.md 4 |
| C4 asks for a title, a key, element types, technologies and labelled one-way arrows; five other producers give similar rules | convention, untested; sources mostly below the quality threshold | review.md 5 |
| In one company, 48 engineers mostly judged C4 with text-defined diagrams successful and missed layout control | measured, descriptive | review.md 5 |
| Diagrams as code is the growing form: Mermaid renders natively on GitHub since 2022 | measured, descriptive | review.md 5 |
| Readers ask what an arrow means, in questions on data-flow, component and flowchart diagrams (about 18,000 and 136,000 views on two of the threads); no study counts the confusion | convention, untested (practitioner questions, SO 2021b, SO 2009d, SESE 2024a) | position.md |
| No controlled study found compares C4 with UML, icon sets with plain boxes, or a key with none | gap (this search did not find one) | position.md |
| Sixteen existing reviews cover UML, notation or visualisation; none isolates reader outcomes of system diagrams or includes grey literature | gap (this search did not find one) | review.md 0 |
