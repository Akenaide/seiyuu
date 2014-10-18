# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from crawl.items import SeiyuuItem
from crawl.items import CharacterItem
from crawl.items import AnimeItem

class SeiyuuPipeline(object):
    def process_seiyuu(self, item, spider):
        return item

    def process_character(self, item, spider):
        return item

    def process_anime(self, item, spider):
        return item

    def process_item(self, item, spider):
        if isinstance(item, SeiyuuItem):
            process_seiyuu(item, spider)

        if isinstance(item, CharacterItem):
            process_character(item, spider)

        if isinstance(item, AnimeItem):
            process_anime(item, spider)
