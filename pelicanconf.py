#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

from dt_authors import *

AUTHOR = u'darktable'
SITENAME = u'darktable'
SITEURL = 'https://www.darktable.org'
SITEURL = ''

PATH = 'content'

THEME = 'theme/dt.org'

TIMEZONE = 'Etc/UTC'

LOCALE = u'C'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = "feed/all.rss.xml"
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = "feed/%s.rss.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
RELATIVE_URLS = False

PLUGIN_PATHS = ['plugins']
PLUGINS = ['summary', 'attach_ledeimg', 'rm_nbsp_title', 'render_math', 'image_links', 'tipue_search', 'social_media', 'article_metadata', 'static_comments', 'image_compare']

THUMBNAIL_SIZE = 960

# DO NOT CHANGE THEM HERE BUT SET THEM IN ANOTHER PLACE!
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN_KEY = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

# web site statistics
PIWIK_URL = 'darktable.org/piwik/'
PIWIK_SITE_ID = 1

# Use pretty type options in output
TYPOGRIFY = True

STATIC_PATHS = ['extra', 'blog', 'news', 'pages', 'images']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/update_website_github.php': {'path': 'update_website_github.php'}
}

# These two options allow us to specify the category
# of the files with a regex.  We basically set 'news'
# and 'blog' even if they're nested in sub-dirs
USE_FOLDER_AS_CATEGORY = False
PATH_METADATA = '(?P<category>blog|news)/.*'


# Path for site content and various URL/SAVE_AS options
# Reminder: "page" is static content like "about", "features"
#           "article" is timely content, "blog" or "news" posts
PATH = 'content'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

MENUITEMS = (
        ('News', '/news/'),
        ('Blog', '/blog/')
    )

DIRECT_TEMPLATES = ['categories', 'tags', 'search', 'small_ledes', 'sitemap']
PAGINATED_DIRECT_TEMPLATES = ['index', 'category', 'tag']

SITEMAP_SAVE_AS = 'sitemap.xml'

# choose a default page lede that sticks out enough to force people to care about it and add a custom lede :-)
DEFAULT_LEDE = '/theme/images/darktable_skull+logo.png'

# Pagination options for list pages
DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
        (1, '{base_name}/', '{base_name}/index.html'),
        (2, '{base_name}/{number}/', '{base_name}/{number}/index.html')
        )

# toc(permalink=True) sets all headers to have an id
# set, and an <a> after the heading.
# see: http://pythonhosted.org/Markdown/extensions/toc.html
MARKDOWN = {
  'extension_configs' : {
    #'markdown.extensions.fenced_code' : {},
    #'markdown.extensions.codehilite' : {'css_class': 'codehilite'},
    'markdown.extensions.extra' : {},
    'markdown.extensions.headerid' : {},
    'markdown.extensions.toc(permalink=)' : {}
  }
}

# these are deprecated, use MARKDOWN instead!
MD_EXTENSIONS = ['extra', 'headerid']

# dummy line i removed before, sorry for the spam.
