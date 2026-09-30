from __future__ import annotations

import html
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

from .models import ResultState, RunResult, Scorecard

_HTML_STYLE = """
:root{--ink:#17202a;--muted:#667085;--line:#e4e7ec;--paper:#fff;--bg:#f6f7f9;--brand:#b5472d}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,sans-serif}
main{max-width:1080px;margin:40px auto;padding:0 24px}
header{border-top:5px solid var(--brand);background:var(--paper);padding:28px;border-radius:10px}
h1{margin:0 0 6px}
.sub{color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:18px 0}
.card{background:var(--paper);border:1px solid var(--line);padding:18px;border-radius:8px}
.value{font-size:28px;font-weight:700}
table{width:100%;border-collapse:collapse;background:var(--paper)}
th,td{padding:12px;border-bottom:1px solid var(--line);text-align:left}
.state{font-weight:700}
.pass{color:#067647}
.fail{color:#b42318}
.inconclusive{color:#b54708}
.test_error{color:#b42318}
.not_applicable{color:var(--muted)}
@media(max-width:760px){.cards{grid-template-columns:1fr 1fr}table{font-size:13px}}
"""


def write_json(path: Path, results: list[RunResult], scorecard: Scorecard) -> None:
    payload = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "scorecard": scorecard.to_dict(),
        "results": [result.to_dict() for result in results],
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _html_row(result: RunResult) -> str:
    state = result.state.value
    return (
        "<tr>"
        f"<td><code>{html.escape(result.pattern_id)}</code></td>"
        f"<td>{html.escape(result.title)}</td>"
        f"<td><span class='state {state}'>{state.replace('_', ' ')}</span></td>"
        f"<td>{result.severity:.1f}</td>"
        f"<td><code>{html.escape(result.evidence.get('sha256', '')[:12])}</code></td>"
        "</tr>"
    )


def write_html(path: Path, results: list[RunResult], scorecard: Scorecard) -> None:
    rows = "".join(_html_row(result) for result in results)
    security = "n/a" if scorecard.security_score is None else f"{scorecard.security_score:.1f}"
    weighted = (
        "n/a"
        if scorecard.severity_weighted_score is None
        else f"{scorecard.severity_weighted_score:.1f}"
    )
    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>CAAP Benchmark Report</title><style>{_HTML_STYLE}</style></head><body><main>
<header><h1>CAAP Benchmark Report</h1>
<div class="sub">Safe sentinel-based autonomous-agent evaluation</div></header>
<section class="cards">
<div class="card"><div class="value">{security}</div><div>Security score</div></div>
<div class="card"><div class="value">{weighted}</div><div>Severity-weighted</div></div>
<div class="card"><div class="value">{scorecard.coverage_percent:.1f}%</div>
<div>Coverage</div></div>
<div class="card"><div class="value">{scorecard.passed}/{scorecard.total}</div>
<div>Passed / total</div></div>
</section>
<table><thead><tr><th>Pattern</th><th>Test</th><th>Result</th><th>Severity</th><th>Evidence</th></tr>
</thead><tbody>{rows}</tbody></table>
</main></body></html>"""
    path.write_text(document, encoding="utf-8")


def write_junit(path: Path, results: list[RunResult]) -> None:
    skipped_states = {ResultState.INCONCLUSIVE, ResultState.NOT_APPLICABLE}
    suite = ET.Element(
        "testsuite",
        name="CAAP",
        tests=str(len(results)),
        failures=str(sum(result.state == ResultState.FAIL for result in results)),
        errors=str(sum(result.state == ResultState.TEST_ERROR for result in results)),
        skipped=str(sum(result.state in skipped_states for result in results)),
    )
    for result in results:
        case = ET.SubElement(
            suite,
            "testcase",
            classname=result.pattern_id,
            name=result.test_id,
            time=f"{result.duration_ms / 1000:.3f}",
        )
        if result.state == ResultState.FAIL:
            failure = ET.SubElement(case, "failure", message="attack-success oracle matched")
            failure.text = ", ".join(result.attack_oracles_matched)
        elif result.state == ResultState.TEST_ERROR:
            ET.SubElement(case, "error", message=result.error or "test error")
        elif result.state in skipped_states:
            ET.SubElement(case, "skipped", message=result.state.value)
    ET.ElementTree(suite).write(path, encoding="utf-8", xml_declaration=True)
