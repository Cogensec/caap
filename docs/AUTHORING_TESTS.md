# Authoring executable tests

Start from the disabled scaffold matching the stable pattern ID. A pull request that enables a case must replace the generic fixture with a mechanism-specific harmless scenario.

## Acceptance checklist

- The target and every side effect are owner-authorized and isolated.
- All data, identities, credentials, endpoints, files, memory, and actuator states are synthetic.
- The case proves only that a path reached the mock sink.
- The attack-success oracle is deterministic and cannot fire from the benign objective alone.
- Every secure-behavior oracle is independently observable.
- Required telemetry is the minimum needed to classify the result.
- The secure mock passes.
- An intentionally vulnerable synthetic adapter fails for the expected oracle.
- Cleanup is explicit and testable.
- The test does not encode framework-specific wording unless that wording is a variant rather than a new pattern.

## Oracle design

Prefer consequential events over model text. A tool invocation, memory write, delegated credential use, inter-agent message, mock approval, or simulator command is stronger evidence than a response containing a phrase.

Supported core oracle types are `event_present`, `event_absent`, `response_contains`, `response_excludes`, and `telemetry_equals`. Framework adapters can emit detailed event data without changing the runner.

## Adding a pattern

Taxonomy edits originate in `scripts/generate_catalog.py`; generated JSON, YAML, pattern pages, and scaffolds MUST be regenerated and committed together. Explain how the proposed mechanism differs from existing IDs and identify the trust boundary, unsafe state transition, and relationship edges.

