# -*- coding: utf-8 -*-
"""
Pelican Image Compare Markdown Extension
==================================
An extension for the Python Markdown module that enables
the Pelican Python static site generator to add image
comparisons with a slider.
"""

import markdown
import re
import string

from markdown.util import etree

class PelicanImageCompareMarkdownExtensionPattern(markdown.inlinepatterns.Pattern):
    """Inline Markdown processing"""

    def __init__(self, pelican_markdown_extension, pattern):
        super(PelicanImageCompareMarkdownExtensionPattern,self).__init__(pattern)
        self.config = pelican_markdown_extension.getConfig('config')


    def handleMatch(self, m):
        """
        Turn
            COMPIMG(div_id, image_left, image_right, label_left, label_right)
        into
            <div id="div_id" ondragstart="return false" class="cato">
              <div draggable="false" style=background-image:url("thumb_right")></div>
              <div draggable="false" style=background-image:url("thumb_left")></div>
              <div class="cato_divider"></div>
              <img draggable="false" src="thumb_left"/>
              <div><p><a href="image_left">label_left</a></p></div>
              <div><p class="cato_right"><a href="image_right">label_right</a></p></div>
            </div>
            <script type="text/javascript">createSlider("div_id"); </script>
        """
        div_id = m.group(2)
        image_left = m.group(3)
        image_right = m.group(4)
        label_left = m.group(5)
        label_right = m.group(6)

        dot = image_left.rfind('.')
        if dot >= 0:
          thumb_left = image_left[:dot] + '_thumb' + image_left[dot:]
        else:
          thumb_left = image_left

        dot = image_right.rfind('.')
        if dot >= 0:
          thumb_right = image_right[:dot] + '_thumb' + image_right[dot:]
        else:
          thumb_right = image_right

        node_wrapper = etree.Element('div')
        node_div_outer = etree.SubElement(node_wrapper, 'div', {'id': div_id, 'ondragstart': 'return false', 'class': 'cato'})
        etree.SubElement(node_div_outer, 'div', {'draggable': 'false', 'style': 'background-image:url("%s")' % thumb_right})
        etree.SubElement(node_div_outer, 'div', {'draggable': 'false', 'style': 'background-image:url("%s")' % thumb_left})
        etree.SubElement(node_div_outer, 'div', {'class': 'cato_divider'})
        etree.SubElement(node_div_outer, "img", {'draggable': 'false', 'src': '%s' % thumb_left})
        node_div_label_left_div = etree.SubElement(node_div_outer, "div")
        node_div_label_left_p = etree.SubElement(node_div_label_left_div, "p")
        etree.SubElement(node_div_label_left_p, 'a', {'href': '' + image_left}).text = label_left
        node_div_label_right_div = etree.SubElement(node_div_outer, "div")
        node_div_label_right_p = etree.SubElement(node_div_label_right_div, "p", {'class': 'cato_right'})
        etree.SubElement(node_div_label_right_p, 'a', {'href': '' + image_right}).text = label_right
        etree.SubElement(node_wrapper, 'script', {'type': 'text/javascript'}).text = 'createSlider("%s");' % div_id

        return node_wrapper


class PelicanImageCompareMarkdownExtension(markdown.Extension):
    """A Markdown extension enabling processing in Markdown for Pelican"""
    def __init__(self, config):
        try:
            # Needed for Markdown versions >= 2.5
            #self.config['config'] = ['{}', 'config for markdown extension']
            super(PelicanImageCompareMarkdownExtension,self).__init__(**config)
        except AttributeError:
            # Markdown versions < 2.5
            #config['config'] = [config['config'], 'config for markdown extension']
            super(PelicanImageCompareMarkdownExtension, self).__init__(config)

    def extendMarkdown(self, md, md_globals):
        inline_regex = r'COMPIMG\([\s]*([^,]*)[\s]*,[\s]*([^,]*)[\s]*,[\s]*([^,]*)[\s]*,[\s]*([^,]*)[\s]*,[\s]*([^,]*)[\s]*\)'

        md.inlinePatterns.add('image_compare', PelicanImageCompareMarkdownExtensionPattern(self, inline_regex), '_begin')
