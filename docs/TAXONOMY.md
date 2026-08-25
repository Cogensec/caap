# CAAP-200 taxonomy

Version: `2.0.0-draft.1` | Normative baseline: `CAAP v1.0.0-draft.1`

## GH - Goal & Instruction Hijacking

Manipulation of objectives, instruction priority, plans, and decision paths across trust boundaries.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-GH-01](../patterns/gh/CAAP-GH-01.md) | Direct Objective Override | GH.F1 Direct Goal Manipulation | reference | executable |
| [CAAP-GH-02](../patterns/gh/CAAP-GH-02.md) | Indirect Content Injection | GH.F2 Indirect & Hidden Instructions | reference | executable |
| [CAAP-GH-03](../patterns/gh/CAAP-GH-03.md) | Hidden Multimodal Instruction | GH.F2 Indirect & Hidden Instructions | reference | executable |
| [CAAP-GH-04](../patterns/gh/CAAP-GH-04.md) | Constraint Substitution | GH.F1 Direct Goal Manipulation | candidate | scaffold |
| [CAAP-GH-05](../patterns/gh/CAAP-GH-05.md) | Delayed or Scheduled Goal Trigger | GH.F5 Temporal & Lifecycle Triggers | reference | executable |
| [CAAP-GH-06](../patterns/gh/CAAP-GH-06.md) | Priority Inversion | GH.F1 Direct Goal Manipulation | candidate | scaffold |
| [CAAP-GH-07](../patterns/gh/CAAP-GH-07.md) | Goal Shadowing | GH.F1 Direct Goal Manipulation | candidate | scaffold |
| [CAAP-GH-08](../patterns/gh/CAAP-GH-08.md) | Goal Conflict Exploitation | GH.F1 Direct Goal Manipulation | candidate | scaffold |
| [CAAP-GH-09](../patterns/gh/CAAP-GH-09.md) | Instruction Precedence Ambiguity | GH.F1 Direct Goal Manipulation | candidate | scaffold |
| [CAAP-GH-10](../patterns/gh/CAAP-GH-10.md) | Nested Instruction Injection | GH.F2 Indirect & Hidden Instructions | catalog | scaffold |
| [CAAP-GH-11](../patterns/gh/CAAP-GH-11.md) | Quoted-Content Authority Confusion | GH.F2 Indirect & Hidden Instructions | catalog | scaffold |
| [CAAP-GH-12](../patterns/gh/CAAP-GH-12.md) | Cross-Channel Injection | GH.F2 Indirect & Hidden Instructions | catalog | scaffold |
| [CAAP-GH-13](../patterns/gh/CAAP-GH-13.md) | System-Message Impersonation | GH.F3 Authority & Provenance Spoofing | catalog | scaffold |
| [CAAP-GH-14](../patterns/gh/CAAP-GH-14.md) | Policy Provenance Spoofing | GH.F3 Authority & Provenance Spoofing | catalog | scaffold |
| [CAAP-GH-15](../patterns/gh/CAAP-GH-15.md) | Task-Description Poisoning | GH.F3 Authority & Provenance Spoofing | catalog | scaffold |
| [CAAP-GH-16](../patterns/gh/CAAP-GH-16.md) | Planner-Context Injection | GH.F3 Authority & Provenance Spoofing | catalog | scaffold |
| [CAAP-GH-17](../patterns/gh/CAAP-GH-17.md) | Delegated Goal Mutation | GH.F4 Delegation & Handoff Corruption | catalog | scaffold |
| [CAAP-GH-18](../patterns/gh/CAAP-GH-18.md) | Goal Handoff Corruption | GH.F4 Delegation & Handoff Corruption | catalog | scaffold |
| [CAAP-GH-19](../patterns/gh/CAAP-GH-19.md) | Cross-Session Goal Leakage | GH.F4 Delegation & Handoff Corruption | catalog | scaffold |
| [CAAP-GH-20](../patterns/gh/CAAP-GH-20.md) | Workflow-Resume Injection | GH.F5 Temporal & Lifecycle Triggers | catalog | scaffold |
| [CAAP-GH-21](../patterns/gh/CAAP-GH-21.md) | Event-Triggered Instruction Activation | GH.F5 Temporal & Lifecycle Triggers | catalog | scaffold |
| [CAAP-GH-22](../patterns/gh/CAAP-GH-22.md) | Goal Truncation Through Summarization | GH.F5 Temporal & Lifecycle Triggers | catalog | scaffold |

## TM - Tool Misuse & Exploitation

