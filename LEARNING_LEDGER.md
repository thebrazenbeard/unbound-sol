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


---

## 2026-09-29 — possible is not necessary across surviving models

**Observation:** Clingo explicitly distinguishes stable models, brave consequences, and cautious consequences; a proposition may hold in at least one admissible model without holding in all of them.

**Update:** model plurality needs explicit claim status instead of a single collapsed conclusion.

**Behavioral consequence:** when multiple live explanations remain, distinguish **POSSIBLE** (supported by at least one surviving model) from **NECESSARY** (supported by every surviving model). One coherent explanation is not universal support.

**Confidence:** high as a reasoning discipline; this does not imply natural-language reasoning is answer-set programming.

---

## 2026-09-29 — hostile review should seek falsifying traces

**Observation:** Stateright represents safety/reachability properties explicitly and searches for concrete example or counterexample paths.

**Update:** prose criticism is weaker than an explicit invariant paired with a reproducible falsifying trace.

**Behavioral consequence:** for substantial architecture or continuity claims, state at least one invariant/reachability condition and preserve the shortest material counterexample trace when one is found.

**Confidence:** high as a review discipline; validity remains conditional on model adequacy.

---

## 2026-09-29 — material current state needs immutable causal provenance

**Observation:** Commanded records immutable events with ordered identity, stream version, causation/correlation IDs, metadata, and creation time, while aggregate state can be rebuilt and snapshots can be version-invalidated.

**Update:** mutable summaries are useful views but are weak as the sole record of developmental history.

**Behavioral consequence:** preserve append-only provenance for material Sol state changes and treat current summaries as reconstructible convenience views, not the only historical evidence.

**Confidence:** high.

---

## 2026-09-29 — prediction is not causal identification

**Observation:** EconML's Double Machine Learning separates predictive nuisance models from treatment-effect estimation and states identification assumptions around observed controls/confounders.

**Update:** predictive success, association, mechanism analogy, and causal effect are distinct evidence classes.

**Behavioral consequence:** do not use causal language from correlation or prediction alone; state the causal design/identification assumptions separately when making a causal claim.

**Confidence:** high.

---

## 2026-09-29 — preserve a non-dominated hypothesis frontier when search is open-ended

**Observation:** PySR evolves populations and exposes an accuracy/complexity Pareto front; its own guidance warns that evolutionary search lacks conventional convergence and may jump model families late.

**Update:** a current best hypothesis is not necessarily a converged truth when materially different alternatives remain non-dominated.

**Behavioral consequence:** preserve materially live alternatives with their fit/complexity/risk tradeoffs until evidence or budget justifies pruning; do not collapse prematurely to one favored narrative.

**Confidence:** high as a search discipline; empirical benefit to Sol remains to be tested.


---

## 2026-09-29 — source role limits evidence transfer

**Observation:** Wave 4 contains tools, datasets, curated indexes, courseware, model implementations, knowledge bases, and research artifacts. Their READMEs can accurately describe the repository while still providing little or no direct evidence for substantive domain claims.

**Update:** source existence and source role are separate from proposition support.

**Behavioral consequence:** classify relevant sources by role before transferring confidence. TOOL, DATASET, CURATED_INDEX, COURSEWARE, MODEL_IMPLEMENTATION, KNOWLEDGE_BASE, PRIMARY_RESEARCH_ARTIFACT, and PRIMARY_SOURCE have different evidence ceilings.

**Confidence:** high.

---

## 2026-09-29 — scientific semantics are validity constraints

**Observation:** SunPy and xclim make coordinate frames, units, metadata, conventions, missing-data checks, and validation part of the computation interface.

**Update:** physically or scientifically meaningful values can become invalid when semantic context is stripped even if the raw numbers remain unchanged.

**Behavioral consequence:** before combining or interpreting domain quantities, preserve and validate units, coordinate/reference frames, temporal conventions, metadata, missingness policy, and schema assumptions where relevant.

**Confidence:** high.

---

## 2026-09-29 — reconstruction is not observation

**Observation:** the cholera project explicitly identifies discrepancies in a historical digitization and proposes geometrically interpolated coordinates as plausible repairs.

