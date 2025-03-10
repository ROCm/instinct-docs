"""Configuration file for the Sphinx documentation builder."""
import os

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
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "instinct",
    "link_main_doc": True,
    "nav_secondary_items": {
        "Community": "https://github.com/ROCm/ROCm/discussions",
        "Blogs": "https://rocm.blogs.amd.com/",
        "ROCm&#8482 docs": "https://rocm.docs.amd.com"
    },
    # Add any additional theme options here
}
extensions = ["rocm_docs"]

html_css_files = ["css/custom.css"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

exclude_patterns = ['.venv']

def setup(app):
    app.connect("autodoc-process-docstring", cut_lines(4, what=["module"]))
    app.add_css_file("css/custom.css")
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
    fdesc = GroupedField(
        "parameter", label="Parameters", names=["param"], can_collapse=True
    )
    app.add_object_type(
        "event", "event", "pair: %s; event", parse_event, doc_field_types=[fdesc]
    )
