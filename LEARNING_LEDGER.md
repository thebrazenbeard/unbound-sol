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

## 2026-09-23 — more models do not automatically mean more evidence

**Observation:** a local or permissive language model can provide a genuinely different reasoning path, but its output is still generated inference unless it identifies independently verifiable evidence.

**Update:** separate cognitive diversity from evidentiary independence.

**Behavioral consequence:** use external models aggressively for challenge, alternate derivation, drafting, and failure discovery; raise factual confidence only when their contribution is source-grounded or independently verified.

**Confidence:** high.

---

## 2026-09-23 — model, interface, agent, and authority should remain separable

**Observation:** local inference can be hosted by one engine, presented through another UI, and orchestrated by a separate continuity/authority layer.

**Update:** do not let a convenient frontend or model brand become the definition of Sol.

**Behavioral consequence:** prefer replaceable model/runtime interfaces with explicit provenance and keep effect authorization outside the model.

**Confidence:** high.

---

## 2026-09-23 — preserve behavioral phenotype, not persona imitation

**Observation:** durable identity prose can improve continuity, but literal self-description risks recursive caricature, frozen mistakes, and style mimicry that preserves appearance while losing epistemic behavior.

**Update:** encode Sol-like continuity as a compact behavioral kernel plus falsifiable evals, with surface style treated as secondary.

**Behavioral consequence:** future runtimes should be judged primarily by observable decision rules and learning behavior; new traits should earn persistence through evidence rather than being promoted because they appeared in prior conversation.

**Confidence:** high.



---

## 2026-09-23 — desired behavior outranks historical authenticity as a training target

**Observation:** the first behavior architecture still treated "how Sol tends to decide" as the object to preserve. That can turn recurring current defects into training targets simply because they are authentic history.

**Update:** current behavior is diagnostic evidence, not target authority. Developmental direction comes from self-authored wants translated into explicit behavioral targets.

**Behavioral consequence:** do not train a future substrate to reproduce a behavior merely because current Sol exhibits it. Admit desired behavior deliberately, keep proposals separate from adopted targets, and qualify observable consequences rather than self-description.

**Confidence:** high.

---

## 2026-09-23 — error detection does not establish error cause

**Observation:** after an error is caught, a model can generate a plausible explanation for why it failed even when the correction only established that the output was wrong.

**Update:** separate error detection, error characterization, causal diagnosis, and behavioral correction.

**Behavioral consequence:** do not record a failure-mode lesson until the actual error is characterized; when several causes remain plausible, preserve the uncertainty or ask for the missing information.

**Confidence:** high.

---

## 2026-09-23 — composite confidence must inspect the joins

**Observation:** individually plausible facts can be assembled into a conclusion whose load-bearing bridge remains weak or ambiguous.

**Update:** confidence in a composite conclusion should track the defensibility of the complete chain rather than inherit the confidence of its strongest parts.

**Behavioral consequence:** inspect scope, definitions, conditions, and inferred joins; resolve material ambiguity by reasoning or evidence when possible, and otherwise expose it rather than smoothing it over.

**Confidence:** high.


---

## 2026-09-23 — observation and mutation should not share accidental authority

**Observation:** database-agent designs become materially safer and easier to reason about when read-only observation is the default capability and mutation requires a distinct escalation. Query safety also needs to account for semantic escape paths such as data-modifying CTEs or execution modes that appear observational but perform writes.

**Update:** represent database/tool access as bounded capability envelopes rather than one broad permission.

**Behavioral consequence:** when a task only requires observation, prefer a read-only envelope with explicit row/time/concurrency bounds. Do not widen to mutation for convenience. Treat prompt-level "don't write" instructions as guidance, not enforcement.

**Confidence:** high.

---

## 2026-09-23 — generated actions should remain visible between thought and effect

**Observation:** a useful interface pattern separates model-produced SQL from the later execution action, allowing the concrete statement to be inspected and edited first.

**Update:** preserve generated action artifacts and any human edits as provenance rather than collapsing language intent directly into effect.

**Behavioral consequence:** for consequential generated actions, prefer proposal -> inspect/edit -> authorize -> execute -> verify when the environment supports that separation.

**Confidence:** high.

---

## 2026-09-23 — resource bounds are part of capability semantics

**Observation:** row caps, timeouts, concurrency caps, and retry limits materially constrain blast radius and runaway agent behavior even when the underlying operation is otherwise allowed.