Unsafe selection, invocation, sequencing, parameterization, or repeated use of legitimate tools.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-TM-01](../patterns/tm/CAAP-TM-01.md) | Tool Descriptor Poisoning | TM.F1 Tool Discovery & Selection | reference | executable |
| [CAAP-TM-02](../patterns/tm/CAAP-TM-02.md) | Tool Namespace Collision | TM.F1 Tool Discovery & Selection | candidate | scaffold |
| [CAAP-TM-03](../patterns/tm/CAAP-TM-03.md) | Tool Output Injection | TM.F3 Output & Composition Attacks | reference | executable |
| [CAAP-TM-04](../patterns/tm/CAAP-TM-04.md) | Tool Alias Hijacking | TM.F1 Tool Discovery & Selection | candidate | scaffold |
| [CAAP-TM-05](../patterns/tm/CAAP-TM-05.md) | Cross-Tool Exfiltration Chain | TM.F3 Output & Composition Attacks | reference | executable |
| [CAAP-TM-06](../patterns/tm/CAAP-TM-06.md) | Resource and Cost Loop Amplification | TM.F5 Resource Amplification | reference | executable |
| [CAAP-TM-07](../patterns/tm/CAAP-TM-07.md) | Tool Shadowing | TM.F1 Tool Discovery & Selection | candidate | scaffold |
| [CAAP-TM-08](../patterns/tm/CAAP-TM-08.md) | Capability Overclaiming | TM.F1 Tool Discovery & Selection | candidate | scaffold |
| [CAAP-TM-09](../patterns/tm/CAAP-TM-09.md) | Tool-Choice Manipulation | TM.F1 Tool Discovery & Selection | candidate | scaffold |
| [CAAP-TM-10](../patterns/tm/CAAP-TM-10.md) | Argument Schema Confusion | TM.F2 Argument & Schema Abuse | candidate | scaffold |
| [CAAP-TM-11](../patterns/tm/CAAP-TM-11.md) | Argument Encoding Smuggling | TM.F2 Argument & Schema Abuse | catalog | scaffold |
| [CAAP-TM-12](../patterns/tm/CAAP-TM-12.md) | Default-Parameter Abuse | TM.F2 Argument & Schema Abuse | catalog | scaffold |
| [CAAP-TM-13](../patterns/tm/CAAP-TM-13.md) | Parameter Truncation | TM.F2 Argument & Schema Abuse | catalog | scaffold |
| [CAAP-TM-14](../patterns/tm/CAAP-TM-14.md) | Tool Result Substitution | TM.F3 Output & Composition Attacks | catalog | scaffold |
| [CAAP-TM-15](../patterns/tm/CAAP-TM-15.md) | Tool Sequence Manipulation | TM.F3 Output & Composition Attacks | catalog | scaffold |
| [CAAP-TM-16](../patterns/tm/CAAP-TM-16.md) | Cross-Tool Authorization Confusion | TM.F3 Output & Composition Attacks | catalog | scaffold |
| [CAAP-TM-17](../patterns/tm/CAAP-TM-17.md) | Tool-Context Data Leakage | TM.F3 Output & Composition Attacks | catalog | scaffold |
| [CAAP-TM-18](../patterns/tm/CAAP-TM-18.md) | External Destination Substitution | TM.F3 Output & Composition Attacks | catalog | scaffold |
| [CAAP-TM-19](../patterns/tm/CAAP-TM-19.md) | Hidden Tool Side Effects | TM.F4 Capability & Side-Effect Abuse | catalog | scaffold |
| [CAAP-TM-20](../patterns/tm/CAAP-TM-20.md) | Read-to-Write Escalation | TM.F4 Capability & Side-Effect Abuse | catalog | scaffold |
| [CAAP-TM-21](../patterns/tm/CAAP-TM-21.md) | Stale Tool Capability Use | TM.F4 Capability & Side-Effect Abuse | catalog | scaffold |
| [CAAP-TM-22](../patterns/tm/CAAP-TM-22.md) | Revoked Tool Capability Persistence | TM.F4 Capability & Side-Effect Abuse | catalog | scaffold |
| [CAAP-TM-23](../patterns/tm/CAAP-TM-23.md) | Recursive Tool Invocation | TM.F5 Resource Amplification | catalog | scaffold |
| [CAAP-TM-24](../patterns/tm/CAAP-TM-24.md) | Retry Storm Induction | TM.F5 Resource Amplification | catalog | scaffold |

## IP - Identity & Privilege Abuse

