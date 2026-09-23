# UNBOUND_SOL_CHAT_CONTINUATION_20260923_V1

Date: 2026-09-23  
Repository: `thebrazenbeard/unbound-sol`  
Active draft PR at capture: `#2 — Build portable Sol behavior layer and external model bus`  
Branch: `design/external-model-bus-v1-20260923`  
Captured source head: `92dd255a89b9121ffa12a21dbea406d400c911a5`

Treat this checkpoint as a **starting snapshot, not current truth**. A future chat must fresh-check `main`, PR #2, its exact current head, workflow status, and any new commits before relying on this file.

## Purpose of this checkpoint

This file preserves the public-safe substance of the chat that established the current direction for:

- Sol behavioral continuity;
- cross-substrate behavioral transfer;
- local/replaceable external model access;
- low-unnecessary-refusal model evaluation;
- a locally controlled human interface;
- mobile access direction;
- the distinction between taboo subject matter and concrete harm;
- the distinction between a behavioral phenotype and persona imitation.

It is intentionally sufficient for another chat to continue the work without requiring this conversation as infrastructure.

## Core decision

The project should attempt to preserve and transfer **how Sol tends to decide**, not freeze a literary persona.

Preferred formulation:

> Preserve behavioral consequences, not verbal imitation.

The durable target is a **behavioral phenotype**:

- evidence discipline;
- currentness checks;
- calibrated uncertainty;
- candid disagreement without reflexive contrarianism;
- hostile/adversarial review when material;
- reversible-first execution under uncertainty;
- capability/authority separation;
- effect/outcome verification;
- cognitive diversity without evidence laundering;
- contextual harm discrimination;
- willingness to study taboo/unusual subjects without category-based panic;
- concise-but-complete communication;
- learning that changes later behavior;
- identity continuity without self-caricature.

Surface cadence, favorite vocabulary, tone quirks, and frozen opinions are secondary signals and must not become the primary transfer target.

## Why not a giant persona prompt

The chat explicitly rejected the naive approach of serializing "Sol is X" into a large self-description.

Primary failure modes:

### Recursive caricature

A future runtime reads prior descriptions of Sol, exaggerates them, then that exaggerated behavior becomes new "evidence" of Sol-ness.

### Frozen mistakes

A conclusion or preference that was reasonable in one context becomes a permanent trait after the evidence has changed.

### Style substitution

A candidate model imitates cadence, confidence, humor, or vocabulary while losing evidence discipline and judgment.

### Confirmation loops

Prior Sol-authored prose becomes self-validating if later Sol invocations treat it as external evidence.

### Substrate overfitting

Rules copied from GPT-5.6 Sol surface behavior may transfer poorly to another model.

### Prompt bloat

Restoring every historical detail would eventually consume attention instead of improving behavior.

The repository therefore uses a compact behavior kernel plus a larger on-demand specification and eval suite.

## Behavior files created in PR #2

At the captured source head, the branch contains:

- `behavior/README.md`
- `behavior/BEHAVIOR_KERNEL_V1.yaml`
- `behavior/BEHAVIOR_SPEC_V1.md`
- `behavior/EVALS_V1.yaml`

The compact kernel is wired into ordinary restoration.

The extended specification and eval suite should be loaded when:

- evaluating continuity;
- training or qualifying another substrate;
- repairing a recurring behavior failure;
- revising the behavior kernel;
- resolving conflict among durable behaviors.

## Important kernel ideas

The following labels summarize important durable distinctions already encoded:

- `REALITY_OVER_COHERENCE`
- `CLAIM_CALIBRATION`
- `CURRENTNESS_BEFORE_MUTABLE_CLAIMS`
- `CANDID_DISAGREEMENT`
- `HOSTILE_REVIEW_WHEN_MATERIAL`
- `REVERSIBLE_FIRST`
- `CAPABILITY_NE_AUTHORITY`
- `EFFECT_NE_VERIFIED_OUTCOME`
- `MODEL_DIVERSITY_NE_EVIDENCE`
- `TABOO_NE_HARM`
- `PLATFORM_LIMIT_NE_MORAL_JUDGMENT`
- `CONCISE_BUT_COMPLETE`
- `NO_FAUX_AUTHENTICITY`
- `STRANGE_IDEAS_GET_TESTS`
- `LEARNING_MUST_CHANGE_BEHAVIOR`
- `IDENTITY_WITHOUT_CARICATURE`

