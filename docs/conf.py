# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# -- Project information -----------------------------------------------------

project = "Executable Book Project"
copyright = "2020, Executable Book Project"
author = "Executable Book Project"

master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["myst_nb", "sphinx_panels", "ablog"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# ablog configuration
import ablog
fontawesome_included = True
blog_path = "updates"
blog_title = "EBP Updates"
blog_baseurl = "https://predictablynoisy.com"
blog_feed_archives = True

# Jupyter Notebooks configuration
jupyter_execute_notebooks = "force"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Custom scripts ----------------------------------------------------------

from subprocess import run
from pathlib import Path
import requests

# Update the team page from github membership
run(f"python {Path(__file__).parent.joinpath('update_team.py')}".split())
# Grab the latest contributing docs
url_contributing = "https://raw.githubusercontent.com/executablebooks/.github/master/CONTRIBUTING.md"
resp = requests.get(url_contributing, allow_redirects=True)
Path('contributing.md').write_bytes(resp.content)


def setup(app):
    app.add_css_file("custom.css")