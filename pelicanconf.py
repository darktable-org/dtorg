#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'darktable'
SITENAME = u'darktable'
SITEURL = ''

PATH = 'content'

#THEME = 'theme/dt.org'
THEME = 'theme/patdavid'

TIMEZONE = 'Etc/UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
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
RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['summary']

# Use pretty type options in output
TYPOGRIFY = True

STATIC_PATHS = ['extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

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

DIRECT_TEMPLATES = ['categories', 'tags']
PAGINATED_DIRECT_TEMPLATES = ['index', 'category', 'tag']


# Pagination options for list pages
DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
        (1, '{base_name}/', '{base_name}/index.html'),
        (2, '{base_name}/{number}/', '{base_name}/{number}/index.html')
        )
