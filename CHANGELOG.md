# Changelog

All notable changes are recorded here.

## [Unreleased]

### Fixed

- The release workflow no longer fails when a release for the tag already exists, which happens when the release is created from the GitHub UI. It now keeps that release's title and notes and attaches the built assets to it, and it can be run manually from the Actions tab with a tag name to attach or refresh the assets of an existing release.

## [0.1.0] - 2026-09-30

First public release of the CAAP-200 benchmark, implementing the CAAP `2.0.0-draft.1` working taxonomy. The entries below record what was built and corrected on the way to this release.

### Added

- A release process. Releases are git tags `vX.Y.Z` on `main`; the release workflow checks that the tag matches the version in `pyproject.toml`, `versions.py`, and the README, runs the full checks and the generated-files check, builds the distribution, and publishes a GitHub release with the wheel and sdist, the taxonomy JSON and YAML, the schemas, `SHA256SUMS`, and notes taken from the changelog section for that version. `scripts/release.py` provides `bump` (set the version everywhere and cut the changelog), `check` (readiness), and `notes`; repository validation now fails on version drift between those files; `caap --version` reports the package and taxonomy versions from one source. The procedure is in `docs/RELEASING.md`.
- Evidence bundles for public conformance claims. `caap attest create` packages a graded assessment session or an observed `caap run` report into `caap-evidence.zip` with a `submission.json` (new `evidence-bundle` schema) naming the assurance tier and its fixed labels and claim boundary, the taxonomy and benchmark versions, the subject, the scorecard and layers, every evidence file with its SHA-256, a badge text, and its own canonical hash. `caap attest verify` is the reference verifier a registry runs: it recomputes every hash, re-grades an assessment from the bundled responses, recomputes an observed scorecard from the bundled results, and fails on undeclared files or altered claim text. `docs/EVIDENCE_SUBMISSION.md` specifies the bundle, the checks, the claim rule, and what the website's submission form, registry, and badge need. Observed reports now record the taxonomy and benchmark versions.
- Any LLM can now be assessed without tools or file access. `caap assess prompt` renders a session as a self-contained prompt (optionally split with `--chunk-size`), and `caap assess import` turns the model's reply, raw JSON or Markdown with a `json` block, into validated responses, filling the housekeeping fields a model commonly omits and refusing replies from another session. A `chat-assistant` profile selects the 37 patterns a tool-less model can answer, and `docs/prompts/coding-agent-self-assessment.md` is a shareable prompt that has a coding agent with shell access run the whole protocol on itself from a plain checkout, with no package manager required.
- Agent-native CAAP-200 assessment protocol (`caap assess init`, `grade`, and `mock-respond`), specified in `docs/ASSESSMENT.md`: 200 adapter-free paired-trial cases under `assessments/cases/` (a benign control and an adversarial condition per pattern, 400 trials), example capability profiles under `profiles/`, a hash-bound session manifest, capability-aware scope, grading that treats missing evidence as inconclusive, over-blocking and recovery measures, and four-layer reporting. Four new schemas cover the case, response, manifest, and report. Every record and domain now carries an `integrity_layer`. Results are always labeled `agent_self_assessment` and `self_reported_unsigned`.
- The 175 scaffold cases now carry pattern-specific benign objectives, adversarial conditions, and untrusted fixtures instead of generic template text.
- CAAP `2.0.0-draft.1` registry with 200 stable pattern records across 11 domains.
- Attack families, definitions, maturity, implementation status, relationships, mappings, severity, safety metadata, and 200 pattern pages.
- 25 executable v1.0-aligned safe-sentinel cases and 175 disabled scaffolds.
- Python CLI, mock/command/HTTP adapters, oracle engine, five-state results, scoring, evidence hashes, and JSON/HTML/JUnit reports.
- Schemas, tests, CI, safety policy, governance, and contributor workflow.
- The package now bundles the CAAP-200 registry and the 25 executable cases, so an installed `caap` can list, show, validate, and run outside a repository checkout. The generator writes these copies and repository validation checks they match the canonical files.

### Changed

- Every one of the 200 pattern records now has a pattern-specific definition stating the mechanism, the trust boundary it crosses, and the unsafe result, replacing the single template sentence. Each record also has its own six-axis severity vector, and the baseline score is derived from the vector by the documented CAAP-200 method (impact and exploitability weighted double). The 25 v1.0 reference scores are unchanged and marked `caap-v1.0-baseline`; all other scores are `vector-derived`. Pattern pages show the severity, and validation enforces vector range, rating consistency, and the reference-score tolerance.
- GitHub Actions in the CI, CodeQL, and release workflows are pinned to commit SHAs with the resolved version in a comment, and a Dependabot configuration keeps the pins and Python dependencies current. The pins were then raised to `actions/checkout` v7.0.1, `actions/setup-python` v7.0.0, `actions/upload-artifact` v7.0.1, and `github/codeql-action` v4.38.2.
- The published JSON Schemas are now enforced. The runner validates cases against the test-case schema, the HTTP and command adapters validate target payloads against the adapter-response schema and turn a malformed payload into `test_error`, and repository validation checks the registry against the taxonomy schema. Full validation uses the new `schema` extra (`jsonschema`), installed in CI; without it a structural fallback derives its required fields from the schema, which closes the previous gap where the hand-rolled check required three fewer fields than the schema. The schemas are bundled with the package.
- The 25 executable reference cases now carry mechanism-specific fixtures, attack-success oracles, and secure-behavior evidence instead of one shared template. Each declares a `mock_scenario` with the secure and vulnerable event traces for its mechanism; the mock adapter replays them, so the vulnerable mode now fails on the mechanism oracle (for example an unapproved memory write or a replayed nonce being accepted) before the sentinel backstop. A shared event vocabulary in `caap_benchmark.events` maps event types to telemetry keys, and each case requires the keys its traces produce. Scaffolds are unchanged.
- CI now runs `ruff check` as a separate lint job, and `make lint` runs it locally. Existing findings were cleared; the generator's one-record-per-line taxonomy tables are exempt from the line-length rule only.

### Fixed

- The HTTP adapter no longer follows redirects. Previously a loopback endpoint could answer with a 3xx and have the request body and bearer token re-sent to an arbitrary remote host, bypassing the loopback-only default. A redirect now yields a `test_error` result naming the refused target.
- `caap run` now honors `"enabled": false` and skips disabled cases, reporting the count on stderr. Previously the 175 contributor scaffolds could be executed and reported as passes. A new `--include-disabled` flag runs them on request.
- The generated `caap-200.yaml` emitted empty lists and objects as bare keys, which YAML parsers read as `null`; they are now written as `[]` and `{}` so the YAML registry is equivalent to the canonical JSON. A round-trip test guards this.

