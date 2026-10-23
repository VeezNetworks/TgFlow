import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "TgFlow"
copyright = "2026, TgFlow Project"
author = "TgFlow Authors"
release = "1.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = "TgFlow Documentation"
html_logo = "_static/logo.png"
html_static_path = ["_static"]

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
}

autodoc_member_order = "bysource"
autodoc_typehints = "description"
