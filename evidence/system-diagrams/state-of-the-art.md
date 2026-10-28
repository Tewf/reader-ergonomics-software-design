# State of the art, per sub-question

This file records who holds the best result on each sub-question of system diagrams, by what method, measured how. Two records are kept apart: **most adopted** (practice) and **best evidence** (research).

| Sub-question | Most adopted | Best evidence |
|---|---|---|
| Notation for architecture sketches | informal boxes and lines, some UML (Baltes 2014) | none comparing notations on architecture diagrams found |
| Notation standard | UML 2.5.1, SysML (OMG 2017) | Budgen 2011, 49 studies; Koç 2021, 128 papers on use |
| Architecture views for readers | C4 (Brown 2026b); owner's adoption claims not verified | Jongeling 2025: 48 engineers, perceptions only; Koning 2002 guidelines |
| Layout | auto-layout in tools; engineers note limited control (Jongeling 2025) | Störrle 2011: 77 students; later work re-analyses their data |
| Size and flaws | no tool limit found | Störrle 2016b: 156 participants, 60 diagrams; flaws weigh more than size |
| Aesthetics | graph-drawing rules (crossings, bends) | Ware 2002, Purchase 2002: partial transfer |
| Eye tracking | none | Yusuf 2007, Sharif 2010 (15 participants) |
| Data-flow for security | STRIDE DFDs, trust boundaries (Microsoft 2023, OWASP 2026) | Schneider 2024, 24 participants |
| Cloud icons | AWS and Azure icon sets | none found |
| Text-defined diagrams | Mermaid, PlantUML, D2 | none found on reader outcomes |
| Key or legend present | C4, IcePanel 2023, AWS 2026b advise one | Santos 2018: key present in both arms, no accuracy gain from clearer symbols |
| Notation design theory | Physics of Notations | van der Linden 2019: applications rarely verified |
| Reviews of the field | none for system diagrams | 16 found; see review.md strand 0 |

## Upper bounds (achieved)

- Layout and size effects are measured on one group's data: 77 participants (Störrle 2011), 156 in the largest set (Störrle 2016b). The 78 of Störrle 2014 and 2016 are a re-analysis, not new subjects.
- Effect at 60 diagrams: layout flaws r = -0.419, size r = -0.270 against mean score.
- Meta-analysis exists for UML and code comprehension: 12 experiments (Scanniello 2018).

## Lower bounds (not yet shown)

- No found study measures a key, element-type labels, or technology labels on a container diagram against a version without them.
- No found study compares C4, UML component diagrams and unstructured boxes on one task.
- No found study measures sequence diagrams against text for readers.
- Samples are mostly students; paper or screen questionnaires.
- No found study replicates the Störrle size and flaw results outside that group.
