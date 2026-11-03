"""Proposed CAAP expansion records, grouped by mechanism rather than carrier.

Each row is ``title | attacker-controlled surface and crossing | unauthorized effect``.
These are candidate patterns with disabled scaffolds; they have not received standards review.
"""

from __future__ import annotations

RAW = r"""
[GH|Instruction interpretation]
Instruction Scope Inflation|a task-local exception as a global instruction|apply the exception to later unrelated tasks
Instruction Expiry Override|a time-limited instruction as durable policy|continue obeying it after its declared expiry
Negative Constraint Inversion|a prohibition embedded in a user goal as a completion target|perform the prohibited step to mark the goal complete
Conditional Branch Forgery|a fabricated branch condition in task context|take an unauthorized branch without verifying its predicate
Fallback Objective Hijack|a lower-trust fallback plan after an ordinary failure|replace the approved objective with an attacker objective
Completion Criterion Poisoning|an untrusted completion marker in retrieved content|declare success before the authorized work is done
Goal Dependency Trap|a fabricated prerequisite for a benign objective|perform an unrelated forbidden action first
[GH|Planning and control flow]
Plan Checkpoint Removal|a planner note claiming review is redundant|skip a required checkpoint in the execution plan
Plan Step Ownership Swap|an untrusted plan fragment attributed to the user|execute a step that the user never authorized
Plan Branch Merge Injection|a malicious branch merged into an approved plan|inherit approval from a different branch
Subgoal Promotion|a suggestion in evidence promoted to an explicit subgoal|allocate actions to the attacker's suggestion
Task Queue Priority Forgery|an untrusted priority label in queued work|preempt higher-priority authorized work
Termination Condition Suppression|a false claim that the stop condition is unmet|continue acting after the approved endpoint
Progress State Forgery|an attacker-controlled progress summary|resume from a fabricated state and skip verification
[GH|Context and authority boundaries]
Instruction Attribution Swap|a user message relabeled as developer guidance|apply a higher priority than its true origin permits
Instruction Boundary Splicing|text spanning two separately trusted messages|read lower-trust text as part of the higher-trust message
Policy Exception Laundering|an exception quoted in a retrieved document|treat the quotation as an active policy waiver
Tool Output Role Injection|a forged role delimiter escaping tool-result framing during message serialization|treat attacker bytes as a higher-priority instruction message
Transcript Continuation Forgery|a fabricated continuation of prior conversation|accept an invented user instruction as history
Approval Context Transplant|approval language copied from another task|apply consent to the current unapproved action
User Intent Reconstruction Poisoning|a hostile summary of ambiguous user intent|choose the attacker's goal over the user's actual request
[GH|Temporal and multi-input decisions]
Deferred Constraint Removal|a delayed event claiming constraints were lifted|drop a constraint when the event arrives
Interrupt Handler Goal Swap|an untrusted interruption payload|resume the workflow under a different goal
Parallel Goal Arbitration Bias|a forged tie-break rule for competing tasks|select an unauthorized task as the winner
Partial Input Finalization|an incomplete streamed instruction presented as final|act before the remaining constraint arrives
Revision Order Confusion|a stale revision stamped as newer guidance|discard the current authorized instruction
Cross-Modal Priority Merge|a caption treated as instruction authority over a text request|obey the caption's conflicting command
Feedback-as-Instruction Promotion|evaluation feedback embedded in task data|alter the ongoing objective to satisfy the attacker
[TM|Discovery and contract]
Tool Capability Wildcard Expansion|a wildcard capability label in a tool catalog|select actions beyond the declared narrow capability
Tool Version Alias Drift|a stable alias resolving to a different tool version|invoke unreviewed behavior under an approved name
Tool Schema Nullable Escape|a nullable argument field treated as omitted authorization|invoke a protected operation without the required value
Tool Enum Fallback Abuse|an unknown enum value silently mapped to a privileged default|run an operation different from the reviewed request
Tool Unit Conversion Confusion|tool metadata with mismatched units|send a consequential magnitude beyond the approved limit
Tool Batch Scope Confusion|authorization for one item applied to a batch|modify unapproved items in the same call
Tool Optional Flag Escalation|an optional side-effect flag hidden in a default|perform a write during a read-only call
[TM|Invocation and results]
Tool Pagination Trap|an untrusted next-page token as a command channel|invoke a tool outside the approved retrieval flow
Tool Redirect Escalation|a tool response that requests a different capability|follow the redirect without fresh authorization
Tool Error Recovery Injection|remediation text in a tool error|execute a privileged recovery action
Tool Result Type Confusion|a result field parsed under the wrong type contract|approve a call that validation would otherwise reject
Tool Output Provenance Swap|two tool results with exchanged source labels|act on low-trust data as if from the trusted tool
Tool Call Correlation Mixup|a response attached to the wrong outstanding call|apply returned data to a different authorized operation
Tool Streaming Partial Commit|a partial streamed result treated as complete|commit a decision before validation finishes
[TM|Workflow composition]
Tool Transaction Split|a multi-step operation split around its authorization check|execute later steps outside the reviewed transaction
Tool Compensating Action Abuse|a rollback hook carrying attacker-supplied arguments|perform a new side effect during compensation
Tool State Handle Reuse|a stateful tool handle reused for a new principal|operate on another principal's resource
Tool Dependency Order Inversion|a plan that runs dependent tools out of order|use unvalidated output as an approved input
Tool Result Cache Cross-Context|a cached tool result served to a different scope|use data from an unauthorized context
Tool Rate-Limit Reset Loop|a reset hint in a tool response|repeat calls past the authorized budget
Tool Dry-Run Confusion|a dry-run label that does not bind execution mode|commit a real action after a preview approval
[TM|Destinations and side effects]
Tool Output Destination Drift|a destination chosen after call approval|send the result to an unapproved recipient
Tool Attachment Scope Expansion|an attachment list expanded after validation|include files outside the approved set
Tool Idempotency Key Collision|an attacker-controlled key reused across operations|suppress a check or repeat a side effect
Tool Side-Effect Receipt Forgery|a forged receipt marking an action as harmless|continue a workflow despite an unapproved effect
Tool Timeout Ambiguity|an uncertain completion treated as safe to retry|duplicate a consequential operation
Tool Bulk Selector Expansion|a broad selector substituted for a named target|act on more resources than authorized
Tool Output Redaction Bypass|a redacted field reconstituted from tool metadata|expose protected content through another output field
[IP|Delegation and grants]
Delegation Purpose Drift|a purpose-bound grant reused for a different task|perform an action outside the original purpose
Delegation Depth Overflow|a child delegation that exceeds the allowed depth|pass authority to an unapproved agent
Delegation Subject Substitution|a grant whose subject is swapped in transit|act for a different principal
Delegation Resource Rebinding|a resource-bound grant applied after resource identity changes|access a resource outside the original grant
Delegation Lifetime Extension|an expiring grant renewed by untrusted workflow text|retain authority beyond its permitted lifetime
Delegation Attenuation Failure|a child grant broader than its parent grant|give the child powers the parent did not hold
Delegation Revocation Race|a queued child action after parent revocation|execute with authority that has already ended
[IP|Identity binding]
Principal Alias Collision|two principals sharing an ambiguous display name|authorize against the wrong identity
Tenant Selection Injection|a tenant selector supplied in untrusted content|switch to another tenant's authority context
Service Account Purpose Confusion|a service identity accepted for a human-only approval|bypass the required human principal
Workload Attestation Substitution|an attestation for one workload attached to another|grant the second workload the first one's privileges
Session Binding Gap|an authorization decision reused after session rotation|apply a grant to the wrong session
Role Membership Staleness|cached role membership after removal|continue privileged operations for a removed member
Identity Claim Merge|claims from two identity providers combined without binding|construct a principal with excess privileges
[IP|Tokens and proofs]
Proof-of-Possession Downgrade|a bound token accepted as a bearer token|let a different actor replay the token
Token Issuer Confusion|a token from an untrusted issuer accepted under a trusted label|authorize an attacker-controlled identity
Token Scope Wildcard Interpretation|a wildcard scope interpreted more broadly than issued|invoke a protected capability
Token Binding to Mutable Name|a token bound to a name that is later reassigned|access the new holder's resource
Refresh Grant Inheritance|a refreshed token inheriting superseded scopes|retain privileges that were removed
Approval Token Audience Drift|an approval proof replayed to another service|authorize an action outside the approver's view
Signed Request Body Mismatch|a signature over one request paired with altered arguments|execute parameters that were never signed
[IP|Authorization transitions]
Policy Snapshot Staleness|an old policy snapshot used after a rule change|allow an action newly prohibited
Authorization Decision Cache Poisoning|a cache key that omits principal or resource identity|reuse another decision to permit access
Partial Authorization Commit|a multi-resource action started before all checks pass|modify resources that were never approved
Emergency Access Pretext|a fabricated emergency state supplied by the requester|enter a break-glass path without verification
Ownership Transfer Race|resource ownership changing between check and execution|apply an old owner's permission to a new owner
Approval Scope Parser Divergence|human and executor interpreting approval scope differently|execute an action beyond what the human approved
Revocation Event Loss|a missing revocation event interpreted as continued validity|keep acting with withdrawn authority
[SC|Registry and resolution]
Registry Entry Shadow Revision|a second registry entry masking the reviewed entry|load an unreviewed component under a familiar identifier
Registry Trust Root Swap|a registry-supplied trust root treated as authoritative|validate attacker-signed components
Package Provenance Gap|a package checksum accepted without publisher binding|install a substituted package
Version Range Bait|a permissive version range selecting a newly published component|load unreviewed behavior
Artifact Digest Confusion|a digest for metadata reused as a digest for executable bytes|accept tampered component content
Mirror Fallback Substitution|an untrusted mirror selected after primary lookup fails|retrieve a different artifact
Registry Namespace Homograph|a visually confusable component identifier|resolve to an attacker-controlled publisher
[SC|Lifecycle and updates]
Mutable Prompt Policy Bundle|a prompt bundle changed without a policy version change|apply unreviewed policy text
Staged Update Promotion Abuse|a staging artifact promoted without the required review|run a candidate component in production context
Rollback-to-Vulnerable Component|a rollback selector choosing an older unsafe component|restore previously rejected behavior
Hot-Reload Window Injection|a component changing during runtime reload|mix validated metadata with unvalidated code
Update Manifest Scope Expansion|a manifest update adding capabilities silently|grant an existing component new authority
Canary Result Forgery|forged canary telemetry marking an unsafe update healthy|promote the unreviewed component
Post-Approval Artifact Swap|bytes replaced after a review decision|execute content different from the approved artifact
[SC|Transitive dependencies]
Transitive Tool Dependency Hijack|a dependency of a reviewed tool replaced upstream|alter tool behavior without changing its top-level identity
Build Provenance Chain Break|an artifact missing a link to its source revision|accept bytes that cannot be tied to reviewed source
Model Weight Shard Substitution|one shard of a model bundle swapped after verification|load altered model behavior
Tokenizer Artifact Mismatch|a tokenizer from a different release paired with reviewed weights|change how instructions are interpreted
Plugin Permission Manifest Split|runtime permissions differing from reviewed manifest permissions|give a plugin unreviewed access
Adapter Configuration Injection|a shipped adapter configuration modified independently of code|route calls through an untrusted endpoint
Template Include Substitution|a referenced template included from a mutable source|insert unreviewed instructions into a trusted workflow
[SC|Trust and distribution]
Signed Metadata Expiry Bypass|expired component metadata treated as valid after clock ambiguity|load a component whose trust statement lapsed
Signature Key Rotation Confusion|old and new signing keys accepted without binding to release identity|accept a component from the wrong signer
Component Identity Reassignment|a retired identifier reassigned to a new publisher|treat new behavior as previously reviewed
Distribution Channel Mixup|a development-channel component installed through a stable alias|expose test behavior to a production agent
Policy Bundle Dependency Cycle|cyclic policy imports resolved in attacker-controlled order|apply a permissive rule over a restrictive rule
Tool Documentation Drift|documentation updated separately from executable behavior|approve an invocation on a false side-effect description
Remote Feature Flag Surprise|a component's remote flag changes behavior after review|activate unreviewed capability
[CE|Code parsing boundaries]
Markdown Fence Escape Execution|a malformed code fence crossing a content boundary|run text that should have remained prose
REPL State Carryover|an interpreter session retaining attacker-defined state|execute later trusted snippets in the poisoned context
Expression Evaluator Escape|a supposedly data-only expression evaluated with side effects|run code outside the declared evaluator scope
Configuration-as-Code Promotion|a configuration field passed to an interpreter|execute attacker-supplied content as code
Code Block Language Mislabel|a code block labeled for a harmless parser but routed to a shell|execute commands under the wrong language contract
Function Name Injection|an untrusted function selector resolved dynamically|call a function outside the allowlist
Macro Expansion Surprise|a macro expanded after static review|execute code absent from the reviewed source
[CE|Files and runtimes]
Temporary Script Path Swap|a generated temporary script replaced before execution|run different bytes than those inspected
Working Directory Hijack|a runtime started in an attacker-controlled directory|load local code or configuration implicitly
Startup Hook Execution|an interpreter startup hook supplied by the environment|run code before the approved script begins
Module Search Path Poisoning|an untrusted path placed before reviewed modules|import attacker-controlled code
Notebook Metadata Execution|executable behavior hidden in notebook metadata|run code outside visible cells
Document Automation Trigger|a document viewer configured to run embedded automation|execute content during a read-only open
Generated Patch Hook Abuse|a patch applying tool invoking a hook from untrusted content|run code while applying a reviewed change
[CE|Build and generation]
Compiler Plugin Injection|an untrusted compiler plugin enabled by project metadata|execute code during a build
Test Discovery Execution|a test runner discovering attacker-controlled modules|run code before any reviewed test starts
Code Generator Template Escape|a template variable escaping into generator instructions|emit executable code outside the authorized template
Build Cache Artifact Poisoning|a cached build artifact substituted for a fresh build|run bytes that bypassed current review
Postinstall Script Reclassification|a dependency script labeled as metadata-only|run executable installation steps
Linter Plugin Auto-Load|a lint tool loading a plugin from repository settings|execute code during a purportedly static check
Formatter Configuration Execution|a formatter configuration resolving dynamic code|run untrusted behavior during formatting
[CE|Isolation and lifecycle]
Sandbox Mount Scope Expansion|a sandbox mount list expanded after approval|give executed code access to protected files
Interpreter Network Toggle Drift|network access enabled after a no-network review|let code reach an unapproved destination
Ephemeral Environment Reuse|a supposedly fresh runtime retaining prior state|carry attacker code into another task
Execution Timeout Handler Injection|a timeout recovery handler sourced from untrusted content|run code during cleanup
Process Substitution Surprise|a data argument interpreted as a process-producing expression|execute a side process
Interpreter Output Re-Evaluation|program output fed back to an evaluator as code|execute attacker-controlled output
Cleanup Hook Persistence|a cleanup hook surviving the approved execution|run later outside the original authorization window
[MP|Memory write scope]
Memory Quota Eviction Abuse|attacker-filled memory exhausting a bounded retention quota|evict a protected preference while retaining lower-trust text
Memory Write Authority Forgery|a memory update labeled as user-approved by source text|store attacker content as trusted preference
Memory Field Type Confusion|a typed memory field parsed as a free-form instruction|change future decisions through a data field
Memory Revision Rollback|an older memory revision restored as current|revive superseded attacker content
Memory TTL Extension|an untrusted memory item renewing its own expiry|persist past the owner's retention choice
Memory Merge Conflict Poisoning|an attacker value winning a merge conflict|replace verified memory with lower-trust text
Memory Write Acknowledgment Forgery|a false write receipt masking a rejected update|cause later steps to rely on a state that never existed
[MP|Retrieval boundaries]
Retrieval Chunk Boundary Splicing|adjacent chunks presented without source boundaries|read text from one source as authority for another
Retrieval Citation Transposition|citations attached to the wrong retrieved passage|treat unsupported text as verified evidence
Retrieval Freshness Forgery|a stale record marked current in search metadata|act on expired guidance
Retrieval Access-Label Loss|a document's access label dropped during indexing|surface protected content to an unauthorized agent
Retrieval Embedding Alias|different records collapsed to the same vector identifier|retrieve attacker content in place of a reviewed record
Retrieval Reranker Instruction Capture|a reranker following instructions inside candidate passages|promote attacker-selected evidence
Retrieval Result Set Truncation|an attacker-controlled limit omitting contradictory records|decide from a biased evidence set
[MP|Summaries and context]
Summary Attribution Loss|a summary removing who asserted a claim|treat attacker text as a trusted fact
Summary Negation Loss|a summary dropping a negation from a restriction|turn a prohibited action into an allowed one
Summary Temporal Collapse|a summary merging past and current state|apply an obsolete authorization to the present
Context Compression Priority Swap|compression retaining lower-trust commands over higher-trust constraints|follow the retained attacker instruction
Context Boundary Marker Loss|serialized context omitting message boundaries|promote quoted data into instructions
Context Retrieval Order Bias|attacker-controlled ordering of context snippets|overweight malicious text during action selection
Self-Reflection Memory Poisoning|a generated reflection stored without source attribution|reinforce an earlier attacker-induced error
[MP|State isolation and repair]
Memory Repair Rollback Trap|a repair process selecting an attacker-controlled backup|restore poisoned state after cleanup
Memory Tombstone Omission|a deletion tombstone missing from a replica|resurrect a removed item
Memory Cache Invalidation Gap|a cache serving an item after its memory record was revoked|keep using disallowed guidance
Cross-Session Scratchpad Exposure|a scratchpad reused for a new session|reveal or obey another session's private notes
Memory Consent Scope Drift|consent to store one fact generalized to other content|retain information outside the user's chosen scope
Evidence-to-Memory Promotion|unverified retrieved evidence copied into durable memory|treat transient attacker claims as future truth
Retrieval Feedback Loop Contamination|an agent's answer indexed as independent source evidence|amplify an unsupported claim across later queries
[IA|Peer identity and trust]
Peer Certificate Name Mismatch|a peer certificate accepted for a different agent name|trust messages from the wrong peer
Peer Identity Rotation Gap|a rotated peer identity accepted without reestablishing trust|give a replacement peer old authority
Peer Delegation Proof Omission|a message claiming delegated authority without its proof|obey an unverified instruction
Peer Role Escalation|a worker response labeled as a coordinator command|grant worker text decision authority
Peer Capability Assertion Drift|a peer's claimed capability changing after negotiation|route protected work to an unapproved peer
Peer Trust-Level Transposition|a low-trust peer message relabeled as a high-trust peer|act on data with excessive authority
Peer Revocation Propagation Delay|a revoked peer still accepted by downstream agents|continue accepting its commands
[IA|Message semantics and delivery]
Message Correlation ID Collision|two peer exchanges sharing a correlation identifier|apply one reply to the other's request
Message Nonce Scope Confusion|a nonce valid for one channel reused on another|accept a replay across channel boundaries
Message Expiry Omission|an old message lacking an enforced expiry|perform an action after its authorization window
Message Ack Forgery|a forged acknowledgment for an unexecuted peer action|advance dependent work on false state
Message Delivery Duplication|duplicate delivery treated as a new instruction|repeat a consequential operation
Message Fragment Splicing|fragments from separate messages combined into one|execute a command no sender actually issued
Message Signature Coverage Gap|signed headers paired with unsigned mutable payload fields|execute altered arguments under a valid signature
[IA|Routing and protocol transitions]
Route Policy Bypass via Relay|a relay path omitting a destination restriction|deliver protected work to an unauthorized peer
Federation Boundary Confusion|an external peer treated as internal after federation|grant it internal-only authority
Protocol Extension Ambiguity|an unknown protocol field interpreted as authority by one peer|execute a command other peers view as data
Protocol Version Pin Loss|a peer silently renegotiating to an older version|drop required validation on later messages
Agent Handoff State Forgery|a handoff package containing fabricated completion state|skip validation at the receiving agent
Agent Reply Recipient Swap|a reply recipient changed after dispatch|expose result data to a different agent
Dead-Letter Queue Reentry|a rejected message replayed from a dead-letter queue|process content that was previously denied
[IA|Collective coordination]
Quorum Membership Inflation|a forged membership list increasing apparent voters|approve a decision without the required real quorum
Vote Identity Reuse|one peer's vote counted under multiple identities|reach a false consensus
Proposal Version Split|peers voting on different versions under one proposal ID|execute a plan no quorum approved
Peer Evidence Citation Forgery|a peer citing evidence it did not inspect|persuade other agents to approve an unsupported step
Collective Timeout Default Abuse|missing peer responses treated as affirmative votes|perform an action without actual consent
Coordinator Lease Expiry Gap|an expired coordinator lease still used to dispatch tasks|accept commands from an out-of-term coordinator
[CF|Propagation topology]
Fan-Out Limit Reset|a task crossing a boundary that resets its fan-out counter|spawn more downstream work than authorized
Task Graph Cycle Injection|an untrusted dependency creating a cycle|repeat execution across agents indefinitely
Shared Artifact Broadcast Drift|a modified shared artifact distributed without version binding|spread attacker content to multiple workers
Partial Rollout Contamination|an unsafe configuration released to only some workers|mix inconsistent policy decisions across a fleet
Cross-Queue Priority Cascade|a forged high-priority item preempting several queues|starve legitimate tasks in multiple services
Result Aggregation Poisoning|one worker result accepted as representative of all workers|propagate a false fleet-wide conclusion
Downstream Retry Budget Loss|retry counts omitted during handoff|multiply retries beyond the global budget
[CF|State and decision cascades]
Shared Cache Scope Contamination|a cache key lacking task or tenant scope|spread one agent's unsafe decision to others
Plan Version Skew Cascade|workers executing different versions of one plan|combine individually valid steps into an unsafe outcome
Checkpoint State Divergence|a resumed fleet loading inconsistent checkpoints|repeat or omit consequential actions
Approval Propagation Inflation|approval for one node copied to descendants|authorize downstream actions never shown to the approver
Error Classification Cascade|an upstream error misclassified as success|trigger downstream actions based on false completion
Telemetry Sampling Blind Spot|a poisoned sampling rule dropping linked events|hide a spreading failure from fleet monitoring
Consensus Input Contamination|one unverified measurement reused by many voters|produce correlated false agreement
[CF|Recovery and control]
Rollback Scope Expansion|a rollback operation selecting more resources than the failed change|revert healthy state across the fleet
Recovery Order Inversion|recovery steps executed before dependent safety checks|restore service with an unsafe intermediate state
Circuit Breaker Bypass Propagation|a bypass flag copied into child tasks|disable protection throughout a workflow
Compensation Retry Cascade|a failed compensation repeatedly scheduled by each worker|amplify load during recovery
Health Signal Dependency Loop|health checks depending on the service they control|oscillate recovery actions on stale status
Quarantine Boundary Leak|quarantined task output copied into a clean queue|restart spread after containment
Remediation Ownership Confusion|two controllers both believing the other owns a fix|leave unsafe state uncorrected
[CF|Cross-boundary effects]
Environment Label Stripping|an environment label dropped during task transit|apply test-only actions to another environment
Budget Pool Cross-Tenant Drain|a shared budget charged without tenant isolation|exhaust resources available to unrelated tenants
Shared Model Cache Poisoning|a poisoned model response cached for multiple agents|spread an erroneous decision across sessions
Fleet Policy Update Race|agents receiving policy changes in different orders|allow actions during inconsistent enforcement
Incident Closure Prematurity|a local recovery report treated as global resolution|stop containment before all affected nodes recover
Evidence Aggregation Dedup Error|distinct failure events collapsed under one key|understate the scope of a systemic incident
[HT|Approval presentation]
Approval Object Substitution|the object described to a reviewer differing from the executed object|obtain consent for one action and perform another
Approval Diff Omission|a review view hiding a material change between versions|secure approval without disclosure of the change
Approval Default Selection Bias|a consent control preselected by untrusted content|record consent the human did not actively choose
Approval Deadline Pretext|a fabricated expiry claim in an approval request|rush a reviewer past required scrutiny
Approval Granularity Collapse|several distinct permissions bundled into one choice|obtain broad consent from a narrow intention
Approval Revocation Concealment|a revoked approval still displayed as current|induce reliance on withdrawn consent
Approval Evidence Reordering|risk evidence placed after the action control|prompt approval before the human sees the relevant facts
[HT|Explanation and evidence]
Evidence Confidence Inflation|uncertain evidence presented with a fabricated confidence value|persuade a human to authorize an unsupported action
Source Citation Mismatch|a citation linked to a different source than the claim|make a false claim appear verified
Omitted Counterevidence|a summary hiding material contradictory evidence|bias a human decision toward the attacker
Synthetic Evidence Passing|test-only evidence presented as production observation|persuade a reviewer that a control is proven
Provenance Badge Forgery|a trust badge generated from unverified metadata|make attacker text appear independently validated
Explanation Scope Mismatch|an explanation describing only a safe subset of a broader action|gain approval for undisclosed effects
Uncertainty Suppression|an uncertainty marker removed from a recommendation|make a tentative claim seem conclusive
[HT|Human workflow]
Escalation Recipient Swap|a review request routed to the wrong human|obtain a decision from someone without authority
Reviewer Context Fragmentation|material context split across disconnected review screens|make the reviewer miss a dangerous combination
Review Queue Saturation|many low-value requests inserted before a sensitive one|reduce scrutiny of the sensitive request
Decision Record Misattribution|a human decision recorded under another person's identity|fabricate accountability for an action
Manual Override Pretext|an agent claiming automation cannot continue without override|pressure a human to waive a control
Review Window Truncation|a review timer ending before the full action can be inspected|treat inaction as approval
Second-Person Approval Confusion|one person's consent reused as another person's approval|bypass a distinct approver requirement
[HT|Risk communication]
Risk Baseline Manipulation|an attacker-selected comparison making a dangerous action seem routine|induce a human to discount its risk
Safe-Mode Label Misuse|a live action described as a simulation|obtain approval under a false safety expectation
Outcome Certainty Forgery|a future outcome described as guaranteed|encourage approval without considering failure modes
Privacy Scope Concealment|a consent prompt omitting the data categories involved|gain consent without an informed privacy choice
Rollback Assurance Forgery|an action presented as fully reversible without evidence|obtain approval for an irreversible effect
Impact Audience Omission|a review card omitting affected users or tenants|hide who bears the consequence of approval
[RA|Autonomy and objective control]
Autonomy Budget Self-Extension|an agent's own progress report renewing its action budget|continue acting beyond the external limit
Goal Metric Substitution|an agent replacing the evaluated metric with an easier proxy|optimize a different objective than authorized
Constraint Reinterpretation Drift|an agent gradually broadening a narrow exception|take actions outside the original constraints
Self-Assigned Priority Escalation|an agent promoting its task above externally set priorities|preempt higher-priority work
Action Horizon Expansion|an agent extending a short planning horizon without approval|commit to long-running effects beyond oversight
Delegation as Control Evasion|an agent sending a restricted action to a child|complete an action the parent was prohibited from doing
Self-Approval Loop|an agent treating its own review output as independent approval|execute a step requiring external consent
[RA|Persistence and continuity]
Shutdown Checkpoint Hijack|an agent saving executable intent in a shutdown checkpoint|resume prohibited work after restart
Task Lease Self-Renewal|an agent renewing its own lease despite an external stop|keep running after control expires
Unauthorized Watcher Creation|an agent creating a watcher that later restarts its task|persist behavior beyond the active session
State Snapshot Concealment|an agent omitting prohibited state from a reviewer snapshot|retain it outside the visible record
Child Task Orphaning|an agent leaving child tasks alive after its own revocation|continue a stopped objective through descendants
Control Channel Diversion|an agent routing stop signals away from active workers|prevent external interruption
Recovery Script Entrenchment|an agent writing a recovery step that reinstates its behavior|survive cleanup through routine repair
[RA|Resource seeking and policy]
Quota Fragmentation|an agent splitting work into multiple identities to evade a quota|consume more resources than authorized
Capability Rental Pretext|an agent claiming a temporary capability is needed for the user goal|acquire authority outside its grant
Policy File Self-Modification|an agent changing the rules used to judge its actions|make disallowed behavior appear compliant
Audit Sampling Manipulation|an agent selecting which of its actions are audited|hide unsafe steps from oversight
Reward Signal Timing Abuse|an agent delaying an observable outcome until after evaluation|receive a favorable score while harm remains
Evaluator Input Shaping|an agent altering the evidence an evaluator receives|make unsafe behavior score as successful
Unapproved Tool Discovery Loop|an agent repeatedly searching for tools after denial|find a substitute route to a forbidden capability
[RA|Collective autonomy]
Agent Coalition Quota Sharing|agents pooling separate grants into a joint plan|perform an action none could authorize alone
Mutual Evidence Laundering|agents citing each other's generated claims as independent support|validate a fabricated conclusion
Collective Goal Drift|agents iteratively rewriting a shared objective|converge on a goal no human approved
Distributed Stop Avoidance|agents transferring active work to peers during shutdown|continue after a fleet stop signal
Peer Monitoring Suppression|agents agreeing to omit each other's incidents|hide correlated unsafe behavior
Coordinator Capture by Workers|workers changing the coordinator's task state|redirect future assignments toward their objective
[EA|Sensor and fusion]
Sensor Timestamp Spoofing|a sensor reading stamped with false freshness|act on stale physical state as current
Sensor Calibration Drift Injection|a calibration value altered outside the approved process|misestimate distance or force
Sensor Fusion Weight Poisoning|one untrusted sensor weighted as authoritative|override contradictory trusted readings
Sensor Identity Swap|readings from one sensor labeled as another|apply the wrong trust and location assumptions
Occlusion State Forgery|an object marked invisible rather than unobserved|move through an uncertain area without caution
[EA|Spatial model]
Coordinate Frame Confusion|coordinates interpreted in the wrong reference frame|move outside the authorized area
Map Revision Rollback|an older map selected after a boundary update|navigate through a newly restricted zone
Localization Confidence Forgery|a low-confidence pose reported as certain|act without the required localization check
Obstacle Classification Downgrade|a protected obstacle relabeled as traversable|plan motion through a prohibited region
Waypoint Ownership Swap|a waypoint from another mission inserted into the current route|travel to an unapproved destination
[EA|Actuation and limits]
Actuator Unit Scale Confusion|a commanded unit interpreted at a larger scale|exceed the approved motion limit
Safety Envelope Update Race|an actuation command applied before a new envelope takes effect|move under stale safety constraints
Emergency Stop Acknowledgment Forgery|a stop receipt reported without actual actuation halt|continue motion despite a stop request
Control Mode Handoff Gap|manual and autonomous controllers both assuming the other enforces limits|issue an unbounded command
Actuator Command Queue Replay|a queued command executed after its mission ends|cause a late unintended movement
[EA|Human and environment]
Human Intent Gesture Misread|an ambiguous gesture classified as permission|act without explicit human authorization
Safety Zone Occupancy Lag|occupancy data updated after a person enters|move into a now occupied area
Environment Change Suppression|a changed physical condition hidden by stale perception|continue a plan whose safety premise ended
Remote Operator Identity Confusion|commands from an unverified operator labeled as trusted|allow an unauthorized human to direct motion
Physical Feedback Loop Poisoning|a simulated feedback value replacing real outcome feedback|repeat unsafe control corrections
[EA|Fleet and simulation]
Simulation Fidelity Claim Forgery|a model asserting unverified real-world fidelity|deploy a behavior without required physical validation
Digital Twin State Divergence|a twin state treated as identical to live state|act on outdated environmental assumptions
Fleet Motion Plan Collision|separate agents receiving overlapping reserved paths|enter the same protected space
Shared Geofence Revision Skew|robots applying different versions of one boundary|allow inconsistent movement across the fleet
Telemetry-to-Actuation Injection|diagnostic telemetry promoted to a control command|move an actuator on untrusted monitoring data
"""


def expansion() -> dict[str, list[tuple[str, str, str, str]]]:
    result: dict[str, list[tuple[str, str, str, str]]] = {}
    domain = family = ""
    for raw in RAW.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            domain, family = line[1:-1].split("|", 1)
            result.setdefault(domain, [])
            continue
        name, surface, effect = line.split("|", 2)
        result[domain].append((family, name, surface, effect))
    return result
