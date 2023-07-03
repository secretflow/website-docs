project = "SecretFlow"
copyright = "2023, Ant Group Co., Ltd"
author = "SecretFlow authors"

# === Sphinx ===

extensions = [
    # Link to other projects' documentation
    "sphinx.ext.intersphinx",
    # NumPy and Google style docstrings
    "sphinx.ext.napoleon",
    # Include docstrings by symbols
    "autodoc2",
    # Markdown and MyST support
    "myst_parser",
    # Shorthands for linking to external resources
    "sphinx.ext.extlinks",
]

exclude_patterns = []

# === External resources ===

extlinks = {"link:repo": ("https://github.com/secretflow/%s", "secretflow/%s")}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# === i18n ===

# Primary language
language = "zh_CN"
# Other available languages
locale_dirs = ["./locales/"]
gettext_compact = False
gettext_uuid = False
gettext_allow_fuzzy_translations = True

# === HTML ===

html_theme = "pydata_sphinx_theme"

# === MyST ===

# Automatically generate anchors for h1 (#) through h6 (######) headings
myst_heading_anchors = 6
# myst_heading_slug_func =

myst_enable_extensions = [
    # Use ::: instead of ``` for directives
    # otherwise it might not play well with formatters and highlighting
    "colon_fence",
    "smartquotes",
    "strikethrough",
    "amsmath",
    # We recommend using $...$ for inline math:
    "dollarmath",
    # Not using linkify. Authors should explicitly mark their links
    # with either <https://example.org> or [example](https://example.org)
    # "linkify",
    "deflist",
    "tasklist",
    "fieldlist",
    # Add HTML attributes to rendered elements
    "attrs_inline",
    "attrs_block",
]

# === Autodoc ===

autodoc2_packages = []
