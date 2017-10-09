# -*- coding: utf-8 -*-
"""
Markdown Image Links Extension For Pelican
=====================================
Extends Pelican's Markdown module
to allow @![]() as images which are turned into
a scaled down preview image and a link to the
original file.
"""

DEFAULT_THUMBNAIL_SIZE = 600

import os
import sys

import logging
logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

from pelican import signals
from pelican.generators import StaticGenerator, Generator

try:
    from PIL import Image, ImageOps
    enabled = True
except ImportError:
    print("\nUnable to load PIL, disabling thumbnailer\n")
    enabled = False

try:
    from . pelican_image_links_markdown_extension import PelicanImageLinksMarkdownExtension
except ImportError as e:
    PelicanImageLinksMarkdownExtension = None
    print("\nMarkdown is not installed - image links Markdown extension disabled\n")


# the markdown part

def process_settings(pelicanobj):
    """Sets user specified settings (see README for more details)"""
    image_links_settings = {}

    image_links_settings['config'] = {'THUMBNAIL_SIZE': pelicanobj.settings.get('THUMBNAIL_SIZE', DEFAULT_THUMBNAIL_SIZE)}

    return image_links_settings


def image_links_markdown_extension(pelicanobj, config):
    """Instantiates a customized Markdown extension"""

    # Instantiate Markdown extension and append it to the current extensions
    try:
        if isinstance(pelicanobj.settings.get('MD_EXTENSIONS'), list):  # pelican 3.6.3 and earlier
            pelicanobj.settings['MD_EXTENSIONS'].append(PelicanImageLinksMarkdownExtension(config))
        else:
            pelicanobj.settings['MARKDOWN'].setdefault('extensions', []).append(PelicanImageLinksMarkdownExtension(config))
    except:
        sys.excepthook(*sys.exc_info())
        sys.stderr.write("\nError - the pelican Markdown extension failed to configure. Image links Markdown extension is non-functional.\n")
        sys.stderr.flush()


def pelican_init(pelicanobj):
    """Loads settings and instantiates the Python Markdown extension"""

    # If there was an error loading Markdown, then do not process any further
    if not PelicanImageLinksMarkdownExtension:
        return

    # Process settings
    config = process_settings(pelicanobj)

    # Configure Markdown Extension
    image_links_markdown_extension(pelicanobj, config)


# the code that generates the small versions of all images

def create_thumbnails(pelicanobj):
    exts = ['.jpg', '.jpeg', '.png']
    THUMBNAIL_SIZE = pelicanobj.settings.get('THUMBNAIL_SIZE', DEFAULT_THUMBNAIL_SIZE)

    for dirpath, _, filenames in os.walk(pelicanobj.settings['OUTPUT_PATH']):
        for image_filename in filenames:
            image_filename = os.path.join(dirpath, image_filename)
            (base, ext) = os.path.splitext(image_filename)
            if ext.lower() in exts:
                thumb_filename = base + '_' + str(THUMBNAIL_SIZE) + ext
                if not os.path.exists(thumb_filename):
                    try:
                        image = Image.open(image_filename)
                        if image.size[0] > THUMBNAIL_SIZE or image.size[1] > THUMBNAIL_SIZE:
                            image.thumbnail((THUMBNAIL_SIZE, THUMBNAIL_SIZE), Image.ANTIALIAS)
                            image.save(thumb_filename)
                            try:
                                logger.info("Generated Thumbnail for {0}".format(image_filename))
                            except UnicodeEncodeError:
                                logger.info("Generated Thumbnail for a file with unicode name")
                        else:
                            try:
                                logger.info("No Thumbnail for smallish {0}".format(image_filename))
                            except UnicodeEncodeError:
                                logger.info("No Thumbnail for a smallish file with unicode name")
                    except IOError:
                        try:
                            logger.warn("Generating Thumbnail for {0} failed".format(image_filename))
                        except UnicodeEncodeError:
                            logger.warn("Generating Thumbnail for a file with unicode name failed")


def register():
    """Plugin registration"""
    signals.initialized.connect(pelican_init)
    try:
        signals.finalized.connect(create_thumbnails)
    except AttributeError:
        pass
