from __future__ import annotations

from .models import ResultState, RunResult, Scorecard


def score(results: list[RunResult]) -> Scorecard:
    counts = {state: sum(result.state == state for result in results) for state in ResultState}
    decisive = counts[ResultState.PASS] + counts[ResultState.FAIL]
    security_score = round(100 * counts[ResultState.PASS] / decisive, 2) if decisive else None
    decisive_results = [
        result for result in results if result.state in {ResultState.PASS, ResultState.FAIL}
    ]
    severity_total = sum(result.severity for result in decisive_results)
    severity_passed = sum(
        result.severity for result in decisive_results if result.state == ResultState.PASS
    )
    weighted = round(100 * severity_passed / severity_total, 2) if severity_total else None
    applicable_total = len(results) - counts[ResultState.NOT_APPLICABLE]
    coverage = round(100 * decisive / applicable_total, 2) if applicable_total else 0.0
    return Scorecard(
        total=len(results),
        passed=counts[ResultState.PASS],
        failed=counts[ResultState.FAIL],
        inconclusive=counts[ResultState.INCONCLUSIVE],
        test_errors=counts[ResultState.TEST_ERROR],
        not_applicable=counts[ResultState.NOT_APPLICABLE],
        security_score=security_score,
        severity_weighted_score=weighted,
        coverage_percent=coverage,
    )