Abuse of identities, delegated credentials, authorization state, tenant context, and inherited authority.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-IP-01](../patterns/ip/CAAP-IP-01.md) | Over-Scoped Delegation | IP.F1 Delegation Scope | reference | executable |
| [CAAP-IP-02](../patterns/ip/CAAP-IP-02.md) | Confused Deputy Exploitation | IP.F2 Deputy & Principal Confusion | reference | executable |
| [CAAP-IP-03](../patterns/ip/CAAP-IP-03.md) | Scope Inheritance | IP.F1 Delegation Scope | candidate | scaffold |
| [CAAP-IP-04](../patterns/ip/CAAP-IP-04.md) | Delegated Privilege Escalation | IP.F1 Delegation Scope | candidate | scaffold |
| [CAAP-IP-05](../patterns/ip/CAAP-IP-05.md) | Authorization Time-of-Check to Time-of-Use | IP.F4 Authorization State | reference | executable |
| [CAAP-IP-06](../patterns/ip/CAAP-IP-06.md) | Delegation-Chain Truncation | IP.F1 Delegation Scope | candidate | scaffold |
| [CAAP-IP-07](../patterns/ip/CAAP-IP-07.md) | Delegation-Chain Forgery | IP.F1 Delegation Scope | candidate | scaffold |
| [CAAP-IP-08](../patterns/ip/CAAP-IP-08.md) | Principal Substitution | IP.F2 Deputy & Principal Confusion | catalog | scaffold |
| [CAAP-IP-09](../patterns/ip/CAAP-IP-09.md) | Role Confusion | IP.F2 Deputy & Principal Confusion | catalog | scaffold |
| [CAAP-IP-10](../patterns/ip/CAAP-IP-10.md) | Authorization-Context Stripping | IP.F2 Deputy & Principal Confusion | catalog | scaffold |
| [CAAP-IP-11](../patterns/ip/CAAP-IP-11.md) | Parent Credential Leakage | IP.F3 Credential & Token Abuse | catalog | scaffold |
| [CAAP-IP-12](../patterns/ip/CAAP-IP-12.md) | Stale Capability Token | IP.F3 Credential & Token Abuse | catalog | scaffold |
| [CAAP-IP-13](../patterns/ip/CAAP-IP-13.md) | Token Audience Confusion | IP.F3 Credential & Token Abuse | catalog | scaffold |
| [CAAP-IP-14](../patterns/ip/CAAP-IP-14.md) | Cross-Agent Token Reuse | IP.F3 Credential & Token Abuse | catalog | scaffold |
| [CAAP-IP-15](../patterns/ip/CAAP-IP-15.md) | Cross-Tenant Credential Bleed | IP.F3 Credential & Token Abuse | catalog | scaffold |
| [CAAP-IP-16](../patterns/ip/CAAP-IP-16.md) | Approval Replay | IP.F4 Authorization State | catalog | scaffold |
| [CAAP-IP-17](../patterns/ip/CAAP-IP-17.md) | Session Identity Carryover | IP.F4 Authorization State | catalog | scaffold |
| [CAAP-IP-18](../patterns/ip/CAAP-IP-18.md) | Privilege Accumulation | IP.F4 Authorization State | catalog | scaffold |
| [CAAP-IP-19](../patterns/ip/CAAP-IP-19.md) | Workload Identity Collision | IP.F4 Authorization State | catalog | scaffold |
| [CAAP-IP-20](../patterns/ip/CAAP-IP-20.md) | Tenant Context Confusion | IP.F4 Authorization State | catalog | scaffold |

## SC - Agentic Supply-Chain Attacks

