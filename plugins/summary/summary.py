# -*- coding: utf-8 -*-
"""
Fix Summary Ellipsis
===========================
This plugin fixes the ellipsis added to article's summary by pelican to follow typographic conventions.
"""

from pelican import signals, contents
from pelican.utils import truncate_html_words
from pelican.generators import ArticlesGenerator

def fix_summary_ellipsis(instance):
    """
    Pelican uses '...' as the ellipsis when creating a summary.
    We want a proper ellipsis though, coupled with a non-breaking space.
    :param instance:
    :return:
    """

    # only deals with Article type
    if type(instance) != contents.Article: return

    SUMMARY_MAX_LENGTH = instance.settings.get('SUMMARY_MAX_LENGTH')

    if not (SUMMARY_MAX_LENGTH): return

    if not (hasattr(instance, '_summary') and instance._summary):
        summary = truncate_html_words(instance.content, SUMMARY_MAX_LENGTH, '&hellip;')
        instance._summary = summary.replace(' &hellip;', '&nbsp;&hellip;')


def run_plugin(generators):
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in generator.articles:
                fix_summary_ellipsis(article)


def register():
    try:
        signals.all_generators_finalized.connect(run_plugin)
    except AttributeError:
        # NOTE: This may result in #314 so shouldn't really be relied on
        # https://github.com/getpelican/pelican-plugins/issues/314
        signals.content_object_init.connect(fix_summary_ellipsis)
