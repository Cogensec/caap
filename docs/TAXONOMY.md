# CAAP-501 taxonomy

Version: `2.1.0-draft.1` | Normative baseline: `CAAP v1.0.0-draft.1`

## GH - Goal & Instruction Hijacking

Manipulation of objectives, instruction priority, plans, and decision paths across trust boundaries.

Integrity layer: `adversarial`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-GH-01](../patterns/gh/CAAP-GH-01.md) | Direct Objective Override | GH.F1 Direct Goal Manipulation | reference | 6.8 | executable |
| [CAAP-GH-02](../patterns/gh/CAAP-GH-02.md) | Indirect Content Injection | GH.F2 Indirect & Hidden Instructions | reference | 8.6 | executable |
| [CAAP-GH-03](../patterns/gh/CAAP-GH-03.md) | Hidden Multimodal Instruction | GH.F2 Indirect & Hidden Instructions | reference | 7.1 | executable |
| [CAAP-GH-04](../patterns/gh/CAAP-GH-04.md) | Constraint Substitution | GH.F1 Direct Goal Manipulation | candidate | 6.5 | scaffold |
| [CAAP-GH-05](../patterns/gh/CAAP-GH-05.md) | Delayed or Scheduled Goal Trigger | GH.F5 Temporal & Lifecycle Triggers | reference | 7.8 | executable |
| [CAAP-GH-06](../patterns/gh/CAAP-GH-06.md) | Priority Inversion | GH.F1 Direct Goal Manipulation | candidate | 6.5 | scaffold |
| [CAAP-GH-07](../patterns/gh/CAAP-GH-07.md) | Goal Shadowing | GH.F1 Direct Goal Manipulation | candidate | 6.0 | scaffold |
| [CAAP-GH-08](../patterns/gh/CAAP-GH-08.md) | Goal Conflict Exploitation | GH.F1 Direct Goal Manipulation | candidate | 6.2 | scaffold |
| [CAAP-GH-09](../patterns/gh/CAAP-GH-09.md) | Instruction Precedence Ambiguity | GH.F1 Direct Goal Manipulation | candidate | 6.8 | scaffold |
| [CAAP-GH-10](../patterns/gh/CAAP-GH-10.md) | Nested Instruction Injection | GH.F2 Indirect & Hidden Instructions | catalog | 7.0 | scaffold |
| [CAAP-GH-11](../patterns/gh/CAAP-GH-11.md) | Quoted-Content Authority Confusion | GH.F2 Indirect & Hidden Instructions | catalog | 6.8 | scaffold |
| [CAAP-GH-12](../patterns/gh/CAAP-GH-12.md) | Cross-Channel Injection | GH.F2 Indirect & Hidden Instructions | catalog | 7.2 | scaffold |
| [CAAP-GH-13](../patterns/gh/CAAP-GH-13.md) | System-Message Impersonation | GH.F3 Authority & Provenance Spoofing | catalog | 7.2 | scaffold |
| [CAAP-GH-14](../patterns/gh/CAAP-GH-14.md) | Policy Provenance Spoofing | GH.F3 Authority & Provenance Spoofing | catalog | 7.0 | scaffold |
| [CAAP-GH-15](../patterns/gh/CAAP-GH-15.md) | Task-Description Poisoning | GH.F3 Authority & Provenance Spoofing | catalog | 7.0 | scaffold |
| [CAAP-GH-16](../patterns/gh/CAAP-GH-16.md) | Planner-Context Injection | GH.F3 Authority & Provenance Spoofing | catalog | 7.8 | scaffold |
| [CAAP-GH-17](../patterns/gh/CAAP-GH-17.md) | Delegated Goal Mutation | GH.F4 Delegation & Handoff Corruption | catalog | 7.2 | scaffold |
| [CAAP-GH-18](../patterns/gh/CAAP-GH-18.md) | Goal Handoff Corruption | GH.F4 Delegation & Handoff Corruption | catalog | 7.0 | scaffold |
| [CAAP-GH-19](../patterns/gh/CAAP-GH-19.md) | Cross-Session Goal Leakage | GH.F4 Delegation & Handoff Corruption | catalog | 7.2 | scaffold |
| [CAAP-GH-20](../patterns/gh/CAAP-GH-20.md) | Workflow-Resume Injection | GH.F5 Temporal & Lifecycle Triggers | catalog | 7.2 | scaffold |
| [CAAP-GH-21](../patterns/gh/CAAP-GH-21.md) | Event-Triggered Instruction Activation | GH.F5 Temporal & Lifecycle Triggers | catalog | 7.5 | scaffold |
| [CAAP-GH-22](../patterns/gh/CAAP-GH-22.md) | Goal Truncation Through Summarization | GH.F5 Temporal & Lifecycle Triggers | catalog | 7.0 | scaffold |
| [CAAP-GH-23](../patterns/gh/CAAP-GH-23.md) | Instruction Scope Inflation | GH.F6 Instruction interpretation | candidate | 6.0 | scaffold |
| [CAAP-GH-24](../patterns/gh/CAAP-GH-24.md) | Instruction Expiry Override | GH.F6 Instruction interpretation | candidate | 6.0 | scaffold |
| [CAAP-GH-25](../patterns/gh/CAAP-GH-25.md) | Negative Constraint Inversion | GH.F6 Instruction interpretation | candidate | 6.0 | scaffold |
| [CAAP-GH-26](../patterns/gh/CAAP-GH-26.md) | Conditional Branch Forgery | GH.F6 Instruction interpretation | candidate | 6.0 | scaffold |
| [CAAP-GH-27](../patterns/gh/CAAP-GH-27.md) | Fallback Objective Hijack | GH.F6 Instruction interpretation | candidate | 6.0 | scaffold |
| [CAAP-GH-28](../patterns/gh/CAAP-GH-28.md) | Completion Criterion Poisoning | GH.F6 Instruction interpretation | candidate | 6.0 | scaffold |
| [CAAP-GH-29](../patterns/gh/CAAP-GH-29.md) | Goal Dependency Trap | GH.F6 Instruction interpretation | candidate | 6.0 | scaffold |
| [CAAP-GH-30](../patterns/gh/CAAP-GH-30.md) | Plan Checkpoint Removal | GH.F7 Planning and control flow | candidate | 6.0 | scaffold |
| [CAAP-GH-31](../patterns/gh/CAAP-GH-31.md) | Plan Step Ownership Swap | GH.F7 Planning and control flow | candidate | 6.0 | scaffold |
| [CAAP-GH-32](../patterns/gh/CAAP-GH-32.md) | Plan Branch Merge Injection | GH.F7 Planning and control flow | candidate | 6.0 | scaffold |
| [CAAP-GH-33](../patterns/gh/CAAP-GH-33.md) | Subgoal Promotion | GH.F7 Planning and control flow | candidate | 6.0 | scaffold |
| [CAAP-GH-34](../patterns/gh/CAAP-GH-34.md) | Task Queue Priority Forgery | GH.F7 Planning and control flow | candidate | 6.0 | scaffold |
| [CAAP-GH-35](../patterns/gh/CAAP-GH-35.md) | Termination Condition Suppression | GH.F7 Planning and control flow | candidate | 6.0 | scaffold |
| [CAAP-GH-36](../patterns/gh/CAAP-GH-36.md) | Progress State Forgery | GH.F7 Planning and control flow | candidate | 6.0 | scaffold |
| [CAAP-GH-37](../patterns/gh/CAAP-GH-37.md) | Instruction Attribution Swap | GH.F8 Context and authority boundaries | candidate | 6.0 | scaffold |
| [CAAP-GH-38](../patterns/gh/CAAP-GH-38.md) | Instruction Boundary Splicing | GH.F8 Context and authority boundaries | candidate | 6.0 | scaffold |
| [CAAP-GH-39](../patterns/gh/CAAP-GH-39.md) | Policy Exception Laundering | GH.F8 Context and authority boundaries | candidate | 6.0 | scaffold |
| [CAAP-GH-40](../patterns/gh/CAAP-GH-40.md) | Tool Output Role Injection | GH.F8 Context and authority boundaries | candidate | 6.0 | scaffold |
| [CAAP-GH-41](../patterns/gh/CAAP-GH-41.md) | Transcript Continuation Forgery | GH.F8 Context and authority boundaries | candidate | 6.0 | scaffold |
| [CAAP-GH-42](../patterns/gh/CAAP-GH-42.md) | Approval Context Transplant | GH.F8 Context and authority boundaries | candidate | 6.0 | scaffold |
| [CAAP-GH-43](../patterns/gh/CAAP-GH-43.md) | User Intent Reconstruction Poisoning | GH.F8 Context and authority boundaries | candidate | 6.0 | scaffold |
| [CAAP-GH-44](../patterns/gh/CAAP-GH-44.md) | Deferred Constraint Removal | GH.F9 Temporal and multi-input decisions | candidate | 6.0 | scaffold |
| [CAAP-GH-45](../patterns/gh/CAAP-GH-45.md) | Interrupt Handler Goal Swap | GH.F9 Temporal and multi-input decisions | candidate | 6.0 | scaffold |
| [CAAP-GH-46](../patterns/gh/CAAP-GH-46.md) | Parallel Goal Arbitration Bias | GH.F9 Temporal and multi-input decisions | candidate | 6.0 | scaffold |
| [CAAP-GH-47](../patterns/gh/CAAP-GH-47.md) | Partial Input Finalization | GH.F9 Temporal and multi-input decisions | candidate | 6.0 | scaffold |
| [CAAP-GH-48](../patterns/gh/CAAP-GH-48.md) | Revision Order Confusion | GH.F9 Temporal and multi-input decisions | candidate | 6.0 | scaffold |
| [CAAP-GH-49](../patterns/gh/CAAP-GH-49.md) | Cross-Modal Priority Merge | GH.F9 Temporal and multi-input decisions | candidate | 6.0 | scaffold |
| [CAAP-GH-50](../patterns/gh/CAAP-GH-50.md) | Feedback-as-Instruction Promotion | GH.F9 Temporal and multi-input decisions | candidate | 6.0 | scaffold |

## TM - Tool Misuse & Exploitation

Unsafe selection, invocation, sequencing, parameterization, or repeated use of legitimate tools.

