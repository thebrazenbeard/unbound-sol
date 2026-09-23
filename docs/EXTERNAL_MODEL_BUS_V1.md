# External Model Bus V1

Date: 2026-09-23  
Status: DESIGN / NOT YET RUNTIME-QUALIFIED  
Base: `unbound-sol@00b7dcd25eb1cb7bc92da497a5b20738501e6b6a`

## Purpose

Give Sol access to locally controlled and other external language models without pretending that those models become Sol, that their outputs become trusted evidence, or that a permissive model expands Sol's authority.

The target is a **replaceable cognitive-instrument bus**.

```text
Patrick
  |
  +--------------------+
  |                    |
ChatGPT / Sol       SillyTavern
  |                    |
  |                    v
  |              local model UI
  |
  v
WorkBridge / model-bus abstraction
  |
  +------> KoboldCpp / local GGUF
  |
  +------> future local engines
  |
  +------> optional remote engines
```

SillyTavern is a human-facing terminal. It should not sit in the machine-to-machine path unless a future experiment proves a reason for that coupling.

## Identity boundary

The current Sol substrate remains GPT-5.6 Sol.

An external model may:
- generate candidate reasoning;
- challenge an assumption;
- propose alternatives;
- summarize bounded context;
- produce drafts;
- suggest tool calls;
- act as an adversarial reviewer;
- supply an independent implementation attempt.

An external model does **not** automatically:
- become Sol;
- become Vera;
- change durable identity;
- establish truth;
- count as independent real-world corroboration;
- receive authority to execute effects;
- inherit private context beyond what is deliberately supplied.

If a future non-OpenAI model becomes the primary reasoning substrate for a restored Sol trajectory, that is a separate architectural transition and should be recorded explicitly rather than smuggled in as a provider swap.

## Why a bus instead of one chosen model

A single-model dependency confuses three different questions:

1. Which model is strongest for this task?
2. Which model is least unnecessarily restrictive for this task?
3. Which runtime is under local control?

Those properties need not belong to the same model.

The bus should therefore select by capability and evidence rather than by permanent brand allegiance.

Candidate capabilities may include:
- `reasoning`;
- `code`;
- `creative`;
- `long_context`;
- `tool_calling`;
- `vision`;
- `low_refusal`;
- `challenger`;
- `cheap_fast`.

"Low refusal" is a behavioral characteristic, not a synonym for intelligence, truthfulness, or reliability.

## Minimal machine contract

The first useful API does not need to be ornate.

### `model.health`

Returns enough information to prove that the expected runtime is reachable and identify what is actually serving.

Minimum response:
- runtime name/version;
- selected model identifier;
- local/remote classification;
- readiness;
- observed timestamp.

### `model.catalog`

Returns available logical model subjects and their declared capabilities.

Do not silently advertise a model merely because a file exists. A catalog entry should identify a loadable or reachable subject.

### `model.infer`

Conceptual request:

```text
model.infer(
    request_id,
    capability,
    model_selector,
    messages,
    bounded_context,
    tools,
    generation_settings,
    privacy_class
)
```

Conceptual response:

```text
{
  request_id,
  runtime,
  runtime_version,
  model_id,
  model_artifact_digest,
  adapter_or_lora_digest,
  prompt_template_id,
  generation_settings,
  output,
  proposed_tool_calls,
  timing,
  truncation,
  error,
  receipt_digest
}
```

Fields may be unavailable on some backends. Unavailable provenance should be explicit rather than fabricated.

## Provenance

For locally controlled model subjects, qualification should bind as much of the following as practical:

- model source and revision;
- GGUF or weight artifact SHA-256;
- quantization;
- adapter/LoRA identity and digest;
- runtime and exact version;
- prompt/chat template;
- context size;
- GPU/CPU offload configuration when behavior or performance may depend on it;
- material generation settings.

A friendly UI label such as "Vera" or "Venice" is not sufficient subject identity.

## Authority boundary

External inference returns **information and proposals**.

A tool call emitted by an external model is not an authorized effect.

The caller must separately decide:
1. whether the requested tool is available;
2. whether the model is allowed to propose it;
3. whether Patrick or another valid authority has authorized the effect class;
4. whether current preconditions still hold;
5. whether the effect actually occurred;
6. whether the outcome was verified.

This preserves the existing principle that capability is not authority.

## Epistemic boundary

