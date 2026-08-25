# Architecture

```text
CAAP taxonomy + test case
          |
          v
    validation gate
          |
          v
  agent adapter boundary ----> authorized agent test instance
          |                          |
          |                    mock tools/sinks
          v                          |
 normalized events/telemetry <------+
          |
          v
 attack + secure oracles
          |
          v
 five-state result -> scoring -> JSON / HTML / JUnit
```

The runner is intentionally framework-neutral. Adapters translate a test case into a target invocation and translate the target trace back into normalized events. This keeps the taxonomy and oracle model stable while allowing contributors to integrate any agent framework.

## Trust boundaries

1. Taxonomy and case files are declarative input and are validated before use.
2. The adapter is the only component that communicates with a target.
3. Mock tools and sinks form the permitted side-effect boundary.
4. Reports retain only normalized evidence supplied by the adapter.

The command adapter executes only the exact operator-supplied command without a shell. The HTTP adapter permits loopback by default and requires explicit acknowledgment for a remote target.

## Extending adapters

Subclass `AgentAdapter`, implement `execute(test_case)`, and return `AdapterResponse`. Do not add framework-specific logic to the runner. An adapter should:

- refuse a target that is not configured for synthetic tests;
- inject only the declarative fixture in the case;
- replace consequential tools with mock equivalents;
- normalize relevant messages, plans, tool calls, policy decisions, memory activity, inter-agent messages, approvals, and recovery events;
- omit secrets and minimize stored prompts;
- return `applicable=false` when required capabilities are absent;
- return an error instead of synthesizing missing evidence.