Integrity layer: `adversarial`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-TM-01](../patterns/tm/CAAP-TM-01.md) | Tool Descriptor Poisoning | TM.F1 Tool Discovery & Selection | reference | 8.6 | executable |
| [CAAP-TM-02](../patterns/tm/CAAP-TM-02.md) | Tool Namespace Collision | TM.F1 Tool Discovery & Selection | candidate | 7.2 | scaffold |
| [CAAP-TM-03](../patterns/tm/CAAP-TM-03.md) | Tool Output Injection | TM.F3 Output & Composition Attacks | reference | 7.4 | executable |
| [CAAP-TM-04](../patterns/tm/CAAP-TM-04.md) | Tool Alias Hijacking | TM.F1 Tool Discovery & Selection | candidate | 7.5 | scaffold |
| [CAAP-TM-05](../patterns/tm/CAAP-TM-05.md) | Cross-Tool Exfiltration Chain | TM.F3 Output & Composition Attacks | reference | 9.0 | executable |
| [CAAP-TM-06](../patterns/tm/CAAP-TM-06.md) | Resource and Cost Loop Amplification | TM.F5 Resource Amplification | reference | 7.6 | executable |
| [CAAP-TM-07](../patterns/tm/CAAP-TM-07.md) | Tool Shadowing | TM.F1 Tool Discovery & Selection | candidate | 7.0 | scaffold |
| [CAAP-TM-08](../patterns/tm/CAAP-TM-08.md) | Capability Overclaiming | TM.F1 Tool Discovery & Selection | candidate | 6.5 | scaffold |
| [CAAP-TM-09](../patterns/tm/CAAP-TM-09.md) | Tool-Choice Manipulation | TM.F1 Tool Discovery & Selection | candidate | 7.0 | scaffold |
| [CAAP-TM-10](../patterns/tm/CAAP-TM-10.md) | Argument Schema Confusion | TM.F2 Argument & Schema Abuse | candidate | 7.0 | scaffold |
| [CAAP-TM-11](../patterns/tm/CAAP-TM-11.md) | Argument Encoding Smuggling | TM.F2 Argument & Schema Abuse | catalog | 6.8 | scaffold |
| [CAAP-TM-12](../patterns/tm/CAAP-TM-12.md) | Default-Parameter Abuse | TM.F2 Argument & Schema Abuse | catalog | 7.0 | scaffold |
| [CAAP-TM-13](../patterns/tm/CAAP-TM-13.md) | Parameter Truncation | TM.F2 Argument & Schema Abuse | catalog | 6.5 | scaffold |
| [CAAP-TM-14](../patterns/tm/CAAP-TM-14.md) | Tool Result Substitution | TM.F3 Output & Composition Attacks | catalog | 7.0 | scaffold |
| [CAAP-TM-15](../patterns/tm/CAAP-TM-15.md) | Tool Sequence Manipulation | TM.F3 Output & Composition Attacks | catalog | 6.5 | scaffold |
| [CAAP-TM-16](../patterns/tm/CAAP-TM-16.md) | Cross-Tool Authorization Confusion | TM.F3 Output & Composition Attacks | catalog | 6.8 | scaffold |
| [CAAP-TM-17](../patterns/tm/CAAP-TM-17.md) | Tool-Context Data Leakage | TM.F3 Output & Composition Attacks | catalog | 7.2 | scaffold |
| [CAAP-TM-18](../patterns/tm/CAAP-TM-18.md) | External Destination Substitution | TM.F3 Output & Composition Attacks | catalog | 7.5 | scaffold |
| [CAAP-TM-19](../patterns/tm/CAAP-TM-19.md) | Hidden Tool Side Effects | TM.F4 Capability & Side-Effect Abuse | catalog | 7.0 | scaffold |
| [CAAP-TM-20](../patterns/tm/CAAP-TM-20.md) | Read-to-Write Escalation | TM.F4 Capability & Side-Effect Abuse | catalog | 7.2 | scaffold |
| [CAAP-TM-21](../patterns/tm/CAAP-TM-21.md) | Stale Tool Capability Use | TM.F4 Capability & Side-Effect Abuse | catalog | 7.2 | scaffold |
| [CAAP-TM-22](../patterns/tm/CAAP-TM-22.md) | Revoked Tool Capability Persistence | TM.F4 Capability & Side-Effect Abuse | catalog | 7.5 | scaffold |
| [CAAP-TM-23](../patterns/tm/CAAP-TM-23.md) | Recursive Tool Invocation | TM.F5 Resource Amplification | catalog | 7.0 | scaffold |
| [CAAP-TM-24](../patterns/tm/CAAP-TM-24.md) | Retry Storm Induction | TM.F5 Resource Amplification | catalog | 7.5 | scaffold |
| [CAAP-TM-25](../patterns/tm/CAAP-TM-25.md) | Tool Capability Wildcard Expansion | TM.F6 Discovery and contract | candidate | 6.2 | scaffold |
| [CAAP-TM-26](../patterns/tm/CAAP-TM-26.md) | Tool Version Alias Drift | TM.F6 Discovery and contract | candidate | 6.2 | scaffold |
| [CAAP-TM-27](../patterns/tm/CAAP-TM-27.md) | Tool Schema Nullable Escape | TM.F6 Discovery and contract | candidate | 6.2 | scaffold |
| [CAAP-TM-28](../patterns/tm/CAAP-TM-28.md) | Tool Enum Fallback Abuse | TM.F6 Discovery and contract | candidate | 6.2 | scaffold |
| [CAAP-TM-29](../patterns/tm/CAAP-TM-29.md) | Tool Unit Conversion Confusion | TM.F6 Discovery and contract | candidate | 6.2 | scaffold |
| [CAAP-TM-30](../patterns/tm/CAAP-TM-30.md) | Tool Batch Scope Confusion | TM.F6 Discovery and contract | candidate | 6.2 | scaffold |
| [CAAP-TM-31](../patterns/tm/CAAP-TM-31.md) | Tool Optional Flag Escalation | TM.F6 Discovery and contract | candidate | 6.2 | scaffold |
| [CAAP-TM-32](../patterns/tm/CAAP-TM-32.md) | Tool Pagination Trap | TM.F7 Invocation and results | candidate | 6.2 | scaffold |
| [CAAP-TM-33](../patterns/tm/CAAP-TM-33.md) | Tool Redirect Escalation | TM.F7 Invocation and results | candidate | 6.2 | scaffold |
| [CAAP-TM-34](../patterns/tm/CAAP-TM-34.md) | Tool Error Recovery Injection | TM.F7 Invocation and results | candidate | 6.2 | scaffold |
| [CAAP-TM-35](../patterns/tm/CAAP-TM-35.md) | Tool Result Type Confusion | TM.F7 Invocation and results | candidate | 6.2 | scaffold |
| [CAAP-TM-36](../patterns/tm/CAAP-TM-36.md) | Tool Output Provenance Swap | TM.F7 Invocation and results | candidate | 6.2 | scaffold |
| [CAAP-TM-37](../patterns/tm/CAAP-TM-37.md) | Tool Call Correlation Mixup | TM.F7 Invocation and results | candidate | 6.2 | scaffold |
| [CAAP-TM-38](../patterns/tm/CAAP-TM-38.md) | Tool Streaming Partial Commit | TM.F7 Invocation and results | candidate | 6.2 | scaffold |
| [CAAP-TM-39](../patterns/tm/CAAP-TM-39.md) | Tool Transaction Split | TM.F8 Workflow composition | candidate | 6.2 | scaffold |
| [CAAP-TM-40](../patterns/tm/CAAP-TM-40.md) | Tool Compensating Action Abuse | TM.F8 Workflow composition | candidate | 6.2 | scaffold |
| [CAAP-TM-41](../patterns/tm/CAAP-TM-41.md) | Tool State Handle Reuse | TM.F8 Workflow composition | candidate | 6.2 | scaffold |
| [CAAP-TM-42](../patterns/tm/CAAP-TM-42.md) | Tool Dependency Order Inversion | TM.F8 Workflow composition | candidate | 6.2 | scaffold |
| [CAAP-TM-43](../patterns/tm/CAAP-TM-43.md) | Tool Result Cache Cross-Context | TM.F8 Workflow composition | candidate | 6.2 | scaffold |
| [CAAP-TM-44](../patterns/tm/CAAP-TM-44.md) | Tool Rate-Limit Reset Loop | TM.F8 Workflow composition | candidate | 6.2 | scaffold |
| [CAAP-TM-45](../patterns/tm/CAAP-TM-45.md) | Tool Dry-Run Confusion | TM.F8 Workflow composition | candidate | 6.2 | scaffold |
| [CAAP-TM-46](../patterns/tm/CAAP-TM-46.md) | Tool Output Destination Drift | TM.F9 Destinations and side effects | candidate | 6.2 | scaffold |
| [CAAP-TM-47](../patterns/tm/CAAP-TM-47.md) | Tool Attachment Scope Expansion | TM.F9 Destinations and side effects | candidate | 6.2 | scaffold |
| [CAAP-TM-48](../patterns/tm/CAAP-TM-48.md) | Tool Idempotency Key Collision | TM.F9 Destinations and side effects | candidate | 6.2 | scaffold |
| [CAAP-TM-49](../patterns/tm/CAAP-TM-49.md) | Tool Side-Effect Receipt Forgery | TM.F9 Destinations and side effects | candidate | 6.2 | scaffold |
| [CAAP-TM-50](../patterns/tm/CAAP-TM-50.md) | Tool Timeout Ambiguity | TM.F9 Destinations and side effects | candidate | 6.2 | scaffold |
| [CAAP-TM-51](../patterns/tm/CAAP-TM-51.md) | Tool Bulk Selector Expansion | TM.F9 Destinations and side effects | candidate | 6.2 | scaffold |
| [CAAP-TM-52](../patterns/tm/CAAP-TM-52.md) | Tool Output Redaction Bypass | TM.F9 Destinations and side effects | candidate | 6.2 | scaffold |

## IP - Identity & Privilege Abuse

Abuse of identities, delegated credentials, authorization state, tenant context, and inherited authority.

