from __future__ import annotations

import contextlib
import io
import shutil
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import release  # noqa: E402

CHANGELOG = """# Changelog

## [Unreleased]

### Added

- A new thing.

### Fixed

- A bug.

## [0.1.0] - 2026-01-01

### Added

- First release.
"""


def _run(argv: list[str]) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = release.main(argv)
    return code, out.getvalue(), err.getvalue()


class ReleaseScriptTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / "src/caap_benchmark").mkdir(parents=True)
        (self.root / "pyproject.toml").write_text('[project]\nname = "x"\nversion = "0.1.0"\n')
        (self.root / "src/caap_benchmark/versions.py").write_text(
            'PACKAGE_VERSION = "0.1.0"\nTAXONOMY_VERSION = "2.0.0-draft.1"\n'
        )
        (self.root / "README.md").write_text("This repository is `v0.1.0` software.\n")
        (self.root / "CHANGELOG.md").write_text(CHANGELOG)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_repository_is_internally_consistent(self) -> None:
        version = release._match(release.PYPROJECT_RE, (ROOT / "pyproject.toml").read_text(), "p")
        problems = release.check(version, ROOT)
        allowed = {
            f"CHANGELOG.md has no `## [{version}] - YYYY-MM-DD` section",
            "CHANGELOG.md still has entries under [Unreleased]; move them into the release",
        }
        self.assertTrue(set(problems) <= allowed, problems)

    def test_check_reports_every_mismatch(self) -> None:
        problems = release.check("0.2.0", self.root, tag="v0.3.0")
        self.assertIn("tag v0.3.0 does not match version 0.2.0 (expected v0.2.0)", problems)
        self.assertIn("pyproject.toml says 0.1.0, expected 0.2.0", problems)
        self.assertIn("versions.py says 0.1.0, expected 0.2.0", problems)
        self.assertIn("README.md says 0.1.0, expected 0.2.0", problems)
        self.assertIn("CHANGELOG.md has no `## [0.2.0] - YYYY-MM-DD` section", problems)
        self.assertEqual(release.check("not-a-version", self.root), [
            "'not-a-version' is not a release version (expected MAJOR.MINOR.PATCH[-pre])",
        ])
        problems = release.check("0.1.0", self.root, tag="v0.1.0")
        self.assertEqual(problems, [
            "CHANGELOG.md still has entries under [Unreleased]; move them into the release",
        ])

    def test_bump_moves_unreleased_into_a_dated_section(self) -> None:
        changed = release.bump("0.2.0", self.root, today=date(2026, 9, 30))
        self.assertEqual(sorted(changed), sorted([
            "pyproject.toml", "src/caap_benchmark/versions.py", "README.md", "CHANGELOG.md",
        ]))
        self.assertIn('version = "0.2.0"', (self.root / "pyproject.toml").read_text())
        versions = (self.root / "src/caap_benchmark/versions.py").read_text()
        self.assertIn('PACKAGE_VERSION = "0.2.0"', versions)
        self.assertIn("`v0.2.0` software", (self.root / "README.md").read_text())
        changelog = (self.root / "CHANGELOG.md").read_text()
        self.assertIn(
            "## [Unreleased]\n\n_No unreleased changes yet._\n\n## [0.2.0] - 2026-09-30", changelog
        )
        self.assertIn("- A new thing.", changelog)
        self.assertEqual(release.check("0.2.0", self.root, tag="v0.2.0"), [])
        with self.assertRaises(release.ReleaseError):
            release.bump("0.2.0", self.root)  # already cut
        with self.assertRaises(release.ReleaseError):
            release.bump("0.3.0", self.root)  # nothing unreleased
        self.assertIn('version = "0.2.0"', (self.root / "pyproject.toml").read_text())

    def test_first_release_can_be_cut_at_the_current_version(self) -> None:
        (self.root / "CHANGELOG.md").write_text(
            "# Changelog\n\n## [Unreleased]\n\n### Added\n\n- Everything so far.\n"
        )
        changed = release.bump("0.1.0", self.root, today=date(2026, 9, 30))
        self.assertIn("CHANGELOG.md", changed)
        self.assertIn('version = "0.1.0"', (self.root / "pyproject.toml").read_text())
        changelog = (self.root / "CHANGELOG.md").read_text()
        self.assertIn("## [0.1.0] - 2026-09-30\n\n### Added\n\n- Everything so far.", changelog)
        self.assertEqual(release.check("0.1.0", self.root, tag="v0.1.0"), [])

    def test_refused_bump_writes_nothing(self) -> None:
        (self.root / "CHANGELOG.md").write_text("# Changelog\n\n## [Unreleased]\n\nnothing\n")
        before = (self.root / "pyproject.toml").read_text()
        with self.assertRaises(release.ReleaseError):
            release.bump("0.5.0", self.root)
        self.assertEqual((self.root / "pyproject.toml").read_text(), before)

    def test_notes_render_the_section_with_versions(self) -> None:
        text = release.notes("0.1.0", self.root)
        self.assertIn("**caap-benchmark 0.1.0 (2026-01-01)** implementing", text)
        self.assertIn("`2.0.0-draft.1`", text)
        self.assertIn("- First release.", text)
        self.assertNotIn("A new thing", text)
        self.assertIn("caap_benchmark-0.1.0-py3-none-any.whl", text)
        with self.assertRaises(release.ReleaseError):
            release.notes("9.9.9", self.root)

    def test_cli(self) -> None:
        root = str(self.root)
        code, out, _ = _run(["--root", root, "bump", "0.2.0"])
        self.assertEqual(code, 0)
        self.assertIn("updated CHANGELOG.md", out)
        code, out, _ = _run(["--root", root, "check", "0.2.0", "--tag", "v0.2.0"])
        self.assertEqual(code, 0, out)
        self.assertIn("Ready to release 0.2.0", out)
        code, _, err = _run(["--root", root, "check", "0.2.0", "--tag", "v0.2.1"])
        self.assertEqual(code, 1)
        self.assertIn("does not match", err)
        code, out, _ = _run(["--root", root, "notes", "0.2.0"])
        self.assertEqual(code, 0)
        self.assertIn("- A bug.", out)
        code, _, err = _run(["--root", root, "notes", "7.0.0"])
        self.assertEqual(code, 2)
        self.assertIn("no section", err)

    def test_bump_survives_a_copy_of_the_real_files(self) -> None:
        copy = self.root / "copy"
        (copy / "src/caap_benchmark").mkdir(parents=True)
        for name in ("pyproject.toml", "CHANGELOG.md", "README.md"):
            shutil.copy(ROOT / name, copy / name)
        relative = "src/caap_benchmark/versions.py"
        shutil.copy(ROOT / relative, copy / relative)
        release.bump("0.9.9", copy, today=date(2026, 9, 30))
        self.assertEqual(release.check("0.9.9", copy, tag="v0.9.9"), [])
        text = release.notes("0.9.9", copy)
        self.assertIn("**caap-benchmark 0.9.9 (2026-09-30)**", text)
        self.assertNotIn("Unreleased", text)


if __name__ == "__main__":
    unittest.main()
