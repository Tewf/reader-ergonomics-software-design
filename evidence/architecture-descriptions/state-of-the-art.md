# State of the art, per sub-question

Two records are kept apart. **Best evidence** is a research record: what was measured, how. **Most adopted** is a practice record: what is used, by an owner's account or a count.

| Sub-question | Best evidence | Most adopted | Measured how |
|---|---|---|---|
| How to divide a description | Ernst 2023: structured against essay, no significant effect | 42010 viewpoints and views; Views and Beyond; arc42 (Starke 2026) twelve sections | one experiment, 65 students; standards untested |
| What to read first | Dagenais 2010 (newcomers seek the broad view); Lethbridge 2003 (46% found documentation effective for big-picture information) | ARCHITECTURE.md bird's-eye overview (matklad 2021); C4 context diagram first (used by 81%, IcePanel 2025) | interviews, surveys; vendor survey |
| How many levels of abstraction | Lethbridge 2003: more abstract, more trusted | C4 four levels; components used by 41% against 81% for context | survey correlation; vendor survey |
| One document or one per task | Rost 2013: 14 mentions of a wish for stakeholder- or task-specific content, and "one-size-fits-all" criticised | arc42 offers lean and thorough tips; Backstage docs per component | open-answer counts; owner's claim |
| Finding information in it | de Graaf 2016 (organisation by readers' questions correlates with retrieval); Rost 2013 (unclear structure is the top complaint, 13 of 42) | search and portals (Backstage 2020) | two case studies; coded open answers |
| Keeping it true | Lethbridge 2003, Rost 2013, Migliorini 2024 (75% of views never updated) | docs as code; stable-facts-only rule (matklad 2021) | survey; repository mining |
| Effect on understanding | Ernst 2023 (code familiarity dominates); Kazman 2016 (mixed); Dzidek 2008 (design documents, maintenance) | no practice measure found | experiment; case study |
| What projects have | Ding 2014b (108 of 2,000 projects); Migliorini 2024 (15k views, 12.2k repositories) | none | repository mining |
| Overviews for machine readers | Gloaguen 2026 (overviews not helpful for coding agents) | architecture in about 70% of agent context files (Zarzycki 2026) | benchmark; census |

## Upper bounds (achieved)

- A controlled comparison of two description formats on newcomer understanding exists, with a replication package (Ernst 2023).
- Open-source architecture views have been mined at scale and classified (Migliorini 2024).
- Reader wishes and defects were counted across 147 industrial respondents (Rost 2013).
- A field trial of adding an architecture document to a live project exists (Kazman 2016).

## Lower bounds (not shown by what this search found)

- No controlled comparison of view schemes, section templates (arc42) or abstraction levels (C4) on reader success.
- No controlled study of the entry page itself: overview-first against none, or a codemap against a prose summary.
- No study with reviewers or operators as the readers; the experiments use newcomers or students.
- No test of whether conformance to 42010 improves comprehension.
- No longitudinal study of whether a description stays read after the first weeks.
