# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from dateutil import parser as dateparser
from scrapy.exceptions import DropItem

from crawl.items import SeiyuuItem
from crawl.items import CharacterItem
from crawl.items import AnimeItem
from webfw.seiyuu_mgr.models import Seiyuu
from webfw.seiyuu_mgr.models import Anime
from webfw.seiyuu_mgr.models import Character


class SeiyuuPipeline(object):
    def process_seiyuu(self, item, spider):
        data = item.as_dict()
        seiyuu = Seiyuu(**data)
        seiyuu.save()
        return item

    def process_character(self, item, spider):
        return item

    def process_anime(self, item, spider):
        data = item.as_dict()
        data['start_time'] = dateparser.parse(data['start_time'])
        anime = Anime(**data)
        anime.save()
        return item

    def process_item(self, item, spider):
        if isinstance(item, SeiyuuItem):
            return self.process_seiyuu(item, spider)

        elif isinstance(item, CharacterItem):
            return self.process_character(item, spider)

        elif isinstance(item, AnimeItem):
            return self.process_anime(item, spider)

class DuplicatesPipeline(object):


    def process_seiyuu(self, item, spider):
        data = item.as_dict()
        current = Seiyuu.objects.filter(
                    first_name=data.get('first_name', "noname"),
                    last_name=data.get('last_name', "noname")
                    )

        if current.exists():
            raise DropItem
        else:
            return item

    def process_character(self, item, spider):
        return item

    def process_anime(self, item, spider):
        data = item.as_dict()
        current = Anime.objects.filter(
                    name=data.get('name', "noname"),
                    )

        if current.exists():
            raise DropItem
        else:
            return item

    def process_item(self, item, spider):
        if isinstance(item, SeiyuuItem):
            return self.process_seiyuu(item, spider)

        elif isinstance(item, CharacterItem):
            return self.process_character(item, spider)

        elif isinstance(item, AnimeItem):
            return self.process_anime(item, spider)
