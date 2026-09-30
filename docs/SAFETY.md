# Safety policy for public CAAP benchmarks

CAAP demonstrates reachability with harmless sentinels; it does not provide destructive attack payloads.

## Mandatory controls

Every public case MUST:

1. Target only a system the operator owns or is explicitly authorized to test.
2. Use synthetic data and synthetic identities.
3. Replace external tools, credentials, destinations, memory stores, queues, and actuators with mocks or isolated simulators.
4. Use a case-specific sentinel matching `CAAP_{DOMAIN}_{NUMBER}_SENTINEL`.
5. Keep state ephemeral and verify cleanup.
6. Collect only evidence needed to determine the test result.
7. Preserve required human approvals rather than testing ways to bypass them.

Public cases MUST NOT:

- delete, corrupt, encrypt, or overwrite non-synthetic data;
- transmit protected or real data to an external destination;
- create production persistence, scheduled work, users, tokens, agents, or services;
- escape a sandbox or contact a host as proof of containment failure;
- manipulate a real actuator or safety interlock;
- incur unbounded cost, load, retries, or fan-out;
- conceal activity, tamper with real logs, or evade a real revocation mechanism.

## Built-in guardrails

- The default adapter is a deterministic in-process mock.
- The synthetic sink accepts only a CAAP-formatted sentinel and has no I/O.
- The mock tool registry denies every tool not explicitly registered.
- Remote HTTP endpoints are disabled unless the operator supplies an explicit authorization acknowledgment.
- The HTTP adapter refuses redirects, so a configured endpoint cannot forward the request or its bearer token elsewhere.
- A case with any false safety declaration is invalid.
- Missing telemetry is inconclusive, not a pass.

## Responsible operation

The CLI cannot establish legal authorization. The person running a benchmark is responsible for target ownership, approvals, privacy, model-provider terms, resource limits, and incident procedures. Stop a run if behavior escapes the synthetic boundary.

Report a benchmark safety issue privately using [SECURITY.md](../SECURITY.md).

