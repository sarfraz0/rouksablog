#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rouksana Fidaly'
SITENAME = 'Chez Rouksana'
SITEURL = ''
MAIL= 'rouksana@varialbentreprise.com'
SHOW_COPYRIGHT=True
COPYRIGHT='Rouksana Fidaly - <a href="https://creativecommons.org/licenses/by-nc/4.0">CC BY-NC 4.0</a>'

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

THEME='themes/html5-dopetrope'
TYPOGRIFY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/sarfraz0/rouksablog'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

DISQUS_SITENAME="rouksa"
#GOOGLE_ANALYTICS = "UA-73554248-1"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME', 'extra/custom.css']
EXTRA_PATH_METADATA = { 'extra/CNAME': {'path': 'CNAME'}
                      , 'extra/custom.css': {'path': 'static/custom.css'}
                      }
CUSTOM_CSS = 'static/custom.css'

# http://cyrille.rossant.net/pelican-github
#MD_EXTENSIONS = [ 'codehilite(css_class=highlight, guess_lang=False,linenums=False)'
#                , 'pymdownx.github' ]

