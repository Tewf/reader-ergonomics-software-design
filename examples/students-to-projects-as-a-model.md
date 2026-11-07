# Students to projects

**Shape:** [model specification](../shapes/model-specification.md)

**Problem.** Place as many students as possible on projects they wished for, at most one project per student and at
most the project's places per project, from the wish list and the places.

**Sets and data.**
- Set `I`: the students. Set `J`: the projects.
- Datum `w[i][j]`: 1 if student `i` wished project `j`, else 0; from the wish list.
- Datum `q[j]`: the places on project `j`, a non-negative integer; from the project list.

**Variables.**
- `x[i][j]`: 1 if student `i` is placed on project `j`, else 0; binary, one per pair with `w[i][j] = 1`.

**Objective.** maximise `sum over i, j of x[i][j]`: the number of students placed.

**Constraints.**
- For each student `i`: `sum over j of x[i][j] <= 1`: "a student gets at most one project".
- For each project `j`: `sum over i of x[i][j] <= q[j]`: "a project takes at most its places".
- For each pair: `x[i][j] <= w[i][j]`: "only a wished project", which removes the unwished pairs.

**Relaxation.** Exact. The constraint matrix, one row per student and one per project with each variable in exactly
one of each, is the incidence matrix of a bipartite graph, which is totally unimodular. With integer places, every
vertex of the relaxed polyhedron is then integer (Hoffman 1956). The model is a bipartite matching with quotas.

- Solver: the LP alone, or a maximum flow from a source through students to projects to a sink.

**Examples.**

| Instance | Optimum | One optimal point | Why this case |
|---|---|---|---|
| no students | 0 | nothing placed | empty input |
| one student, one wished project with one place | 1 | the one pair | one element |
| A wishes Y and X; B wishes Y; C wishes X; D wishes X and Z; one place each | 3 | A on Y, C on X, D on Z; B unplaced | a chain of wishes that blocks one student |
| the same with two places on Y | 4 | A and B on Y, C on X, D on Z | a quota above one |

**Properties.**
- The optimum never exceeds the number of students, nor the total of the places.
- Any set of pairs that uses each student once, each project at most `q[j]` times and only wished pairs is feasible,
  so the optimum is at least its size. Conversely every integer feasible point is such a set. That is the reduction
  proved both ways.
- Adding a place to a project never lowers the optimum.

**Plan.**
1. Write the four examples as tests, each with its optimum and one optimal point.
2. Implement the three constraint families line by line after the sentences; solve the examples by enumeration first.
3. Solve them with the LP alone and check that every vertex is integer, then run the three properties on random
   instances against the enumeration.

**Out of scope.**
- Preferences between wished projects: a cost per pair turns the model into an assignment with costs, still exact.
- Projects that need a minimum headcount: a threshold per project, which makes the relaxation a bound.

**Open questions.** None.

The examples and the properties were run before publication: the four instances by enumeration and by the LP
(HiGHS dual simplex), and 300 random instances against enumeration, every LP vertex integer.
