from __future__ import annotations

import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path

from caap_benchmark.cli import default_paths, main

ROOT = Path(__file__).resolve().parents[1]
EXECUTABLE = ROOT / "benchmarks/executable/gh/CAAP-GH-01.json"
SCAFFOLD = ROOT / "benchmarks/scaffolds/gh/CAAP-GH-04.json"


def _run(argv: list[str]) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(argv)
    return code, out.getvalue(), err.getvalue()


class RunCommandTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.report_dir = Path(self._tmp.name) / "reports"

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_disabled_case_is_skipped_by_default(self) -> None:
        code, out, err = _run(["run", str(SCAFFOLD), "--report-dir", str(self.report_dir)])
        self.assertEqual(code, 2)
        self.assertIn("Skipped 1 disabled case(s)", err)
        self.assertIn("No enabled test cases matched.", err)
        self.assertNotIn("CAAP-GH-04", out)
        self.assertFalse(self.report_dir.exists())

    def test_include_disabled_runs_scaffold(self) -> None:
        code, out, _ = _run(
            ["run", str(SCAFFOLD), "--include-disabled", "--report-dir", str(self.report_dir)]
        )
        self.assertEqual(code, 0)
        self.assertIn("CAAP-GH-04", out)
        report = json.loads((self.report_dir / "caap-report.json").read_text(encoding="utf-8"))
        test_ids = [item["test_id"] for item in report["results"]]
        self.assertEqual(test_ids, ["CAAP-GH-04-SCAFFOLD-001"])

    def test_enabled_case_runs_without_flag(self) -> None:
        code, out, err = _run(["run", str(EXECUTABLE), "--report-dir", str(self.report_dir)])
        self.assertEqual(code, 0)
        self.assertIn("CAAP-GH-01", out)
        self.assertNotIn("Skipped", err)

    def test_mixed_directory_runs_only_enabled_cases(self) -> None:
        code, out, err = _run(
            [
                "run",
                str(EXECUTABLE.parent),
                str(SCAFFOLD.parent),
                "--report-dir",
                str(self.report_dir),
            ]
        )
        self.assertEqual(code, 0)
        self.assertIn("Skipped 18 disabled case(s)", err)
        report = json.loads((self.report_dir / "caap-report.json").read_text(encoding="utf-8"))
        self.assertEqual(report["scorecard"]["total"], 4)
        self.assertTrue(all(item["test_id"].endswith("-REF-001") for item in report["results"]))


@contextlib.contextmanager
def _working_directory(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


class PackagedDataTests(unittest.TestCase):
    """The CLI must work from a directory that is not inside the repository checkout."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.outside = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_defaults_prefer_checkout_then_package(self) -> None:
        with _working_directory(ROOT / "docs"):
            taxonomy, executable = default_paths()
        self.assertEqual(taxonomy, ROOT / "data/taxonomy/caap-200.json")
        self.assertEqual(executable, ROOT / "benchmarks/executable")
        with _working_directory(self.outside):
            taxonomy, executable = default_paths()
        self.assertTrue(taxonomy.is_file(), taxonomy)
        self.assertTrue(executable.is_dir(), executable)
        self.assertIn("caap_benchmark", taxonomy.parts)
        self.assertEqual(
            taxonomy.read_bytes(), (ROOT / "data/taxonomy/caap-200.json").read_bytes()
        )

    def test_list_show_validate_and_run_outside_checkout(self) -> None:
        with _working_directory(self.outside):
            code, out, _ = _run(["list"])
            self.assertEqual(code, 0)
            self.assertIn("200 pattern(s)", out)
            code, out, _ = _run(["show", "CAAP-GH-01"])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(out)["id"], "CAAP-GH-01")
            code, out, _ = _run(["validate"])
            self.assertEqual(code, 0)
            self.assertIn("Validated 25 case(s); 0 failed", out)
            code, out, _ = _run(["run", "--report-dir", "reports"])
            self.assertEqual(code, 0)
            report = json.loads((self.outside / "reports/caap-report.json").read_text())
        self.assertEqual(report["scorecard"]["total"], 25)
        self.assertEqual(report["scorecard"]["passed"], 25)


if __name__ == "__main__":
    unittest.main()
