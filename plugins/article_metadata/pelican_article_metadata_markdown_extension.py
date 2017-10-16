# -*- coding: utf-8 -*-
"""
Pelican Article Metadata Markdown Extension
==================================
An extension for the Python Markdown module that enables
the Pelican Python static site generator to add access
fields from the metadata header of other markdown files.
"""

import markdown
import re
import string
import os

from markdown.util import etree

class PelicanArticleMetadataMarkdownExtensionPattern(markdown.inlinepatterns.Pattern):
    """Inline Markdown processing"""

    def __init__(self, pelican_markdown_extension, pattern):
        super(PelicanArticleMetadataMarkdownExtensionPattern,self).__init__(pattern)
        self.config = pelican_markdown_extension.getConfig('config')


    def handleMatch(self, m):
        node = etree.Element('span')
        # TODO: do we want to assign some special class to the span?
        #node.set('class', 'article_metadata')

        content = self.config['PATH']
        field = m.group(3)
        filename = m.group(4)
        if filename[0] == '/':
            filename = filename[1:]
        filename = os.path.join(content, filename)

        search = re.compile(field + r':[\s]*(.*)')

        try:
            with open(filename, 'r') as f:
                for line in f:
                    match = search.match(line)
                    if match:
                        break
        except IOError:
            match = None

        if match:
            node.text = match.group(1)
        else:
            node.text = m.group(2)

        return node


class PelicanArticleMetadataMarkdownExtension(markdown.Extension):
    """A Markdown extension enabling processing in Markdown for Pelican"""
    def __init__(self, config):
        try:
            # Needed for Markdown versions >= 2.5
            self.config['config'] = ['{}', 'config for markdown extension']
            super(PelicanArticleMetadataMarkdownExtension,self).__init__(**config)
        except AttributeError:
            # Markdown versions < 2.5
            config['config'] = [config['config'], 'config for markdown extension']
            super(PelicanArticleMetadataMarkdownExtension, self).__init__(config)

    def extendMarkdown(self, md, md_globals):
        inline_regex = r'({article.([^}]+)}([^\s\]]+))'

        md.inlinePatterns.add('article_metadata', PelicanArticleMetadataMarkdownExtensionPattern(self, inline_regex), '_begin')
