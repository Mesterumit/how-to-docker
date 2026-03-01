# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Docker for AI/ML'
copyright = '2026, Dr. George Perdrizet'
author = 'Dr. George Perdrizet'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser',  # For Markdown support
    'sphinxcontrib.mermaid',  # For Mermaid diagrams
    'sphinx_design',  # For tabs and other design elements
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# The suffix(es) of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

# -- MyST parser configuration -----------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# Make external links open in new tabs
myst_links_external_new_tab = True