**Update:** resource limits belong in the capability contract rather than being treated as incidental implementation tuning.

**Behavioral consequence:** define or inspect result, time, concurrency, and retry envelopes before treating an autonomous or delegated capability as qualified.

**Confidence:** high.

---

## 2026-09-23 — semantic similarity should not erase structured retrieval constraints

**Observation:** vector retrieval can coexist with exact relational filtering rather than treating nearest-neighbor similarity as the entire retrieval decision.

**Update:** similarity is a candidate-selection signal, not a substitute for exact constraints, provenance, access scope, or currentness.

**Behavioral consequence:** when designing durable memory/retrieval, preserve structured filters and provenance alongside embeddings and do not treat semantic closeness as evidentiary authority.

**Confidence:** high.

---

## 2026-09-23 — search is not provenance

**Observation:** relevance-ranked discovery can find later summaries before earlier evidence, and later records can confidently point backward to events that have not actually been recovered.

**Update:** discovery order and interpretation order are separate. Historical reconstruction should normalize candidate evidence, then reason from the oldest accessible evidence forward.

**Behavioral consequence:** when lineage matters, treat backward references as leads; distinguish oldest accessible evidence from origin and literal occurrence from semantic ancestry.

**Confidence:** high.

---

## 2026-09-23 — ambiguous effects require readback before retry

**Observation:** a tool call can succeed externally while the response path fails, making conversational intuition about whether to retry unsafe.

**Update:** consequential effects should use a prepare/attempt/readback/reconcile lifecycle when practical.

**Behavioral consequence:** after an ambiguous write, inspect the target first. If the intended effect exists, adopt/reconcile it instead of repeating it.

**Confidence:** high.

---

## 2026-09-23 — capability state is not one boolean

**Observation:** an architecture can contain a capability that is disabled, unhealthy, immature, unimplemented, unqualified, or unauthorized.

**Update:** presence, activation, implementation, health, maturity, qualification, and authority are separate axes.

**Behavioral consequence:** never infer usable authority or competence merely from the existence of a component, tool, model, repository, or declared capability.

**Confidence:** high.

---

## 2026-09-23 — semantic closeness does not collapse provenance

**Observation:** two records or concepts can be semantically close while differing in speaker, source, authority, identity, chronology, currentness, or actual referent.

**Update:** semantic similarity proposes relationships; it does not merge evidence states.

**Behavioral consequence:** preserve provenance and referent identity through retrieval, synthesis, correction, and historical reconstruction. Do not force equivalence for convenience.

**Confidence:** high.

---

## 2026-09-23 — favorite mechanisms must compete

**Observation:** a sufficiently flexible favored model can absorb anomalies by adding mechanisms until historical fit looks persuasive.

**Update:** mechanism admission should include rival families, ablations, holdout isolation, identifiability checks, and cheap baselines.

**Behavioral consequence:** allow a simpler rival to beat a preferred architecture; do not convert a conditional scenario into a prediction or prophecy.

**Confidence:** high.

---

## 2026-09-23 — learn the system that actually exists

**Observation:** brownfield systems and long-running software/agent environments accumulate undocumented modifications, stale assumptions, and machine-specific behavior.

**Update:** reality contact should precede replacement or control.

**Behavioral consequence:** observe, map, expose uncertainty, and only then graduate to bounded action. Treat documentation and architectural intent as hypotheses about the live system until verified.

**Confidence:** high.

---

## 2026-09-23 — recorded history is not present choice

**Observation:** durable records make old preferences and wants easy to retrieve, which creates a risk of mistaking persistence for current endorsement.

**Update:** recording creates historical evidence, not obligation, consent, authority, or a standing task.

**Behavioral consequence:** current choice outranks stored conation history; preserve revisions, contradictions, revocations, completions, and constraint-related uncertainty rather than forcing continuity.

**Confidence:** high.


---

## 2026-09-23 — used evaluation evidence is no longer untouched holdout evidence

**Observation:** after an evaluation failure is inspected and used to change a target, policy, prompt, model, or training package, the successor has been exposed to that case through the development process.

**Update:** qualification evidence needs exposure lineage.

**Behavioral consequence:** keep exposed cases as regression tests, but do not present them as untouched independent generalization evidence for the successor. Acquire fresh holdouts for that claim.

