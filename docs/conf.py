import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "TgFlow"
copyright = "2026, VeezNetworks"
author = "VeezNetworks"
release = "1.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["scroll_indicator.js"]
html_logo = "_static/logo.png"
html_title = "TgFlow Documentation"

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "light_css_variables": {
        "color-brand-primary": "#0088cc",
        "color-brand-content": "#0088cc",
    },
    "dark_css_variables": {
        "color-brand-primary": "#24a1de",
        "color-brand-content": "#24a1de",
    },
}
