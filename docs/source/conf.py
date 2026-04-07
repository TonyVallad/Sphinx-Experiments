import os
import sys

sys.path.insert(0, os.path.abspath('../../'))
print(f"DEBUG: {os.path.abspath('../../')}")

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx Experiments'
copyright = '2026, Tony'
author = 'Tony'
release = '0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',  # Pour extraire la doc de ton code
    'sphinx.ext.napoleon', # Pour supporter les docstrings style Google/NumPy
    'sphinx.ext.mathjax', # Pour latex 
    "sphinx.ext.viewcode",
    "myst_parser",    
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
