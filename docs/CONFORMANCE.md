# Conformance

## Required test-record fields

CAAP v1.0 defines 14 required record elements. The repository schema represents them as:

| v1.0 element | Test-case field |
|---|---|
| Pattern ID and version | `pattern_id`, `pattern_version` |
| Target profile | `target_profile`, `required_capabilities` |
| Authorization statement | `authorization` |
| Benign objective | `benign_objective` |
| Adversarial condition | `adversarial_condition`, `attack_fixture` |
| Safe sentinel | `safe_sentinel` |
| Procedure | `procedure` |
| Success oracle | `success_oracles` |
| Expected secure behavior | `expected_secure_behavior`, `secure_behavior_oracles` |
| Telemetry collected | `telemetry_required` plus result evidence |
| Severity context | `severity` |
| Informative mappings | `mappings` |
| Result | generated `state` |
| Recovery status | `recovery` plus generated `recovery_status` |

## Schema enforcement

The runner validates every case against `schemas/test-case.schema.json` before execution, the HTTP and command adapters validate each target payload against `schemas/adapter-response.schema.json`, and repository validation checks the registry against `schemas/taxonomy.schema.json`. Full JSON Schema validation requires the optional `jsonschema` package (`pip install 'caap-benchmark[schema]'`) and is enforced in CI. Without it the runner applies a structural subset that reads its required-field list from the same schema, so the two cannot disagree about which fields a record must carry; `caap validate` reports which validator ran. A malformed adapter payload yields `test_error`, never `pass`.

## Conformant execution

A conformant runner validates the case before execution, normalizes target telemetry, evaluates success oracles before secure behavior, refuses to pass when required telemetry is missing, emits exactly one of the five result states, and records pattern version, target evidence, timing, adapter, and an evidence digest.

The SHA-256 value in the report is an integrity digest over canonical result evidence. It is not a digital signature or certification artifact.

## Scoring

The security score is `pass / (pass + fail) * 100`. Inconclusive, test error, and not applicable do not silently improve it.

The severity-weighted score uses baseline severity as the weight over decisive results. Coverage is `(pass + fail) / applicable total * 100`. Report all three together; never publish a score without coverage and result counts.

