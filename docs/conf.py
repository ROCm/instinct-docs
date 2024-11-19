import os
import sys

# Path setup
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Dummy Project'
author = 'Your Name'
release = '0.1'

# General configuration
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']
templates_path = ['_templates']
exclude_patterns = []

# Options for HTML output
html_theme = 'alabaster'
html_static_path = ['_static']

