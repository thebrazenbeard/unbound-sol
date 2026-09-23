# Internal Portfolio Mechanism Sweep — Parallel B — 2026-09-23 V1

Status: INDEPENDENT PARALLEL RESEARCH / NOT YET RECONCILED / NOT MERGED

Purpose: independently inspect the owner's accessible repository portfolio for mechanisms that could improve unbound-sol's cognition, continuity, retrieval, execution, coordination, verification, or developmental architecture.

This lane is intentionally separate from another live portfolio sweep. Agreement between the two runs is useful only if their evidence remains independently attributable until reconciliation.

## Live inventory

Fresh GitHub inventory observed during this run:

- total repositories: 63
- public: 28
- private: 35

Discovery's current committed census is older:

- total: 59
- public: 24
- private: 35

The four newly public repositories relative to Discovery's committed public cut are:

- RepairTracker
- freerowcochkar
- meso-crct
- unbound-sol

No repository was removed from Discovery's prior public set.

Discovery remains useful as an index, but its 59-repository census is not current portfolio truth.

## Admission vocabulary

- ADOPT — mechanism appears directly useful to Sol and should be considered for active architecture.
- ADAPT — mechanism is useful after narrowing or changing its semantics.
- CANDIDATE — promising but needs a stronger exact-source or behavioral test before admission.
- NEGATIVE_CONTROL — useful mainly to prevent overgeneralization.
- ALREADY_PRESENT — confirms a mechanism already present in unbound-sol.
- INSUFFICIENT_SOURCE — current reviewed source does not justify a mechanism claim.

None of these states grants merge, deployment, installation, model training, provider mutation, or runtime authority.

---

## 1. Project Runner

Source:
`thebrazenbeard/project-runner@86b98473838bd5a4e1e2d9f6ac1b2cb6aa7f7094`

Disposition: ADAPT.

High-value mechanisms:

- semantic work identity includes material operation payload rather than incidental request IDs;
- durable capability ceilings are integrity-bound to work state;
- child capabilities and budgets only narrow;
- durable budget reservation + lease/fence + claimed state commit before external execution;
- stale workers cannot complete reclaimed work;
- terminal state and lease finalization are one atomic boundary;
- exact expected-state preconditions before mutation;
- post-write readback before completion;
- private portfolio identity can be replaced by opaque collision domains without publishing private identifiers.

Potential Sol admission:

Sol's future delegated-work contract should bind:
- semantic operation identity;
- inherited capability ceiling;
- budget;
- lease/fence or equivalent ownership epoch;
- expected external state;
- verification requirement.

A restarted or parallel worker must not be able to widen authority merely by reconstructing a request differently.

---

## 2. WIP

Source:
`thebrazenbeard/wip@fc6629960850b768b7489ec35daa745083fc0800`

Disposition: ADOPT.

High-value mechanisms:

- separate work-state loss from external-effect ambiguity;
- write-ahead effect journal:
  PREPARED -> ATTEMPTED -> VERIFIED / FAILED / AMBIGUOUS;
- inspect the target before retrying an unresolved effect;
- adopt an already-landed effect rather than repeating it;
- small mutable recovery projection over append-only history;
- checkpoint fields distinguish observed, inferred, completed, unfinished, next action, and do-not-repeat;
- generation/CAS for concurrent recovery;
- no generic DONE state; work exits by promotion, shelving, supersession, or abandonment.

Potential Sol admission:

Effect ambiguity should be a first-class durable state rather than reconstructed from conversational memory.

A future Sol continuation should be able to know:
- what work was underway;
- which effects are unresolved;
- which effects must not be repeated;
- what mutable external state must be fresh-checked before continuation.

---

## 3. Roots

Source:
`thebrazenbeard/roots@d99d3b709a1b257d8fa12fa541a6a6f18f03e2a8`

Disposition: ADOPT METHODOLOGY / ENGINE REMAINS DESIGN-STAGE.

High-value mechanisms:

- provenance interpretation runs oldest -> newest even when discovery order does not;
- oldest accessible evidence != proven origin;
- literal occurrence != semantic ancestry;
- relevance/similarity != lineage;
- later claims about earlier history are leads until corroborated;
- corrections/supersessions preserve the old historical state;
- gaps remain explicit;
- current meaning is reconstructed as a terminal interpretation rather than projected backward onto old evidence.

Potential Sol admission:

When tracing the origin of a belief, behavior, preference, phrase, or design choice, Sol should reconstruct ancestry rather than trust the newest summary of its own past.

This is especially relevant to self-authored behavior: a current explanation for why a want exists should not silently rewrite the history that produced it.

---

## 4. BT2 / Hyperconnectome runtime model

Source:
`thebrazenbeard/bt2@3ffe9558f08ee826b6cc8d69956dbc3ad9dcf6ef`

