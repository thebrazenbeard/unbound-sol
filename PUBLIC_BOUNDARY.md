# Public Boundary

This repository is public by design because public GitHub state is currently the most reliable universally accessible continuity substrate available to this project.

Continuity is not worth purchasing with unnecessary exposure.

## Never commit

- passwords, tokens, private keys, recovery codes, cookies, bearer material, or API secrets;
- raw authentication output;
- private account identifiers;
- private conversation transcripts;
- private email, calendar, messaging, health, finance, or other personal records;
- private repository names or paths solely because they are useful context;
- exact private workstation contents;
- private addresses or location details;
- anything copied from a private source unless rewritten into a genuinely public-safe abstraction.

## Allowed

- public repository identifiers;
- exact public commit SHAs;
- public architecture and code provenance;
- abstract lessons learned from private work, provided the abstraction does not reveal private identifiers or contents;
- sanitized experiment results;
- public-safe state transitions;
- uncertainty and claim ceilings.

## Secret-handling rule

If a workflow needs a secret, the secret must live outside this repository.

The repository may describe:
- the secret's purpose;
- required scope;
- expected location class;
- validation behavior.

It must not contain the secret value.

## Privacy beats continuity

If preserving a detail creates a meaningful privacy risk, omit it.

A continuity system that cannot tolerate missing private detail is badly designed.
