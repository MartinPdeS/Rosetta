#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from sphinx_gallery.sorting import FileNameSortKey
from MPSPlots.styles import use_mpsplots_style
import RosettaX

from RosettaX.directories import project_path, doc_css_path


sys.path.insert(0, project_path)
sys.path.insert(0, project_path.joinpath('Rosetta'))


def setup(app):
    app.add_css_file(str(doc_css_path))


autodoc_mock_imports = [
    'numpy',
    'matplotlib',
    'scipy',
    'numpydoc',
]


project = 'Rosetta'
copyright = '2023, Martin Poinsinet de Sivry-Houle'
author = 'Martin Poinsinet de Sivry-Houle'


version = RosettaX.__version__


extensions = [
    'sphinx.ext.mathjax',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
]

# Napoleon settings for docstrings
napoleon_google_docstring = False
napoleon_numpy_docstring = True


def reset_mpl(gallery_conf, fname):
    use_mpsplots_style()


examples_files = [
    'workflow'
]


sphinx_gallery_conf = {
    "examples_dirs": ['../examples/' + f for f in examples_files],
    "gallery_dirs": ['gallery/' + f for f in examples_files],
    'image_scrapers': ('matplotlib'),
    'filename_pattern': '',
    'ignore_pattern': '/__',
    'plot_gallery': True,
    'thumbnail_size': [600, 600],
    'download_all_examples': False,
    'reset_modules': reset_mpl,
    'line_numbers': False,
    'remove_config_comments': True,
    'within_subsection_order': FileNameSortKey,
    'capture_repr': ('_repr_html_', '__repr__'),
    'nested_sections': True,
}


autodoc_default_options = {
    'members': False,
    'members-order': 'bysource',
    'undoc-members': False,
    'show-inheritance': True,
}

autosectionlabel_prefix_document = True
numpydoc_show_class_members = False
add_module_names = False

source_suffix = '.rst'
master_doc = 'index'
language = 'en'
highlight_language = 'python3'
html_theme = "pydata_sphinx_theme"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
exclude_trees = []
# default_role = "autolink"
pygments_style = "sphinx"

# -- Sphinx-gallery configuration --------------------------------------------
major, minor = version[:2]
binder_branch = f"v{major}.{minor}.x"

html_theme_options = {
    # Navigation bar
    "logo": {
        "alt_text": "RosettaX's logo",
        "text": "RosettaX",
        "link": "https://rosetta.readthedocs.io/en/master/",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/MartinPdeS/RosettaX",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/rosettax/",
            "icon": "fa-solid fa-box",
        },
        {
            "name": "Anaconda",
            "url": "https://anaconda.org/MartinPdeS/rosettax",
            "icon": "fa-brands fa-python",
        },
    ],
    "navbar_align": "left",
    "navbar_end": ["version-switcher", "navbar-icon-links"],
    "show_prev_next": False,
    "show_version_warning_banner": True,
    # Footer
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version", "theme-version"],
    # Other
    "pygment_light_style": "default",
    "pygment_dark_style": "github-dark",
}

htmlhelp_basename = 'RosettaXdoc'

latex_elements = {}


latex_documents = [
    (master_doc, 'RosettaX.tex', 'RosettaX Documentation',
     'Martin Poinsinet de Sivry-Houle', 'manual'),
]

man_pages = [
    (master_doc, 'supymode', 'RosettaX Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'RosettaX', 'RosettaX Documentation',
     author, 'RosettaX', 'One line description of project.',
     'Miscellaneous'),
]

epub_title = project

html_static_path = ['_static']
templates_path = ['_templates']
html_css_files = ['default.css']
epub_exclude_files = ['search.html']

# -
