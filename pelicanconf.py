#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'INSERT NAME'
SITENAME = u'INSERT NAME'
SITEURL = 'file:///home/NAME/pelican-test/output'
INDEX_SAVE_AS = 'blog_index.html'

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["render_math"]

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None#'feeds'


DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

#THEME = 'notmyidea'

STATIC_PATHS = [
    'images', 
    'extra/icona.png'
]
EXTRA_PATH_METADATA = {
    'extra/icona.png': {'path': 'icona.png'},
}
LOGO = 'icona.png'