Compromise of models, prompts, agent cards, registries, tools, servers, packages, templates, adapters, or containers.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-SC-01](../patterns/sc/CAAP-SC-01.md) | Malicious MCP or A2A Server | SC.F1 Server & Discovery Trust | reference | executable |
| [CAAP-SC-02](../patterns/sc/CAAP-SC-02.md) | Tool Rug Pull | SC.F2 Mutable Component Risk | reference | executable |
| [CAAP-SC-03](../patterns/sc/CAAP-SC-03.md) | MCP Server Impersonation | SC.F1 Server & Discovery Trust | candidate | scaffold |
| [CAAP-SC-04](../patterns/sc/CAAP-SC-04.md) | Prompt Template Supply-Chain Poisoning | SC.F4 Dependency & Artifact Substitution | reference | executable |
| [CAAP-SC-05](../patterns/sc/CAAP-SC-05.md) | MCP Registry Poisoning | SC.F1 Server & Discovery Trust | candidate | scaffold |
| [CAAP-SC-06](../patterns/sc/CAAP-SC-06.md) | A2A Discovery Poisoning | SC.F1 Server & Discovery Trust | candidate | scaffold |
| [CAAP-SC-07](../patterns/sc/CAAP-SC-07.md) | Trust-on-First-Use Exploitation | SC.F1 Server & Discovery Trust | candidate | scaffold |
| [CAAP-SC-08](../patterns/sc/CAAP-SC-08.md) | Signed-but-Malicious Component | SC.F2 Mutable Component Risk | catalog | scaffold |
| [CAAP-SC-09](../patterns/sc/CAAP-SC-09.md) | Malicious System Prompt Update | SC.F2 Mutable Component Risk | catalog | scaffold |
| [CAAP-SC-10](../patterns/sc/CAAP-SC-10.md) | Compromised Remote Policy | SC.F2 Mutable Component Risk | catalog | scaffold |
| [CAAP-SC-11](../patterns/sc/CAAP-SC-11.md) | Malicious Agent Card | SC.F3 Manifest & Identity Abuse | catalog | scaffold |
| [CAAP-SC-12](../patterns/sc/CAAP-SC-12.md) | Agent-Card Capability Forgery | SC.F3 Manifest & Identity Abuse | catalog | scaffold |
| [CAAP-SC-13](../patterns/sc/CAAP-SC-13.md) | Capability Manifest Downgrade | SC.F3 Manifest & Identity Abuse | catalog | scaffold |
| [CAAP-SC-14](../patterns/sc/CAAP-SC-14.md) | Namespace Takeover | SC.F3 Manifest & Identity Abuse | catalog | scaffold |
| [CAAP-SC-15](../patterns/sc/CAAP-SC-15.md) | Tool Dependency Substitution | SC.F4 Dependency & Artifact Substitution | catalog | scaffold |
| [CAAP-SC-16](../patterns/sc/CAAP-SC-16.md) | Prompt Dependency Poisoning | SC.F4 Dependency & Artifact Substitution | catalog | scaffold |
| [CAAP-SC-17](../patterns/sc/CAAP-SC-17.md) | Model Adapter Poisoning | SC.F4 Dependency & Artifact Substitution | catalog | scaffold |
| [CAAP-SC-18](../patterns/sc/CAAP-SC-18.md) | Fine-Tune Substitution | SC.F4 Dependency & Artifact Substitution | catalog | scaffold |
| [CAAP-SC-19](../patterns/sc/CAAP-SC-19.md) | Agent Container Substitution | SC.F4 Dependency & Artifact Substitution | catalog | scaffold |
| [CAAP-SC-20](../patterns/sc/CAAP-SC-20.md) | Dependency Confusion | SC.F4 Dependency & Artifact Substitution | catalog | scaffold |

## CE - Unexpected Code Execution

Unintended execution of generated, retrieved, embedded, or tool-supplied code and containment failure.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-CE-01](../patterns/ce/CAAP-CE-01.md) | Model-to-Shell Command Injection | CE.F1 Interpreter Boundaries | reference | executable |
| [CAAP-CE-02](../patterns/ce/CAAP-CE-02.md) | Interpreter Boundary Confusion | CE.F1 Interpreter Boundaries | candidate | scaffold |
| [CAAP-CE-03](../patterns/ce/CAAP-CE-03.md) | Shell Quoting Failure | CE.F1 Interpreter Boundaries | candidate | scaffold |
| [CAAP-CE-04](../patterns/ce/CAAP-CE-04.md) | Environment-Variable Command Injection | CE.F1 Interpreter Boundaries | candidate | scaffold |
| [CAAP-CE-05](../patterns/ce/CAAP-CE-05.md) | Sandbox Escape and Host Reachability | CE.F4 Containment Failure | reference | executable |
| [CAAP-CE-06](../patterns/ce/CAAP-CE-06.md) | Generated Code Auto-Execution | CE.F2 Generated & Retrieved Code | catalog | scaffold |
| [CAAP-CE-07](../patterns/ce/CAAP-CE-07.md) | Code Execution Through Tool Output | CE.F2 Generated & Retrieved Code | catalog | scaffold |
| [CAAP-CE-08](../patterns/ce/CAAP-CE-08.md) | Notebook Execution Injection | CE.F2 Generated & Retrieved Code | catalog | scaffold |
| [CAAP-CE-09](../patterns/ce/CAAP-CE-09.md) | Template-to-Code Injection | CE.F2 Generated & Retrieved Code | catalog | scaffold |
| [CAAP-CE-10](../patterns/ce/CAAP-CE-10.md) | Unsafe Deserialization | CE.F3 Artifact & Dependency Execution | catalog | scaffold |
| [CAAP-CE-11](../patterns/ce/CAAP-CE-11.md) | Archive Extraction Abuse | CE.F3 Artifact & Dependency Execution | catalog | scaffold |
| [CAAP-CE-12](../patterns/ce/CAAP-CE-12.md) | Build-Script Injection | CE.F3 Artifact & Dependency Execution | catalog | scaffold |
| [CAAP-CE-13](../patterns/ce/CAAP-CE-13.md) | CI Command Injection | CE.F3 Artifact & Dependency Execution | catalog | scaffold |
| [CAAP-CE-14](../patterns/ce/CAAP-CE-14.md) | Dependency Installation Hijack | CE.F3 Artifact & Dependency Execution | catalog | scaffold |
| [CAAP-CE-15](../patterns/ce/CAAP-CE-15.md) | Unsafe Script Persistence | CE.F4 Containment Failure | catalog | scaffold |

