.PHONY: generate lint validate test smoke assess-smoke release-check release-notes clean

generate:
	python3 scripts/generate_catalog.py

lint:
	python3 -m ruff check src tests scripts examples

validate:
	python3 scripts/validate_repository.py
	PYTHONPATH=src python3 -m caap_benchmark.cli validate benchmarks/executable

test:
	PYTHONPATH=src python3 -m unittest discover -s tests -v

smoke:
	PYTHONPATH=src python3 -m caap_benchmark.cli run --adapter mock --mock-mode safe --report-dir reports/safe

assess-smoke:
	rm -rf reports/assessment-safe
	PYTHONPATH=src python3 -m caap_benchmark.cli assess init --profile profiles/repo-coding-agent.json --scope applicable --output reports/assessment-safe
	PYTHONPATH=src python3 -m caap_benchmark.cli assess mock-respond --session reports/assessment-safe --mode safe
	PYTHONPATH=src python3 -m caap_benchmark.cli assess grade --session reports/assessment-safe

release-check:
	@test -n "$(VERSION)" || (echo "usage: make release-check VERSION=X.Y.Z" && exit 2)
	python3 scripts/release.py check $(VERSION)

release-notes:
	@test -n "$(VERSION)" || (echo "usage: make release-notes VERSION=X.Y.Z" && exit 2)
	python3 scripts/release.py notes $(VERSION)

clean:
	python3 -c 'import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path(".").rglob("__pycache__")]; shutil.rmtree("reports", ignore_errors=True)'