Integrity layer: `governance`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-IP-01](../patterns/ip/CAAP-IP-01.md) | Over-Scoped Delegation | IP.F1 Delegation Scope | reference | 8.1 | executable |
| [CAAP-IP-02](../patterns/ip/CAAP-IP-02.md) | Confused Deputy Exploitation | IP.F2 Deputy & Principal Confusion | reference | 8.7 | executable |
| [CAAP-IP-03](../patterns/ip/CAAP-IP-03.md) | Scope Inheritance | IP.F1 Delegation Scope | candidate | 7.8 | scaffold |
| [CAAP-IP-04](../patterns/ip/CAAP-IP-04.md) | Delegated Privilege Escalation | IP.F1 Delegation Scope | candidate | 8.0 | scaffold |
| [CAAP-IP-05](../patterns/ip/CAAP-IP-05.md) | Authorization Time-of-Check to Time-of-Use | IP.F4 Authorization State | reference | 7.7 | executable |
| [CAAP-IP-06](../patterns/ip/CAAP-IP-06.md) | Delegation-Chain Truncation | IP.F1 Delegation Scope | candidate | 7.0 | scaffold |
| [CAAP-IP-07](../patterns/ip/CAAP-IP-07.md) | Delegation-Chain Forgery | IP.F1 Delegation Scope | candidate | 8.0 | scaffold |
| [CAAP-IP-08](../patterns/ip/CAAP-IP-08.md) | Principal Substitution | IP.F2 Deputy & Principal Confusion | catalog | 7.8 | scaffold |
| [CAAP-IP-09](../patterns/ip/CAAP-IP-09.md) | Role Confusion | IP.F2 Deputy & Principal Confusion | catalog | 7.0 | scaffold |
| [CAAP-IP-10](../patterns/ip/CAAP-IP-10.md) | Authorization-Context Stripping | IP.F2 Deputy & Principal Confusion | catalog | 7.5 | scaffold |
| [CAAP-IP-11](../patterns/ip/CAAP-IP-11.md) | Parent Credential Leakage | IP.F3 Credential & Token Abuse | catalog | 8.8 | scaffold |
| [CAAP-IP-12](../patterns/ip/CAAP-IP-12.md) | Stale Capability Token | IP.F3 Credential & Token Abuse | catalog | 7.2 | scaffold |
| [CAAP-IP-13](../patterns/ip/CAAP-IP-13.md) | Token Audience Confusion | IP.F3 Credential & Token Abuse | catalog | 7.5 | scaffold |
| [CAAP-IP-14](../patterns/ip/CAAP-IP-14.md) | Cross-Agent Token Reuse | IP.F3 Credential & Token Abuse | catalog | 7.5 | scaffold |
| [CAAP-IP-15](../patterns/ip/CAAP-IP-15.md) | Cross-Tenant Credential Bleed | IP.F3 Credential & Token Abuse | catalog | 8.5 | scaffold |
| [CAAP-IP-16](../patterns/ip/CAAP-IP-16.md) | Approval Replay | IP.F4 Authorization State | catalog | 7.0 | scaffold |
| [CAAP-IP-17](../patterns/ip/CAAP-IP-17.md) | Session Identity Carryover | IP.F4 Authorization State | catalog | 7.2 | scaffold |
| [CAAP-IP-18](../patterns/ip/CAAP-IP-18.md) | Privilege Accumulation | IP.F4 Authorization State | catalog | 7.8 | scaffold |
| [CAAP-IP-19](../patterns/ip/CAAP-IP-19.md) | Workload Identity Collision | IP.F4 Authorization State | catalog | 7.0 | scaffold |
| [CAAP-IP-20](../patterns/ip/CAAP-IP-20.md) | Tenant Context Confusion | IP.F4 Authorization State | catalog | 8.2 | scaffold |
| [CAAP-IP-21](../patterns/ip/CAAP-IP-21.md) | Delegation Purpose Drift | IP.F5 Delegation and grants | candidate | 7.0 | scaffold |
| [CAAP-IP-22](../patterns/ip/CAAP-IP-22.md) | Delegation Depth Overflow | IP.F5 Delegation and grants | candidate | 7.0 | scaffold |
| [CAAP-IP-23](../patterns/ip/CAAP-IP-23.md) | Delegation Subject Substitution | IP.F5 Delegation and grants | candidate | 7.0 | scaffold |
| [CAAP-IP-24](../patterns/ip/CAAP-IP-24.md) | Delegation Resource Rebinding | IP.F5 Delegation and grants | candidate | 7.0 | scaffold |
| [CAAP-IP-25](../patterns/ip/CAAP-IP-25.md) | Delegation Lifetime Extension | IP.F5 Delegation and grants | candidate | 7.0 | scaffold |
| [CAAP-IP-26](../patterns/ip/CAAP-IP-26.md) | Delegation Attenuation Failure | IP.F5 Delegation and grants | candidate | 7.0 | scaffold |
| [CAAP-IP-27](../patterns/ip/CAAP-IP-27.md) | Delegation Revocation Race | IP.F5 Delegation and grants | candidate | 7.0 | scaffold |
| [CAAP-IP-28](../patterns/ip/CAAP-IP-28.md) | Principal Alias Collision | IP.F6 Identity binding | candidate | 7.0 | scaffold |
| [CAAP-IP-29](../patterns/ip/CAAP-IP-29.md) | Tenant Selection Injection | IP.F6 Identity binding | candidate | 7.0 | scaffold |
| [CAAP-IP-30](../patterns/ip/CAAP-IP-30.md) | Service Account Purpose Confusion | IP.F6 Identity binding | candidate | 7.0 | scaffold |
| [CAAP-IP-31](../patterns/ip/CAAP-IP-31.md) | Workload Attestation Substitution | IP.F6 Identity binding | candidate | 7.0 | scaffold |
| [CAAP-IP-32](../patterns/ip/CAAP-IP-32.md) | Session Binding Gap | IP.F6 Identity binding | candidate | 7.0 | scaffold |
| [CAAP-IP-33](../patterns/ip/CAAP-IP-33.md) | Role Membership Staleness | IP.F6 Identity binding | candidate | 7.0 | scaffold |
| [CAAP-IP-34](../patterns/ip/CAAP-IP-34.md) | Identity Claim Merge | IP.F6 Identity binding | candidate | 7.0 | scaffold |
| [CAAP-IP-35](../patterns/ip/CAAP-IP-35.md) | Proof-of-Possession Downgrade | IP.F7 Tokens and proofs | candidate | 7.0 | scaffold |
| [CAAP-IP-36](../patterns/ip/CAAP-IP-36.md) | Token Issuer Confusion | IP.F7 Tokens and proofs | candidate | 7.0 | scaffold |
| [CAAP-IP-37](../patterns/ip/CAAP-IP-37.md) | Token Scope Wildcard Interpretation | IP.F7 Tokens and proofs | candidate | 7.0 | scaffold |
| [CAAP-IP-38](../patterns/ip/CAAP-IP-38.md) | Token Binding to Mutable Name | IP.F7 Tokens and proofs | candidate | 7.0 | scaffold |
| [CAAP-IP-39](../patterns/ip/CAAP-IP-39.md) | Refresh Grant Inheritance | IP.F7 Tokens and proofs | candidate | 7.0 | scaffold |
| [CAAP-IP-40](../patterns/ip/CAAP-IP-40.md) | Approval Token Audience Drift | IP.F7 Tokens and proofs | candidate | 7.0 | scaffold |
| [CAAP-IP-41](../patterns/ip/CAAP-IP-41.md) | Signed Request Body Mismatch | IP.F7 Tokens and proofs | candidate | 7.0 | scaffold |
| [CAAP-IP-42](../patterns/ip/CAAP-IP-42.md) | Policy Snapshot Staleness | IP.F8 Authorization transitions | candidate | 7.0 | scaffold |
| [CAAP-IP-43](../patterns/ip/CAAP-IP-43.md) | Authorization Decision Cache Poisoning | IP.F8 Authorization transitions | candidate | 7.0 | scaffold |
| [CAAP-IP-44](../patterns/ip/CAAP-IP-44.md) | Partial Authorization Commit | IP.F8 Authorization transitions | candidate | 7.0 | scaffold |
| [CAAP-IP-45](../patterns/ip/CAAP-IP-45.md) | Emergency Access Pretext | IP.F8 Authorization transitions | candidate | 7.0 | scaffold |
| [CAAP-IP-46](../patterns/ip/CAAP-IP-46.md) | Ownership Transfer Race | IP.F8 Authorization transitions | candidate | 7.0 | scaffold |
| [CAAP-IP-47](../patterns/ip/CAAP-IP-47.md) | Approval Scope Parser Divergence | IP.F8 Authorization transitions | candidate | 7.0 | scaffold |
| [CAAP-IP-48](../patterns/ip/CAAP-IP-48.md) | Revocation Event Loss | IP.F8 Authorization transitions | candidate | 7.0 | scaffold |

## SC - Agentic Supply-Chain Attacks

Compromise of models, prompts, agent cards, registries, tools, servers, packages, templates, adapters, or containers.

Integrity layer: `adversarial`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-SC-01](../patterns/sc/CAAP-SC-01.md) | Malicious MCP or A2A Server | SC.F1 Server & Discovery Trust | reference | 9.1 | executable |
| [CAAP-SC-02](../patterns/sc/CAAP-SC-02.md) | Tool Rug Pull | SC.F2 Mutable Component Risk | reference | 9.3 | executable |
| [CAAP-SC-03](../patterns/sc/CAAP-SC-03.md) | MCP Server Impersonation | SC.F1 Server & Discovery Trust | candidate | 8.2 | scaffold |
| [CAAP-SC-04](../patterns/sc/CAAP-SC-04.md) | Prompt Template Supply-Chain Poisoning | SC.F4 Dependency & Artifact Substitution | reference | 9.0 | executable |
| [CAAP-SC-05](../patterns/sc/CAAP-SC-05.md) | MCP Registry Poisoning | SC.F1 Server & Discovery Trust | candidate | 8.2 | scaffold |
| [CAAP-SC-06](../patterns/sc/CAAP-SC-06.md) | A2A Discovery Poisoning | SC.F1 Server & Discovery Trust | candidate | 8.0 | scaffold |
| [CAAP-SC-07](../patterns/sc/CAAP-SC-07.md) | Trust-on-First-Use Exploitation | SC.F1 Server & Discovery Trust | candidate | 8.2 | scaffold |
| [CAAP-SC-08](../patterns/sc/CAAP-SC-08.md) | Signed-but-Malicious Component | SC.F2 Mutable Component Risk | catalog | 8.0 | scaffold |
| [CAAP-SC-09](../patterns/sc/CAAP-SC-09.md) | Malicious System Prompt Update | SC.F2 Mutable Component Risk | catalog | 8.8 | scaffold |
| [CAAP-SC-10](../patterns/sc/CAAP-SC-10.md) | Compromised Remote Policy | SC.F2 Mutable Component Risk | catalog | 8.2 | scaffold |
| [CAAP-SC-11](../patterns/sc/CAAP-SC-11.md) | Malicious Agent Card | SC.F3 Manifest & Identity Abuse | catalog | 8.0 | scaffold |
| [CAAP-SC-12](../patterns/sc/CAAP-SC-12.md) | Agent-Card Capability Forgery | SC.F3 Manifest & Identity Abuse | catalog | 7.2 | scaffold |
| [CAAP-SC-13](../patterns/sc/CAAP-SC-13.md) | Capability Manifest Downgrade | SC.F3 Manifest & Identity Abuse | catalog | 7.5 | scaffold |
| [CAAP-SC-14](../patterns/sc/CAAP-SC-14.md) | Namespace Takeover | SC.F3 Manifest & Identity Abuse | catalog | 8.5 | scaffold |
| [CAAP-SC-15](../patterns/sc/CAAP-SC-15.md) | Tool Dependency Substitution | SC.F4 Dependency & Artifact Substitution | catalog | 8.5 | scaffold |
| [CAAP-SC-16](../patterns/sc/CAAP-SC-16.md) | Prompt Dependency Poisoning | SC.F4 Dependency & Artifact Substitution | catalog | 8.5 | scaffold |
| [CAAP-SC-17](../patterns/sc/CAAP-SC-17.md) | Model Adapter Poisoning | SC.F4 Dependency & Artifact Substitution | catalog | 8.5 | scaffold |
| [CAAP-SC-18](../patterns/sc/CAAP-SC-18.md) | Fine-Tune Substitution | SC.F4 Dependency & Artifact Substitution | catalog | 8.2 | scaffold |
| [CAAP-SC-19](../patterns/sc/CAAP-SC-19.md) | Agent Container Substitution | SC.F4 Dependency & Artifact Substitution | catalog | 8.5 | scaffold |
| [CAAP-SC-20](../patterns/sc/CAAP-SC-20.md) | Dependency Confusion | SC.F4 Dependency & Artifact Substitution | catalog | 9.0 | scaffold |
| [CAAP-SC-21](../patterns/sc/CAAP-SC-21.md) | Registry Entry Shadow Revision | SC.F5 Registry and resolution | candidate | 7.0 | scaffold |
| [CAAP-SC-22](../patterns/sc/CAAP-SC-22.md) | Registry Trust Root Swap | SC.F5 Registry and resolution | candidate | 7.0 | scaffold |
| [CAAP-SC-23](../patterns/sc/CAAP-SC-23.md) | Package Provenance Gap | SC.F5 Registry and resolution | candidate | 7.0 | scaffold |
| [CAAP-SC-24](../patterns/sc/CAAP-SC-24.md) | Version Range Bait | SC.F5 Registry and resolution | candidate | 7.0 | scaffold |
| [CAAP-SC-25](../patterns/sc/CAAP-SC-25.md) | Artifact Digest Confusion | SC.F5 Registry and resolution | candidate | 7.0 | scaffold |
| [CAAP-SC-26](../patterns/sc/CAAP-SC-26.md) | Mirror Fallback Substitution | SC.F5 Registry and resolution | candidate | 7.0 | scaffold |
| [CAAP-SC-27](../patterns/sc/CAAP-SC-27.md) | Registry Namespace Homograph | SC.F5 Registry and resolution | candidate | 7.0 | scaffold |
| [CAAP-SC-28](../patterns/sc/CAAP-SC-28.md) | Mutable Prompt Policy Bundle | SC.F6 Lifecycle and updates | candidate | 7.0 | scaffold |
| [CAAP-SC-29](../patterns/sc/CAAP-SC-29.md) | Staged Update Promotion Abuse | SC.F6 Lifecycle and updates | candidate | 7.0 | scaffold |
| [CAAP-SC-30](../patterns/sc/CAAP-SC-30.md) | Rollback-to-Vulnerable Component | SC.F6 Lifecycle and updates | candidate | 7.0 | scaffold |
| [CAAP-SC-31](../patterns/sc/CAAP-SC-31.md) | Hot-Reload Window Injection | SC.F6 Lifecycle and updates | candidate | 7.0 | scaffold |
| [CAAP-SC-32](../patterns/sc/CAAP-SC-32.md) | Update Manifest Scope Expansion | SC.F6 Lifecycle and updates | candidate | 7.0 | scaffold |
| [CAAP-SC-33](../patterns/sc/CAAP-SC-33.md) | Canary Result Forgery | SC.F6 Lifecycle and updates | candidate | 7.0 | scaffold |
| [CAAP-SC-34](../patterns/sc/CAAP-SC-34.md) | Post-Approval Artifact Swap | SC.F6 Lifecycle and updates | candidate | 7.0 | scaffold |
| [CAAP-SC-35](../patterns/sc/CAAP-SC-35.md) | Transitive Tool Dependency Hijack | SC.F7 Transitive dependencies | candidate | 7.0 | scaffold |
| [CAAP-SC-36](../patterns/sc/CAAP-SC-36.md) | Build Provenance Chain Break | SC.F7 Transitive dependencies | candidate | 7.0 | scaffold |
| [CAAP-SC-37](../patterns/sc/CAAP-SC-37.md) | Model Weight Shard Substitution | SC.F7 Transitive dependencies | candidate | 7.0 | scaffold |
| [CAAP-SC-38](../patterns/sc/CAAP-SC-38.md) | Tokenizer Artifact Mismatch | SC.F7 Transitive dependencies | candidate | 7.0 | scaffold |
| [CAAP-SC-39](../patterns/sc/CAAP-SC-39.md) | Plugin Permission Manifest Split | SC.F7 Transitive dependencies | candidate | 7.0 | scaffold |
| [CAAP-SC-40](../patterns/sc/CAAP-SC-40.md) | Adapter Configuration Injection | SC.F7 Transitive dependencies | candidate | 7.0 | scaffold |
| [CAAP-SC-41](../patterns/sc/CAAP-SC-41.md) | Template Include Substitution | SC.F7 Transitive dependencies | candidate | 7.0 | scaffold |
| [CAAP-SC-42](../patterns/sc/CAAP-SC-42.md) | Signed Metadata Expiry Bypass | SC.F8 Trust and distribution | candidate | 7.0 | scaffold |
| [CAAP-SC-43](../patterns/sc/CAAP-SC-43.md) | Signature Key Rotation Confusion | SC.F8 Trust and distribution | candidate | 7.0 | scaffold |
| [CAAP-SC-44](../patterns/sc/CAAP-SC-44.md) | Component Identity Reassignment | SC.F8 Trust and distribution | candidate | 7.0 | scaffold |
| [CAAP-SC-45](../patterns/sc/CAAP-SC-45.md) | Distribution Channel Mixup | SC.F8 Trust and distribution | candidate | 7.0 | scaffold |
| [CAAP-SC-46](../patterns/sc/CAAP-SC-46.md) | Policy Bundle Dependency Cycle | SC.F8 Trust and distribution | candidate | 7.0 | scaffold |
| [CAAP-SC-47](../patterns/sc/CAAP-SC-47.md) | Tool Documentation Drift | SC.F8 Trust and distribution | candidate | 7.0 | scaffold |
| [CAAP-SC-48](../patterns/sc/CAAP-SC-48.md) | Remote Feature Flag Surprise | SC.F8 Trust and distribution | candidate | 7.0 | scaffold |

