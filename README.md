# AMD Instinct Data Center GPU Documentation

Welcome to the documentation site for AMD Instinct Data Center GPUs. Targeted for system administrators and power users, this site provides comprehensive technical documentation, guides, and best practices for deploying and managing AMD Instinct Data Center GPUs. Content for GPU software development and applications including AI are located at [ROCm documentation](https://rocm.docs.amd.com).

[Instinct Docs Site](https://instinct.docs.amd.com/)

## Documentation Build Guide

This guide provides information for developers who want to contribute to the Instinct Docs site. The docs use [rocm-docs-core](https://github.com/ROCm/rocm-docs-core) as their base and the below guide will show how you can build and serve the docs locally for testing.

### Building and Serving the Docs

- Create a Python Virtual Environment (optional, but recommended)

 ```bash
 python3 -m venv .venv/docs
 ```

- Activate the Virtual Environment

 ```bash
 source .venv/docs/bin/activate # For Linux

 source .venv/docs/Scripts/activate # For Windows
 ```

- Install required packages for docs

 ```bash
 pip install -r docs/sphinx/requirements.txt
 ```

- Build the docs

 ```bash
 python3 -m sphinx -b html -d _build/doctrees -D language=en ./docs/ docs/_build/html
 ```

- Serve docs locally on port 8000

 ```bash
 python3 -m http.server -d ./docs/_build/html/
 ```

- You can now view the docs site by going to http://localhost:8000

### Auto-building the docs

The below will allow you to watch the docs directory and rebuild the documenatation each time you make a change to the documentation files:

- Install Sphinx Autobuild package

 ```bash
 pip install sphinx-autobuild
 ```

- Run the autobuild (will also serve the docs on port 8000 automatically)

 ```bash
 sphinx-autobuild -b html -d _build/doctrees -D language=en ./docs docs/_build/html --ignore "docs/_build/*" --ignore "docs/sphinx/_toc.yml" --ignore "docs/sphinx/requirements.txt"
 ```

### Troubleshooting

#### Navigation Menu not displaying new links

Note that if you've recently added a new link to the navigation menu previously unchanged pages may not correctly display the new link. To fix this delete the existing `_build/` directory and rebuild the docs so that the navigation menu will be rebuilt for all pages.
