# Reader style: a model as implementer

How the software design principles change when the reader is a language model that writes the code from the
document: a coding agent given a specification, a design document or an architecture description. It has three
parts: who the reader is, the overrides, and what is open.

## Who

- **Reader:** a coding agent that implements what the document specifies, and whose output a person then reviews.
- **Expertise:** expert in programming languages and common algorithms; a novice in this system and its decisions.
- **Medium:** a model's context window, where every token costs and long context can dilute what matters.
- **Reading mode:** the whole document at once, then back to it by search while it works.

## Overrides

| Principle | Change | Why |
|---|---|---|
| [Examples and properties as tests](../principles/specification/examples-as-tests.md) | strengthen: the examples are given as runnable tests, and the properties as property-based tests, before any code | tests that clarify intent raised pass rates by about 22 to 54 points with Codex (Lahiri 2022, benchmarks); GPT-4 produced a verified Dafny method with a strong specification for 58% of 178 problems with a chain of thought and retrieval, and 19% with no context (Misu 2024) |
| [Contract before steps](../principles/specification/contract-before-steps.md) | strengthen: the contract is written as checkable assertions; when the model writes them, a person checks them against the examples | programmers accepted wrong generated assertions about half the time, as confidently as correct ones (Kaufman 2026, a preprint, 86 programmers) |
| [Code-like steps](../principles/specification/code-like-steps.md) | keep: a written plan before code helps, by a few points | 2.5 to 4.4 points over six models (Jin 2025); naive chain of thought can lower accuracy |
| [Order a description by the reader's questions](../principles/structure/by-the-readers-questions.md) | relax its length: keep the map of parts short and searchable, and link the rest | repository overviews did not help coding agents in two settings and raised cost by over 20% (Gloaguen 2026), although about 68% of agent context files carry architecture content (Chatlatanagulchai 2025) |
| (shape line) | strengthen: every document names its shape, so the agent can find the rules it follows | convention, untested |

## Thresholds

None changed.

## Open questions

- The benchmarks are single functions with a simulated user; no study gives a model a whole design document and
  measures the code that comes back.
- No study was found of a model reading an architecture description and keeping its invariants.