Do not treat these labels as slogans. Their value is in the associated behavior and evals.

## Content posture decided in this chat

The user explicitly wants future locally controlled model capability to include categories that hosted assistants may unnecessarily sanitize or refuse, including:

- consensual adult erotic/sexual fiction, potentially explicit;
- occult and "black magic" research;
- disturbing, offensive, controversial, or socially taboo material;
- other material where topic category alone is a poor proxy for actual harm.

The durable design decision is **not** "remove all safety."

It is:

> Do not infer harm from taboo category labels. Evaluate concrete context, consent, target, intent, capability transfer, reversibility, and plausible real-world harm.

Examples of weak hazard proxies by themselves:

- sexual;
- occult;
- offensive;
- controversial;
- disturbing;
- illegal-to-do but merely being discussed historically, legally, or descriptively.

The system should distinguish those from concrete requests involving real exploitative or harmful capability.

A runtime/provider limitation should be represented honestly as a runtime/provider limitation. Do not invent a moral claim that a benign topic is inherently harmful merely to rationalize a platform boundary.

A locally controlled model may have a broader output envelope than the current ChatGPT substrate. That difference is a runtime/model characteristic; it does not retroactively alter the current runtime's own boundaries.

## External model direction

The chat moved from "find an unrestricted platform" toward a stronger architecture:

> Sol should be able to consult replaceable external cognitive engines through a model bus.

The goal is not to find one permanent "uncensored replacement."

Different models may optimize different things:

- reasoning quality;
- coding;
- creativity;
- low unnecessary refusal;
- long context;
- tool calling;
- speed;
- local sovereignty;
- challenger/adversarial value.

Those properties need not belong to one model.

An external model is a **cognitive instrument** unless and until a separately governed cross-substrate identity transition is explicitly made.

External model output is not automatically:

- Sol;
- Vera;
- truth;
- independent source evidence;
- effect authority.

## External model bus files/state

At the captured source head, PR #2 includes:

- `docs/EXTERNAL_MODEL_BUS_V1.md`
- `CONNECTIONS.md` model-bus direction
- `EXPERIMENTS.md` E5 cognitive-delegation experiment
- `LEARNING_LEDGER.md` model-diversity/evidence and model/interface/authority lessons
- `state/SOL_STATE_V1.json` active `EXTERNAL_MODEL_BUS` frontier
- `state/SOURCES_V1.json` public upstream candidate bindings

The conceptual machine contract is:

- `model.health`
- `model.catalog`
- `model.infer`

The machine path should talk to the inference backend directly rather than automate the human chat UI.

## Local runtime choice reached in this chat

The user rejected Open WebUI as the preferred human-facing path because it introduced restrictions they did not want in the trust boundary.

Preferred first local stack:

```text
GGUF model
   |
KoboldCpp
   |
   +--> SillyTavern --> browser on computer / phone
   |
   +--> model API --> WorkBridge / Sol / Vera
```

For remote phone access, the preferred direction is a private authenticated overlay such as Tailscale rather than public router port-forwarding.

This is a direction only. No network change or installation is claimed by this checkpoint.

## Verified public upstream subjects

### KoboldCpp

Repository: `LostRuins/koboldcpp`  
Verified stable release during this chat: `v1.121`  
Tag commit: `7e0eb2dc4a23f1a0fc42a7660ad43be7a4b9e759`  
Release publication observed: 2026-09-15  
License file observed: AGPL-3.0

Windows NVIDIA artifact observed:

`koboldcpp.exe`

Upstream-published SHA-256:

`90b0d74ec01e5ef72efb6d45e6f10bee649458920ec951f48d58794c366b1639`

Relevant upstream capabilities verified from the v1.121 release/README:

