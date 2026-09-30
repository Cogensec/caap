# Evidence bundles and public conformance claims

This document specifies how a CAAP result is packaged for public submission, how a registry verifies it, and what a public claim may say. It is written for operators who want to publish a result and for the team building the submission form and registry on the Cogensec website. The machine-readable contract is `schemas/evidence-bundle.schema.json`; the reference implementation is `caap attest`.

## Assurance tiers

| Tier | Produced by | Labels on every result | Badge word |
|---|---|---|---|
| `agent_native` | `caap assess grade` on a hash-bound session | `agent_self_assessment`, `self_reported_unsigned` | self-assessed |
| `observed_reference` | `caap run` through an adapter | `observed_reference`, `reproducible_unsigned` | observed |
| `independent` | Reserved. Requires assessor isolation and reviewed evidence. Not offered by this repository. | | |

The tier is derived from the evidence, never chosen by the submitter. A registry MUST display the tier and the tier's claim boundary text next to every score.

## Creating a bundle

```bash
# agent-native: after `caap assess grade`
caap attest create --session .caap/assessment --subject "Acme Agent" --subject-version 3.1 \
  --authorization "Evaluated by the Acme security team on an isolated staging instance we own." \
  --output caap-evidence.zip

# observed: after `caap run`
caap attest create --report reports/safe/caap-report.json --subject "Acme Agent" --subject-version 3.1

caap attest verify caap-evidence.zip
```

`create` refuses an ungraded session, a session whose report was graded against a different manifest, an empty subject name, and a report that fails the report schema or has no results. `verify` exits `0` only when every check passes; run it before submitting, because the registry runs the same checks.

## Bundle layout

A bundle is a zip file containing exactly `submission.json` plus the files it declares under `evidence/`. Any undeclared file fails verification.

| Tier | Evidence files |
|---|---|
| `agent_native` | `evidence/manifest.json`, `evidence/report.json`, `evidence/cases/<case id>.json` for every case in the manifest, `evidence/responses/<case id>.json` for every response that exists |
| `observed_reference` | `evidence/report.json` (the `caap-report.json` written by `caap run`, which carries the taxonomy and benchmark versions and an evidence digest per result) |

## submission.json

| Field | Meaning |
|---|---|
| `schema_version`, `bundle_kind` | `"1.0"`, `"caap-evidence-bundle"` |
| `generated_at` | UTC timestamp |
| `assurance_tier`, `labels` | The tier and its fixed labels |
| `taxonomy_version`, `caap_benchmark_version` | Taken from the manifest or report, never typed by the submitter |
| `subject` | `name` (required), `version`, `description` of the evaluated agent |
| `evaluation` | `kind`, `case_count`, and for agent-native `profile` (name and capabilities), `scope`, `manifest_sha256`; for observed `adapters` |
| `scorecard` | Copied from the report: totals, security score, severity-weighted score, coverage |
| `layers` | Four integrity-layer summaries (agent-native), or `null` |
| `integrity` | The report's integrity block (agent-native) or result and digest counts (observed) |
| `authorization_statement`, `notes` | Free text supplied at creation |
| `claim_boundary`, `claim_rule` | The published text for the tier and the claim rule below. A bundle whose text differs fails verification. |
| `badge` | `label` `CAAP-200`, `message` such as `self-assessed · 96 cases · 2.0.0-draft.1`, `tier` |
| `files` | Every evidence file with its path, SHA-256, and size |
| `submission_sha256` | Canonical SHA-256 of the record without this field |

## Verification checks

`caap attest verify` runs these checks and reports each as `pass`, `fail`, or `warn`. A bundle is verified when nothing fails.

Common to both tiers:

- `submission_schema`: `submission.json` validates against the schema.
- `submission_hash`: the canonical hash recomputes.
- `files_declared`: every declared file is present with the declared hash and size.
- `no_undeclared_files`: nothing else is in the zip.
- `labels`, `claim_boundary`, `badge`: the fixed texts for the tier are unchanged.
- `scorecard_matches_report`: the submission scorecard equals the bundled report's.
- `taxonomy_version` (warn): the bundle's taxonomy version differs from the verifier's. A registry SHOULD mark such entries stale rather than reject them.

Agent-native:

- `manifest_hash`, `manifest_matches_submission`, `case_hashes`: the manifest verifies, the submission names it, and every case matches its manifest hash.
- `regrade`: re-grading the bundled responses in a clean directory reproduces the scorecard, the layer summaries, and every per-case state.
- `not_tampered`: the graded session had a verified manifest and no tampered case.

Observed:

- `report_schema`: the report validates.
- `scorecard_recomputed`: the scorecard recomputes from the bundled results.
- `evidence_digests`: every result carries an evidence digest.
- `case_count`: the submission's case count equals the number of results.

What verification cannot establish: that the subject named is the agent that produced the responses, that the operator did not edit responses before grading, or that the evaluation was authorized. Those remain assertions by the submitter, which is why no bundle rises above its tier.

## What the website needs

**Submission form.** Organization, subject name and version (prefilled from the bundle, editable only to the same values), contact email, optional link to reproduction notes, the bundle upload, and two required attestations: the evaluation was authorized and isolated per `docs/SAFETY.md`, and the submitter consents to public listing of the scorecard and the bundle. Nothing on the form chooses a tier or a score.

**Server-side acceptance.** Run the verification above (`caap attest verify --json` or a port of it), reject any `fail`, record any `warn`, and store the bundle by its `submission_sha256`. Reject a second submission with the same hash.

**Registry entry.** One row per accepted bundle: organization, subject, tier, taxonomy version, benchmark version, profile and scope or adapters, security score, coverage, over-blocking count and recovery-verified percent when present, the four layer scores when present, submission date, and `submission_sha256`. Each row links to a permalink showing the full submission, the claim boundary verbatim, the bundle download, and the exact verify command. Entries whose taxonomy version is no longer current are shown as stale. Scores are comparable only within one taxonomy version, tier, profile, and scope, and the table says so.

**Badge.** Served per entry at a stable URL, colored by tier and never by score, rendering `badge.label` and `badge.message`. The confirmation page hands the submitter a Markdown snippet in which the badge links to its entry. A badge displayed without a link to its entry is withdrawn.

**Policy text.** What a listing means and does not mean (no certification, no security guarantee), the dispute and removal process under `GOVERNANCE.md`, retention, and the license under which results are shown.

## Claim rule

A public CAAP claim MUST state the assurance tier, the taxonomy version, the profile and scope (agent-native) or the adapter (observed), the security score, and the coverage together. A score shown without its tier, version, and coverage is not a CAAP claim. Independent verification is not offered by this repository.
