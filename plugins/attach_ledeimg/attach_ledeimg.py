from pelican import signals, contents
from pprint import pprint
import re

'''
This plugin will check for a lede-img or wordpress_lede
in the frontmatter, and {attach} it to the page so that
pelican moves the file to the same directory as the source
file.

It will also go back through the files and remove the 
temp {attach}'d image tag.
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
    gen = generator
    for art in gen.articles:
        if hasattr( art, 'wordpress_lede' ):
            lede = ur'<img src=\".*?' + re.escape( art.wordpress_lede ) + ur'\" class=\"hidden-lede\">'
            art._content = re.sub( lede , '', art._content)
        elif hasattr( art, 'lede' ):
            lede = ur'<img src=\".*?' + re.escape( art.lede ) + ur'\" class=\"hidden-lede\">'
            art._content = re.sub( lede , '', art._content)


def u_detach_lede( generator, writer ):
    for writ in writer._written_files:
        lede = re.compile(r'<img src=.*?class=\"hidden-lede\">')
        try:
            with open( writ, "r" ) as f:
                s = f.read().decode('utf-8')
                tmp = lede.sub( '', s)
            with open( writ, "w") as f:
                f.write( tmp.encode('utf-8') )
        except:
            print "Error opening written files to replace {attach}'d img tag"

                    

def register():
    #signals.article_generator_preread.connect( attach_lede )
    signals.article_generator_pretaxonomy.connect( attach_lede )
    #signals.article_generator_write_article.connect( detach_lede )
    signals.article_writer_finalized.connect( u_detach_lede )
