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
html_copy_source = True
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "instinct",
    "link_main_doc": False,
    "repository_url": "https://github.com/rocm/instinct-docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "nav_secondary_items": {
        "Community": "https://github.com/ROCm/ROCm/discussions",
        "Blogs": "https://rocm.blogs.amd.com/",
        "ROCm&#8482 Docs": "https://rocm.docs.amd.com",
        "ROCm Developer Hub": "https://www.amd.com/en/developer/resources/rocm-hub.html",
    },
    # Add any additional theme options here
}
html_title = "Systems and Infrastructure"
extensions = ["rocm_docs", "sphinx_reredirects"]

html_static_path = ['_static', 'images']

html_css_files = ["index.css"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

exclude_patterns = ['.venv']

# Redirects for pages removed in favor of the canonical ROCm-hosted docs.
# sphinx-reredirects generates a static meta-refresh/JS redirect file at each
# old docname's build path, so old bookmarks/links land on the live page
# instead of 404ing.
redirects = {
    "gpu-arch/gpu-arch": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/index.html",
    "gpu-arch/mi100": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi100.html",
    "gpu-arch/mi250": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi250.html",
    "gpu-arch/mi300": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi300.html",
    "gpu-arch/mi300-mi200-performance-counters": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi300-mi200-performance-counters.html",
    "gpu-arch/mi350": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi350.html",
}

# Generate llms.txt and llms-full.txt after each build (the llms.txt standard,
# https://llmstxt.org/). See the rocm-docs-core guide:
# https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/user_guide/llms.html
rocm_docs_generate_llms = True

# Pages (by docname) whose primary (left) sidebar should be collapsed by default.
# #pst-primary-sidebar-checkbox restores the sidebar.

COLLAPSE_PRIMARY_SIDEBAR = {"system-admin/cluster"}

_COLLAPSE_SIDEBAR_STYLE = """
<style id="default-collapsed-primary-sidebar">
  html .bd-container .bd-sidebar-primary {
    margin-left: -20%;
    opacity: 0;
    visibility: hidden;
  }
  html body #pst-primary-sidebar-checkbox:checked ~ .bd-container .bd-sidebar-primary {
    margin-left: 0;
    opacity: 1;
    visibility: visible;
  }
  html body .prev-next-footer {
    display: none;
  }
</style>
"""


def collapse_primary_sidebar(app, pagename, templatename, context, doctree):
    if pagename in COLLAPSE_PRIMARY_SIDEBAR:
        context["metatags"] = context.get("metatags", "") + _COLLAPSE_SIDEBAR_STYLE


def setup(app):
    app.add_css_file("css/index.css")
    app.connect("html-page-context", collapse_primary_sidebar)
