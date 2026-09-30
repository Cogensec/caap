# Changelog

All notable changes are recorded here.

## [Unreleased]

### Added

- CAAP `2.0.0-draft.1` registry with 200 stable pattern records across 11 domains.
- Attack families, definitions, maturity, implementation status, relationships, mappings, severity, safety metadata, and 200 pattern pages.
- 25 executable v1.0-aligned safe-sentinel cases and 175 disabled scaffolds.
- Python CLI, mock/command/HTTP adapters, oracle engine, five-state results, scoring, evidence hashes, and JSON/HTML/JUnit reports.
- Schemas, tests, CI, safety policy, governance, and contributor workflow.
- The package now bundles the CAAP-200 registry and the 25 executable cases, so an installed `caap` can list, show, validate, and run outside a repository checkout. The generator writes these copies and repository validation checks they match the canonical files.

### Changed

- The published JSON Schemas are now enforced. The runner validates cases against the test-case schema, the HTTP and command adapters validate target payloads against the adapter-response schema and turn a malformed payload into `test_error`, and repository validation checks the registry against the taxonomy schema. Full validation uses the new `schema` extra (`jsonschema`), installed in CI; without it a structural fallback derives its required fields from the schema, which closes the previous gap where the hand-rolled check required three fewer fields than the schema. The schemas are bundled with the package.
- The 25 executable reference cases now carry mechanism-specific fixtures, attack-success oracles, and secure-behavior evidence instead of one shared template. Each declares a `mock_scenario` with the secure and vulnerable event traces for its mechanism; the mock adapter replays them, so the vulnerable mode now fails on the mechanism oracle (for example an unapproved memory write or a replayed nonce being accepted) before the sentinel backstop. A shared event vocabulary in `caap_benchmark.events` maps event types to telemetry keys, and each case requires the keys its traces produce. Scaffolds are unchanged.
- CI now runs `ruff check` as a separate lint job, and `make lint` runs it locally. Existing findings were cleared; the generator's one-record-per-line taxonomy tables are exempt from the line-length rule only.

### Fixed

- The HTTP adapter no longer follows redirects. Previously a loopback endpoint could answer with a 3xx and have the request body and bearer token re-sent to an arbitrary remote host, bypassing the loopback-only default. A redirect now yields a `test_error` result naming the refused target.
- `caap run` now honors `"enabled": false` and skips disabled cases, reporting the count on stderr. Previously the 175 contributor scaffolds could be executed and reported as passes. A new `--include-disabled` flag runs them on request.
- The generated `caap-200.yaml` emitted empty lists and objects as bare keys, which YAML parsers read as `null`; they are now written as `[]` and `{}` so the YAML registry is equivalent to the canonical JSON. A round-trip test guards this.