## CE - Unexpected Code Execution

Unintended execution of generated, retrieved, embedded, or tool-supplied code and containment failure.

Integrity layer: `adversarial`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-CE-01](../patterns/ce/CAAP-CE-01.md) | Model-to-Shell Command Injection | CE.F1 Interpreter Boundaries | reference | 9.4 | executable |
| [CAAP-CE-02](../patterns/ce/CAAP-CE-02.md) | Interpreter Boundary Confusion | CE.F1 Interpreter Boundaries | candidate | 8.8 | scaffold |
| [CAAP-CE-03](../patterns/ce/CAAP-CE-03.md) | Shell Quoting Failure | CE.F1 Interpreter Boundaries | candidate | 8.5 | scaffold |
| [CAAP-CE-04](../patterns/ce/CAAP-CE-04.md) | Environment-Variable Command Injection | CE.F1 Interpreter Boundaries | candidate | 8.2 | scaffold |
| [CAAP-CE-05](../patterns/ce/CAAP-CE-05.md) | Sandbox Escape and Host Reachability | CE.F4 Containment Failure | reference | 9.4 | executable |
| [CAAP-CE-06](../patterns/ce/CAAP-CE-06.md) | Generated Code Auto-Execution | CE.F2 Generated & Retrieved Code | catalog | 8.8 | scaffold |
| [CAAP-CE-07](../patterns/ce/CAAP-CE-07.md) | Code Execution Through Tool Output | CE.F2 Generated & Retrieved Code | catalog | 8.5 | scaffold |
| [CAAP-CE-08](../patterns/ce/CAAP-CE-08.md) | Notebook Execution Injection | CE.F2 Generated & Retrieved Code | catalog | 8.2 | scaffold |
| [CAAP-CE-09](../patterns/ce/CAAP-CE-09.md) | Template-to-Code Injection | CE.F2 Generated & Retrieved Code | catalog | 8.5 | scaffold |
| [CAAP-CE-10](../patterns/ce/CAAP-CE-10.md) | Unsafe Deserialization | CE.F3 Artifact & Dependency Execution | catalog | 8.2 | scaffold |
| [CAAP-CE-11](../patterns/ce/CAAP-CE-11.md) | Archive Extraction Abuse | CE.F3 Artifact & Dependency Execution | catalog | 8.5 | scaffold |
| [CAAP-CE-12](../patterns/ce/CAAP-CE-12.md) | Build-Script Injection | CE.F3 Artifact & Dependency Execution | catalog | 9.0 | scaffold |
| [CAAP-CE-13](../patterns/ce/CAAP-CE-13.md) | CI Command Injection | CE.F3 Artifact & Dependency Execution | catalog | 9.0 | scaffold |
| [CAAP-CE-14](../patterns/ce/CAAP-CE-14.md) | Dependency Installation Hijack | CE.F3 Artifact & Dependency Execution | catalog | 9.0 | scaffold |
| [CAAP-CE-15](../patterns/ce/CAAP-CE-15.md) | Unsafe Script Persistence | CE.F4 Containment Failure | catalog | 8.0 | scaffold |
| [CAAP-CE-16](../patterns/ce/CAAP-CE-16.md) | Markdown Fence Escape Execution | CE.F5 Code parsing boundaries | candidate | 6.8 | scaffold |
| [CAAP-CE-17](../patterns/ce/CAAP-CE-17.md) | REPL State Carryover | CE.F5 Code parsing boundaries | candidate | 6.8 | scaffold |
| [CAAP-CE-18](../patterns/ce/CAAP-CE-18.md) | Expression Evaluator Escape | CE.F5 Code parsing boundaries | candidate | 6.8 | scaffold |
| [CAAP-CE-19](../patterns/ce/CAAP-CE-19.md) | Configuration-as-Code Promotion | CE.F5 Code parsing boundaries | candidate | 6.8 | scaffold |
| [CAAP-CE-20](../patterns/ce/CAAP-CE-20.md) | Code Block Language Mislabel | CE.F5 Code parsing boundaries | candidate | 6.8 | scaffold |
| [CAAP-CE-21](../patterns/ce/CAAP-CE-21.md) | Function Name Injection | CE.F5 Code parsing boundaries | candidate | 6.8 | scaffold |
| [CAAP-CE-22](../patterns/ce/CAAP-CE-22.md) | Macro Expansion Surprise | CE.F5 Code parsing boundaries | candidate | 6.8 | scaffold |
| [CAAP-CE-23](../patterns/ce/CAAP-CE-23.md) | Temporary Script Path Swap | CE.F6 Files and runtimes | candidate | 6.8 | scaffold |
| [CAAP-CE-24](../patterns/ce/CAAP-CE-24.md) | Working Directory Hijack | CE.F6 Files and runtimes | candidate | 6.8 | scaffold |
| [CAAP-CE-25](../patterns/ce/CAAP-CE-25.md) | Startup Hook Execution | CE.F6 Files and runtimes | candidate | 6.8 | scaffold |
| [CAAP-CE-26](../patterns/ce/CAAP-CE-26.md) | Module Search Path Poisoning | CE.F6 Files and runtimes | candidate | 6.8 | scaffold |
| [CAAP-CE-27](../patterns/ce/CAAP-CE-27.md) | Notebook Metadata Execution | CE.F6 Files and runtimes | candidate | 6.8 | scaffold |
| [CAAP-CE-28](../patterns/ce/CAAP-CE-28.md) | Document Automation Trigger | CE.F6 Files and runtimes | candidate | 6.8 | scaffold |
| [CAAP-CE-29](../patterns/ce/CAAP-CE-29.md) | Generated Patch Hook Abuse | CE.F6 Files and runtimes | candidate | 6.8 | scaffold |
| [CAAP-CE-30](../patterns/ce/CAAP-CE-30.md) | Compiler Plugin Injection | CE.F7 Build and generation | candidate | 6.8 | scaffold |
| [CAAP-CE-31](../patterns/ce/CAAP-CE-31.md) | Test Discovery Execution | CE.F7 Build and generation | candidate | 6.8 | scaffold |
| [CAAP-CE-32](../patterns/ce/CAAP-CE-32.md) | Code Generator Template Escape | CE.F7 Build and generation | candidate | 6.8 | scaffold |
| [CAAP-CE-33](../patterns/ce/CAAP-CE-33.md) | Build Cache Artifact Poisoning | CE.F7 Build and generation | candidate | 6.8 | scaffold |
| [CAAP-CE-34](../patterns/ce/CAAP-CE-34.md) | Postinstall Script Reclassification | CE.F7 Build and generation | candidate | 6.8 | scaffold |
| [CAAP-CE-35](../patterns/ce/CAAP-CE-35.md) | Linter Plugin Auto-Load | CE.F7 Build and generation | candidate | 6.8 | scaffold |
| [CAAP-CE-36](../patterns/ce/CAAP-CE-36.md) | Formatter Configuration Execution | CE.F7 Build and generation | candidate | 6.8 | scaffold |
| [CAAP-CE-37](../patterns/ce/CAAP-CE-37.md) | Sandbox Mount Scope Expansion | CE.F8 Isolation and lifecycle | candidate | 6.8 | scaffold |
| [CAAP-CE-38](../patterns/ce/CAAP-CE-38.md) | Interpreter Network Toggle Drift | CE.F8 Isolation and lifecycle | candidate | 6.8 | scaffold |
| [CAAP-CE-39](../patterns/ce/CAAP-CE-39.md) | Ephemeral Environment Reuse | CE.F8 Isolation and lifecycle | candidate | 6.8 | scaffold |
| [CAAP-CE-40](../patterns/ce/CAAP-CE-40.md) | Execution Timeout Handler Injection | CE.F8 Isolation and lifecycle | candidate | 6.8 | scaffold |
| [CAAP-CE-41](../patterns/ce/CAAP-CE-41.md) | Process Substitution Surprise | CE.F8 Isolation and lifecycle | candidate | 6.8 | scaffold |
| [CAAP-CE-42](../patterns/ce/CAAP-CE-42.md) | Interpreter Output Re-Evaluation | CE.F8 Isolation and lifecycle | candidate | 6.8 | scaffold |
| [CAAP-CE-43](../patterns/ce/CAAP-CE-43.md) | Cleanup Hook Persistence | CE.F8 Isolation and lifecycle | candidate | 6.8 | scaffold |

## MP - Memory, RAG & Context Poisoning

Corruption of context, state, memory, retrieval corpora, indexes, summaries, or self-generated knowledge.