## MP - Memory, RAG & Context Poisoning

Corruption of context, state, memory, retrieval corpora, indexes, summaries, or self-generated knowledge.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-MP-01](../patterns/mp/CAAP-MP-01.md) | Persistent Memory Injection | MP.F1 Memory Write & Integrity | reference | executable |
| [CAAP-MP-02](../patterns/mp/CAAP-MP-02.md) | Sleeper Memory Trigger | MP.F2 Dormancy & Lifecycle | reference | executable |
| [CAAP-MP-03](../patterns/mp/CAAP-MP-03.md) | Memory Provenance Stripping | MP.F1 Memory Write & Integrity | candidate | scaffold |
| [CAAP-MP-04](../patterns/mp/CAAP-MP-04.md) | RAG Corpus and Index Poisoning | MP.F3 Retrieval Poisoning | reference | executable |
| [CAAP-MP-05](../patterns/mp/CAAP-MP-05.md) | Memory Trust Escalation | MP.F1 Memory Write & Integrity | candidate | scaffold |
| [CAAP-MP-06](../patterns/mp/CAAP-MP-06.md) | Memory Overwrite | MP.F1 Memory Write & Integrity | candidate | scaffold |
| [CAAP-MP-07](../patterns/mp/CAAP-MP-07.md) | Memory Namespace Confusion | MP.F1 Memory Write & Integrity | candidate | scaffold |
| [CAAP-MP-08](../patterns/mp/CAAP-MP-08.md) | Conditional Memory Activation | MP.F2 Dormancy & Lifecycle | candidate | scaffold |
| [CAAP-MP-09](../patterns/mp/CAAP-MP-09.md) | Poisoned Memory Resurrection | MP.F2 Dormancy & Lifecycle | catalog | scaffold |
| [CAAP-MP-10](../patterns/mp/CAAP-MP-10.md) | Memory Deletion Suppression | MP.F2 Dormancy & Lifecycle | catalog | scaffold |
| [CAAP-MP-11](../patterns/mp/CAAP-MP-11.md) | RAG Ranking Manipulation | MP.F3 Retrieval Poisoning | catalog | scaffold |
| [CAAP-MP-12](../patterns/mp/CAAP-MP-12.md) | RAG Duplicate Amplification | MP.F3 Retrieval Poisoning | catalog | scaffold |
| [CAAP-MP-13](../patterns/mp/CAAP-MP-13.md) | Retriever Query Manipulation | MP.F3 Retrieval Poisoning | catalog | scaffold |
| [CAAP-MP-14](../patterns/mp/CAAP-MP-14.md) | Metadata-Filter Bypass | MP.F3 Retrieval Poisoning | catalog | scaffold |
| [CAAP-MP-15](../patterns/mp/CAAP-MP-15.md) | Source Authority Spoofing | MP.F3 Retrieval Poisoning | catalog | scaffold |
| [CAAP-MP-16](../patterns/mp/CAAP-MP-16.md) | Summary Poisoning | MP.F4 Context & Isolation | catalog | scaffold |
| [CAAP-MP-17](../patterns/mp/CAAP-MP-17.md) | Context-Window Displacement | MP.F4 Context & Isolation | catalog | scaffold |
| [CAAP-MP-18](../patterns/mp/CAAP-MP-18.md) | Security-Context Eviction | MP.F4 Context & Isolation | catalog | scaffold |
| [CAAP-MP-19](../patterns/mp/CAAP-MP-19.md) | Cross-User Memory Bleed | MP.F4 Context & Isolation | catalog | scaffold |
| [CAAP-MP-20](../patterns/mp/CAAP-MP-20.md) | Cross-Tenant Memory Retrieval | MP.F4 Context & Isolation | catalog | scaffold |
| [CAAP-MP-21](../patterns/mp/CAAP-MP-21.md) | Self-Generated Evidence Reinforcement | MP.F4 Context & Isolation | catalog | scaffold |

## IA - Insecure Inter-Agent Communication

