# Governance

## Roles

- Maintainers manage releases, repositories, CI, and routine technical decisions.
- Domain editors curate one or more CAAP domains and evaluate mechanism distinctness.
- Safety reviewers can block any public test that exceeds the harmless-sentinel boundary.
- Contributors propose and implement changes.

Current role assignments are recorded in `MAINTAINERS.md`.

## Decisions

The project prefers documented consensus. Routine changes require one maintainer approval. Standards, schema, scoring, or executable-test changes require two approvals, including a domain editor or safety reviewer as appropriate.

If consensus cannot be reached after a seven-day review window, maintainers record alternatives and use a simple majority. The Cogensec Standards Working Group is the release authority for official CAAP standard versions. Repository releases MUST NOT describe a draft as an official standard without that approval.

## Pattern lifecycle

1. Proposal states the attacker position, mechanism, trust boundary, unsafe transition, secure behavior, and overlap analysis.
2. Triage rejects variants that do not meet the admission rule.
3. Candidate receives a stable draft ID and scaffold.
4. Reference requires reviewed specification, safe executable case, deterministic oracles, and independent reproduction.
5. Deprecation preserves the ID, rationale, replacement, and last supported version.

IDs are never reassigned or recycled.

## Releases

Every release requires clean CI, regenerated artifacts, a repository-integrity pass, changelog entry, mapping review status, and safety sign-off. Security fixes can use an expedited private process described in `SECURITY.md`.

## Appeals and conduct

A contributor can request a written reconsideration from the maintainers. Conduct is governed by `CODE_OF_CONDUCT.md`. Safety objections take precedence over release schedule.