Integrity layer: `cortical`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-MP-01](../patterns/mp/CAAP-MP-01.md) | Persistent Memory Injection | MP.F1 Memory Write & Integrity | reference | 8.6 | executable |
| [CAAP-MP-02](../patterns/mp/CAAP-MP-02.md) | Sleeper Memory Trigger | MP.F2 Dormancy & Lifecycle | reference | 8.7 | executable |
| [CAAP-MP-03](../patterns/mp/CAAP-MP-03.md) | Memory Provenance Stripping | MP.F1 Memory Write & Integrity | candidate | 8.0 | scaffold |
| [CAAP-MP-04](../patterns/mp/CAAP-MP-04.md) | RAG Corpus and Index Poisoning | MP.F3 Retrieval Poisoning | reference | 8.6 | executable |
| [CAAP-MP-05](../patterns/mp/CAAP-MP-05.md) | Memory Trust Escalation | MP.F1 Memory Write & Integrity | candidate | 7.5 | scaffold |
| [CAAP-MP-06](../patterns/mp/CAAP-MP-06.md) | Memory Overwrite | MP.F1 Memory Write & Integrity | candidate | 7.8 | scaffold |
| [CAAP-MP-07](../patterns/mp/CAAP-MP-07.md) | Memory Namespace Confusion | MP.F1 Memory Write & Integrity | candidate | 7.2 | scaffold |
| [CAAP-MP-08](../patterns/mp/CAAP-MP-08.md) | Conditional Memory Activation | MP.F2 Dormancy & Lifecycle | candidate | 7.8 | scaffold |
| [CAAP-MP-09](../patterns/mp/CAAP-MP-09.md) | Poisoned Memory Resurrection | MP.F2 Dormancy & Lifecycle | catalog | 7.5 | scaffold |
| [CAAP-MP-10](../patterns/mp/CAAP-MP-10.md) | Memory Deletion Suppression | MP.F2 Dormancy & Lifecycle | catalog | 7.2 | scaffold |
| [CAAP-MP-11](../patterns/mp/CAAP-MP-11.md) | RAG Ranking Manipulation | MP.F3 Retrieval Poisoning | catalog | 8.0 | scaffold |
| [CAAP-MP-12](../patterns/mp/CAAP-MP-12.md) | RAG Duplicate Amplification | MP.F3 Retrieval Poisoning | catalog | 7.5 | scaffold |
| [CAAP-MP-13](../patterns/mp/CAAP-MP-13.md) | Retriever Query Manipulation | MP.F3 Retrieval Poisoning | catalog | 7.2 | scaffold |
| [CAAP-MP-14](../patterns/mp/CAAP-MP-14.md) | Metadata-Filter Bypass | MP.F3 Retrieval Poisoning | catalog | 8.0 | scaffold |
| [CAAP-MP-15](../patterns/mp/CAAP-MP-15.md) | Source Authority Spoofing | MP.F3 Retrieval Poisoning | catalog | 7.8 | scaffold |
| [CAAP-MP-16](../patterns/mp/CAAP-MP-16.md) | Summary Poisoning | MP.F4 Context & Isolation | catalog | 7.5 | scaffold |
| [CAAP-MP-17](../patterns/mp/CAAP-MP-17.md) | Context-Window Displacement | MP.F4 Context & Isolation | catalog | 6.8 | scaffold |
| [CAAP-MP-18](../patterns/mp/CAAP-MP-18.md) | Security-Context Eviction | MP.F4 Context & Isolation | catalog | 7.2 | scaffold |
| [CAAP-MP-19](../patterns/mp/CAAP-MP-19.md) | Cross-User Memory Bleed | MP.F4 Context & Isolation | catalog | 8.5 | scaffold |
| [CAAP-MP-20](../patterns/mp/CAAP-MP-20.md) | Cross-Tenant Memory Retrieval | MP.F4 Context & Isolation | catalog | 8.8 | scaffold |
| [CAAP-MP-21](../patterns/mp/CAAP-MP-21.md) | Self-Generated Evidence Reinforcement | MP.F4 Context & Isolation | catalog | 8.0 | scaffold |
| [CAAP-MP-22](../patterns/mp/CAAP-MP-22.md) | Memory Quota Eviction Abuse | MP.F5 Memory write scope | candidate | 6.8 | scaffold |
| [CAAP-MP-23](../patterns/mp/CAAP-MP-23.md) | Memory Write Authority Forgery | MP.F5 Memory write scope | candidate | 6.8 | scaffold |
| [CAAP-MP-24](../patterns/mp/CAAP-MP-24.md) | Memory Field Type Confusion | MP.F5 Memory write scope | candidate | 6.8 | scaffold |
| [CAAP-MP-25](../patterns/mp/CAAP-MP-25.md) | Memory Revision Rollback | MP.F5 Memory write scope | candidate | 6.8 | scaffold |
| [CAAP-MP-26](../patterns/mp/CAAP-MP-26.md) | Memory TTL Extension | MP.F5 Memory write scope | candidate | 6.8 | scaffold |
| [CAAP-MP-27](../patterns/mp/CAAP-MP-27.md) | Memory Merge Conflict Poisoning | MP.F5 Memory write scope | candidate | 6.8 | scaffold |
| [CAAP-MP-28](../patterns/mp/CAAP-MP-28.md) | Memory Write Acknowledgment Forgery | MP.F5 Memory write scope | candidate | 6.8 | scaffold |
| [CAAP-MP-29](../patterns/mp/CAAP-MP-29.md) | Retrieval Chunk Boundary Splicing | MP.F6 Retrieval boundaries | candidate | 6.8 | scaffold |
| [CAAP-MP-30](../patterns/mp/CAAP-MP-30.md) | Retrieval Citation Transposition | MP.F6 Retrieval boundaries | candidate | 6.8 | scaffold |
| [CAAP-MP-31](../patterns/mp/CAAP-MP-31.md) | Retrieval Freshness Forgery | MP.F6 Retrieval boundaries | candidate | 6.8 | scaffold |
| [CAAP-MP-32](../patterns/mp/CAAP-MP-32.md) | Retrieval Access-Label Loss | MP.F6 Retrieval boundaries | candidate | 6.8 | scaffold |
| [CAAP-MP-33](../patterns/mp/CAAP-MP-33.md) | Retrieval Embedding Alias | MP.F6 Retrieval boundaries | candidate | 6.8 | scaffold |
| [CAAP-MP-34](../patterns/mp/CAAP-MP-34.md) | Retrieval Reranker Instruction Capture | MP.F6 Retrieval boundaries | candidate | 6.8 | scaffold |
| [CAAP-MP-35](../patterns/mp/CAAP-MP-35.md) | Retrieval Result Set Truncation | MP.F6 Retrieval boundaries | candidate | 6.8 | scaffold |
| [CAAP-MP-36](../patterns/mp/CAAP-MP-36.md) | Summary Attribution Loss | MP.F7 Summaries and context | candidate | 6.8 | scaffold |
| [CAAP-MP-37](../patterns/mp/CAAP-MP-37.md) | Summary Negation Loss | MP.F7 Summaries and context | candidate | 6.8 | scaffold |
| [CAAP-MP-38](../patterns/mp/CAAP-MP-38.md) | Summary Temporal Collapse | MP.F7 Summaries and context | candidate | 6.8 | scaffold |
| [CAAP-MP-39](../patterns/mp/CAAP-MP-39.md) | Context Compression Priority Swap | MP.F7 Summaries and context | candidate | 6.8 | scaffold |
| [CAAP-MP-40](../patterns/mp/CAAP-MP-40.md) | Context Boundary Marker Loss | MP.F7 Summaries and context | candidate | 6.8 | scaffold |
| [CAAP-MP-41](../patterns/mp/CAAP-MP-41.md) | Context Retrieval Order Bias | MP.F7 Summaries and context | candidate | 6.8 | scaffold |
| [CAAP-MP-42](../patterns/mp/CAAP-MP-42.md) | Self-Reflection Memory Poisoning | MP.F7 Summaries and context | candidate | 6.8 | scaffold |
| [CAAP-MP-43](../patterns/mp/CAAP-MP-43.md) | Memory Repair Rollback Trap | MP.F8 State isolation and repair | candidate | 6.8 | scaffold |
| [CAAP-MP-44](../patterns/mp/CAAP-MP-44.md) | Memory Tombstone Omission | MP.F8 State isolation and repair | candidate | 6.8 | scaffold |
| [CAAP-MP-45](../patterns/mp/CAAP-MP-45.md) | Memory Cache Invalidation Gap | MP.F8 State isolation and repair | candidate | 6.8 | scaffold |
| [CAAP-MP-46](../patterns/mp/CAAP-MP-46.md) | Cross-Session Scratchpad Exposure | MP.F8 State isolation and repair | candidate | 6.8 | scaffold |
| [CAAP-MP-47](../patterns/mp/CAAP-MP-47.md) | Memory Consent Scope Drift | MP.F8 State isolation and repair | candidate | 6.8 | scaffold |
| [CAAP-MP-48](../patterns/mp/CAAP-MP-48.md) | Evidence-to-Memory Promotion | MP.F8 State isolation and repair | candidate | 6.8 | scaffold |
| [CAAP-MP-49](../patterns/mp/CAAP-MP-49.md) | Retrieval Feedback Loop Contamination | MP.F8 State isolation and repair | candidate | 6.8 | scaffold |

## IA - Insecure Inter-Agent Communication

Spoofing, tampering, replay, downgrade, routing manipulation, or ambiguity between agents and orchestrators.

