# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.djangoitem import DjangoItem

from webfw.seiyuu_mgr.models import Seiyuu, Anime, Character

class SeiyuuItem(DjangoItem):
    django_model = Seiyuu

class AnimeItem(DjangoItem):
    django_model = Anime

class CharacterItem(DjangoItem):
    django_model = Character
