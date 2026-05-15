"""Configuration file for the Sphinx documentation builder."""
import os
from sphinx import addnodes
from pathlib import Path
import shutil

external_projects_remote_repository = ""
external_projects_current_project = "dcgpu"
external_projects = ["gpu-operator", "device-metrics-exporter"]
external_projects_path = "projects.yaml"

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "instinct.docs.amd.com")
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
project = "instinct"

version = "1.0.0"
release = version
html_title = ""
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved."

# Required settings
html_copy_source = True
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "instinct",
    "link_main_doc": True,
    "use_download_button": True,
    "nav_secondary_items": {
        "Community": "https://github.com/ROCm/ROCm/discussions",
        "Blogs": "https://rocm.blogs.amd.com/",
        "ROCm&#8482 Docs": "https://rocm.docs.amd.com",
        "ROCm Developer Hub": "https://www.amd.com/en/developer/resources/rocm-hub.html",
    },
    # Add any additional theme options here
}
extensions = ["rocm_docs"]

html_static_path = ['_static', 'images']

html_css_files = ["index.css"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

exclude_patterns = ['.venv']

EXCLUDED_DIRS = {
    "_build",
    "_templates",
    "_static",
    ".git",
    ".venv",
}

def should_skip(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.parts)


def generate_combined_markdown(app, exception):
    if exception:
        return

    docs_root = Path(app.srcdir)
    output_file = Path(app.outdir) / "llms.txt"
    base_file = docs_root / "llms.txt"

    combined = []

    if base_file.exists():
        combined.append(base_file.read_text(encoding="utf-8"))
    else:
        combined.append("# AMD Instinct Data Center GPU Documentation\n")

    all_files = sorted(docs_root.rglob("*.md"))

    for doc_file in all_files:
        if should_skip(doc_file):
            continue

        if doc_file == base_file:
            continue

        relative = doc_file.relative_to(docs_root)

        combined.append(f"\n---\n")
        combined.append(f"\n# {relative}\n")

        try:
            content = doc_file.read_text(encoding="utf-8")
            combined.append(content)
            combined.append("\n")

        except Exception as e:
            combined.append(f"\n[ERROR reading file: {e}]\n")

    output_file.write_text(
        "\n".join(combined),
        encoding="utf-8",
    )

def setup(app):
    app.add_css_file("css/index.css")
    app.connect("build-finished", generate_combined_markdown)
