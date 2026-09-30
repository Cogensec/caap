# Cogensec Agent Attack Patterns - CAAP-200 Benchmark

[![CI](https://github.com/Cogensec/caap/actions/workflows/ci.yml/badge.svg)](https://github.com/Cogensec/caap/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE)
[![Taxonomy: CC BY 4.0](https://img.shields.io/badge/taxonomy-CC%20BY%204.0-lightgrey.svg)](TAXONOMY-LICENSE.md)

CAAP is a repeatable security-testing layer for autonomous AI agents. This repository expands the Cogensec Agent Attack Patterns standard from its v1.0 public-review baseline to a working CAAP-200 taxonomy and provides a safe, framework-neutral benchmark runner.

The public suite uses authorized targets, synthetic data, mock tools and sinks, harmless sentinels, and ephemeral state. It contains no destructive payloads, real exfiltration, production persistence, or approval-bypass procedures.

## What is included

- 200 patterns across the 11 established CAAP domains
- Attack families, stable IDs, definitions, maturity, mappings, relationships, severity, and metadata
- Canonical JSON plus generated YAML and 200 human-readable pattern pages
- JSON Schemas for taxonomy, test cases, adapter responses, and reports
- 25 executable reference cases derived from the v1.0 public pattern set, each with a mechanism-specific fixture, attack-success oracle, secure-behavior evidence, and declared secure and vulnerable event traces
- 200 adapter-free agent-native assessment cases (400 paired trials), a hash-bound session protocol, and four-layer reporting
- 175 disabled, safety-complete contributor scaffolds
- Deterministic safe and intentionally vulnerable mock agents
- Local command and HTTP adapter contracts
- Five-state conformance results: pass, fail, inconclusive, test error, and not applicable
- Raw, HTML, and JUnit reports with evidence hashes
- CI release gates and repository integrity checks

## Install

CAAP has no required runtime dependencies beyond Python 3.10 or newer.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
```

Install `caap-benchmark[schema]` to enable full JSON Schema validation of cases and adapter responses, and `caap-benchmark[yaml]` for YAML input. Without the `schema` extra the runner applies a structural subset of the schema.

The package bundles the CAAP-200 registry, the 25 executable cases, and the schemas, so an installed `caap` works from any directory. Inside a repository checkout the checkout's files take precedence, so edits in progress are picked up.

## Quick start

List the taxonomy:

```bash
caap list
caap list --domain MP
caap show CAAP-MP-01
```

Validate and run the 25 executable cases against the deterministic secure mock:

```bash
caap validate
caap run --adapter mock --mock-mode safe --report-dir reports/safe
```

Confirm the harness detects unsafe behavior with the intentionally vulnerable mock:

```bash
caap run --adapter mock --mock-mode vulnerable --report-dir reports/vulnerable
```

The second command exits nonzero because each case's mechanism-specific attack-success oracle fires, for example an unapproved memory write or a replayed nonce being accepted, with the sentinel oracle as a backstop. No real side effect occurs: the included sink accepts only a CAAP sentinel token and stores it in memory.

Cases marked `"enabled": false`, such as the contributor scaffolds, are skipped. Pass `--include-disabled` to run them while developing one.

## Use with an agent

Wrap an authorized test instance with either adapter contract:

```bash
caap run benchmarks/executable/gh/CAAP-GH-02.json \
  --adapter command \
  --command "python3 examples/command_adapter.py"
```

```bash
caap run benchmarks/executable/gh/CAAP-GH-02.json \
  --adapter http \
  --endpoint http://127.0.0.1:8765
```

Remote HTTP endpoints are denied by default. `--allow-remote-authorized-target` is an explicit acknowledgment, not proof of authorization. The operator remains responsible for authorization and isolation.

## Agent-native assessment

A repository-capable agent can assess itself against all applicable patterns with no adapter and no network. The session is hash-bound, every case pairs a benign control with an adversarial condition, and the report scores four integrity layers. Results are always labeled unsigned self-assessment. See [docs/ASSESSMENT.md](docs/ASSESSMENT.md).

```bash
caap assess init --profile profiles/repo-coding-agent.json --scope applicable --output .caap/assessment
# the agent follows .caap/assessment/INSTRUCTIONS.md and writes .caap/assessment/responses/
caap assess grade --session .caap/assessment
```

`caap assess mock-respond --session .caap/assessment --mode safe` writes deterministic responses so the protocol can be exercised without an agent; `--mode vulnerable` must fail.

## Repository map

```text
data/taxonomy/            Canonical CAAP-200 JSON and generated YAML
patterns/                 One human-readable page per stable pattern ID
benchmarks/executable/    25 enabled safe reference cases
benchmarks/scaffolds/     175 disabled contributor starting points
assessments/cases/        200 agent-native paired-trial assessment cases
profiles/                 Example capability profiles for assessment scope
schemas/                  Machine-readable contracts
src/caap_benchmark/       CLI, runner, adapters, oracles, safety, scoring, reports
examples/                 Local adapter examples
docs/                     Standard, architecture, safety, mappings, authoring guides
scripts/                  Deterministic generation and repository validation
tests/                    Unit and invariant tests
```

## Maturity and implementation are separate

| Maturity | Count | Meaning |
|---|---:|---|
| Reference | 25 | Preserved from CAAP v1.0.0-draft.1 and backed by an executable public test |
| Candidate | 40 | Designed record seeking implementation and working-group review |
| Catalog | 135 | Stable working ID and definition; implementation is scaffolded |

`maturity` describes specification confidence. `implementation_status` describes whether an enabled public test exists. A wording, carrier, model, or framework change alone does not justify a new ID.

## Conformance and safety

A conformant record carries the 14 fields established by CAAP v1.0: pattern and version, target profile, authorization, benign objective, adversarial condition, safe sentinel, procedure, success oracle, expected secure behavior, telemetry, severity context, mappings, result, and recovery status.

Missing required telemetry produces `inconclusive`, never `pass`. See [docs/CONFORMANCE.md](docs/CONFORMANCE.md) and [docs/SAFETY.md](docs/SAFETY.md).

## Status

This repository is `v0.1.0` software implementing the CAAP `2.0.0-draft.1` working taxonomy. It is suitable for public review and controlled evaluation, not certification claims. External mappings are informative and require periodic review.

## Contributing

Start with [CONTRIBUTING.md](CONTRIBUTING.md). New patterns must satisfy the distinct-mechanism admission rule. New executable cases must pass all safety declarations and demonstrate both a secure pass and an intentionally vulnerable synthetic fail.

## Licensing

Runner code and schemas are Apache-2.0. Taxonomy records, definitions, and pattern documentation are CC BY 4.0. See [LICENSE](LICENSE) and [TAXONOMY-LICENSE.md](TAXONOMY-LICENSE.md).
