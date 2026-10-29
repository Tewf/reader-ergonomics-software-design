# Position: what is known, what is not, what this repository adds

This file separates what research has measured from what practice does, and says what this repository adds. It never confuses "nobody has done this" with "we have not seen it".

## Known

- Metrics of design predict faults in a controlled set of eight systems (Basili 1996b) and in a model that found over 90% of faulty classes (Briand 2000, secondary). Error-prone files cluster in a few architecture subspaces (Xiao 2014; Mo 2015, secondary). Organisational metrics beat code metrics in one large case (Nagappan 2008).
- Socio-technical congruence predicted failures in two industrial projects (Cataldo 2013, secondary) and was unrelated to bugs and churn in 25 open source projects (Mauerer 2022): the effect depends on the setting.
- Mirroring of organisation and structure is prevalent but not universal in industry and firm studies, and not supported in open collaborative projects, over 142 studies (Colfer 2016).
- Patterns have no firm general support in 11 experiments; documenting them helps pattern-relevant tasks in small programs (Zhang 2012; Prechelt 2002).
- A monolith can beat services on one machine, and vertical scaling can be cheaper (Blinowski 2022).
- Architectural decisions rank first as a source of technical debt among 1,831 survey participants (Ernst 2015, secondary).
- Erosion has non-technical causes that deserve equal attention (Li 2022).

## Not known

- No controlled study compares design methods (ADD against none) on a real system.
- No controlled study shows that evaluating an architecture before building raises the quality of the result.
- No controlled study tests information hiding as a decomposition criterion, and no intervention study shows that restructuring lowers change cost; the evidence for modularity is predictive and observational.
- No study found that measures the architectural quality of code a model writes from a given architecture (Schmid 2025 names it underexplored).
- This search did not read the full text of most formal sources; a result may exist in a paper read by title only.

## Where practice runs ahead of the evidence

- Style guides, [well-architected](../system-design/frame.md) pillars and Radar techniques give advice with no study behind it (Microsoft 2025; AWS 2026d; ThoughtWorks 2017).
- The microservices default spread before controlled comparisons; companies now report both moves (Mendonca 2021; Noonan 2018).
- The inverse Conway maneuver is a method built on a law that holds in part (Colfer 2016).

## Reasoning of architects

- Studies of designers show satisficing and naturalistic decisions (Tang 2015; Zannier 2007, summary lines, secondary) and a catalogue of 37 biases with little work on mitigation (Mohanani 2020). Methods such as ADD do not state which of these they address.

## Where evidence is ignored or unused by practice

- Zhang 2012 found no firm support for patterns in general, while practitioners still debate named patterns by the direction of dependencies, without citing studies (SESE 2022b).
- Colfer 2016 shows exceptions to mirroring; the Team Topologies key-concepts page does not mention Conway's law or its exceptions (Team Topologies 2026).

## What this repository adds

- A pool of 95 sources on one question, graded, with the boundary to four neighbour topics.
- A table of which claims are measured and which are convention (README).
- A map of what was not found, so a later reviewer starts from it.
- It adds no new measurement and makes no claim to the state of the art.

## For the repository's own rules

- Link a decision to its structure rule, and say whether the rule is measured or convention.
- When the reader is a model, say which structure the model must keep; no measured effect is known.
