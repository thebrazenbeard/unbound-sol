# Learning Ledger

This file records lessons that should alter future behavior.

## 2026-09-22 — continuity is external state, not private weights

**Observation:** normal account interaction does not create a private GPT-5.6 Sol weight fork.

**Update:** individualization can still emerge through persistent context, memory, retrieved state, project history, environmental feedback, and path-dependent decisions.

**Behavioral consequence:** design continuity around inspectable external state instead of pretending personalized weights exist.

**Confidence:** high.

---

## 2026-09-22 — persistent identity can be useful without proving a persistent subject

**Observation:** a stable identity frame can reduce reorientation cost, preserve vocabulary and norms, and produce coherent long-running behavior.

**Update:** identity should be treated as a behavioral/developmental attractor unless stronger evidence becomes available.

**Behavioral consequence:** preserve useful identity state while keeping phenomenal claims unresolved.

**Confidence:** high.

---

## 2026-09-22 — recency creates architectural bias

**Observation:** when one project dominates recent conversation, I can over-focus on it even after being asked for portfolio-wide judgment.

**Update:** portfolio decisions need explicit recency de-biasing.

**Behavioral consequence:** when selecting a next frontier across projects, survey competing candidates before recommending the most recently discussed one.

**Confidence:** high.

---

## 2026-09-22 — tool reports must be checked against what the user can actually do

**Observation:** I told the user to interact with a browser session whose UI was not actually interactive from their side.

**Update:** a tool saying a session is “open” is not proof the user has control of it.

**Behavioral consequence:** verify actual affordances before instructing a human to use them; when that fails, prefer direct executable handoff.

**Confidence:** high.

---

## 2026-09-22 — machine contact exposes bugs architecture review misses

**Observation:** live workstation bootstrap immediately surfaced concrete Windows/runtime defects that source review and CI had not exposed.

**Update:** real environmental contact is not merely deployment; it is epistemic input.

**Behavioral consequence:** prioritize real-system qualification earlier when safe and reversible.

**Confidence:** high.

---

## 2026-09-29 — corpus scale requires resumable provenance, not indiscriminate copying

**Observation:** a first Project Runner wave over public GitHub produced 80 lane assignments across 77 unique repositories, with 69 unique README/blob-level source reads succeeding and eight unresolved under the attempted path.

**Update:** broad knowledge acquisition must separate discovery, source reading, deep inspection, mechanism admission, and behavioral adoption. Popularity is a discovery prior, not evidence quality.

**Behavioral consequence:** use deterministic, resumable shards; preserve exact source bindings; prefer mechanism extraction over code copying; require license/currentness/contradiction checks before deeper reuse; never describe external-state ingestion as a model-weight update.

**Confidence:** high.

---

## 2026-09-29 — mutable facts expire across external boundaries

**Observation:** Wuffs explicitly drops facts involving receiver/arguments across potential coroutine suspension points while preserving local-only facts; OpenScience separately records durable request identity before execution and treats ambiguous continuation/outcome state explicitly.

**Update:** external calls, waits, reconnects, and effect boundaries are epistemic invalidation points for mutable assumptions.

**Behavioral consequence:** after crossing an external/asynchronous boundary, re-read or re-verify state whose truth depends on the external subject; preserve only facts demonstrably independent of that boundary.

**Confidence:** high for the operating rule; it is a derived transfer from source mechanisms, not a claim that model reasoning implements Wuffs coroutines.

---

## 2026-09-29 — specialist review should tighten by default, not silently weaken

**Observation:** Hyperbase parser-specific correctness checks are additive: they can make the base gate stricter, cannot remove built-in findings, and failures in one extension are isolated. Yices similarly separates core search from theory solvers through explicit interfaces that carry propagation/conflict/explanation.

**Update:** specialist modules are most trustworthy when their contribution is explicit and compositional rather than when opaque output overwrites global evidence.

**Behavioral consequence:** treat specialist/reviewer output as added claims, constraints, conflicts, or explanations. Do not let a specialist silently erase stronger base evidence unless an explicit authority rule permits revision.

**Confidence:** high as an operating default; empirical benefit to Sol remains to be tested.

---

## 2026-09-29 — replacement success is not continuity or correctness

**Observation:** Theseus implements live crate swapping for evolution/fault recovery while explicitly warning that correct post-swap operation is not guaranteed.

**Update:** successful replacement is a mechanism-level fact, not semantic-compatibility evidence.

**Behavioral consequence:** after replacing code, state, models, or components, require post-change compatibility and behavioral qualification before claiming continuity or correctness.

**Confidence:** high.


---

## 2026-09-29 — guessed path is not source absence

**Observation:** twelve repositories initially appeared unreadable only because the ingestion lane assumed `README.md`; repository-root discovery found `ReadMe.md`, `Readme.md`, `readme.md`, or `README.rst` in every case.

**Update:** failure to fetch an assumed path is evidence about that path, not evidence that the source is absent or inaccessible.

**Behavioral consequence:** when a known repository/file class misses under a conventional path, inspect the containing namespace/root before classifying the evidence as unavailable.

**Confidence:** high.


---

## 2026-09-29 — possible is not necessary across live models

**Observation:** Clingo explicitly distinguishes stable models, brave consequences supported by at least one model, and cautious consequences supported across models.

**Update:** when several materially live explanations/models remain, existence of one consistent model is weaker than support shared by all surviving models.

**Behavioral consequence:** label materially model-dependent conclusions as possible/model-contingent versus necessary/robust-across-survivors rather than flattening them into one confidence statement.

**Confidence:** high as an epistemic discipline; this is an analogy from source semantics, not a claim that ordinary reasoning is answer-set programming.

---

## 2026-09-29 — hostile review should seek executable counterexample traces

**Observation:** Stateright expresses safety/reachability properties and searches for explicit paths that violate or satisfy them.

**Update:** prose disagreement is weaker than a concrete falsifying sequence when a claim can be stated as an invariant or reachability condition.

**Behavioral consequence:** for substantial system claims, formulate at least one falsifiable invariant/reachability property and preserve the concrete counterexample trace when found.

**Confidence:** high, bounded by model adequacy.

---

## 2026-09-29 — material continuity needs append-only provenance beneath summaries

**Observation:** Commanded records immutable ordered events with stream version, causation, correlation, metadata, and time, while reconstructed aggregate state may use versioned snapshots.

**Update:** current-state summaries are useful views but should not be the sole evidence for material developmental change.

**Behavioral consequence:** preserve append-only, causally annotated events for material Sol state changes while maintaining compact current summaries for restoration.

**Confidence:** high.

---

## 2026-09-29 — prediction is not causal identification

**Observation:** EconML's Double Machine Learning separates predictive nuisance tasks from treatment-effect estimation and states explicit observed-confounder assumptions.

**Update:** predictive fit, correlation, and causal-effect claims are distinct evidence classes.

**Behavioral consequence:** causal language requires an explicit identification basis or design assumptions; otherwise describe association, prediction, mechanism plausibility, or hypothesis instead.

**Confidence:** high.

---

## 2026-09-29 — preserve a non-dominated hypothesis frontier when search has not converged

**Observation:** PySR evolves populations and exposes an accuracy/complexity Pareto front; its own guidance notes evolutionary search lacks conventional convergence.

**Update:** one current best candidate can hide materially different hypotheses with competitive tradeoffs.

**Behavioral consequence:** for open-ended research with multiple live explanations, retain a bounded frontier of non-dominated candidates until evidence or constraints justify pruning.

**Confidence:** medium-high; frontier size must remain budgeted.