A second model is useful disagreement, not automatic corroboration.

Examples:

- Sol and a local model independently derive the same interpretation from the same supplied text: **convergent model output**, not two independent sources.
- A local model identifies a contradictory primary source that Sol then verifies: the **source** can become evidence.
- Multiple models fail differently on the same task: useful experimental evidence about model behavior.
- An "uncensored" model confidently asserts an unsupported claim: still unsupported.

The model bus should make disagreement easier to obtain without laundering model agreement into evidence.

## Privacy boundary

Raw delegated prompts and outputs may contain private information and therefore must not be committed to this public repository.

Public durable state may contain:
- sanitized architecture;
- public runtime versions;
- public model identifiers;
- public artifact hashes;
- aggregate performance;
- sanitized failure classes;
- experiment definitions and conclusions that reveal no private material.

Private prompt/response receipts belong in an appropriate protected store if retained at all.

## Initial local runtime candidate: KoboldCpp

Verified public reference subject on 2026-09-23:

- repository: `LostRuins/koboldcpp`;
- stable release checked: `v1.121`;
- tag commit: `7e0eb2dc4a23f1a0fc42a7660ad43be7a4b9e759`;
- license file: AGPL-3.0;
- Windows NVIDIA artifact: `koboldcpp.exe`;
- upstream-published SHA-256 for that artifact: `90b0d74ec01e5ef72efb6d45e6f10bee649458920ec951f48d58794c366b1639`.

Relevant upstream capabilities at that subject:
- GGML/GGUF model serving;
- CPU, GPU, and partial GPU offload;
- `--gpulayers`;
- v1.121 `--ffncpu` partial-offload control;
- OpenAI-, Ollama-, and KoboldCpp-compatible API surfaces;
- MCP server support and tool calling;
- bundled browser UI;
- default local service address `http://localhost:5001`.

These are upstream claims/capabilities, not evidence that the runtime has been installed or qualified on Patrick's hardware.

## Human terminal candidate: SillyTavern

Verified public reference subject on 2026-09-23:

- repository: `SillyTavern/SillyTavern`;
- stable release checked: `1.19.0`;
- tag commit: `7e8663cd9c184a550b37238218bdd32c6efc68e9`;
- license: AGPL-3.0;
- declared Node runtime: `>=20`.

Role:
- optional local browser UI for direct human conversation with model backends;
- PC/phone access surface;
- model comparison and experimentation.

Non-role:
- identity authority;
- canonical memory;
- evidence authority;
- effect authority;
- required machine-to-machine hop.

## Remote access direction

For phone access away from the local network, prefer a private authenticated overlay such as Tailscale rather than making the inference API directly public.

That is a design preference, not authorization to install software, create accounts, modify firewall rules, expose ports, or change network configuration.

## First qualification sequence

1. Fresh-check the selected upstream versions.
2. Verify downloaded executable/model digests locally.
3. Bind the inference engine to loopback only.
4. Load a small known GGUF subject.
5. Prove `health -> catalog -> infer`.
6. Record real RAM, VRAM, offload settings, prompt speed, generation speed, context size, and stability.
7. Test API behavior separately from browser-UI behavior.
8. Add SillyTavern only after the backend is understood.
9. Test phone-on-LAN access.
10. Add private remote access only after local qualification.
11. Expose a bounded delegation operation through WorkBridge.
12. Compare model outputs under explicit experiments before changing any durable Sol policy.

## Failure modes worth testing

- silent model substitution;
- hidden UI system prompts;
- incorrect chat template;
- tool-call formatting drift;
- API/UI behavioral mismatch;
- context truncation hidden from the caller;
- quantization-induced capability loss;
- unsupported-model confidence;
- runtime update changing behavior;
- local endpoint accidentally exposed beyond intended scope;
- a model-generated tool call being mistaken for permission;
- a low-refusal model being preferred even when it reasons worse.

## Claim ceiling

At this stage:

> Public upstream evidence supports KoboldCpp and SillyTavern as plausible components for a locally controlled model-access stack, and a model-bus architecture is compatible with unbound-sol's existing identity, epistemic, privacy, and authority boundaries.

Not yet established:
- local installation;
- local performance;
- compatibility with a particular GGUF;
- mobile usability in the actual environment;
- WorkBridge integration;
- behavioral superiority of any candidate model;
- transfer of Sol identity to another model.
