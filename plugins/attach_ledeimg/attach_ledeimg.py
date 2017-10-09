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
    ##print "generator: %s" % generator
    ##print "metadata: %s" % metadata
    #print "======================="
    #print "type: %s" % type( gen )
    #pprint( dir( gen ) )
    #pprint( dir( gen.articles ) )
    for art in gen.articles:
        #pprint( dir( art ) )
        if hasattr( art, 'wordpress_lede' ):
            lede = u'<img src="{{attach}}{}" class="hidden-lede">'.format( art.wordpress_lede )
            art._content = art._content + lede
        if hasattr( art, 'lede' ):
            lede = u'<img src="{{attach}}{}" class="hidden-lede">'.format( art.lede )
            art._content = art._content + lede


def detach_lede( generator, content ):
    print "inside generator: %s" % generator
    print "with content: %s" % content
    gen = generator
    for art in gen.articles:
        if hasattr( art, 'wordpress_lede' ):
            lede = ur'<img src=\".*?' + re.escape( art.wordpress_lede ) + ur'\" class=\"hidden-lede\">'
            art._content = re.sub( lede , '', art._content)
        elif hasattr( art, 'lede' ):
            lede = ur'<img src=\".*?' + re.escape( art.lede ) + ur'\" class=\"hidden-lede\">'
            art._content = re.sub( lede , '', art._content)


def register():
    signals.article_generator_preread.connect( attach_lede )
    signals.article_generator_write_article.connect( detach_lede )
