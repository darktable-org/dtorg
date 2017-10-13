# -*- coding: utf-8 -*-
"""
Pelican Image Links Markdown Extension
==================================
An extension for the Python Markdown module that enables
the Pelican Python static site generator to add preview
images with a link to the original file.
"""

import markdown
import re
import string

from markdown.util import etree

class PelicanImageLinksMarkdownExtensionPattern(markdown.inlinepatterns.Pattern):
    """Inline Markdown processing"""

    def __init__(self, pelican_markdown_extension, pattern):
        super(PelicanImageLinksMarkdownExtensionPattern,self).__init__(pattern)
        self.config = pelican_markdown_extension.getConfig('config')


    def handleMatch(self, m):
        """
        Turn
            @![alt text](filename.jpg "A Title!")
        into
            <span>[![alt text](filename_thumb.jpg)]({attach}filename.jpg)</span>
        """
        node = etree.Element('span')
        # TODO: do we want to assign some special class to the span?
        #node.set('class', 'image_preview')

        alt = m.group(2)
        title = ''
        src = m.group(9)

        src_parts = src.split()
        if src_parts:
            src = src_parts[0]
            if src[0] == "<" and src[-1] == ">":
                src = src[1:-1]
        else:
            src = ''
        if len(src_parts) > 1:
            title = ' ' + string.join(src_parts[1:])

        src_parts = src.rsplit('.', 1)
        if len(src_parts) == 2:
            thumbnail = src_parts[0] + '_thumb' + '.' + src_parts[1]
        else:
            thumbnail = src

        node.text = '[![' + alt + '](' + thumbnail + title + ')]({attach}' + src + ')'

        return node


class PelicanImageLinksMarkdownExtension(markdown.Extension):
    """A Markdown extension enabling processing in Markdown for Pelican"""
    def __init__(self, config):
        try:
            # Needed for Markdown versions >= 2.5
            self.config['config'] = ['{}', 'config for markdown extension']
            super(PelicanImageLinksMarkdownExtension,self).__init__(**config)
        except AttributeError:
            # Markdown versions < 2.5
            config['config'] = [config['config'], 'config for markdown extension']
            super(PelicanImageLinksMarkdownExtension, self).__init__(config)

    def extendMarkdown(self, md, md_globals):
        inline_regex = r'@' + markdown.inlinepatterns.IMAGE_LINK_RE

        md.inlinePatterns.add('image_links', PelicanImageLinksMarkdownExtensionPattern(self, inline_regex), '_begin')
