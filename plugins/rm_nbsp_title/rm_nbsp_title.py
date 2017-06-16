from pelican import signals, contents
from pprint import pprint
import re

'''
This plugin will check for a lede-img or wordpress_lede
in the frontmatter, and {attach} it to the page so that
pelican moves the file to the same directory as the source
file
'''

def attach_lede( generator ):

    gen = generator
    for art in gen.articles:
        #print "title: %s" % art.title
        art.title = re.sub( ur'&nbsp;(\S+)$', r' \g<1>', art.title)


def register():
    signals.article_generator_pretaxonomy.connect( attach_lede )
