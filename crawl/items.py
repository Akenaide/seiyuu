#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.djangoitem import DjangoItem

from webfw.seiyuu_mgr.models import Seiyuu, Anime, Character

class MyItem(DjangoItem):
    def as_dict(self):
        return dict((k, self.get(k)) for k in self._values)

class SeiyuuItem(MyItem):
    django_model = Seiyuu

class AnimeItem(MyItem):
    django_model = Anime

class CharacterItem(MyItem):
    django_model = Character
    anime = scrapy.Field()
    seiyuu = scrapy.Field()