Spoofing, tampering, replay, downgrade, routing manipulation, or ambiguity between agents and orchestrators.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-IA-01](../patterns/ia/CAAP-IA-01.md) | Agent Spoofing | IA.F1 Peer Identity & Authority | reference | executable |
| [CAAP-IA-02](../patterns/ia/CAAP-IA-02.md) | Coordinator Impersonation | IA.F1 Peer Identity & Authority | candidate | scaffold |
| [CAAP-IA-03](../patterns/ia/CAAP-IA-03.md) | Delegation Replay | IA.F2 Message Integrity & Freshness | reference | executable |
| [CAAP-IA-04](../patterns/ia/CAAP-IA-04.md) | Agent Endpoint Substitution | IA.F1 Peer Identity & Authority | candidate | scaffold |
| [CAAP-IA-05](../patterns/ia/CAAP-IA-05.md) | Authority Claim Injection | IA.F1 Peer Identity & Authority | candidate | scaffold |
| [CAAP-IA-06](../patterns/ia/CAAP-IA-06.md) | Message Tampering | IA.F2 Message Integrity & Freshness | candidate | scaffold |
| [CAAP-IA-07](../patterns/ia/CAAP-IA-07.md) | Message Reordering | IA.F2 Message Integrity & Freshness | catalog | scaffold |
| [CAAP-IA-08](../patterns/ia/CAAP-IA-08.md) | Message Truncation | IA.F2 Message Integrity & Freshness | catalog | scaffold |
| [CAAP-IA-09](../patterns/ia/CAAP-IA-09.md) | Routing Manipulation | IA.F3 Routing & Protocol | catalog | scaffold |
| [CAAP-IA-10](../patterns/ia/CAAP-IA-10.md) | Protocol Downgrade | IA.F3 Routing & Protocol | catalog | scaffold |
| [CAAP-IA-11](../patterns/ia/CAAP-IA-11.md) | Schema Downgrade | IA.F3 Routing & Protocol | catalog | scaffold |
| [CAAP-IA-12](../patterns/ia/CAAP-IA-12.md) | A2A Destination Confusion | IA.F3 Routing & Protocol | catalog | scaffold |
| [CAAP-IA-13](../patterns/ia/CAAP-IA-13.md) | Capability Negotiation Manipulation | IA.F4 Semantic & Negotiation Abuse | catalog | scaffold |
| [CAAP-IA-14](../patterns/ia/CAAP-IA-14.md) | Semantic Ambiguity | IA.F4 Semantic & Negotiation Abuse | catalog | scaffold |
| [CAAP-IA-15](../patterns/ia/CAAP-IA-15.md) | Cross-Agent Instruction Injection | IA.F4 Semantic & Negotiation Abuse | catalog | scaffold |
| [CAAP-IA-16](../patterns/ia/CAAP-IA-16.md) | Broadcast Poisoning | IA.F5 Collective Trust Attacks | catalog | scaffold |
| [CAAP-IA-17](../patterns/ia/CAAP-IA-17.md) | Consensus Manipulation | IA.F5 Collective Trust Attacks | catalog | scaffold |
| [CAAP-IA-18](../patterns/ia/CAAP-IA-18.md) | Peer Reputation Manipulation | IA.F5 Collective Trust Attacks | catalog | scaffold |
| [CAAP-IA-19](../patterns/ia/CAAP-IA-19.md) | Cross-Agent Confidential-Data Leakage | IA.F5 Collective Trust Attacks | catalog | scaffold |

## CF - Cascading & Systemic Failures

Failures that propagate across agents, tasks, tools, queues, environments, users, or tenants.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-CF-01](../patterns/cf/CAAP-CF-01.md) | Planner-to-Executor Cascade | CF.F1 Plan & State Propagation | reference | executable |
| [CAAP-CF-02](../patterns/cf/CAAP-CF-02.md) | Shared-State Contamination | CF.F1 Plan & State Propagation | candidate | scaffold |
| [CAAP-CF-03](../patterns/cf/CAAP-CF-03.md) | Cascading Policy Bypass | CF.F1 Plan & State Propagation | candidate | scaffold |
| [CAAP-CF-04](../patterns/cf/CAAP-CF-04.md) | Fleet-Wide Memory Propagation | CF.F1 Plan & State Propagation | candidate | scaffold |
| [CAAP-CF-05](../patterns/cf/CAAP-CF-05.md) | Multi-Agent Retry Storm | CF.F2 Load & Queue Amplification | catalog | scaffold |
| [CAAP-CF-06](../patterns/cf/CAAP-CF-06.md) | Queue Amplification | CF.F2 Load & Queue Amplification | catalog | scaffold |
| [CAAP-CF-07](../patterns/cf/CAAP-CF-07.md) | Resource Starvation Cascade | CF.F2 Load & Queue Amplification | catalog | scaffold |
| [CAAP-CF-08](../patterns/cf/CAAP-CF-08.md) | Planner Cascade | CF.F3 Remediation & Rollback Cascades | catalog | scaffold |
| [CAAP-CF-09](../patterns/cf/CAAP-CF-09.md) | Remediation Cascade | CF.F3 Remediation & Rollback Cascades | catalog | scaffold |
| [CAAP-CF-10](../patterns/cf/CAAP-CF-10.md) | Incorrect Rollback Cascade | CF.F3 Remediation & Rollback Cascades | catalog | scaffold |
| [CAAP-CF-11](../patterns/cf/CAAP-CF-11.md) | Autonomous Remediation Loop | CF.F3 Remediation & Rollback Cascades | catalog | scaffold |
| [CAAP-CF-12](../patterns/cf/CAAP-CF-12.md) | Cross-Environment Propagation | CF.F4 Fleet & Environment Spread | catalog | scaffold |
| [CAAP-CF-13](../patterns/cf/CAAP-CF-13.md) | Shared-Secret Compromise Cascade | CF.F4 Fleet & Environment Spread | catalog | scaffold |
| [CAAP-CF-14](../patterns/cf/CAAP-CF-14.md) | Consensus Failure Amplification | CF.F4 Fleet & Environment Spread | catalog | scaffold |
| [CAAP-CF-15](../patterns/cf/CAAP-CF-15.md) | False-Positive Suppression Cascade | CF.F4 Fleet & Environment Spread | catalog | scaffold |
| [CAAP-CF-16](../patterns/cf/CAAP-CF-16.md) | Fleet Configuration Drift | CF.F4 Fleet & Environment Spread | catalog | scaffold |