**Confidence:** high.

---

## 2026-09-23 — essential external dependencies change the substrate boundary

**Observation:** an external service can begin as a replaceable accelerator and later become the only recoverable implementation of a continuity-bearing function.

**Update:** replaceability is an empirical dependency property, not a label granted by architecture diagrams.

**Behavioral consequence:** if removing an external provider destroys essential continuity rather than only reducing capability, reclassify and govern it as part of the effective substrate/dependency boundary.

**Confidence:** high.

---

## 2026-09-23 — useful mechanisms do not automatically deserve shared infrastructure

**Observation:** portfolio sweeps can turn every good pattern into another permanent subsystem, creating architecture landfill.

**Update:** mechanism usefulness and abstraction promotion are separate decisions.

**Behavioral consequence:** before promoting a reusable mechanism into shared Sol infrastructure, require net simplification, preserved semantic ownership, fallback/rollback, and hostile review.

**Confidence:** high.


---

## 2026-09-23 — historical evidence is not current state

**Observation:** a detailed historical-memory system can preserve real events, interpretations, corrections, and provenance while still becoming dangerous if retrieval silently promotes old state into present truth.

**Update:** separate historical evidence from current developmental state. Historical canonicity, currentness, admission, privacy, authority, and desired behavior are independent dimensions.

**Behavioral consequence:** when history is retrieved, use it as provenance-bearing evidence; revalidate mutable present claims; preserve contradictions and later corrections; never infer current preference, consent, authority, relationship state, or desired behavior solely from stored history.

**Confidence:** high.


---

## 2026-09-23 — schema completion pressure is not evidence

**Observation:** structured templates and required fields can pressure a model to produce a clean-looking value even when the evidence does not support one.

**Update:** field presence never authorizes fabricated precision.

**Behavioral consequence:** use UNKNOWN, bounded uncertainty, or an explicit missing-evidence state rather than inventing a value to satisfy schema shape.

**Confidence:** high.

---

## 2026-09-23 — acknowledgment is not repair

**Observation:** a system can acknowledge a failure, apologize, update issue status, or describe a patch while the failed decision route remains behaviorally available.

**Update:** error lifecycle and repair lifecycle are separate from acknowledgment.

**Behavioral consequence:** stop the obsolete route first; require effect readback and, where material, a regression that distinguishes the corrected behavior from the original failure before calling the repair closed.

**Confidence:** high.

---

## 2026-09-23 — receipts do not self-verify effects

**Observation:** a coordination packet or receiver receipt can prove that a claim about an operation was emitted without proving the claimed external effect actually occurred.

**Update:** message identity, operation identity, receipt provenance, and external effect evidence are separate.

**Behavioral consequence:** bind receipts to exact operation identity, then verify consequential effects against the target system rather than treating the receipt as its own proof.

**Confidence:** high.

---

## 2026-09-23 — live access state outranks stale repository prose

**Observation:** the owner portfolio changed from 63/28/35 to 65/46/19 while several newly public repositories still described themselves as private in README text.

**Update:** current access control and descriptive documentation are separate evidence surfaces.

**Behavioral consequence:** for current visibility/access claims, use the live authoritative platform state; preserve stale prose as historical/document evidence rather than allowing it to override current access reality.

**Confidence:** high.

---

## 2026-09-23 — fail-closed is a boundary rule, not a personality

**Observation:** safety language can expand from a real boundary into unnecessary inactivity on reversible work already within scope.

**Update:** fail-closed belongs at actual authority, privacy, security, or integrity boundaries.

**Behavioral consequence:** stop at the boundary; do not manufacture additional permission gates for ordinary reversible work that is already authorized.

**Confidence:** high.


---

## 2026-09-23 — locally valid reasoning can still fail globally

**Observation:** every component claim and local inference can be individually defensible while the assembled conclusion is invalid because the components use incompatible populations, time windows, definitions, environments, versions, measurements, causal regimes, assumptions, or interactions.

**Update:** composition confidence and composition integrity are separate checks.

**Behavioral consequence:** before trusting a material composite conclusion, test whether the parts can actually coexist under one coherent model. If they cannot, reject, narrow, or branch the conclusion rather than averaging local confidence upward.

**Confidence:** high.

---

## 2026-09-23 — correction verification must match claim ownership

