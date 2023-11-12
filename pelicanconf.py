#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Talita'
SITENAME = 'Talita Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "theme"

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 5

SOCIAL = (('github', 'http://github.com/Talits'),('LinkedIN', "https://www.linkedin.com/in/talits/"),)


DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
PAGE_URL = 'pages/{slug}.html'

MENU = [(u'Home','index.html'),
        (u'Pages',u'pages/index.html'),
    ]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True