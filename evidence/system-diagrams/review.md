# Review

This file reviews the sources on system diagrams by strand: existing reviews first, then theory, controlled studies, layout, and practice. Numbers are from the primary source unless marked (secondary: read in an abstract or in another paper). Each source's quality is in [sources](sources.md).

## 0. Existing reviews (Garousi 2019, Guideline 2)

Sixteen reviews were found. None includes grey literature and none is about reader outcomes of system diagrams.

On UML evidence:
- Pretorius 2008: mapping study of 33 papers; the largest group studies comprehension.
- Budgen 2011: 49 publications to end 2008; researchers take the UML as given (secondary).
- Fernández-Sáez 2013: mapping of 38 papers (63 experiments, 3 case studies) on UML in maintenance; only 3 papers test help for code; generalisation doubtful (secondary; figures not checked).
- Guo 2017: a further-evidence review on UML; found, not read.
- Koç 2021: 128 papers, 2000-2019; UML used mostly for design, class diagrams most (secondary).
- Baldassarre 2019: belief that models help maintenance is scarcely tested, mostly UML (secondary).
- Alhazmi 2026: 26 studies of sequence diagrams in education; comprehension is the main topic (secondary).

On notation and understanding:
- van der Linden 2019: 70 applications of the **Physics of Notations** (a design theory for visual notations, strand 1); new notations adopted it with few verifiable details.
- Dikici 2018: 1066 retrieved, 45 analysed, process-model understandability; findings inconsistent; thresholds for size unknown (secondary; the text was not reached, so these figures and its description of the Störrle experiments were not checked).
- Houy 2012: no consensus on what model understandability means (secondary).

On visualisation:
- Shahin 2014: 53 of 23,056 papers, 1999-2011; graph, notation, matrix and metaphor techniques; few adopted in industry (secondary; figures not checked).
- Chotisarn 2020: 105 of 1440 entries, 2013-2019, sorted by structure, behaviour, evolution.
- Merino 2018: 387 SOFTVIS/VISSOFT papers, 181 studied; 62 of them lack a strong evaluation (abstract; secondary).
- Filho 2019: mapping of visual solutions for architecture evolution; found, not read.
- Obaidellah 2018: 63 eye-tracking studies in programming; UML is the most used representation after Java code (secondary).
- Rahmanian 2026: 64 studies of language models drawing UML and ER diagrams; evaluation is by metrics and rater scoring of the generated diagrams, not by reader tasks (primary abstract).

How this review differs:
- It isolates reader outcomes of diagrams of a system (layout, size, key, labels, notation).
- It adds 21 scored grey sources and a practice baseline.
- It rechecks the primary papers: the layout and size results rest on one group's data (strand 2).

## 1. Theory of notations

- Moody 2009a: the **Physics of Notations** is a design theory of perceptual properties of notations (secondary: abstract).
  - Its nine principles: semiotic clarity, perceptual discriminability, semantic transparency, complexity management, cognitive integration, visual expressiveness, dual coding, graphic economy, cognitive fit (secondary: Guerreiro 2023 tabulates them).
- Moody 2009b applies it to the UML family and Moody 2010 to i*; both are analyses with no participants.
- Störrle 2013 applied it to UML use case diagrams and found it too imprecise to apply objectively (secondary: abstract).
- Santos 2018: 57 novices, standard versus more transparent i* symbols, with a language key; no gain in accuracy or speed, less visual effort. This is the one test found that has a key present, with no key-absent arm.
- van der Linden 2018: 104 practitioner responses rank notation requirements differently for experts and non-experts (secondary).
- Green 1996 and Blackwell 2003: **cognitive dimensions**, a vocabulary without scores.
- Grade: convention; experimental support is indirect.

## 2. Controlled studies of UML and layout

- Arisholm 2006: for complex maintenance tasks, UML documentation improved correctness and design quality, with no time saving.
- Scanniello 2018: a meta-analysis of 12 experiments (the observation count was not checked); design-phase models help source-code comprehension, analysis-phase models hurt (secondary: abstract).
- Fernández-Sáez 2014: a family of experiments on level of detail; result not read.
- Störrle 2011: 77 BSc and MSc students in three experiments (78 took part, 77 completed); each participant saw a given model in one layout only.
  - Right answers 6.35 versus 6.76 of ten, +6.5%; time per right answer 38.37 s versus 31.68 s, 17.4% faster; clarity 5.61 versus 7.81, +28.2%.
- Störrle 2012 reports experiments D to F (class, sequence and state machine diagrams, about 78 participants); not read, described in Störrle 2014 and 2016b.
- Störrle 2014 and Störrle 2016 re-analyse the 2012 experiments D to F (78 participants, over 1200 measurements), not the 2011 data; they are not new experiments.
  - Performance falls with diagram size (slope -0.014 per element); correlation exceeds -0.7 for poor layouts; experts are less affected.
