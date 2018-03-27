#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import datetime

from dateutil import parser as dateparser
from scrapy.exceptions import DropItem

from crawl.items import SeiyuuItem
from crawl.items import CharacterItem
from crawl.items import AnimeItem
from crawl import tools
from crawl import settings
from webfw.seiyuu_mgr.models import Seiyuu
from webfw.seiyuu_mgr.models import Anime
from webfw.seiyuu_mgr.models import Character
from webfw.seiyuu_mgr.models import Season

date_format = re.compile(r"(.*20[0-9]+)")


class SeiyuuPipeline(object):
    def process_seiyuu(self, item, spider):
        data = item.as_dict()
        if data["first_name"]:
            seiyuu = Seiyuu(**data)
            seiyuu.save()
        return item

    def process_character(self, item, spider):
        data = item.as_dict()
        try:
            seiyuu = Seiyuu.objects.get(first_name=data["seiyuu"]['first_name'],
                    last_name=data["seiyuu"]["last_name"])
        except Seiyuu.DoesNotExist:
            seiyuu = None
        anime = Anime.objects.get(name=data["anime"]["name"])
        data.pop("anime", None)
        data.pop("seiyuu", None)

        if data['first_name']:
            character = Character(**data)
            character.save()
            character.anime.add(anime)
            if seiyuu:
                character.seiyuu.add(seiyuu)
            character.save()
        return item

    def process_anime(self, item, spider):
        data = item.as_dict()
        start_time = data['start_time']
        if "to" in start_time:
            start_time = start_time.split("to")[0]
        find = date_format.search(start_time)
        if find:
            data['start_time'] = dateparser.parse(find.group())
            season = tools.get_season(data['start_time'], return_django_obj=True)[0]
        else:
            data['start_time'] = None
            season = None

        data["season"] = season
        anime = Anime(**data)
        anime.save()
        return item

    def process_item(self, item, spider):
        if settings.DEPLOY_VERSION:
            return item
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
        data = item.as_dict()
        current = Character.objects.filter(
                    first_name=data.get('first_name', "noname").strip(),
                    last_name=data.get('last_name', "noname").strip(),
                    )

        if current.exists():
            anime = Anime.objects.get(name=data["anime"]["name"])
            character = current[0]
            character.anime.add(anime)
            character.save()
            raise DropItem
        else:
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
        if settings.DEPLOY_VERSION:
            return item
        if isinstance(item, SeiyuuItem):
            return self.process_seiyuu(item, spider)

        elif isinstance(item, CharacterItem):
            return self.process_character(item, spider)

        elif isinstance(item, AnimeItem):
            return self.process_anime(item, spider)
