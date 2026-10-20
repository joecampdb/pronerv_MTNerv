# Optional GitHub Actions templates

The publication credential could push source but did not have GitHub's `workflow`
scope. These templates are retained here instead of implying CI is active.
All documented tests were run locally before publication.

To enable CI, use a GitHub credential with workflow permission (or the GitHub
web editor) to place `atlas-ci.yml` in `.github/workflows/`.

The current viewer deploys from the `gh-pages` branch via GitHub's built-in
Pages deployment. `pages.yml` is an optional alternative for a future switch to
Actions-based Pages. Do not enable both publication mechanisms simultaneously.

To update the current viewer after changing source, run the local checks, then
publish the contents of `alanine-nerve/dist/` to the root of `gh-pages`.
The branch contains static assets only. It should never contain credentials,
raw MD inputs, or unrelated simulation outputs.