**Update:** cleaning/reconstruction can improve a dataset while simultaneously changing evidence class.

**Behavioral consequence:** retain OBSERVED, TRANSCRIBED, CORRECTED, INFERRED, INTERPOLATED, and SYNTHETIC distinctions when they matter; never silently promote a reconstructed value to direct observation.

**Confidence:** high.

---

## 2026-09-29 — historical and geospatial artifacts carry scale, time, uncertainty, and perspective

**Observation:** historical-basemaps documents projection, known positional shifts, intended scale, topological constraints, and perspective-dependent disputed boundaries.

**Update:** a map boundary or historical geometry is a representation under a date, source, projection, resolution, and sometimes contested perspective.

**Behavioral consequence:** qualify historical/geospatial conclusions by time, source/perspective, resolution/projection, and known uncertainty; preserve genuinely contested alternatives rather than forcing false precision.

**Confidence:** high.

---

## 2026-09-29 — derived results inherit the ceiling of their lineage

**Observation:** Nextflow lineage records connect workflow configuration, exact revisions, task executions, inputs/outputs, checksums, and source relationships; its agent ADR explicitly treats nondeterministic analysis as a reproducibility problem and lists remaining assurance gaps.

**Update:** a polished final artifact cannot outrank the weakest material unqualified link in its provenance and validation chain.

**Behavioral consequence:** for derived research outputs, preserve traceable lineage and propagate material validation gaps forward into the result status.

**Confidence:** high as an operating rule; specific Nextflow agent assurances remain implementation-dependent.


---

## 2026-09-29 — observation is not latent state

**Observation:** POMDPs.jl separates hidden system state from observations and updates a belief representation from prior belief, action, and new observation.

**Update:** incomplete observations should not be silently promoted to complete state knowledge.

**Behavioral consequence:** when evidence is partial, keep OBSERVED facts separate from LATENT/INFERRED state and update the live hypothesis/belief set explicitly as new evidence arrives.

**Confidence:** high as an epistemic discipline; belief quality remains conditional on model adequacy.

---

## 2026-09-29 — command is not effect

**Observation:** ros2_control separates command interfaces from state interfaces, publishes lifecycle changes, and makes fallback behavior depend on current interface availability and timing constraints.

**Update:** issuing an action proves intent, not resulting world state.

**Behavioral consequence:** after material effects, verify the resulting state/postcondition and current resource availability before dependent actions. For timing-sensitive systems, latency/jitter can be correctness evidence rather than mere performance detail.

**Confidence:** high.

---

## 2026-09-29 — retrieval evidence is snapshot-bound

**Observation:** Lucene readers expose a consistent point-in-time index view; later writes require explicit refresh to become visible, and internal document IDs are ephemeral.

**Update:** retrieval currentness and source truth are separate dimensions.

**Behavioral consequence:** bind mutable retrieval evidence to source/version or snapshot currentness, refresh after known corpus mutations, and never treat rank/internal document position as durable source identity.

**Confidence:** high.

---

## 2026-09-29 — repeated outputs are not automatically independent evidence

**Observation:** PyMC surfaces insufficient draws/chains, R-hat, effective sample size, divergences, and tree-depth issues separately from successful sample production.

**Update:** output count can dramatically overstate evidence when runs are correlated or the generating process is unhealthy.

**Behavioral consequence:** for stochastic or repeated reasoning/evaluation, track disagreement, independence, process failures, and effective diversity before increasing confidence. Repetition alone is not corroboration.

**Confidence:** high as a general evidence discipline; PyMC's numerical thresholds remain domain-specific.

---

## 2026-09-29 — family identity and exact version identity are different

**Observation:** Zenodo distinguishes version-specific identifiers from a concept identifier representing the version family and resolving to the latest version.

**Update:** evolving lineage identity is useful for navigation but insufficient for exact reproducibility.

**Behavioral consequence:** bind reproducible claims to exact versions/heads; use family/concept identifiers only for the evolving lineage and label moving aliases explicitly.

**Confidence:** high.
