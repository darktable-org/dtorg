# -*- coding: utf-8 -*-
"""
Markdown Image Compare Extension For Pelican
=====================================
Extends Pelican's Markdown module
to support COMPIMG() function for
inserting image comparison with a
slider and the required js + css.
"""

import os
import sys

import logging
logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

from pelican import signals
from pelican.generators import StaticGenerator, Generator

try:
    from . pelican_image_compare_markdown_extension import PelicanImageCompareMarkdownExtension
except ImportError as e:
    PelicanImageCompareMarkdownExtension = None
    print("\nMarkdown is not installed - image compare Markdown extension disabled\n")


def process_settings(pelicanobj):
    """Sets user specified settings (see README for more details)"""
    image_compare_settings = {}

    return image_compare_settings


def image_compare_markdown_extension(pelicanobj, config):
    """Instantiates a customized Markdown extension"""

    # Instantiate Markdown extension and append it to the current extensions
    try:
        if isinstance(pelicanobj.settings.get('MD_EXTENSIONS'), list):  # pelican 3.6.3 and earlier
            pelicanobj.settings['MD_EXTENSIONS'].append(PelicanImageCompareMarkdownExtension(config))
        else:
            pelicanobj.settings['MARKDOWN'].setdefault('extensions', []).append(PelicanImageCompareMarkdownExtension(config))
    except:
        sys.excepthook(*sys.exc_info())
        sys.stderr.write("\nError - the pelican Markdown extension failed to configure. Image compare Markdown extension is non-functional.\n")
        sys.stderr.flush()


def pelican_init(pelicanobj):
    """Loads settings and instantiates the Python Markdown extension"""

    # If there was an error loading Markdown, then do not process any further
    if not PelicanImageCompareMarkdownExtension:
        return

    # Process settings
    config = process_settings(pelicanobj)

    # Configure Markdown Extension
    image_compare_markdown_extension(pelicanobj, config)


def register():
    """Plugin registration"""
    signals.initialized.connect(pelican_init)
