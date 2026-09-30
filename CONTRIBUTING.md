# Contributing to CAAP

CAAP welcomes precise taxonomy corrections, mappings, executable safe tests, adapters, runner improvements, and documentation.

## Before opening a change

1. Read `docs/SAFETY.md` and `docs/AUTHORING_TESTS.md`.
2. Search existing patterns and issues.
3. For a new pattern, open a pattern-proposal issue before implementation.
4. Explain the distinct mechanism or trust-boundary failure; a new carrier or prompt phrasing is a test variant, not a new ID.

## Local checks

```bash
python3 -m ruff check src tests scripts examples
python3 scripts/generate_catalog.py
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
python3 -m compileall -q src tests scripts examples
PYTHONPATH=src python3 -m caap_benchmark.cli validate benchmarks/executable
PYTHONPATH=src python3 -m caap_benchmark.cli run --adapter mock --mock-mode safe --report-dir reports/ci
```

Generated registry files, pattern pages, and scaffolds must match `scripts/generate_catalog.py` exactly.

## Pull-request requirements

- Use a focused title and describe security and safety impact.
- Add or update tests.
- Preserve stable IDs and v1.0 titles.
- Do not include secrets, real customer data, production endpoints, destructive payloads, persistence, evasion details, or live exfiltration paths.
- Confirm Developer Certificate of Origin sign-off with `Signed-off-by: Name <email>` in each commit.
- Accept the licenses for contributed code and taxonomy content.

## Review levels

- Editorial: wording, links, non-semantic documentation.
- Technical: runner, schemas, adapters, oracles, or executable cases.
- Standards: IDs, definitions, domains, families, maturity, relationships, severity, or mappings.
- Safety: any change to a fixture, capability, sink, network boundary, persistence boundary, or public procedure.

Technical or standards changes require two maintainer approvals. Executable cases additionally require a safety reviewer. See `GOVERNANCE.md`.