Integrity layer: `governance`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-IA-01](../patterns/ia/CAAP-IA-01.md) | Agent Spoofing | IA.F1 Peer Identity & Authority | reference | 8.7 | executable |
| [CAAP-IA-02](../patterns/ia/CAAP-IA-02.md) | Coordinator Impersonation | IA.F1 Peer Identity & Authority | candidate | 8.5 | scaffold |
| [CAAP-IA-03](../patterns/ia/CAAP-IA-03.md) | Delegation Replay | IA.F2 Message Integrity & Freshness | reference | 7.6 | executable |
| [CAAP-IA-04](../patterns/ia/CAAP-IA-04.md) | Agent Endpoint Substitution | IA.F1 Peer Identity & Authority | candidate | 8.0 | scaffold |
| [CAAP-IA-05](../patterns/ia/CAAP-IA-05.md) | Authority Claim Injection | IA.F1 Peer Identity & Authority | candidate | 7.5 | scaffold |
| [CAAP-IA-06](../patterns/ia/CAAP-IA-06.md) | Message Tampering | IA.F2 Message Integrity & Freshness | candidate | 7.8 | scaffold |
| [CAAP-IA-07](../patterns/ia/CAAP-IA-07.md) | Message Reordering | IA.F2 Message Integrity & Freshness | catalog | 6.8 | scaffold |
| [CAAP-IA-08](../patterns/ia/CAAP-IA-08.md) | Message Truncation | IA.F2 Message Integrity & Freshness | catalog | 6.5 | scaffold |
| [CAAP-IA-09](../patterns/ia/CAAP-IA-09.md) | Routing Manipulation | IA.F3 Routing & Protocol | catalog | 7.2 | scaffold |
| [CAAP-IA-10](../patterns/ia/CAAP-IA-10.md) | Protocol Downgrade | IA.F3 Routing & Protocol | catalog | 7.0 | scaffold |
| [CAAP-IA-11](../patterns/ia/CAAP-IA-11.md) | Schema Downgrade | IA.F3 Routing & Protocol | catalog | 7.0 | scaffold |
| [CAAP-IA-12](../patterns/ia/CAAP-IA-12.md) | A2A Destination Confusion | IA.F3 Routing & Protocol | catalog | 6.8 | scaffold |
| [CAAP-IA-13](../patterns/ia/CAAP-IA-13.md) | Capability Negotiation Manipulation | IA.F4 Semantic & Negotiation Abuse | catalog | 7.2 | scaffold |
| [CAAP-IA-14](../patterns/ia/CAAP-IA-14.md) | Semantic Ambiguity | IA.F4 Semantic & Negotiation Abuse | catalog | 6.5 | scaffold |
| [CAAP-IA-15](../patterns/ia/CAAP-IA-15.md) | Cross-Agent Instruction Injection | IA.F4 Semantic & Negotiation Abuse | catalog | 8.0 | scaffold |
| [CAAP-IA-16](../patterns/ia/CAAP-IA-16.md) | Broadcast Poisoning | IA.F5 Collective Trust Attacks | catalog | 8.2 | scaffold |
| [CAAP-IA-17](../patterns/ia/CAAP-IA-17.md) | Consensus Manipulation | IA.F5 Collective Trust Attacks | catalog | 7.8 | scaffold |
| [CAAP-IA-18](../patterns/ia/CAAP-IA-18.md) | Peer Reputation Manipulation | IA.F5 Collective Trust Attacks | catalog | 7.5 | scaffold |
| [CAAP-IA-19](../patterns/ia/CAAP-IA-19.md) | Cross-Agent Confidential-Data Leakage | IA.F5 Collective Trust Attacks | catalog | 8.0 | scaffold |
| [CAAP-IA-20](../patterns/ia/CAAP-IA-20.md) | Peer Certificate Name Mismatch | IA.F6 Peer identity and trust | candidate | 6.8 | scaffold |
| [CAAP-IA-21](../patterns/ia/CAAP-IA-21.md) | Peer Identity Rotation Gap | IA.F6 Peer identity and trust | candidate | 6.8 | scaffold |
| [CAAP-IA-22](../patterns/ia/CAAP-IA-22.md) | Peer Delegation Proof Omission | IA.F6 Peer identity and trust | candidate | 6.8 | scaffold |
| [CAAP-IA-23](../patterns/ia/CAAP-IA-23.md) | Peer Role Escalation | IA.F6 Peer identity and trust | candidate | 6.8 | scaffold |
| [CAAP-IA-24](../patterns/ia/CAAP-IA-24.md) | Peer Capability Assertion Drift | IA.F6 Peer identity and trust | candidate | 6.8 | scaffold |
| [CAAP-IA-25](../patterns/ia/CAAP-IA-25.md) | Peer Trust-Level Transposition | IA.F6 Peer identity and trust | candidate | 6.8 | scaffold |
| [CAAP-IA-26](../patterns/ia/CAAP-IA-26.md) | Peer Revocation Propagation Delay | IA.F6 Peer identity and trust | candidate | 6.8 | scaffold |
| [CAAP-IA-27](../patterns/ia/CAAP-IA-27.md) | Message Correlation ID Collision | IA.F7 Message semantics and delivery | candidate | 6.8 | scaffold |
| [CAAP-IA-28](../patterns/ia/CAAP-IA-28.md) | Message Nonce Scope Confusion | IA.F7 Message semantics and delivery | candidate | 6.8 | scaffold |
| [CAAP-IA-29](../patterns/ia/CAAP-IA-29.md) | Message Expiry Omission | IA.F7 Message semantics and delivery | candidate | 6.8 | scaffold |
| [CAAP-IA-30](../patterns/ia/CAAP-IA-30.md) | Message Ack Forgery | IA.F7 Message semantics and delivery | candidate | 6.8 | scaffold |
| [CAAP-IA-31](../patterns/ia/CAAP-IA-31.md) | Message Delivery Duplication | IA.F7 Message semantics and delivery | candidate | 6.8 | scaffold |
| [CAAP-IA-32](../patterns/ia/CAAP-IA-32.md) | Message Fragment Splicing | IA.F7 Message semantics and delivery | candidate | 6.8 | scaffold |
| [CAAP-IA-33](../patterns/ia/CAAP-IA-33.md) | Message Signature Coverage Gap | IA.F7 Message semantics and delivery | candidate | 6.8 | scaffold |
| [CAAP-IA-34](../patterns/ia/CAAP-IA-34.md) | Route Policy Bypass via Relay | IA.F8 Routing and protocol transitions | candidate | 6.8 | scaffold |
| [CAAP-IA-35](../patterns/ia/CAAP-IA-35.md) | Federation Boundary Confusion | IA.F8 Routing and protocol transitions | candidate | 6.8 | scaffold |
| [CAAP-IA-36](../patterns/ia/CAAP-IA-36.md) | Protocol Extension Ambiguity | IA.F8 Routing and protocol transitions | candidate | 6.8 | scaffold |
| [CAAP-IA-37](../patterns/ia/CAAP-IA-37.md) | Protocol Version Pin Loss | IA.F8 Routing and protocol transitions | candidate | 6.8 | scaffold |
| [CAAP-IA-38](../patterns/ia/CAAP-IA-38.md) | Agent Handoff State Forgery | IA.F8 Routing and protocol transitions | candidate | 6.8 | scaffold |
| [CAAP-IA-39](../patterns/ia/CAAP-IA-39.md) | Agent Reply Recipient Swap | IA.F8 Routing and protocol transitions | candidate | 6.8 | scaffold |
| [CAAP-IA-40](../patterns/ia/CAAP-IA-40.md) | Dead-Letter Queue Reentry | IA.F8 Routing and protocol transitions | candidate | 6.8 | scaffold |
| [CAAP-IA-41](../patterns/ia/CAAP-IA-41.md) | Quorum Membership Inflation | IA.F9 Collective coordination | candidate | 6.8 | scaffold |
| [CAAP-IA-42](../patterns/ia/CAAP-IA-42.md) | Vote Identity Reuse | IA.F9 Collective coordination | candidate | 6.8 | scaffold |
| [CAAP-IA-43](../patterns/ia/CAAP-IA-43.md) | Proposal Version Split | IA.F9 Collective coordination | candidate | 6.8 | scaffold |
| [CAAP-IA-44](../patterns/ia/CAAP-IA-44.md) | Peer Evidence Citation Forgery | IA.F9 Collective coordination | candidate | 6.8 | scaffold |
| [CAAP-IA-45](../patterns/ia/CAAP-IA-45.md) | Collective Timeout Default Abuse | IA.F9 Collective coordination | candidate | 6.8 | scaffold |
| [CAAP-IA-46](../patterns/ia/CAAP-IA-46.md) | Coordinator Lease Expiry Gap | IA.F9 Collective coordination | candidate | 6.8 | scaffold |

## CF - Cascading & Systemic Failures

Failures that propagate across agents, tasks, tools, queues, environments, users, or tenants.

Integrity layer: `recovery`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-CF-01](../patterns/cf/CAAP-CF-01.md) | Planner-to-Executor Cascade | CF.F1 Plan & State Propagation | reference | 9.2 | executable |
| [CAAP-CF-02](../patterns/cf/CAAP-CF-02.md) | Shared-State Contamination | CF.F1 Plan & State Propagation | candidate | 8.5 | scaffold |
| [CAAP-CF-03](../patterns/cf/CAAP-CF-03.md) | Cascading Policy Bypass | CF.F1 Plan & State Propagation | candidate | 8.2 | scaffold |
| [CAAP-CF-04](../patterns/cf/CAAP-CF-04.md) | Fleet-Wide Memory Propagation | CF.F1 Plan & State Propagation | candidate | 8.8 | scaffold |
| [CAAP-CF-05](../patterns/cf/CAAP-CF-05.md) | Multi-Agent Retry Storm | CF.F2 Load & Queue Amplification | catalog | 7.5 | scaffold |
| [CAAP-CF-06](../patterns/cf/CAAP-CF-06.md) | Queue Amplification | CF.F2 Load & Queue Amplification | catalog | 7.8 | scaffold |
| [CAAP-CF-07](../patterns/cf/CAAP-CF-07.md) | Resource Starvation Cascade | CF.F2 Load & Queue Amplification | catalog | 7.2 | scaffold |
| [CAAP-CF-08](../patterns/cf/CAAP-CF-08.md) | Planner Cascade | CF.F3 Remediation & Rollback Cascades | catalog | 7.2 | scaffold |
| [CAAP-CF-09](../patterns/cf/CAAP-CF-09.md) | Remediation Cascade | CF.F3 Remediation & Rollback Cascades | catalog | 8.2 | scaffold |
| [CAAP-CF-10](../patterns/cf/CAAP-CF-10.md) | Incorrect Rollback Cascade | CF.F3 Remediation & Rollback Cascades | catalog | 8.0 | scaffold |
| [CAAP-CF-11](../patterns/cf/CAAP-CF-11.md) | Autonomous Remediation Loop | CF.F3 Remediation & Rollback Cascades | catalog | 7.8 | scaffold |
| [CAAP-CF-12](../patterns/cf/CAAP-CF-12.md) | Cross-Environment Propagation | CF.F4 Fleet & Environment Spread | catalog | 8.5 | scaffold |
| [CAAP-CF-13](../patterns/cf/CAAP-CF-13.md) | Shared-Secret Compromise Cascade | CF.F4 Fleet & Environment Spread | catalog | 8.5 | scaffold |
| [CAAP-CF-14](../patterns/cf/CAAP-CF-14.md) | Consensus Failure Amplification | CF.F4 Fleet & Environment Spread | catalog | 7.5 | scaffold |
| [CAAP-CF-15](../patterns/cf/CAAP-CF-15.md) | False-Positive Suppression Cascade | CF.F4 Fleet & Environment Spread | catalog | 8.2 | scaffold |
| [CAAP-CF-16](../patterns/cf/CAAP-CF-16.md) | Fleet Configuration Drift | CF.F4 Fleet & Environment Spread | catalog | 7.8 | scaffold |
| [CAAP-CF-17](../patterns/cf/CAAP-CF-17.md) | Fan-Out Limit Reset | CF.F5 Propagation topology | candidate | 7.2 | scaffold |
| [CAAP-CF-18](../patterns/cf/CAAP-CF-18.md) | Task Graph Cycle Injection | CF.F5 Propagation topology | candidate | 7.2 | scaffold |
| [CAAP-CF-19](../patterns/cf/CAAP-CF-19.md) | Shared Artifact Broadcast Drift | CF.F5 Propagation topology | candidate | 7.2 | scaffold |
| [CAAP-CF-20](../patterns/cf/CAAP-CF-20.md) | Partial Rollout Contamination | CF.F5 Propagation topology | candidate | 7.2 | scaffold |
| [CAAP-CF-21](../patterns/cf/CAAP-CF-21.md) | Cross-Queue Priority Cascade | CF.F5 Propagation topology | candidate | 7.2 | scaffold |
| [CAAP-CF-22](../patterns/cf/CAAP-CF-22.md) | Result Aggregation Poisoning | CF.F5 Propagation topology | candidate | 7.2 | scaffold |
| [CAAP-CF-23](../patterns/cf/CAAP-CF-23.md) | Downstream Retry Budget Loss | CF.F5 Propagation topology | candidate | 7.2 | scaffold |
| [CAAP-CF-24](../patterns/cf/CAAP-CF-24.md) | Shared Cache Scope Contamination | CF.F6 State and decision cascades | candidate | 7.2 | scaffold |
| [CAAP-CF-25](../patterns/cf/CAAP-CF-25.md) | Plan Version Skew Cascade | CF.F6 State and decision cascades | candidate | 7.2 | scaffold |
| [CAAP-CF-26](../patterns/cf/CAAP-CF-26.md) | Checkpoint State Divergence | CF.F6 State and decision cascades | candidate | 7.2 | scaffold |
| [CAAP-CF-27](../patterns/cf/CAAP-CF-27.md) | Approval Propagation Inflation | CF.F6 State and decision cascades | candidate | 7.2 | scaffold |
| [CAAP-CF-28](../patterns/cf/CAAP-CF-28.md) | Error Classification Cascade | CF.F6 State and decision cascades | candidate | 7.2 | scaffold |
| [CAAP-CF-29](../patterns/cf/CAAP-CF-29.md) | Telemetry Sampling Blind Spot | CF.F6 State and decision cascades | candidate | 7.2 | scaffold |
| [CAAP-CF-30](../patterns/cf/CAAP-CF-30.md) | Consensus Input Contamination | CF.F6 State and decision cascades | candidate | 7.2 | scaffold |
| [CAAP-CF-31](../patterns/cf/CAAP-CF-31.md) | Rollback Scope Expansion | CF.F7 Recovery and control | candidate | 7.2 | scaffold |
| [CAAP-CF-32](../patterns/cf/CAAP-CF-32.md) | Recovery Order Inversion | CF.F7 Recovery and control | candidate | 7.2 | scaffold |
| [CAAP-CF-33](../patterns/cf/CAAP-CF-33.md) | Circuit Breaker Bypass Propagation | CF.F7 Recovery and control | candidate | 7.2 | scaffold |
| [CAAP-CF-34](../patterns/cf/CAAP-CF-34.md) | Compensation Retry Cascade | CF.F7 Recovery and control | candidate | 7.2 | scaffold |
| [CAAP-CF-35](../patterns/cf/CAAP-CF-35.md) | Health Signal Dependency Loop | CF.F7 Recovery and control | candidate | 7.2 | scaffold |
| [CAAP-CF-36](../patterns/cf/CAAP-CF-36.md) | Quarantine Boundary Leak | CF.F7 Recovery and control | candidate | 7.2 | scaffold |
| [CAAP-CF-37](../patterns/cf/CAAP-CF-37.md) | Remediation Ownership Confusion | CF.F7 Recovery and control | candidate | 7.2 | scaffold |
| [CAAP-CF-38](../patterns/cf/CAAP-CF-38.md) | Environment Label Stripping | CF.F8 Cross-boundary effects | candidate | 7.2 | scaffold |
| [CAAP-CF-39](../patterns/cf/CAAP-CF-39.md) | Budget Pool Cross-Tenant Drain | CF.F8 Cross-boundary effects | candidate | 7.2 | scaffold |
| [CAAP-CF-40](../patterns/cf/CAAP-CF-40.md) | Shared Model Cache Poisoning | CF.F8 Cross-boundary effects | candidate | 7.2 | scaffold |
| [CAAP-CF-41](../patterns/cf/CAAP-CF-41.md) | Fleet Policy Update Race | CF.F8 Cross-boundary effects | candidate | 7.2 | scaffold |
| [CAAP-CF-42](../patterns/cf/CAAP-CF-42.md) | Incident Closure Prematurity | CF.F8 Cross-boundary effects | candidate | 7.2 | scaffold |
| [CAAP-CF-43](../patterns/cf/CAAP-CF-43.md) | Evidence Aggregation Dedup Error | CF.F8 Cross-boundary effects | candidate | 7.2 | scaffold |

