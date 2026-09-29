# Global GitHub Ingestion V1

## Purpose

This work turns the user's "ingest every repo you can" instruction into a resumable Project Runner program. Literal exhaustive ingestion of all GitHub in one session is not technically possible, and indiscriminate copying would be epistemically poor and licensing-hostile. The durable objective is therefore **coverage that can keep expanding without losing provenance**.

The target is not a model-weight update. GPT-5.6 Sol remains the underlying substrate. What can change is the external developmental layer: source maps, retrieval surfaces, tested mechanisms, reasoning defaults, and future behavior after restoration.

## Project Runner execution model

Wave 1 used ten collision-independent source-analysis lanes. Each lane had a bounded eight-repository fan-out and a read-only effect ceiling.

1. model learning
2. agents
3. memory / RAG
4. knowledge graphs / semantics
5. distributed systems / data
6. compilers / runtimes
7. robotics / embodiment
8. neuroscience / cognition
9. verification / security
10. reference / discovery indexes

The wave contained 80 lane assignments across 77 unique public repositories. README/blob-level source reads succeeded for 72 lane assignments (69 unique repositories). Eight unique sources remain unresolved because the assumed README path could not be fetched. Those are preserved as unresolved, not treated as absent.

## First-wave synthesis

The strongest reusable pattern is not "copy more code." It is **layered generalization with provenance**:

- model-learning repositories provide training, differentiation, autograd, transformer and engineering knowledge;
- agent repositories emphasize decomposition, tool use, orchestration, memory and execution surfaces;
- RAG and knowledge-graph repositories expose competing retrieval models: vector, graph, hierarchical/reasoning-based, live-data and code-structure retrieval;
- distributed-system repositories reinforce consensus/currentness, caching, failure handling, scaling and durable state;
- compiler/runtime repositories show staged transformation, typed intermediate representations and correctness/performance tradeoffs;
- robotics and ML-systems repositories force contact with sensing, control, timing, hardware and real-world failure;
- neuroscience/cognition repositories provide experiment design, neural simulation, physiological acquisition and computational-neuroscience constraints;
- formal-verification repositories provide an important counterweight to heuristic confidence: executable specifications, proof obligations and verified compilation/cryptography;
- curated indexes are valuable as discovery graphs but are not evidence that their linked material is correct.

These are candidate mechanisms. README evidence alone does not qualify an implementation or scientific claim.

## Admission rule

A source may change durable Sol behavior only after recording:

1. exact repository and source binding;
2. license/reuse status when implementation details matter;
3. extracted proposition or mechanism;
4. evidence class and currentness;
5. contradictions/rival approaches;
6. hostile review or falsifier where material;
7. a concrete future behavioral consequence.

Popularity and stars are discovery signals, not epistemic authority.

## Expansion strategy

The program should keep expanding through deterministic shards: topic × language × size × creation/update windows × star bands, with pagination checkpoints. Curated indexes seed lower-popularity and niche discovery. Duplicate repositories collapse by repository identity while preserving multi-lane relevance.

No claim of "GitHub complete" is allowed until the traversed query space and API limits justify it. Coverage reports must distinguish discovered, source-read, deeply inspected, mechanism-admitted, rejected, and unresolved sources.

## Current frontier

Wave 2 should deepen the highest-information sources rather than merely increase the count: memory architectures, retrieval/knowledge graphs, agent control, formal verification, distributed currentness, embodied systems, and neuroscience experiment methodology. In parallel, discovery shards should continue widening the corpus.


## Wave 2 — diversity expansion

Wave 2 deliberately reduced Wave 1's popularity bias by sampling lower-star and niche repositories across scientific computing, theorem proving, databases, programming languages and virtual machines, research operating systems, search/indexing, scientific tooling, cognitive/neuroscience work, autonomous systems, and knowledge representation.

Wave 2 executed 80 lane assignments across 78 unique repositories. Seventy-six lane reads succeeded (74 unique repositories); four unique repositories remain unresolved under the attempted README path.

Across Waves 1 and 2, the current ledger contains **160 lane assignments across 155 unique public repositories**. After exact repository-root repair of filename/case/extension mismatches, **all 155 unique repositories now have successful blob-bound source reads**. These numbers are corpus-coverage facts, not intelligence scores.

### Deep-inspection lane

Five Wave 2 sources were promoted beyond README-level inspection and bound to exact repository heads in `state/global-github/DEEP_DIVE_2026-09-29_V1.json`:

- OpenScience — durable request receipts, idempotent run identity, explicit indeterminate/ambiguous outcomes, and non-replay of unfinished external effects after process loss;
- Yices 2 — explicit SAT/SMT core ↔ theory-solver interfaces carrying propagation, conflict and explanation;
- Hyperbase — additive correctness checks that can tighten but not silently weaken base validation;
- Wuffs — explicit suspension semantics that invalidate facts tied to mutable receiver/argument state across suspension boundaries;
- Theseus — live component replacement with an explicit warning that successful swapping does not guarantee correctness.

The transferred lessons are operating patterns, not claims that Sol internally implements these systems.

## Current frontier after Wave 2

The next expansion should do three things in parallel:

1. run contradiction-seeking deep dives on architectures that *disagree* with the current admitted defaults;
2. execute the new behavioral probes in `EXPERIMENTS.md` for currentness invalidation, monotonic specialist review, and replacement-vs-continuity;
3. deepen source evidence from README/docs into implementation/tests and explicit license metadata before broader mechanism admission.

Coverage should also begin tracking languages, topic families, repository age/update bands, and evidence depth so the corpus can expose its own blind spots.


### Source-path repair

The original 12 unresolved reads were reclassified after repository-root inspection. Every case was a path convention mismatch, not an inaccessible repository: variants included `ReadMe.md`, `Readme.md`, `readme.md`, and `README.rst`. The corresponding work-unit inputs now bind the exact discovered path and blob SHA, preserve the initial failed path, and all 20 wave work units are back in `VERIFYING`.
