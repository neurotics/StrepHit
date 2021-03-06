# -*- coding: utf-8 -*-
"""
    sphinx_wikisyntax
    ~~~~~~~~~~~~~~~~~~~~

    Sphinx extension to generate documentation in wikisyntax format
"""

from builder import WikisyntaxBuilder

def setup(app):
    app.add_builder(WikisyntaxBuilder)