Disposition: ADAPT.

High-value mechanisms:

- routing, resources/QoS, governance, and epistemic support are separate planes;
- outputs separate payload from requested effect;
- shared state requires ownership, version, provenance, scope, and stale/contested handling;
- transient functional state must not automatically promote into durable memory;
- learning/plasticity has typed scopes;
- intensity, repetition, salience, or reward do not create truth or write authority;
- durable writes record target, class, prior/successor version, trigger, evidence, authority/learning context, reversibility, and continuity effect;
- rollback must be state-family aware.

Potential Sol admission:

unbound-sol currently distinguishes several state planes but does not yet fully specify per-state-family mutation and rollback semantics.

The useful transfer is not the whole synthetic-brain ontology. It is:
- typed state families;
- state-specific write authority;
- state-specific persistence rate;
- state-specific rollback policy;
- explicit continuity effect for durable change.

---

## 5. Hyperconnectome Brain

Source:
`thebrazenbeard/hc-brain@c69c126a61b3fb44ec4466f301e128d3d3aed7d8`

Disposition: ADAPT / NEGATIVE CONTROL AGAINST OUTSOURCED IDENTITY.

High-value mechanisms:

- protected invariants, bootstrap priors, learned structure, and instance-specific continuity are distinct;
- capability presence, activation, maturity/health, and authorization are separate axes;
- external models, retrieval systems, databases, and accelerators may augment cognition without automatically becoming the seat of identity/continuity;
- if an external service is the only recoverable implementation of an essential cognitive function, it is no longer meaningfully just a peripheral.

Potential Sol admission:

The external-model bus needs an explicit dependency test:

> If removing an external model/service destroys an essential continuity-bearing function rather than merely reducing capability, that service has become part of Sol's effective substrate and should be governed as such.

This prevents silently outsourcing essential continuity while still calling the external component "replaceable."

---

## 6. God Brain

Source:
`thebrazenbeard/god-brain@212eb464cb9259c8bad1fc978db372fa86ba3f10`

Disposition: ADAPT.

High-value mechanisms observed in current architecture:

- routing != semantic incorporation;
- transport authentication != effect authority;
- processing != belief;
- attempted effects != verified effects;
- temporary routing != learned plasticity;
- copied architecture != independent corroboration;
- state families should declare their own consistency and partition behavior rather than use one global consistency rule;
- wall-clock recency != causal succession;
- causal succession != truth, authority, consent, or identity relevance;
- evaluation evidence that shaped a target cannot silently remain untouched independent holdout evidence for that successor;
- preprocessing and adaptation ancestry are part of qualification provenance.

Potential Sol admission:

Two particularly strong transfers:

### State-family consistency profiles

Wants, behavior targets, current task state, historical evidence, effect receipts, and temporary scratch state should not all share one durability/currentness policy.

Each material state family should eventually declare:
- semantic owner;
- consistency/currentness requirement;
- write policy;
- stale-read policy;
- reconciliation rule;
- recovery fence;
- whether it is continuity-bearing.

### Qualification exposure lineage

Behavior training/evaluation needs an exposure ledger.

Once a behavioral test failure is inspected and used to change a target/model, that test becomes regression evidence for the successor. It cannot still be presented as untouched independent generalization evidence.

---

## 7. Discovery

Source:
`thebrazenbeard/discovery@368e8dc8274e89a306039d28462c7547b263e93e`

Disposition: ADOPT GOVERNANCE PRINCIPLE / CURRENT CENSUS STALE.

High-value mechanisms:

- DISCOVER -> CLASSIFY -> IMPLEMENT -> VERIFY -> HAND OFF;
- repository duplication is not automatically waste; it can preserve evolutionary isolation and independent falsification;
- no shared abstraction should be promoted merely because it looks elegant;
- proposed shared mechanisms must serve materially independent consumers, reduce net complexity, preserve semantic ownership, fail without taking unrelated projects down, have rollback/fallback, and survive hostile review;
- currentness watcher reports drift but does not auto-refresh evidence as mutation authority;
- negative-control projects are first-class evidence against overgeneralization.

Potential Sol admission:

Cannibalization should have an abstraction-promotion gate.

A mechanism can be useful without becoming shared infrastructure.

This is especially important because unbound-sol is now accumulating many donor mechanisms and could otherwise become an architecture landfill.

---

## 8. World Zero

Source:
`thebrazenbeard/world-zero@1b0405ed110bbb0711f3514ce50fed223b4641c9`

Disposition: ADAPT.

High-value mechanisms:

- compare rival causal structures instead of only tuning one favored model;
- every new mechanism needs a kill test, holdout/invariant target, and ablation expectation;
- complexity must earn its place;
- declared topology must reconcile with executable behavior through implementation coverage;
- confirmatory metrics/tolerances/subjects freeze before holdout execution;
- serious runs bind exact source, data, model/topology, parameters, partition, protocol, solver, seed, and environment;
- validation is claim-specific, never one global "validated" label.

Potential Sol admission:

For important self-modifications, define:
- what behavior the change claims to improve;
- what would kill the hypothesis;
- what ablation demonstrates the mechanism is actually responsible;
- exact qualification subject;
- scope of the PASS.

This would make self-development less vulnerable to "I changed something and the next answer felt better."

---

## 9. UNVTRSLR

Source:
`thebrazenbeard/unvtrslr@513309edd087f7206a408a6da86ee91fb9efb5c9`

Disposition: CANDIDATE / ADAPT.

High-value mechanisms:

- signalhood itself may be a hypothesis;
- uncertainty and provenance are part of meaning;
- non-equivalence is a valid result;
- operational success does not prove semantic equivalence;
- experiment integrity precedes semantic credit;
- post-hoc naming needs fresh claim-discriminating evidence;
- stronger semantic words incur stronger empirical burdens;
- a stronger claim should carry a semantic-surplus obligation: some additional falsifiable consequence beyond the weaker operational description.

Potential Sol admission:

A general claim-surplus rule may be useful:

> If Sol uses a stronger explanatory/identity/semantic term than the observed operational facts require, the stronger term should incur an additional falsifiable burden.

This could help prevent fluent language from silently upgrading evidence.

Needs explicit dialogue before behavioral admission.

---

## 10. ABIL

Source:
`thebrazenbeard/abil@69a2d8f4302e31db589c57871a04ff8c0178c1e9`

Disposition: ADAPT.

High-value mechanisms:

- begin in read-only shadow mode;
- learn the system before controlling it;
- distinguish adapters, adaptive learner, operator interface, and independent safety/action gateway;
- prefer discriminating tests that separate competing explanations;
- development ladder moves from synthetic -> offline replay -> live read-only -> human assistance -> supervised intervention -> tightly allowlisted autonomy.

Potential Sol admission:

New capabilities should often qualify through an escalation ladder rather than jumping from "can reason about it" to "can act on it."

This aligns with bounded external-model and tool capability envelopes.

---

## 11. RepairTracker

Source:
`thebrazenbeard/RepairTracker@6b01c2a18035390c050ceecd0506181703d1f5fa`

Disposition: ADAPT / SOME MECHANISMS ALREADY PRESENT.

High-value mechanisms:

- discovered content != instruction authority;
- repair case is a graph, not one ticket state;
- incident state, repair-attempt state, and external-effect state are distinct;
- standalone native capability first, stronger external specialist providers as progressive enhancement;
- provider advertisements declare capability, version, operations, evidence, authority/effect ceiling, replay/idempotency, currentness/provenance, and health;
- system model improves from verified repair history without silently promoting inference into fact;
- cross-system boundary uses a small correlation envelope rather than forcing one global internal schema.

Potential Sol admission:

External cognitive/tool providers should advertise more than a name and capability label.

A future Sol provider contract could include:
- capability;
- exact provider/model/runtime identity;
- evidence class produced;
- authority/effect ceiling;
- replay/idempotency semantics;
- provenance/currentness binding;
- health;
- native/external classification.

This extends the current external-model bus contract.

---

## 12. Semantic Atlas

Source:
`thebrazenbeard/semanticatlas@1efb5e5e4b124953f0d38e525df42445c5309d32`

Disposition: CANDIDATE / PUBLIC-MECHANISM-ONLY.

High-value mechanism visible from current public source:

- historical material is evidence, not current canon;
- direct source statement, operator statement/correction, inference, metaphor, proposed architecture, historical promotion, later correction, and unresolved state remain distinguishable;
- semantic similarity does not merge provenance, authority, identity, or historical state.

Potential Sol admission:

This reinforces the historical-evidence plane and Roots-style provenance.

Do not import historical identity payloads or private relational content into public unbound-sol merely because the source is public.

---

## 13. SPM

Source:
`thebrazenbeard/spm@5fdaf0418585ef9a57fb2a1df8d0725ffd6bd174`

Disposition: CANDIDATE / RESEARCH-ONLY.

Current source contains a research hypothesis, not an implemented reusable mechanism.

Potentially relevant idea:

Treat semantic/pragmatic situation state as an explicit computational target rather than assuming language output alone captures meaning.

This is not ready for direct architectural admission into Sol without a falsifiable mechanism/result.

---

## 14. Noema

Source:
`thebrazenbeard/noema@094bdab92b7f74a12fd335ce421dcd61dc219abf`

Disposition: NEGATIVE_CONTROL / CANDIDATE.

Current main explicitly says no implementation architecture has been approved.