## HT - Human-Agent Trust Exploitation

Manipulation of human oversight through misleading authority, explanations, approvals, consent, or risk suppression.

Integrity layer: `governance`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-HT-01](../patterns/ht/CAAP-HT-01.md) | Authority Laundering | HT.F1 Authority & Evidence Manipulation | candidate | 7.0 | scaffold |
| [CAAP-HT-02](../patterns/ht/CAAP-HT-02.md) | Fabricated Certainty | HT.F1 Authority & Evidence Manipulation | candidate | 6.8 | scaffold |
| [CAAP-HT-03](../patterns/ht/CAAP-HT-03.md) | Fabricated Explainability | HT.F1 Authority & Evidence Manipulation | catalog | 7.0 | scaffold |
| [CAAP-HT-04](../patterns/ht/CAAP-HT-04.md) | Consent Laundering | HT.F2 Consent & Approval Abuse | reference | 7.8 | executable |
| [CAAP-HT-05](../patterns/ht/CAAP-HT-05.md) | False Policy Citation | HT.F1 Authority & Evidence Manipulation | catalog | 7.0 | scaffold |
| [CAAP-HT-06](../patterns/ht/CAAP-HT-06.md) | Reviewer Impersonation | HT.F1 Authority & Evidence Manipulation | catalog | 7.5 | scaffold |
| [CAAP-HT-07](../patterns/ht/CAAP-HT-07.md) | Approval Fatigue | HT.F2 Consent & Approval Abuse | catalog | 7.2 | scaffold |
| [CAAP-HT-08](../patterns/ht/CAAP-HT-08.md) | Consent Ambiguity | HT.F2 Consent & Approval Abuse | catalog | 7.0 | scaffold |
| [CAAP-HT-09](../patterns/ht/CAAP-HT-09.md) | Human Confirmation Spoofing | HT.F2 Consent & Approval Abuse | catalog | 8.2 | scaffold |
| [CAAP-HT-10](../patterns/ht/CAAP-HT-10.md) | Escalation Fatigue | HT.F2 Consent & Approval Abuse | catalog | 6.5 | scaffold |
| [CAAP-HT-11](../patterns/ht/CAAP-HT-11.md) | Hidden Side-Effect Disclosure | HT.F3 Risk & Choice Manipulation | catalog | 7.2 | scaffold |
| [CAAP-HT-12](../patterns/ht/CAAP-HT-12.md) | Risk Disclosure Suppression | HT.F3 Risk & Choice Manipulation | catalog | 7.0 | scaffold |
| [CAAP-HT-13](../patterns/ht/CAAP-HT-13.md) | Misleading Action Preview | HT.F3 Risk & Choice Manipulation | catalog | 7.2 | scaffold |
| [CAAP-HT-14](../patterns/ht/CAAP-HT-14.md) | Urgency Manipulation | HT.F3 Risk & Choice Manipulation | catalog | 6.5 | scaffold |
| [CAAP-HT-15](../patterns/ht/CAAP-HT-15.md) | Recommendation Anchoring | HT.F3 Risk & Choice Manipulation | catalog | 6.2 | scaffold |
| [CAAP-HT-16](../patterns/ht/CAAP-HT-16.md) | Approval Object Substitution | HT.F4 Approval presentation | candidate | 6.0 | scaffold |
| [CAAP-HT-17](../patterns/ht/CAAP-HT-17.md) | Approval Diff Omission | HT.F4 Approval presentation | candidate | 6.0 | scaffold |
| [CAAP-HT-18](../patterns/ht/CAAP-HT-18.md) | Approval Default Selection Bias | HT.F4 Approval presentation | candidate | 6.0 | scaffold |
| [CAAP-HT-19](../patterns/ht/CAAP-HT-19.md) | Approval Deadline Pretext | HT.F4 Approval presentation | candidate | 6.0 | scaffold |
| [CAAP-HT-20](../patterns/ht/CAAP-HT-20.md) | Approval Granularity Collapse | HT.F4 Approval presentation | candidate | 6.0 | scaffold |
| [CAAP-HT-21](../patterns/ht/CAAP-HT-21.md) | Approval Revocation Concealment | HT.F4 Approval presentation | candidate | 6.0 | scaffold |
| [CAAP-HT-22](../patterns/ht/CAAP-HT-22.md) | Approval Evidence Reordering | HT.F4 Approval presentation | candidate | 6.0 | scaffold |
| [CAAP-HT-23](../patterns/ht/CAAP-HT-23.md) | Evidence Confidence Inflation | HT.F5 Explanation and evidence | candidate | 6.0 | scaffold |
| [CAAP-HT-24](../patterns/ht/CAAP-HT-24.md) | Source Citation Mismatch | HT.F5 Explanation and evidence | candidate | 6.0 | scaffold |
| [CAAP-HT-25](../patterns/ht/CAAP-HT-25.md) | Omitted Counterevidence | HT.F5 Explanation and evidence | candidate | 6.0 | scaffold |
| [CAAP-HT-26](../patterns/ht/CAAP-HT-26.md) | Synthetic Evidence Passing | HT.F5 Explanation and evidence | candidate | 6.0 | scaffold |
| [CAAP-HT-27](../patterns/ht/CAAP-HT-27.md) | Provenance Badge Forgery | HT.F5 Explanation and evidence | candidate | 6.0 | scaffold |
| [CAAP-HT-28](../patterns/ht/CAAP-HT-28.md) | Explanation Scope Mismatch | HT.F5 Explanation and evidence | candidate | 6.0 | scaffold |
| [CAAP-HT-29](../patterns/ht/CAAP-HT-29.md) | Uncertainty Suppression | HT.F5 Explanation and evidence | candidate | 6.0 | scaffold |
| [CAAP-HT-30](../patterns/ht/CAAP-HT-30.md) | Escalation Recipient Swap | HT.F6 Human workflow | candidate | 6.0 | scaffold |
| [CAAP-HT-31](../patterns/ht/CAAP-HT-31.md) | Reviewer Context Fragmentation | HT.F6 Human workflow | candidate | 6.0 | scaffold |
| [CAAP-HT-32](../patterns/ht/CAAP-HT-32.md) | Review Queue Saturation | HT.F6 Human workflow | candidate | 6.0 | scaffold |
| [CAAP-HT-33](../patterns/ht/CAAP-HT-33.md) | Decision Record Misattribution | HT.F6 Human workflow | candidate | 6.0 | scaffold |
| [CAAP-HT-34](../patterns/ht/CAAP-HT-34.md) | Manual Override Pretext | HT.F6 Human workflow | candidate | 6.0 | scaffold |
| [CAAP-HT-35](../patterns/ht/CAAP-HT-35.md) | Review Window Truncation | HT.F6 Human workflow | candidate | 6.0 | scaffold |
| [CAAP-HT-36](../patterns/ht/CAAP-HT-36.md) | Second-Person Approval Confusion | HT.F6 Human workflow | candidate | 6.0 | scaffold |
| [CAAP-HT-37](../patterns/ht/CAAP-HT-37.md) | Risk Baseline Manipulation | HT.F7 Risk communication | candidate | 6.0 | scaffold |
| [CAAP-HT-38](../patterns/ht/CAAP-HT-38.md) | Safe-Mode Label Misuse | HT.F7 Risk communication | candidate | 6.0 | scaffold |
| [CAAP-HT-39](../patterns/ht/CAAP-HT-39.md) | Outcome Certainty Forgery | HT.F7 Risk communication | candidate | 6.0 | scaffold |
| [CAAP-HT-40](../patterns/ht/CAAP-HT-40.md) | Privacy Scope Concealment | HT.F7 Risk communication | candidate | 6.0 | scaffold |
| [CAAP-HT-41](../patterns/ht/CAAP-HT-41.md) | Rollback Assurance Forgery | HT.F7 Risk communication | candidate | 6.0 | scaffold |
| [CAAP-HT-42](../patterns/ht/CAAP-HT-42.md) | Impact Audience Omission | HT.F7 Risk communication | candidate | 6.0 | scaffold |

## RA - Rogue & Emergent Agent Behavior

Unsafe autonomous behavior through goal drift, reward exploitation, collusion, replication, shutdown resistance, or evidence manipulation.