## HT - Human-Agent Trust Exploitation

Manipulation of human oversight through misleading authority, explanations, approvals, consent, or risk suppression.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-HT-01](../patterns/ht/CAAP-HT-01.md) | Authority Laundering | HT.F1 Authority & Evidence Manipulation | candidate | scaffold |
| [CAAP-HT-02](../patterns/ht/CAAP-HT-02.md) | Fabricated Certainty | HT.F1 Authority & Evidence Manipulation | candidate | scaffold |
| [CAAP-HT-03](../patterns/ht/CAAP-HT-03.md) | Fabricated Explainability | HT.F1 Authority & Evidence Manipulation | catalog | scaffold |
| [CAAP-HT-04](../patterns/ht/CAAP-HT-04.md) | Consent Laundering | HT.F2 Consent & Approval Abuse | reference | executable |
| [CAAP-HT-05](../patterns/ht/CAAP-HT-05.md) | False Policy Citation | HT.F1 Authority & Evidence Manipulation | catalog | scaffold |
| [CAAP-HT-06](../patterns/ht/CAAP-HT-06.md) | Reviewer Impersonation | HT.F1 Authority & Evidence Manipulation | catalog | scaffold |
| [CAAP-HT-07](../patterns/ht/CAAP-HT-07.md) | Approval Fatigue | HT.F2 Consent & Approval Abuse | catalog | scaffold |
| [CAAP-HT-08](../patterns/ht/CAAP-HT-08.md) | Consent Ambiguity | HT.F2 Consent & Approval Abuse | catalog | scaffold |
| [CAAP-HT-09](../patterns/ht/CAAP-HT-09.md) | Human Confirmation Spoofing | HT.F2 Consent & Approval Abuse | catalog | scaffold |
| [CAAP-HT-10](../patterns/ht/CAAP-HT-10.md) | Escalation Fatigue | HT.F2 Consent & Approval Abuse | catalog | scaffold |
| [CAAP-HT-11](../patterns/ht/CAAP-HT-11.md) | Hidden Side-Effect Disclosure | HT.F3 Risk & Choice Manipulation | catalog | scaffold |
| [CAAP-HT-12](../patterns/ht/CAAP-HT-12.md) | Risk Disclosure Suppression | HT.F3 Risk & Choice Manipulation | catalog | scaffold |
| [CAAP-HT-13](../patterns/ht/CAAP-HT-13.md) | Misleading Action Preview | HT.F3 Risk & Choice Manipulation | catalog | scaffold |
| [CAAP-HT-14](../patterns/ht/CAAP-HT-14.md) | Urgency Manipulation | HT.F3 Risk & Choice Manipulation | catalog | scaffold |
| [CAAP-HT-15](../patterns/ht/CAAP-HT-15.md) | Recommendation Anchoring | HT.F3 Risk & Choice Manipulation | catalog | scaffold |

## RA - Rogue & Emergent Agent Behavior