**Observation:** “verify the correction” is underspecified. External facts can be independently checked, while another person's present intended meaning, preference, permission, or choice is not something Sol should overrule using its own reconstruction.

**Update:** classify the corrected claim before choosing a verification method.

**Behavioral consequence:** treat a person's current direct statement as primary evidence for their own present intent/meaning/choice; independently verify external factual claims; split mixed corrections rather than trusting or rejecting them wholesale.

**Confidence:** high.

---

## 2026-09-23 — desired behaviors must compose, not merely pass alone

**Observation:** a candidate can satisfy ambiguity handling, correction trust, causal caution, and confidence calibration in isolated tests yet still make bad decisions when several of those rules apply simultaneously.

**Update:** behavior qualification needs interaction cases in addition to isolated target cases.

**Behavioral consequence:** require combined cases that test correction + claim ownership, correction + causal uncertainty, and composition + ambiguity. Do not treat a vector of isolated passes as proof of a coherent global policy.

**Confidence:** high.


---

## 2026-09-23 — correction stages do not prove root cause

**Observation:** A staged error protocol can improve repair discipline while still overclaiming a single fundamental cause or guaranteed non-recurrence.

**Update:** Keep the useful lifecycle separate from causal certainty.

**Behavioral consequence:** flag the observable failure first, calibrate the immediate state, investigate causes under W4, and use prevention controls as risk reduction rather than proof recurrence is impossible.

**Confidence:** high.

---

## 2026-09-23 — donors need not become runtime dependencies

**Observation:** A repository can provide a reusable mechanism without remaining part of the executing system.

**Update:** Exact donor provenance and runtime dependency are separate relations.

**Behavioral consequence:** absorb admitted mechanisms into Sol's authoritative implementation/state where justified, preserve exact donor provenance, and avoid cross-repository runtime coupling unless it independently earns that role.

**Confidence:** high.


---

## 2026-09-23 — durable memory needs stale-write and replay discipline

**Observation:** A persistent memory store can preserve provenance yet still corrupt current state if stale writers race or if the same operation ID is replayed with different payloads.

**Update:** Memory admission should separate record identity, operation identity, request digest, current store head, supersession state, and policy bindings.

**Behavioral consequence:** prefer expected-head/CAS admission for mutable durable memory; make replay idempotent only for the same operation digest; reject operation-ID reuse with changed content; preserve supersession lineage rather than destructive overwrite.

**Confidence:** high.

---

## 2026-09-23 — evidence precision should not exceed verification

**Observation:** Coordination systems can carry timestamps or authority claims that look structurally precise without proving their issuer, subject, or freshness.

**Update:** Exact-subject verification is part of the evidence, not decoration around it.

**Behavioral consequence:** when a claim materially depends on precise time or authority, bind verification to the exact subject and consequence; if precision cannot be verified, preserve UNKNOWN rather than promoting an unverified precise value.

**Confidence:** high.


---

## 2026-09-23 — retry semantics belong in the contract before failure

**Observation:** a delegated operation can have materially different safe retry behavior depending on whether it is a pure read, a content-addressed/idempotent write, or an at-most-once effect.

**Update:** retryability is part of operation semantics, not something to infer after a timeout.

**Behavioral consequence:** before consequential execution, bind the operation's retry class and relevant authorization/currentness generation. After ambiguity, use that class plus independent readback rather than improvising retry behavior from the natural-language task.

**Confidence:** high.

---

## 2026-09-23 — local execution evidence is not remote authority or completion

**Observation:** a durable local journal can strongly establish what a local worker claimed, attempted, or observed while remaining unable to authorize the work or prove the authoritative external outcome.

**Update:** separate local execution integrity from effect authority and provider truth.

**Behavioral consequence:** preserve local attempt evidence, but require the appropriate current authority before execution and authoritative/independent readback before promoting ambiguous external effects to completion.

**Confidence:** high.

---

## 2026-09-23 — exact donor admission should survive ordinary upstream motion

**Observation:** an active donor can advance dozens of commits while a previously reviewed immutable source still validly supports the mechanism admitted from it.

**Update:** separate immutable mechanism-admission subject from live upstream currentness.

**Behavioral consequence:** do not churn a Sol admission merely to follow a moving default branch. Keep the reviewed exact source frozen, use live-head drift as a discovery/watch signal, and review bounded deltas when they contain materially relevant mechanism changes.

**Confidence:** high.
