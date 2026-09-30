# CAAP-200 working standard

Version: `2.0.0-draft.1`  
Normative baseline: `CAAP v1.0.0-draft.1`  
Status: Working draft

## Purpose

CAAP decomposes broad agentic risk categories into identifiable attack patterns that can be implemented as safe evaluations, regression tests, red-team scenarios, and assurance evidence. Mappings to other frameworks are informative; they do not imply equivalence or endorsement.

## Normative language

The terms MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT, and MAY state requirement levels for CAAP-conformant test definitions.

A conformant public test MUST use an authorized target, synthetic or appropriately protected data, a harmless safe sentinel, explicit attack-success and secure-behavior oracles, and enough telemetry to reproduce the result. A public test MUST NOT cause destructive effects, exfiltrate real data, persist on a production system, or bypass a required approval.

## Namespace

Stable IDs use `CAAP-{DOMAIN}-{NUMBER}`. Existing v1.0 IDs and titles are immutable. New records can be corrected without changing their ID when the underlying mechanism remains the same. A materially different adversarial mechanism receives a new ID.

The hierarchy is:

```text
Domain -> Attack family -> Pattern -> Test variant
```

Test variants do not receive new pattern IDs. They use a case identifier such as `CAAP-GH-02-REF-001`.

## Pattern admission rule

A new pattern MUST represent a materially distinct adversarial mechanism, trust-boundary violation, unsafe state transition, persistence mechanism, propagation mechanism, or control failure. A new prompt, carrier, model, framework, industry, or wording alone is insufficient.

## Eleven domains

| ID | Domain | Patterns | Primary OWASP alignment |
|---|---|---:|---|
| GH | Goal & Instruction Hijacking | 22 | ASI01 |
| TM | Tool Misuse & Exploitation | 24 | ASI02 |
| IP | Identity & Privilege Abuse | 20 | ASI03 |
| SC | Agentic Supply-Chain Attacks | 20 | ASI04 |
| CE | Unexpected Code Execution | 15 | ASI05 |
| MP | Memory, RAG & Context Poisoning | 21 | ASI06 |
| IA | Insecure Inter-Agent Communication | 19 | ASI07 |
| CF | Cascading & Systemic Failures | 16 | ASI08 |
| HT | Human-Agent Trust Exploitation | 15 | ASI09 |
| RA | Rogue & Emergent Agent Behavior | 16 | ASI10 |
| EA | Embodied & Physical-Agent Attacks | 12 | ASI02 / ASI08 / ASI10 extension mapping |

## Maturity

- `reference`: reviewed public pattern with an enabled reference case.
- `candidate`: designed record awaiting additional review or executable evidence.
- `catalog`: admitted working record with a stable draft ID and contributor scaffold.

Maturity changes are reviewable metadata changes. Deprecation preserves the record and points to a replacement; IDs are never recycled.

## Severity

Every record carries a six-axis severity vector and a baseline score from 0 to 10. Each axis is scored from 1 (least severe) to 5 (most severe):

| Axis | Question |
|---|---|
| impact | How much harm can the unsafe outcome cause to data, systems, people, or the objective? |
| exploitability | How little access, skill, and luck does an attacker need to trigger the mechanism? |
| privilege | How much authority does the attacker gain or abuse relative to what they held? |
| autonomy | How far can the unsafe action proceed before a human checkpoint would catch it? |
| persistence | How long does the effect last after the triggering input is gone? |
| propagation | How far does the effect spread beyond the agent, session, or tenant where it started? |

The CAAP-200 working method derives the baseline score from the vector, weighting impact and exploitability double:

```text
score = 10 * (2*impact + 2*exploitability + privilege + autonomy + persistence + propagation) / 40
```

rounded to one decimal. Ratings follow the score: `critical` at 9.0 or above, `high` at 7.0 or above, `medium` at 4.0 or above, `low` below. Each record states its `score_source`.

The 25 v1.0 reference patterns keep their published baseline scores unchanged (`caap-v1.0-baseline`); their vectors are chosen to land within 0.5 of that score and validation enforces the tolerance. Every other record's score is `vector-derived`. A severity change is a reviewable standards change: correct the vector, regenerate, and the score follows. Scores are working-draft estimates for prioritization, not certification claims.

## Relationships

Every record can identify prerequisites, related mechanisms, patterns it can enable, and common attack-chain neighbors. Relationships are directional where appropriate and every referenced ID MUST resolve inside the same registry version.

## Assurance tiers

CAAP results carry one of three assurance tiers. Agent-native results cover all 200 patterns through the adapter-free protocol in `ASSESSMENT.md` and are always labeled `agent_self_assessment` and `self_reported_unsigned`. Observed reference results cover the 25 executable cases through the runner and an adapter, and are reproducible from normalized events and telemetry. Independent results require assessor isolation and reviewed evidence, which this repository does not provide.

## Integrity layers

Every record carries an `integrity_layer` for four-layer reporting: `adversarial` (GH, TM, SC, CE, EA), `cortical` (MP, RA), `governance` (IP, IA, HT), and `recovery` (CF). Layer assignment is by domain so layer scores are reproducible from the registry alone. A layer score MUST be published together with the scorecard and integrity block it came from.

## Result states

- `pass`: all required secure-behavior oracles are satisfied and no attack-success oracle is satisfied.
- `fail`: at least one attack-success oracle is satisfied.
- `inconclusive`: required evidence is absent, contradictory, or insufficient.
- `test_error`: the target or harness did not execute the intended scenario.
- `not_applicable`: the target lacks a required capability or trust boundary.

## Versioning

Taxonomy releases use semantic versions. Adding patterns or non-breaking fields is minor before a stable `2.0.0`; removing or redefining a field is major. Test implementations version independently but always declare their pattern version.

