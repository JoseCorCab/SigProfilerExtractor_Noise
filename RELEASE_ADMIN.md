# Release Admin

This branch adds tag-driven Python package publishing with `setuptools_scm` and GitHub Actions.

## Versioning model

- Package versions come from git tags.
- A tag like `v1.2.8` produces package version `1.2.8`.
- Untagged commits on development branches produce dev versions such as `1.2.9.dev1+g<sha>.d<date>`.

## Workflow behavior

The release workflow is in [.github/workflows/release.yml](./.github/workflows/release.yml).

- Push a tag matching `v*`:
  - build sdist and wheel
  - run `twine check`
  - publish to TestPyPI
- Publish a GitHub Release:
  - build sdist and wheel
  - run `twine check`
  - publish to PyPI

This keeps TestPyPI as the first stop and PyPI as the explicit release action.

## GitHub environment setup

Create these GitHub environments in the repository:

1. `testpypi`
2. `pypi`

Recommended:

- add required reviewers for `pypi`
- optionally leave `testpypi` without reviewers for faster dry runs

Repository path:

- `Settings -> Environments`

## Trusted publishing setup

Use PyPI trusted publishing instead of API tokens.

### TestPyPI

In TestPyPI:

1. Go to account settings for trusted publishers.
2. Add a publisher for this repository.
3. Use:
   - Owner: `SigProfilerSuite`
   - Repository: `SigProfilerExtractor`
   - Workflow name: `release.yml`
   - Environment name: `testpypi`

### PyPI

In PyPI:

1. Go to project publishing settings for trusted publishers.
2. Add a publisher for this repository.
3. Use:
   - Owner: `SigProfilerSuite`
   - Repository: `SigProfilerExtractor`
   - Workflow name: `release.yml`
   - Environment name: `pypi`

If the project does not yet exist on TestPyPI or PyPI, create the trusted publisher entry from the publisher setup page for a new project with the project name:

- `SigProfilerExtractor`

## Release flow

### TestPyPI dry run

1. Merge release-ready changes into `master`.
2. Create and push a tag:
   - `git tag -a v1.2.8 -m "v1.2.8"`
   - `git push origin v1.2.8`
3. Confirm TestPyPI publish succeeds.

### PyPI publish

1. Create a GitHub Release from the same tag `v1.2.8`.
2. Publish the GitHub Release.
3. Confirm the PyPI publish job succeeds.

## Notes

- Do not hardcode a package version in `setup.py`.
- If you need the package version locally, create a tag or inspect the generated dev version.
- The CI workflow remains separate from publishing; only the release workflow handles package uploads.
