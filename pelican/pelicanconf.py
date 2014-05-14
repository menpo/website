#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Avoid having hard coded paths to these files
THEME = '../themes/zurb-F5-basic'

AUTHOR = u'Patrick Snape'
SITENAME = u'menpo'
SITEURL = u'http://menpo.io'
        
TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISQUS_SITENAME = u'menpo'

PATH = '../content'
STATIC_PATHS = ['pages/installation/windows/images']

ARTICLE_DIR = u'articles'
PAGE_DIR = u'pages'
INDEX_SAVE_AS = 'blog/index.html'
OUTPUT_PATH = u'../static_website_output'

PAGE_URL = u'{slug}.html'
PAGE_SAVE_AS = u'{slug}.html'
PAGE_LANG_URL = u'{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = u'{slug}-{lang}.html'


ARTICLE_URL = u'blog/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = u'blog/{date:%Y}/{slug}/index.html'
CATEGORIES_SAVE_AS = u'blog/categories.html'
CATEGORIES_URL = u'blog/categories.html'
CATEGORY_URL = u'blog/category/{slug}.html'
CATEGORY_SAVE_AS = u'blog/category/{slug}.html'
TAG_URL = u'blog/tag/{slug}.html'
TAG_SAVE_AS = u'blog/tag/{slug}.html'
TAGS_URL = u'blog/tags.html'
TAGS_SAVE_AS = u'blog/tags.html'
AUTHOR_URL = u'blog/author/{slug}.html'
AUTHOR_SAVE_AS = u'blog/author/{slug}.html'
AUTHORS_URL = u'blog/authors.html'
AUTHORS_SAVE_AS = u'blog/authors.html'
ARCHIVES_SAVE_AS = u'blog/archives.html'
