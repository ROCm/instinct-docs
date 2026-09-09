"""Configuration file for the Sphinx documentation builder."""
import os

external_projects_remote_repository = ""
external_projects_current_project = "dcgpu"
external_projects = ["gpu-operator", "device-metrics-exporter"]
external_projects_path = "projects.yaml"

html_baseurl = os.environ.get(
    "READTHEDOCS_CANONICAL_URL",
    os.environ.get("DOCS_BASE_URL", "instinct.docs.amd.com"),
)
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
    "flavor": "instinct-design",
    "link_main_doc": True,
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

# Landing-page card layout. Loaded after the instinct-design flavor's
# own sheet so its card rules win on the index page.
html_css_files = ["index.css"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

# system-admin/_cards holds reusable `.id-card` HTML partials pulled in via
# MyST {include} directives (see docs/system-admin/*.md). They aren't
# standalone pages, so keep them out of document discovery / the toctree.
exclude_patterns = ['.venv', 'system-admin/_cards/*']

# Redirects for pages removed in favor of the canonical ROCm-hosted docs.
# sphinx-reredirects generates a static meta-refresh/JS redirect file at each
# old docname's build path, so old bookmarks/links land on the live page
# instead of 404ing.
_GSID_VERTICALS_BASE = "https://instinct.docs.amd.com/projects/gsid-verticals-docs/en/latest"

redirects = {
    "gpu-arch/gpu-arch": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/index.html",
    "gpu-arch/mi100": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi100.html",
    "gpu-arch/mi250": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi250.html",
    "gpu-arch/mi300": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi300.html",
    "gpu-arch/mi300-mi200-performance-counters": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi300-mi200-performance-counters.html",
    "gpu-arch/mi350": "https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi350.html",
    # Industries/Verticals content moved to its own project (gsid-verticals-docs).
    # Most old docnames map 1:1 to a page there; DevitoPRO and GSplat were dropped
    # or never migrated, so those two fall back to the nearest index page.
    "vision/index": f"{_GSID_VERTICALS_BASE}/vision/index.html",
    "vision/ai": f"{_GSID_VERTICALS_BASE}/vision/ai.html",
    "vision/decode": f"{_GSID_VERTICALS_BASE}/vision/decode.html",
    "vision/preprocess": f"{_GSID_VERTICALS_BASE}/vision/preprocess.html",
    "data-science/index": f"{_GSID_VERTICALS_BASE}/data-science/index.html",
    "data-science/hipDF": f"{_GSID_VERTICALS_BASE}/data-science/hipDF.html",
    "data-science/hipGRAPH": f"{_GSID_VERTICALS_BASE}/data-science/hipGRAPH.html",
    "data-science/hipVS": f"{_GSID_VERTICALS_BASE}/data-science/hipVS.html",
    "data-science/hipMM": f"{_GSID_VERTICALS_BASE}/data-science/hipMM.html",
    "data-science/hipRAFT": f"{_GSID_VERTICALS_BASE}/data-science/hipRAFT.html",
    "life-science/index": f"{_GSID_VERTICALS_BASE}/life-science/index.html",
    "life-science/hipCIM": f"{_GSID_VERTICALS_BASE}/life-science/hipCIM.html",
    "life-science/MONAI": f"{_GSID_VERTICALS_BASE}/life-science/MONAI.html",
    "finance/index": f"{_GSID_VERTICALS_BASE}/finance/index.html",
    "finance/xgboost": f"{_GSID_VERTICALS_BASE}/finance/xgboost.html",
    "finance/lightgbm": f"{_GSID_VERTICALS_BASE}/finance/lightgbm.html",
    "finance/thundergbm": f"{_GSID_VERTICALS_BASE}/finance/thundergbm.html",
    "isv-apps/index": f"{_GSID_VERTICALS_BASE}/isv-apps/index.html",
    "isv-apps/ansys-fluent": f"{_GSID_VERTICALS_BASE}/isv-apps/ansys-fluent.html",
    "isv-apps/ansys-mechanical": f"{_GSID_VERTICALS_BASE}/isv-apps/ansys-mechanical.html",
    "isv-apps/cadence-fidelity": f"{_GSID_VERTICALS_BASE}/isv-apps/cadence-fidelity.html",
    "isv-apps/devito": f"{_GSID_VERTICALS_BASE}/isv-apps/index.html",
    "isv-apps/siemens": f"{_GSID_VERTICALS_BASE}/isv-apps/siemens.html",
    "isv-apps/stone-ridge": f"{_GSID_VERTICALS_BASE}/isv-apps/stone-ridge.html",
    "simulation/gsplat": f"{_GSID_VERTICALS_BASE}/index.html",
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
    app.connect("html-page-context", collapse_primary_sidebar)