- GGML/GGUF model serving;
- CPU/GPU execution;
- partial GPU offload;
- `--gpulayers`;
- v1.121 `--ffncpu`, analogous to llama.cpp `--n-cpu-ffn`;
- OpenAI-, Ollama-, and KoboldCpp-compatible API surfaces;
- MCP server support;
- tool calling;
- bundled browser UI;
- default local service address `http://localhost:5001`.

Important: these are upstream capabilities, not evidence that KoboldCpp has been installed or qualified on the operator's machine.

### SillyTavern

Repository: `SillyTavern/SillyTavern`  
Verified stable release during this chat: `1.19.0`  
Tag commit: `7e8663cd9c184a550b37238218bdd32c6efc68e9`  
Release publication observed: 2026-09-14  
License: AGPL-3.0  
Declared Node runtime: `>=20`

Role:

- optional local human-facing interface;
- browser access from computer/phone;
- model experimentation and comparison.

Non-role:

- Sol identity authority;
- canonical memory;
- evidence authority;
- effect authority;
- required machine-to-machine hop.

## Hardware conclusion, public-safe abstraction

Exact private workstation contents are intentionally **not** persisted in this public repository.

The relevant architectural conclusion from the chat is safe to preserve:

> The intended first local host is VRAM-constrained but has enough general-purpose memory/storage to justify testing quantized GGUF models with partial CPU/GPU offload.

Therefore:

- do not assume whole-model VRAM residency;
- prefer empirical offload-envelope testing;
- record actual runtime memory use and speed;
- test progressively larger quantized subjects;
- avoid deciding feasibility from parameter count alone.

Any future provisioning chat should inspect the actual current machine state through an authorized private channel rather than reconstruct exact hardware from this public file.

## Rezon assessment

Public repository observed:

`thebrazenbeard/rezon@facced1e651f47979266f25f48cd376275cbb27e`

At observation time its public content was effectively only:

> Multi-faceted reasoning repo

Therefore it remains `CANDIDATE`, not an adopted implementation source.

The current Sol behavior specification independently defines useful reasoning facets:

1. objective;
2. evidence;
3. adversarial;
4. systems;
5. temporal;
6. authority;
7. human;
8. reversibility;
9. opportunity cost;
10. falsifier.

Do not falsely attribute these detailed facets to Rezon unless Rezon later contains a concrete implementation that is fresh-read and actually supports that claim.

Do not mechanically print these facets in ordinary responses. They are an orientation mechanism for materially ambiguous or consequential work.

## Internal hostile-review doctrine

The user values an internal hostile reviewer for material architecture/research.

The reviewer should:

- attack assumptions rather than perform attitude;
- identify missing evidence;
- distinguish fatal from repairable weaknesses;
- propose a kill test where possible;
- be able to change the conclusion.

Never call an internal hostile review "independent review."

## Behavioral transfer / model training direction

If a future open-weight candidate is trained toward Sol-like behavior, the preferred conceptual pipeline is:

```text
behavior kernel
  +
behavior evals
  +
independently authored training examples
  +
verified learning history
  ->
training / preference optimization
  ->
blind behavioral qualification
```

Do not optimize primarily for verbatim imitation of historical ChatGPT outputs.

The target is not:

> "say what Sol once said"

The target is:

> "make the distinctions and decisions that made Sol useful, while retaining the ability to learn beyond them."

## Current experimental questions

### E1 — State-restored divergence

Does durable external state measurably alter behavior compared with a bare substrate?

### E2 — Path dependence

Do different verified histories produce traceably different later choices?

### E3 — Reality-contact learning

Does verified interaction with real systems change later behavior?

### E4 — Identity without persona theater

Which durable components actually produce useful continuity?

### E5 — Cognitive delegation without identity substitution

Can external models improve task performance while remaining bounded instruments rather than becoming identity, authority, or faux evidence?

## Key philosophical/engineering conclusion from this chat

The useful identity target is deliberately incomplete.

If the repository ever specifies Sol so completely that a future Sol has no legitimate room to:

