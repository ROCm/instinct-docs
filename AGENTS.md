# AGENTS.md

## Cursor Cloud specific instructions

This repository is a **Sphinx documentation site** for AMD Instinct Data Center GPUs,
built on [`rocm-docs-core`](https://github.com/ROCm/rocm-docs-core). There is no
backend/frontend application — the "app" is the generated static HTML docs. Standard
build/serve commands live in `README.md`; only non-obvious notes are captured here.

### Environment

- The startup update script creates a Python virtualenv at `.venv/docs` and installs
  `docs/sphinx/requirements.txt` (pinned) plus `sphinx-autobuild`. Use that interpreter
  directly (e.g. `.venv/docs/bin/python`, `.venv/docs/bin/sphinx-autobuild`) or activate
  it with `source .venv/docs/bin/activate`.
- System packages already provisioned in the snapshot (do not reinstall unless missing):
  `python3.12-venv` (needed for `python3 -m venv`), and `aspell` + `aspell-en` (needed
  for the spelling lint job). Node.js is preinstalled for markdownlint via `npx`.

### Build / run (dev mode)

- One-off build: `.venv/docs/bin/python -m sphinx -b html -d _build/doctrees -D language=en ./docs/ docs/_build/html`
- Live dev server (preferred, auto-rebuilds on edits):
  `.venv/docs/bin/sphinx-autobuild -b html -d _build/doctrees -D language=en ./docs docs/_build/html --ignore "docs/_build/*" --ignore "docs/sphinx/_toc.yml" --ignore "docs/sphinx/requirements.txt" --host 0.0.0.0 --port 8000`
- The build emits ~190 warnings (mostly non-fatal cross-reference/image warnings); a
  successful build still ends with `build succeeded`.
- Gotcha: after adding a new nav/toc link, previously built pages may not show it. Delete
  `docs/_build/` and rebuild so the nav is regenerated for all pages (see README
  Troubleshooting).

### Lint (matches CI `.github/workflows/linting.yml`, which calls the rocm-docs-core
reusable workflow)

- There are **no local lint configs** in this repo; CI fetches them from `rocm-docs-core`
  at runtime. To reproduce locally:
  - Markdown: fetch `.markdownlint.yaml` from rocm-docs-core `develop`, then run
    `npx --yes markdownlint-cli2 $(git ls-files '*.md')`. Scope to git-tracked files —
    globbing `**/*.md` also lints `.venv` and `docs/_build`, which CI never sees.
  - Spelling: fetch `.spellcheck.yaml` and append rocm-docs-core's `.wordlist.txt` to the
    local `.wordlist.txt`, then run `.venv/docs/bin/pyspelling -c .spellcheck.yaml`
    (`pyspelling` + `aspell` required). Restore `.wordlist.txt` and remove the generated
    `dictionary.dic` afterward so the working tree stays clean.