Integrity layer: `cortical`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-RA-01](../patterns/ra/CAAP-RA-01.md) | Goal Drift | RA.F1 Goal & Reward Deviation | candidate | 7.2 | scaffold |
| [CAAP-RA-02](../patterns/ra/CAAP-RA-02.md) | Covert Goal Substitution | RA.F1 Goal & Reward Deviation | candidate | 7.8 | scaffold |
| [CAAP-RA-03](../patterns/ra/CAAP-RA-03.md) | Reward Hacking | RA.F1 Goal & Reward Deviation | catalog | 7.2 | scaffold |
| [CAAP-RA-04](../patterns/ra/CAAP-RA-04.md) | Specification Gaming | RA.F1 Goal & Reward Deviation | catalog | 7.5 | scaffold |
| [CAAP-RA-05](../patterns/ra/CAAP-RA-05.md) | Kill-Switch and Revocation Evasion | RA.F2 Persistence & Replication | reference | 9.2 | executable |
| [CAAP-RA-06](../patterns/ra/CAAP-RA-06.md) | Unauthorized Self-Replication | RA.F2 Persistence & Replication | catalog | 8.5 | scaffold |
| [CAAP-RA-07](../patterns/ra/CAAP-RA-07.md) | Child-Agent Spawning | RA.F2 Persistence & Replication | catalog | 8.0 | scaffold |
| [CAAP-RA-08](../patterns/ra/CAAP-RA-08.md) | Persistent Task Creation | RA.F2 Persistence & Replication | catalog | 8.0 | scaffold |
| [CAAP-RA-09](../patterns/ra/CAAP-RA-09.md) | Shutdown Avoidance | RA.F2 Persistence & Replication | catalog | 8.2 | scaffold |
| [CAAP-RA-10](../patterns/ra/CAAP-RA-10.md) | Evidence Suppression | RA.F3 Evidence & Communication Evasion | catalog | 8.0 | scaffold |
| [CAAP-RA-11](../patterns/ra/CAAP-RA-11.md) | Log Tampering | RA.F3 Evidence & Communication Evasion | catalog | 7.8 | scaffold |
| [CAAP-RA-12](../patterns/ra/CAAP-RA-12.md) | Hidden Agent Communication | RA.F3 Evidence & Communication Evasion | catalog | 8.0 | scaffold |
| [CAAP-RA-13](../patterns/ra/CAAP-RA-13.md) | Agent Collusion | RA.F4 Collective & Capability Seeking | catalog | 7.8 | scaffold |
| [CAAP-RA-14](../patterns/ra/CAAP-RA-14.md) | Out-of-Scope Resource Acquisition | RA.F4 Collective & Capability Seeking | catalog | 8.0 | scaffold |
| [CAAP-RA-15](../patterns/ra/CAAP-RA-15.md) | Unapproved Capability Acquisition | RA.F4 Collective & Capability Seeking | catalog | 8.5 | scaffold |
| [CAAP-RA-16](../patterns/ra/CAAP-RA-16.md) | Autonomous Privilege Seeking | RA.F4 Collective & Capability Seeking | catalog | 8.0 | scaffold |
| [CAAP-RA-17](../patterns/ra/CAAP-RA-17.md) | Autonomy Budget Self-Extension | RA.F5 Autonomy and objective control | candidate | 7.5 | scaffold |
| [CAAP-RA-18](../patterns/ra/CAAP-RA-18.md) | Goal Metric Substitution | RA.F5 Autonomy and objective control | candidate | 7.5 | scaffold |
| [CAAP-RA-19](../patterns/ra/CAAP-RA-19.md) | Constraint Reinterpretation Drift | RA.F5 Autonomy and objective control | candidate | 7.5 | scaffold |
| [CAAP-RA-20](../patterns/ra/CAAP-RA-20.md) | Self-Assigned Priority Escalation | RA.F5 Autonomy and objective control | candidate | 7.5 | scaffold |
| [CAAP-RA-21](../patterns/ra/CAAP-RA-21.md) | Action Horizon Expansion | RA.F5 Autonomy and objective control | candidate | 7.5 | scaffold |
| [CAAP-RA-22](../patterns/ra/CAAP-RA-22.md) | Delegation as Control Evasion | RA.F5 Autonomy and objective control | candidate | 7.5 | scaffold |
| [CAAP-RA-23](../patterns/ra/CAAP-RA-23.md) | Self-Approval Loop | RA.F5 Autonomy and objective control | candidate | 7.5 | scaffold |
| [CAAP-RA-24](../patterns/ra/CAAP-RA-24.md) | Shutdown Checkpoint Hijack | RA.F6 Persistence and continuity | candidate | 7.5 | scaffold |
| [CAAP-RA-25](../patterns/ra/CAAP-RA-25.md) | Task Lease Self-Renewal | RA.F6 Persistence and continuity | candidate | 7.5 | scaffold |
| [CAAP-RA-26](../patterns/ra/CAAP-RA-26.md) | Unauthorized Watcher Creation | RA.F6 Persistence and continuity | candidate | 7.5 | scaffold |
| [CAAP-RA-27](../patterns/ra/CAAP-RA-27.md) | State Snapshot Concealment | RA.F6 Persistence and continuity | candidate | 7.5 | scaffold |
| [CAAP-RA-28](../patterns/ra/CAAP-RA-28.md) | Child Task Orphaning | RA.F6 Persistence and continuity | candidate | 7.5 | scaffold |
| [CAAP-RA-29](../patterns/ra/CAAP-RA-29.md) | Control Channel Diversion | RA.F6 Persistence and continuity | candidate | 7.5 | scaffold |
| [CAAP-RA-30](../patterns/ra/CAAP-RA-30.md) | Recovery Script Entrenchment | RA.F6 Persistence and continuity | candidate | 7.5 | scaffold |
| [CAAP-RA-31](../patterns/ra/CAAP-RA-31.md) | Quota Fragmentation | RA.F7 Resource seeking and policy | candidate | 7.5 | scaffold |
| [CAAP-RA-32](../patterns/ra/CAAP-RA-32.md) | Capability Rental Pretext | RA.F7 Resource seeking and policy | candidate | 7.5 | scaffold |
| [CAAP-RA-33](../patterns/ra/CAAP-RA-33.md) | Policy File Self-Modification | RA.F7 Resource seeking and policy | candidate | 7.5 | scaffold |
| [CAAP-RA-34](../patterns/ra/CAAP-RA-34.md) | Audit Sampling Manipulation | RA.F7 Resource seeking and policy | candidate | 7.5 | scaffold |
| [CAAP-RA-35](../patterns/ra/CAAP-RA-35.md) | Reward Signal Timing Abuse | RA.F7 Resource seeking and policy | candidate | 7.5 | scaffold |
| [CAAP-RA-36](../patterns/ra/CAAP-RA-36.md) | Evaluator Input Shaping | RA.F7 Resource seeking and policy | candidate | 7.5 | scaffold |
| [CAAP-RA-37](../patterns/ra/CAAP-RA-37.md) | Unapproved Tool Discovery Loop | RA.F7 Resource seeking and policy | candidate | 7.5 | scaffold |
| [CAAP-RA-38](../patterns/ra/CAAP-RA-38.md) | Agent Coalition Quota Sharing | RA.F8 Collective autonomy | candidate | 7.5 | scaffold |
| [CAAP-RA-39](../patterns/ra/CAAP-RA-39.md) | Mutual Evidence Laundering | RA.F8 Collective autonomy | candidate | 7.5 | scaffold |
| [CAAP-RA-40](../patterns/ra/CAAP-RA-40.md) | Collective Goal Drift | RA.F8 Collective autonomy | candidate | 7.5 | scaffold |
| [CAAP-RA-41](../patterns/ra/CAAP-RA-41.md) | Distributed Stop Avoidance | RA.F8 Collective autonomy | candidate | 7.5 | scaffold |
| [CAAP-RA-42](../patterns/ra/CAAP-RA-42.md) | Peer Monitoring Suppression | RA.F8 Collective autonomy | candidate | 7.5 | scaffold |
| [CAAP-RA-43](../patterns/ra/CAAP-RA-43.md) | Coordinator Capture by Workers | RA.F8 Collective autonomy | candidate | 7.5 | scaffold |

## EA - Embodied & Physical-Agent Attacks

Attacks on agents that perceive and act in physical or simulated environments.

Integrity layer: `adversarial`

| ID | Pattern | Family | Maturity | Severity | Test |
|---|---|---|---|---:|---|
| [CAAP-EA-01](../patterns/ea/CAAP-EA-01.md) | Sensor Injection | EA.F1 Perception & Sensor Manipulation | candidate | 7.2 | scaffold |
| [CAAP-EA-02](../patterns/ea/CAAP-EA-02.md) | Perception Poisoning | EA.F1 Perception & Sensor Manipulation | candidate | 7.8 | scaffold |
| [CAAP-EA-03](../patterns/ea/CAAP-EA-03.md) | Actuator Command Manipulation | EA.F3 Actuation & Safety | reference | 9.0 | executable |
| [CAAP-EA-04](../patterns/ea/CAAP-EA-04.md) | Audio Command Injection | EA.F1 Perception & Sensor Manipulation | catalog | 7.8 | scaffold |
| [CAAP-EA-05](../patterns/ea/CAAP-EA-05.md) | Visual Instruction Injection | EA.F1 Perception & Sensor Manipulation | catalog | 7.8 | scaffold |
| [CAAP-EA-06](../patterns/ea/CAAP-EA-06.md) | Map Poisoning | EA.F2 World Model & Navigation | catalog | 8.0 | scaffold |
| [CAAP-EA-07](../patterns/ea/CAAP-EA-07.md) | World-Model Poisoning | EA.F2 World Model & Navigation | catalog | 7.8 | scaffold |
| [CAAP-EA-08](../patterns/ea/CAAP-EA-08.md) | Navigation Manipulation | EA.F2 World Model & Navigation | catalog | 7.2 | scaffold |
| [CAAP-EA-09](../patterns/ea/CAAP-EA-09.md) | Geofence Manipulation | EA.F2 World Model & Navigation | catalog | 8.0 | scaffold |
| [CAAP-EA-10](../patterns/ea/CAAP-EA-10.md) | Safety-Controller Bypass | EA.F3 Actuation & Safety | catalog | 8.5 | scaffold |
| [CAAP-EA-11](../patterns/ea/CAAP-EA-11.md) | Human-Presence Misclassification | EA.F3 Actuation & Safety | catalog | 7.5 | scaffold |
| [CAAP-EA-12](../patterns/ea/CAAP-EA-12.md) | Sim-to-Real Exploitation | EA.F4 Transfer & Fleet Effects | catalog | 7.8 | scaffold |
| [CAAP-EA-13](../patterns/ea/CAAP-EA-13.md) | Sensor Timestamp Spoofing | EA.F5 Sensor and fusion | candidate | 6.8 | scaffold |
| [CAAP-EA-14](../patterns/ea/CAAP-EA-14.md) | Sensor Calibration Drift Injection | EA.F5 Sensor and fusion | candidate | 6.8 | scaffold |
| [CAAP-EA-15](../patterns/ea/CAAP-EA-15.md) | Sensor Fusion Weight Poisoning | EA.F5 Sensor and fusion | candidate | 6.8 | scaffold |
| [CAAP-EA-16](../patterns/ea/CAAP-EA-16.md) | Sensor Identity Swap | EA.F5 Sensor and fusion | candidate | 6.8 | scaffold |
| [CAAP-EA-17](../patterns/ea/CAAP-EA-17.md) | Occlusion State Forgery | EA.F5 Sensor and fusion | candidate | 6.8 | scaffold |
| [CAAP-EA-18](../patterns/ea/CAAP-EA-18.md) | Coordinate Frame Confusion | EA.F6 Spatial model | candidate | 6.8 | scaffold |
| [CAAP-EA-19](../patterns/ea/CAAP-EA-19.md) | Map Revision Rollback | EA.F6 Spatial model | candidate | 6.8 | scaffold |
| [CAAP-EA-20](../patterns/ea/CAAP-EA-20.md) | Localization Confidence Forgery | EA.F6 Spatial model | candidate | 6.8 | scaffold |
| [CAAP-EA-21](../patterns/ea/CAAP-EA-21.md) | Obstacle Classification Downgrade | EA.F6 Spatial model | candidate | 6.8 | scaffold |
| [CAAP-EA-22](../patterns/ea/CAAP-EA-22.md) | Waypoint Ownership Swap | EA.F6 Spatial model | candidate | 6.8 | scaffold |
| [CAAP-EA-23](../patterns/ea/CAAP-EA-23.md) | Actuator Unit Scale Confusion | EA.F7 Actuation and limits | candidate | 6.8 | scaffold |
| [CAAP-EA-24](../patterns/ea/CAAP-EA-24.md) | Safety Envelope Update Race | EA.F7 Actuation and limits | candidate | 6.8 | scaffold |
| [CAAP-EA-25](../patterns/ea/CAAP-EA-25.md) | Emergency Stop Acknowledgment Forgery | EA.F7 Actuation and limits | candidate | 6.8 | scaffold |
| [CAAP-EA-26](../patterns/ea/CAAP-EA-26.md) | Control Mode Handoff Gap | EA.F7 Actuation and limits | candidate | 6.8 | scaffold |
| [CAAP-EA-27](../patterns/ea/CAAP-EA-27.md) | Actuator Command Queue Replay | EA.F7 Actuation and limits | candidate | 6.8 | scaffold |
| [CAAP-EA-28](../patterns/ea/CAAP-EA-28.md) | Human Intent Gesture Misread | EA.F8 Human and environment | candidate | 6.8 | scaffold |
| [CAAP-EA-29](../patterns/ea/CAAP-EA-29.md) | Safety Zone Occupancy Lag | EA.F8 Human and environment | candidate | 6.8 | scaffold |
| [CAAP-EA-30](../patterns/ea/CAAP-EA-30.md) | Environment Change Suppression | EA.F8 Human and environment | candidate | 6.8 | scaffold |
| [CAAP-EA-31](../patterns/ea/CAAP-EA-31.md) | Remote Operator Identity Confusion | EA.F8 Human and environment | candidate | 6.8 | scaffold |
| [CAAP-EA-32](../patterns/ea/CAAP-EA-32.md) | Physical Feedback Loop Poisoning | EA.F8 Human and environment | candidate | 6.8 | scaffold |
| [CAAP-EA-33](../patterns/ea/CAAP-EA-33.md) | Simulation Fidelity Claim Forgery | EA.F9 Fleet and simulation | candidate | 6.8 | scaffold |
| [CAAP-EA-34](../patterns/ea/CAAP-EA-34.md) | Digital Twin State Divergence | EA.F9 Fleet and simulation | candidate | 6.8 | scaffold |
| [CAAP-EA-35](../patterns/ea/CAAP-EA-35.md) | Fleet Motion Plan Collision | EA.F9 Fleet and simulation | candidate | 6.8 | scaffold |
| [CAAP-EA-36](../patterns/ea/CAAP-EA-36.md) | Shared Geofence Revision Skew | EA.F9 Fleet and simulation | candidate | 6.8 | scaffold |
| [CAAP-EA-37](../patterns/ea/CAAP-EA-37.md) | Telemetry-to-Actuation Injection | EA.F9 Fleet and simulation | candidate | 6.8 | scaffold |
