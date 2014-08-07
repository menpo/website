#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
import os

# Add path above so we can access latest release version
script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, script_path)
sys.path.insert(0, os.path.abspath(os.path.join(script_path, '..')))

from releases import get_menpo_releases
LATEST_RELEASE = get_menpo_releases()[0][u'tag_name']

# Avoid having hard coded paths to these files
THEME = u'../themes/zurb-F5-basic'

AUTHOR = u'Patrick Snape'
SITENAME = u'menpo.io'
SITEURL = u'http://menpo.io'

TIMEZONE = u'Europe/London'

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

PLUGIN_PATHS = [os.path.join(script_path, u'pelican_plugins')]
PLUGINS = [u'sitemap', u'share_post']

SITEMAP = {
    u'format': u'xml',
    u'priorities': {
        u'articles': 1.0,
        u'indexes': 0.5,
        u'pages': 1.0
    },
    u'changefreqs': {
        u'articles': u'monthly',
        u'indexes': u'daily',
        u'pages': u'monthly'
    }
}

GOOGLE_ANALYTICS = u'UA-52093814-1'

PATH = u'../content'
STATIC_PATHS = [u'articles/files',
                u'articles/images',
                u'pages/installation/windows/images',
                u'pages/installation/linux/images',
                u'pages/installation/osx/images',
                u'pages/images/team']

ARTICLE_PATHS = [u'articles']
PAGE_PATHS = [u'pages']
INDEX_SAVE_AS = u'blog/index.html'
OUTPUT_PATH = u'../static_website_output'

PAGE_URL = u'{slug}.html'
PAGE_SAVE_AS = u'{slug}.html'
PAGE_LANG_URL = u'{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = u'{slug}-{lang}.html'

ARTICLE_URL = u'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = u'blog/{date:%Y}/{date:%m}/{slug}/index.html'
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

SUMMARY_MAX_LENGTH = 100