- Störrle 2016b pools the 2011 and 2012 data into 156 participants, 60 diagrams of five UML types, about 14,000 data points; the participants again come from earlier experiments of the same group.
  - Size correlates with mean score at r = -0.270 (medium); layout flaws at r = -0.419 (large).
  - Under its counting rules the centre size is 44 elements (all data), 49 (2011 data) and 65 (2012 data); under the 2014 rules it was about 50.
  - Its guidelines: at most 15-20 flaws, a flaw rate of at most 0.5, and fix flaws before cutting elements.

## 3. Layout aesthetics and eye tracking

- Purchase 2002: users' preferences among aesthetics on UML differ from those on abstract graphs (secondary).
- Eichelberger 2009 is quoted in Störrle 2014 as finding no significant impact of quality on class diagrams (secondary; the paper itself is behind a paywall).
- Ware 2002: on path finding, after path length, continuity and edge crossings cost most (secondary).
- Yusuf 2007: layouts that carry design information, and stereotypes, helped class-diagram tasks (secondary).
- Sharif 2010: 15 participants, 8 role-detection questions, eye tracker; canonical layout improved time for four patterns and accuracy for two.
- Found, not read: Sharif 2009a and 2009b (layout of class diagrams), Soh 2012 (expertise), Byelas 2006 (areas of interest on architecture diagrams).
- Cepeda Porras 2010 compared pattern representations in class diagrams (result not read; paywall).

## 4. Practice of drawing

- Cherubini 2007: whiteboard diagrams are transient and decisions drawn there are often lost (secondary).
- Baltes 2014: 394 respondents; most recent sketches had some UML elements but were informal, and over half were on paper or whiteboard.
- Petre 2013: 50 interviews, 5 patterns of UML use (secondary). Mangano 2015 studies sketching at the whiteboard (found, not read).
- Dobing 2006 and Störrle 2017 survey industrial use of UML, and how widespread it is stays contested.
- Ozkaya 2020: 109 practitioners; class diagrams lead for structure, deployment diagrams for physical structure (secondary; figures not checked).
- Hebig 2016: 21,316 UML diagrams in 3,295 of the 1.24 million projects scanned (10% of GitHub), mostly made at project start (secondary). Ho-Quang 2017: collaboration is the main motive (secondary).
- Koning 2002: guidelines for IT-architecture diagrams, tested with three groups of architects (secondary).
- Nicacio 2022: 5 architecture diagrams from company blogs shown to 34 respondents (132 invited); their descriptions matched the author text poorly; 41% disagreed that all expected elements were present. Five guidelines follow: identify elements, define notation, give detail, mark start and end of reading, use technology symbols.

## 5. Practice: standards, notations, tools and guides

- OMG 2017 (UML 2.5.1), Annex A: a diagram is a graphical representation of part of a model; frame and heading are optional. This reading found no layout rule there. OMG 2024 (SysML v2) is the systems successor; only its landing page was read.
- The C4 model (Brown 2026b, Brown 2026d): a title with type and scope; a key; element type and short description; technology on containers; one-way labelled arrows; a 21-question review checklist.
  - It is its owner's guidance, cites no study, and scores below the quality threshold.
  - Brown 2026c offers adoption claims (10,000 people taught) and advises keeping UML if it works.
- Other producers state similar rules.
  - Label every line, add a key and a title (IcePanel 2023).
  - Name the product beside each icon (Microsoft 2026b).
  - One concept per diagram, with alt text (Fuchsia 2025).
  - Same shape, same meaning; shapes, not colour (GitLab 2026).
  - Text contrast of 4.5:1 (AWS 2026b).
- Data-flow diagrams: symbol sets (Wikipedia 2026b, secondary); trust boundaries drawn as lines or boxes and flows labelled with protocol (Microsoft 2023); high-level overview plus detail (OWASP 2026).
  - Schneider 2024: 24 participants; a DFD traced to code raised correctness of security answers by 41%. Mbaka 2024 is a planned experiment with no results.
- Industrial use of C4: Jongeling 2025, 48 respondents (about 30% response) after two years of C4 in PlantUML beside code; most felt successful; 7 named limited layout control. The figures were not checked: the text was not reached. Mavrogiorgou 2025 and Jokste 2024 describe use without measuring readers.
- Cloud icons: AWS 2026 publishes icon sets; its icon page gives no drawing rules.
- Diagrams as code: GitHub renders Mermaid since 2022-02-14 (GitHub 2022). Brown 2021 names drift as the main failure.
- On 2026-10-28 Mermaid had 90,911 stars, PlantUML 13,383 and D2 25,750 (Mermaid 2026, PlantUML 2026, D2 2026), and 69.4 million npm downloads in a month (npm 2026): adoption counts, not reader benefit.
