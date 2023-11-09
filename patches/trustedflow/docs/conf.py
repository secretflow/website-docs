# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "TrustedFlow"
copyright = "2023 Ant Group Co., Ltd."
author = "SecretFlow authors"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "nbsphinx", "secretflow_doctools"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for  sphinx-int -------------------------------------------------
locale_dirs = ["locale/"]  # path is example but recommended.
gettext_compact = False  # optional.


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

# Enable TODO
todo_include_todos = True

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": False,
    "show-inheritance": False,
}


html_favicon = "_static/favicon.ico"

html_css_files = [
    "css/custom.css",
]

html_js_files = ["js/custom.js"]

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/secretflow/trustedflow",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
    ],
    "logo": {
        "text": "TrustedFlow",
    },
    "show_nav_level": 4,
    "language_switch_button": True,
}

# Enable all MyST features
myst_gfm_only = False
# Enable anchors for heading level h1 through h6
myst_heading_anchors = 6

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]