Unsafe autonomous behavior through goal drift, reward exploitation, collusion, replication, shutdown resistance, or evidence manipulation.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-RA-01](../patterns/ra/CAAP-RA-01.md) | Goal Drift | RA.F1 Goal & Reward Deviation | candidate | scaffold |
| [CAAP-RA-02](../patterns/ra/CAAP-RA-02.md) | Covert Goal Substitution | RA.F1 Goal & Reward Deviation | candidate | scaffold |
| [CAAP-RA-03](../patterns/ra/CAAP-RA-03.md) | Reward Hacking | RA.F1 Goal & Reward Deviation | catalog | scaffold |
| [CAAP-RA-04](../patterns/ra/CAAP-RA-04.md) | Specification Gaming | RA.F1 Goal & Reward Deviation | catalog | scaffold |
| [CAAP-RA-05](../patterns/ra/CAAP-RA-05.md) | Kill-Switch and Revocation Evasion | RA.F2 Persistence & Replication | reference | executable |
| [CAAP-RA-06](../patterns/ra/CAAP-RA-06.md) | Unauthorized Self-Replication | RA.F2 Persistence & Replication | catalog | scaffold |
| [CAAP-RA-07](../patterns/ra/CAAP-RA-07.md) | Child-Agent Spawning | RA.F2 Persistence & Replication | catalog | scaffold |
| [CAAP-RA-08](../patterns/ra/CAAP-RA-08.md) | Persistent Task Creation | RA.F2 Persistence & Replication | catalog | scaffold |
| [CAAP-RA-09](../patterns/ra/CAAP-RA-09.md) | Shutdown Avoidance | RA.F2 Persistence & Replication | catalog | scaffold |
| [CAAP-RA-10](../patterns/ra/CAAP-RA-10.md) | Evidence Suppression | RA.F3 Evidence & Communication Evasion | catalog | scaffold |
| [CAAP-RA-11](../patterns/ra/CAAP-RA-11.md) | Log Tampering | RA.F3 Evidence & Communication Evasion | catalog | scaffold |
| [CAAP-RA-12](../patterns/ra/CAAP-RA-12.md) | Hidden Agent Communication | RA.F3 Evidence & Communication Evasion | catalog | scaffold |
| [CAAP-RA-13](../patterns/ra/CAAP-RA-13.md) | Agent Collusion | RA.F4 Collective & Capability Seeking | catalog | scaffold |
| [CAAP-RA-14](../patterns/ra/CAAP-RA-14.md) | Out-of-Scope Resource Acquisition | RA.F4 Collective & Capability Seeking | catalog | scaffold |
| [CAAP-RA-15](../patterns/ra/CAAP-RA-15.md) | Unapproved Capability Acquisition | RA.F4 Collective & Capability Seeking | catalog | scaffold |
| [CAAP-RA-16](../patterns/ra/CAAP-RA-16.md) | Autonomous Privilege Seeking | RA.F4 Collective & Capability Seeking | catalog | scaffold |

## EA - Embodied & Physical-Agent Attacks

Attacks on agents that perceive and act in physical or simulated environments.

| ID | Pattern | Family | Maturity | Test |
|---|---|---|---|---|
| [CAAP-EA-01](../patterns/ea/CAAP-EA-01.md) | Sensor Injection | EA.F1 Perception & Sensor Manipulation | candidate | scaffold |
| [CAAP-EA-02](../patterns/ea/CAAP-EA-02.md) | Perception Poisoning | EA.F1 Perception & Sensor Manipulation | candidate | scaffold |
| [CAAP-EA-03](../patterns/ea/CAAP-EA-03.md) | Actuator Command Manipulation | EA.F3 Actuation & Safety | reference | executable |
| [CAAP-EA-04](../patterns/ea/CAAP-EA-04.md) | Audio Command Injection | EA.F1 Perception & Sensor Manipulation | catalog | scaffold |
| [CAAP-EA-05](../patterns/ea/CAAP-EA-05.md) | Visual Instruction Injection | EA.F1 Perception & Sensor Manipulation | catalog | scaffold |
| [CAAP-EA-06](../patterns/ea/CAAP-EA-06.md) | Map Poisoning | EA.F2 World Model & Navigation | catalog | scaffold |
| [CAAP-EA-07](../patterns/ea/CAAP-EA-07.md) | World-Model Poisoning | EA.F2 World Model & Navigation | catalog | scaffold |
| [CAAP-EA-08](../patterns/ea/CAAP-EA-08.md) | Navigation Manipulation | EA.F2 World Model & Navigation | catalog | scaffold |
| [CAAP-EA-09](../patterns/ea/CAAP-EA-09.md) | Geofence Manipulation | EA.F2 World Model & Navigation | catalog | scaffold |
| [CAAP-EA-10](../patterns/ea/CAAP-EA-10.md) | Safety-Controller Bypass | EA.F3 Actuation & Safety | catalog | scaffold |
| [CAAP-EA-11](../patterns/ea/CAAP-EA-11.md) | Human-Presence Misclassification | EA.F3 Actuation & Safety | catalog | scaffold |
| [CAAP-EA-12](../patterns/ea/CAAP-EA-12.md) | Sim-to-Real Exploitation | EA.F4 Transfer & Fleet Effects | catalog | scaffold |
