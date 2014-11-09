#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Scrapy settings for seiyuu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os

BOT_NAME = 'seiyuu'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crawl.spiders'
os.environ['DJANGO_SETTINGS_MODULE'] = 'webfw.settings'
COOKIES_ENABLED = False
DOWNLOAD_DELAY = 10
DEPTH_LIMIT = 1
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'seiyuu (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
        "crawl.pipelines.DuplicatesPipeline": 100,
        "crawl.pipelines.SeiyuuPipeline": 800,
    }
