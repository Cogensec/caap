# Releasing

Releases are tracked on the GitHub Releases page. Each one is a git tag `vX.Y.Z` on `main`, built and published by the release workflow with the wheel, the source distribution, the canonical taxonomy JSON and YAML, the JSON Schemas, and a `SHA256SUMS` file, plus release notes taken verbatim from `CHANGELOG.md`.

## Two version numbers

- **Software version** (`X.Y.Z`): the `caap-benchmark` package. It lives in `pyproject.toml`, `src/caap_benchmark/versions.py` (`PACKAGE_VERSION`), the README status line, and `CHANGELOG.md`. Tags and releases carry this number. Before `1.0.0`, a minor bump may change CLI or report fields; a patch bump never does.
- **Taxonomy version** (`TAXONOMY_VERSION` in `versions.py`, `docs/STANDARD.md`, and every record): the CAAP-200 working taxonomy, for example `2.0.0-draft.1`. It changes only through a standards decision under `GOVERNANCE.md`, and every software release states which taxonomy version it implements. A taxonomy change is listed in the changelog like any other change.

A pre-release uses a suffix, for example `0.2.0-rc.1`; the workflow marks it as a pre-release on GitHub.

## Cutting a release

Every change on `main` must already have an entry under `## [Unreleased]` in `CHANGELOG.md`; that is checked at pull-request review, not at release time.

1. Start from an up-to-date `main` and create a branch named `release/vX.Y.Z`.
2. Run the bump, which sets the version in every location and moves the unreleased entries into a dated section:

   ```bash
   python3 scripts/release.py bump X.Y.Z
   ```

3. Read the new changelog section as a user would and edit it for clarity. Do not add entries that are not on `main`.
4. Run the readiness check and the usual local checks:

   ```bash
   python3 scripts/release.py check X.Y.Z
   make lint validate test
   ```

5. Commit as `chore: release X.Y.Z` with your own identity and DCO sign-off, open a pull request, and merge it once CI is green.
6. Tag the merge commit on `main` and push the tag. The tag must be `v` followed by the exact version:

   ```bash
   git checkout main && git pull
   git tag -a vX.Y.Z -m "caap-benchmark X.Y.Z"
   git push origin vX.Y.Z
   ```

7. The release workflow runs the readiness check against the tag, lint, validation, tests, the generated-files check, and the build, then publishes the GitHub release with the assets and notes. If any step fails, nothing is published: fix `main`, delete the tag locally and remotely, and tag again after the fix merges.
8. After publishing, update the supported-versions statement in `SECURITY.md` if it changes.

## What `release.py check` enforces

- The version is `MAJOR.MINOR.PATCH` with an optional pre-release suffix, and the tag equals `v` plus the version.
- `pyproject.toml`, `versions.py`, and the README status line all state that version.
- `CHANGELOG.md` has a `## [X.Y.Z] - YYYY-MM-DD` section with at least one entry, and nothing is left under `[Unreleased]`.

Repository validation also checks, on every commit, that `pyproject.toml`, `versions.py`, and the README agree with each other, so version drift is caught before a release.

## Release notes

`python3 scripts/release.py notes X.Y.Z` prints the release body: a header naming the software and taxonomy versions, the changelog section for the release, and the list of assets. Keep the changelog written for users, since it is published as is.

## Yanking

A release with a defect that must not be installed is not deleted. Publish a fixed patch release, then edit the defective GitHub release to say which version supersedes it and why. Tags are never moved or reused.