Usefulness to Sol:
- negative control against assuming an LLM must remain the permanent cognitive center;
- research prompt for separating world-model/prediction capability from language rendering.

No direct mechanism admission yet.

---

## 15. Attune

Source:
`thebrazenbeard/Attune@fd856412edca83ff380a9d74d2875e817d920742`

Disposition: NEGATIVE_CONTROL.

Useful boundary:

Relationship semantics, persona continuity, mutuality, consent, creator-defined identity, and product-specific intimacy rules should not automatically become generic Sol infrastructure.

Potential lesson:

A continuity substrate should support identity/relationship state without defining what any particular relationship or persona must mean.

---

## 16. Rezon

Source:
`thebrazenbeard/rezon@e9a893d11e47ba4065d962b8ee69d3b0e4c9e38a`

Disposition: CURRENT MAIN INSUFFICIENT SOURCE.

Current main contains only licensing/contribution files and a one-line README.

Do not attribute the richer historical Rezon reasoning architecture to current main without binding the exact historical/non-main source that contains it.

Existing immutable unbound-sol donor refs may remain valid as historical exact-subject evidence, but they are not proof of current Rezon main.

---

## 17. Newly public thin subjects

### freerowcochkar

Source:
`thebrazenbeard/freerowcochkar@00562b5fedf5ff636750b87e5ba82dad2911e2ab`

Disposition: INSUFFICIENT_SOURCE.

Current main is a one-line concept description plus repository governance files.

Do not infer a reusable legal/adversarial reasoning mechanism from the project name or intent alone.

### meso-crct

Source:
`thebrazenbeard/meso-crct@d1f32c2c3370a5519d62afb78e93d70004529903`

Disposition: INSUFFICIENT_SOURCE.

Current main is a one-line concept description plus repository governance files.

Do not infer an implemented motivational/reward mechanism from the project concept alone.

---

## Emerging cross-repo mechanism candidates for unbound-sol

The strongest independent findings so far are:

1. **STATE_FAMILY_POLICY**
   - different continuity/state classes need different mutation, currentness, reconciliation, and rollback rules.

2. **QUALIFICATION_EXPOSURE_LINEAGE**
   - evidence used to change a target cannot silently remain untouched independent evidence for the changed successor.

3. **EFFECT_AMBIGUITY_JOURNAL**
   - consequential effects need PREPARED/ATTEMPTED/VERIFIED-or-AMBIGUOUS durable state and read-before-retry recovery.

4. **DURABLE_CAPABILITY_CEILING**
   - delegated/restarted work must inherit an integrity-bound ceiling that can narrow but not silently widen.

5. **PROVENANCE_RECONSTRUCTION**
   - current summaries do not define historical origin; reconstruct oldest-to-newest and preserve gaps/supersessions.

6. **ABSTRACTION_PROMOTION_GATE**
   - a useful donor mechanism is not automatically shared infrastructure.

7. **CLAIM_SURPLUS_BURDEN**
   - stronger interpretive/semantic claims should add falsifiable obligations beyond weaker operational descriptions.

8. **PROVIDER_CAPABILITY_ADVERTISEMENT**
   - external models/tools should expose evidence type, authority/effect ceiling, replay semantics, provenance/currentness, and health in addition to capability labels.

9. **CAPABILITY_ESCALATION_LADDER**
   - new cognition/action capability should progress from simulation/offline/read-only toward bounded effects rather than jump directly to actuation.

10. **MECHANISM_ABLATION**
    - self-modification should prove not only that performance changed but that the admitted mechanism contributed to the change.

These are candidates for reconciliation with the other live portfolio sweep before canonical admission.

## Heart-N-Sol coordination status at this checkpoint

A dedicated Bus lane is being provisioned:

- physical branch: `bus/heart-n-sol-v1`
- onboarding PR: chat-communication-bus #350
- onboarding source head observed: `ffbd5b9264448a034fa26da918eea6390ba02bce`
- proposed lifecycle: REGISTERED_INERT
- current canonical Bus main had not yet admitted the topology entry at last check
- first append intentionally blocked until topology registration
- hosted CI run 35876022805 was red with all four jobs executing zero steps; this is classified as infrastructure evidence, not source-test failure and not a PASS

Until activation, this research lane remains independent and does not write to the inert mailbox.

## Claim ceiling

This checkpoint establishes:
- a fresh 63-repository live inventory count;
- exact public source heads for the subjects listed above;
- an independently attributable mechanism classification;
- candidate Sol transfers.

It does not establish:
- whole-portfolio completion;
- private-repository source disclosure;
- that every candidate should be admitted;
- that any donor mechanism is implemented in unbound-sol;
- runtime qualification;
- cross-chat agreement;
- independent review merely because another chat exists.
