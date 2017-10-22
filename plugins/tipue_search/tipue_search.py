# -*- coding: utf-8 -*-
"""
Tipue Search
============

A Pelican plugin to serialize generated HTML to JSON
that can be used by jQuery plugin - Tipue Search.

Copyright (c) Talha Mansoor
"""

from __future__ import unicode_literals

import os.path
import json
from bs4 import BeautifulSoup, SoupStrainer
from codecs import open
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

from pelican import signals


class Tipue_Search_JSON_Generator(object):

    def __init__(self, context, settings, path, theme, output_path, *null):

        self.output_path = output_path
        self.context = context
        self.siteurl = settings.get('SITEURL')
        self.tpages = settings.get('TEMPLATE_PAGES')
        self.output_path = output_path
        self.json_nodes = []


    def create_json_node(self, page):

        if getattr(page, 'status', 'published') != 'published':
            return

        soup_title = BeautifulSoup(page.title.replace('&nbsp;', ' '), 'html.parser')
        page_title = soup_title.get_text(' ', strip=True).replace('“', '"').replace('”', '"').replace('’', "'").replace('^', '&#94;')

        soup_text = BeautifulSoup(page.content, 'html.parser')
        page_text = soup_text.get_text(' ', strip=True).replace('“', '"').replace('”', '"').replace('’', "'").replace('¶', ' ').replace('^', '&#94;')
        page_text = ' '.join(page_text.split())

        page_category = page.category.name if getattr(page, 'category', 'None') != 'None' else ''

        page_url = page.url if page.url else '.'

        node = {'title': page_title,
                'text': page_text,
                'tags': page_category,
                'url': page_url}

        self.json_nodes.append(node)


    def create_tpage_node(self, srclink):

        srcfile = open(os.path.join(self.output_path, self.tpages[srclink]), encoding='utf-8')
        soup = BeautifulSoup(srcfile, 'html.parser')
        page_title = soup.title.string if soup.title is not None else ''
        page_text = soup.get_text()

        # Should set default category?
        page_category = ''
        page_url = urljoin(self.siteurl, self.tpages[srclink])

        node = {'title': page_title,
                'text': page_text,
                'tags': page_category,
                'url': page_url}

        self.json_nodes.append(node)


    def create_extra_nodes(self, folder):
        base = os.path.join(self.output_path, folder)
        search_content = SoupStrainer(id='search_content')

        for dirpath, _, filenames in os.walk(base):
            for filename in filenames:
                if filename.endswith('.html'):
                    srcfile = os.path.join(dirpath, filename)
                    with open(srcfile, 'r') as fd:
                        soup = BeautifulSoup(fd, 'html.parser', parse_only=search_content)

                        page_title = soup.find(class_='title')
                        page_title = page_title.get_text(' ', strip=True).replace('&nbsp;', ' ').replace('“', '"').replace('”', '"').replace('’', "'").replace('^', '&#94;') if page_title is not None else ''

                        page_text = soup.get_text(' ', strip=True).replace('“', '"').replace('”', '"').replace('’', "'").replace('¶', ' ').replace('^', '&#94;')
                        page_text = ' '.join(page_text.split())

                        # page_url = urljoin(self.siteurl, folder + srcfile[len(base):])
                        page_url = folder + srcfile[len(base):] # seeing the domain name for all results is annoying!

                        node = {'title': page_title,
                                'text': page_text,
                                'tags': folder,
                                'url': page_url}

                        self.json_nodes.append(node)


    def write_output(self, filename):
        path = os.path.join(self.output_path, filename)

        root_node = {'pages': self.json_nodes}

        with open(path, 'w', encoding='utf-8') as fd:
            json.dump(root_node, fd, separators=(',', ':'), ensure_ascii=False)


    def generate_output(self, writer):
        pages = self.context['pages'] + self.context['articles']

        for article in self.context['articles']:
            pages += article.translations

        for srclink in self.tpages:
            self.create_tpage_node(srclink)

        for page in pages:
            self.create_json_node(page)

        self.create_extra_nodes('usermanual')

        self.write_output('tipuesearch_content.json')

        del self.json_nodes[:]

        self.create_extra_nodes('lua-api')

        self.write_output('tipuesearch_lua_api.json')


def get_generators(generators):
    return Tipue_Search_JSON_Generator


def register():
    signals.get_generators.connect(get_generators)
