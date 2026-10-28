# Review

Surveys first, then the controlled studies, then practice. Numbers are from the primary source unless marked (secondary).

## 1. Theory of notations

- Moody 2009a: the **Physics of Notations** is a design theory of perceptual properties of notations, synthesised from theory and evidence in several fields (secondary: abstract).
  - It names nine principles, among them semiotic clarity, perceptual discriminability, semantic transparency, complexity management, dual coding (secondary).
  - It was published as a theory to evaluate, compare and improve notations, not as an experiment.
- Moody 2009b applies it to the UML family; Moody 2010 applies it to the i* notation. Both are expert evaluations.
- van der Linden 2019 reviewed 70 applications: those that designed new notations mostly adopted the theory uncritically, with few verifiable details (secondary).
- Störrle 2013 proposes an operationalisation so that applications become checkable (abstract not available to this search).
- Green 1996 and Blackwell 2003: **cognitive dimensions**, a vocabulary (viscosity, hidden dependencies, role-expressiveness and others) to compare notations by activity. It gives no scores.
- Grade: convention; experimental support is indirect.

## 2. Controlled studies of UML and layout

- Budgen 2011: 49 empirical publications to end 2008. Researchers use the UML as given and rarely ask how to make it more effective (secondary).
- Arisholm 2006: controlled experiments at two sites. For complex maintenance tasks, past a learning curve, UML documentation improved functional correctness and design quality. No time saving (secondary).
- Scanniello 2018: 12 experiments pooled. Design-phase models appear to help comprehension; analysis-phase models appear to hurt (secondary: snippet of the paper).
- Fernández-Sáez 2014: a family of experiments on the level of detail of UML diagrams; results not read.
- Störrle 2011: 77 students in three experiments, compound good versus bad layouts on requirements-analysis diagrams.
  - Right answers 6.35 (bad) versus 6.76 (good) out of ten, +6.5%.
  - Time per right answer 38.37 s versus 31.68 s, 17.4% faster.
  - Clarity rating 5.61 versus 7.81, +28.2%.
  - Grade: measured; students, paper questionnaires.
- Störrle 2014: 78 participants, over 1200 measurements. Performance falls as diagram size rises; the correlation exceeds -0.7 for poor layouts in the novice subset.
  - The fitted line has slope -0.014 per element.
  - The author reads 20 to 60 elements as the range where an average modeler answers about half the questions correctly.
  - Experts are much less affected than novices.
- Störrle 2016 extends this to a larger data set and two more diagram types (secondary).

## 3. Layout aesthetics and eye tracking

- Purchase 2002: on UML diagrams, users' preferences among aesthetics differ from those found on abstract graphs (secondary).
- Eichelberger 2009 is quoted in Störrle 2014 as finding no significant impact of quality on class diagrams.
- Ware 2002: on path finding in node-link graphs, after path length, continuity and edge crossings cost most; branching at nodes also matters (secondary).
- Yusuf 2007: 
  - layouts that carry design information, and stereotypes, helped class-diagram tasks;
  - gaze differed by expertise (secondary).
- Sharif 2010: 15 participants, 8 role-detection questions, eye tracker. A canonical layout improved time for all four patterns and accuracy for two (secondary).
  - Classes close together and in canonical layout acted as visual beacons, even against general aesthetics.
- Cepeda Porras 2010 compared design-pattern representations in class diagrams (result not read).

## 4. Practice of drawing

- Cherubini 2007: whiteboard diagrams are transient; design decisions drawn there are often lost (secondary).
- Baltes 2014: survey of 394 people. Most recent sketches or diagrams contained some UML elements but were informal; more than half were on paper or whiteboard (secondary).
- Petre 2013: 50 interviews, 50 companies, 5 patterns of UML use (secondary).
- Dobing 2006 and Störrle 2017 survey industrial use; the question of how widespread UML is stays contested.
- Ozkaya 2020: 109 practitioners; class diagrams top choice for most structural models, deployment diagrams for physical structure (secondary).
- Hebig 2016: 10% of GitHub (1.24 million projects) scanned; 21,316 UML diagrams in 3,295 projects, mostly created in a short phase at project start (secondary).
- Ho-Quang 2017: 485 answers from 458 open-source projects; collaboration is the main motive (secondary).
- Koning 2002 wrote guidelines for IT-architecture diagrams (hierarchy, layout, colour, form) and tested them with three groups of practising architects (secondary).

## 5. Practice: standards, notations and tools

- OMG 2017 defines UML 2.5.1. SysML is its systems profile; OMG 2024 covers SysML v2. Neither was read here.
- The C4 model (Brown 2026b): notation independent. It asks for:
  - a title stating type and scope;
  - a key for shapes, colours, borders, lines and arrowheads;
  - the type and a short description on each element, the technology on each container;
  - one-way, specifically labelled relationships, with protocol between containers;
  - consistent colour, checked for print and colour blindness.
  - This is its owner's guidance (C4 model).
- Data-flow diagrams: DeMarco and Gane and Sarson symbol sets (Wikipedia 2026b, secondary). DFDs are the input to STRIDE and LINDDUN threat modelling (Sion 2018, secondary).
- Schneider 2024: 24 participants; a DFD with traceability to code raised correctness of security-analysis answers by 41% (secondary).
- Cloud icons: AWS publishes icon sets and guidelines (AWS 2026); its networking guide asks for legibility at 700 px width (AWS 2026b, secondary). Azure and Google Cloud guides were not read.
- Diagrams as code:
  - GitHub renders Mermaid in Markdown since 2022-02-14 (GitHub 2022; the page gives no usage numbers).
  - On 2026-10-28 the Mermaid repository had 90,912 stars and npm reported 69.4 million downloads for the last month (Mermaid 2026, npm 2026). PlantUML 13,383 stars, D2 25,750.
  - These are adoption counts, not evidence of reader benefit.
