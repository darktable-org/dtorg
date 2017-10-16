# -*- coding: utf-8 -*-
"""
Markdown Article Metadata Extension For Pelican
=====================================
Extends Pelican's Markdown module
to allow inserting fields from the metadata
header of markdown files by using
{article.field}/path/to/file.md
"""

import os
import sys

import logging
logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

from pelican import signals
from pelican.generators import StaticGenerator, Generator

try:
    from . pelican_article_metadata_markdown_extension import PelicanArticleMetadataMarkdownExtension
except ImportError as e:
    PelicanArticleMetadataMarkdownExtension = None
    print("\nMarkdown is not installed - article metadata Markdown extension disabled\n")


def process_settings(pelicanobj):
    """Sets user specified settings (see README for more details)"""
    article_metadata_settings = {}

    article_metadata_settings['config'] = {'PATH': pelicanobj.settings['PATH']}

    return article_metadata_settings


def article_metadata_markdown_extension(pelicanobj, config):
    """Instantiates a customized Markdown extension"""

    # Instantiate Markdown extension and append it to the current extensions
    try:
        if isinstance(pelicanobj.settings.get('MD_EXTENSIONS'), list):  # pelican 3.6.3 and earlier
            pelicanobj.settings['MD_EXTENSIONS'].append(PelicanArticleMetadataMarkdownExtension(config))
        else:
            pelicanobj.settings['MARKDOWN'].setdefault('extensions', []).append(PelicanArticleMetadataMarkdownExtension(config))
    except:
        sys.excepthook(*sys.exc_info())
        sys.stderr.write("\nError - the pelican Markdown extension failed to configure. Article Metadata Markdown extension is non-functional.\n")
        sys.stderr.flush()


def pelican_init(pelicanobj):
    """Loads settings and instantiates the Python Markdown extension"""

    # If there was an error loading Markdown, then do not process any further
    if not PelicanArticleMetadataMarkdownExtension:
        return

    # Process settings
    config = process_settings(pelicanobj)

    # Configure Markdown Extension
    article_metadata_markdown_extension(pelicanobj, config)


def register():
    """Plugin registration"""
    signals.initialized.connect(pelican_init)
