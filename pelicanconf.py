#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# AUTHOR = u'David Talbot'
SITENAME = u'David Talbot'
SITEURL = 'http://niceguydave.com'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', '/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-theme-jesuisfree'

GOOGLE_ANALYTICS = 'UA-12339594-2'
SOCIAL = (('twitter', 'https://twitter.com/niceguydave'),
          ('google+', 'https://plus.google.com/u/0/+DavidTalbot1974'),
          ('lastfm', 'http://www.last.fm/user/squij'),
          ('github', 'https://github.com/niceguydave'),)

STATIC_PATHS = ['images']

PLUGINS = [
    'minification',
]
