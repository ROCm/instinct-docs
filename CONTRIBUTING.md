# Contributing to AMD GPU Systems and Infrastructure documentation

Thanks for your interest in improving this site. This repository is a documentation-only project built with [Sphinx](https://www.sphinx-doc.org/) and [MyST](https://myst-parser.readthedocs.io/) via [rocm-docs-core](https://github.com/ROCm/rocm-docs-core), and published through Read the Docs.

## How to propose a change

1. Fork the repository and create a branch for your change.
2. Edit or add Markdown (MyST) content under `docs/`.
3. Build and review the site locally (see below) before opening a pull request.
4. Open a pull request against the `develop` branch, describing what changed and why.

Small fixes (typos, broken links, clarifications) are welcome without prior discussion. For larger structural changes (new sections, navigation changes), please open an issue first to discuss the approach.

## Building the documentation locally

See the [README](README.md#documentation-build-guide) for full setup instructions. In short:

```bash
python3 -m venv .venv/docs
source .venv/docs/bin/activate
pip install -r docs/sphinx/requirements.txt
python3 -m sphinx -b html -d _build/doctrees -D language=en ./docs/ docs/_build/html
```

Then serve `docs/_build/html/` locally to review your changes before submitting.

## Linting and spelling

Pull requests are checked by CI for:

- **Markdown linting** — standard Markdown formatting rules.
- **Spelling** — checked against a dictionary plus this repo's [`.wordlist.txt`](.wordlist.txt). If you introduce a legitimate technical term, product name, or acronym that isn't recognized, add it to `.wordlist.txt` in the same PR.

Both checks run automatically on every pull request; please fix any reported issues before requesting review.

## Reporting issues

If you find a problem with the documentation but aren't able to submit a fix yourself, please [open an issue](../../issues) describing the page, the problem, and (if applicable) the expected content.

For security-related concerns, see [SECURITY.md](SECURITY.md) instead of filing a public issue.
