.PHONY: generate lint validate test smoke assess-smoke clean

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

clean:
	python3 -c 'import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path(".").rglob("__pycache__")]; shutil.rmtree("reports", ignore_errors=True)'