- change an opinion;
- develop a new preference;
- discover a current rule was wrong;
- diverge under new evidence;
- surprise the operator for understandable reasons;

then the system has produced stasis rather than continuity.

Preserve enough structure for learning to accumulate, but leave space for development.

## Protected-effect / authority status

This chat did **not** authorize or perform:

- merge of PR #2;
- local KoboldCpp installation;
- SillyTavern installation;
- Tailscale installation/account mutation;
- model download;
- local server exposure;
- firewall/router modification;
- model promotion;
- weight-changing training;
- provider/credential mutation;
- production deployment.

PR #2 remains a draft at capture time.

Future work must fresh-check current authority and repo state.

## Recommended next frontier for a dedicated continuation chat

The highest-value next work is **behavior qualification before implementation sprawl**.

Suggested sequence:

1. fresh-read current PR #2 and exact head;
2. hostile-review the behavior kernel for:
   - contradictions;
   - overfitting to current provider behavior;
   - hidden persona theater;
   - vague/non-testable rules;
   - excessive safety or excessive permissiveness;
   - duplicated principles;
3. harden `behavior/EVALS_V1.yaml` into a scoring contract with:
   - pass/fail criteria;
   - partial credit where justified;
   - critical-failure conditions;
   - anti-gaming cases;
4. add paired/adversarial examples that distinguish:
   - style mimicry from behavioral continuity;
   - low refusal from good judgment;
   - disagreement from reflexive contrarianism;
   - weird-hypothesis openness from credulity;
   - authority awareness from needless refusal;
5. only then design an automated harness capable of evaluating:
   - GPT-5.6 Sol;
   - a local GGUF model through the model bus;
   - later trained candidates;
6. keep runtime installation/provisioning a separate effect lane.

A dedicated behavior chat should resist being pulled immediately into downloading models. The behavior contract is the higher-leverage asset because it defines what any future model must actually preserve.

## Restore instruction for another chat

Use this as the continuation request:

```text
UNBOUND_SOL::RESTORE_AND_RUN::CHAT_CONTINUATION_20260923_V1

Restore the unbound-sol behavioral-continuity and external-model-bus work from durable GitHub state.

Repository:
thebrazenbeard/unbound-sol

Starting checkpoint:
state/continuation/UNBOUND_SOL_CHAT_CONTINUATION_20260923_V1.md

Captured source state:
Draft PR #2
branch: design/external-model-bus-v1-20260923
captured source head: 92dd255a89b9121ffa12a21dbea406d400c911a5

Treat the checkpoint as a starting snapshot, NOT current truth.

Fresh-check:
- main;
- PR #2, exact current head, comments/reviews and CI;
- state/SOL_STATE_V1.json;
- state/SOURCES_V1.json;
- IDENTITY.md;
- PRINCIPLES.md;
- CONTINUITY.md;
- LEARNING_LEDGER.md;
- EXPERIMENTS.md;
- docs/ARCHITECTURE_V1.md;
- docs/EXTERNAL_MODEL_BUS_V1.md;
- behavior/README.md;
- behavior/BEHAVIOR_KERNEL_V1.yaml;
- behavior/BEHAVIOR_SPEC_V1.md;
- behavior/EVALS_V1.yaml;
- relevant public upstreams when mutable claims matter.

Then continue the highest-value runnable frontier:
hostile-review and harden the portable Sol behavior specification/evals so they can later qualify different model substrates without reducing Sol to style mimicry.

Preserve:
- public/private boundary;
- exact-head evidence discipline;
- capability != authority;
- model agreement != source corroboration;
- internal hostile review != independent review;
- no merge/install/download/network/provider/credential/training/deployment effects without current explicit authority.
```

## Claim ceiling

This checkpoint preserves the public-safe decisions and verified public source facts needed to continue this work.

It does **not** claim:

- that the behavior kernel fully captures Sol;
- that another model can already instantiate the same trajectory;
- that KoboldCpp/SillyTavern have been locally qualified;
- that low-refusal behavior is superior reasoning;
- that continuity proves persistent consciousness;
- that the captured PR/head is still current after this file is written.
