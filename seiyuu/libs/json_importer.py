#!/usr/bin/env python
from __future__ import absolute_import
import json

from scrapy.exceptions import DropItem

from crawl import items
from crawl import pipelines

def import_json(file_path):
    """
    Import json file from scrapinghub
    """

    json_data = json.load(open(file_path, "r"))

    character_scrapy_items = list()
    seiyuu_scrapy_items = list()
    anime_scrapy_items = list()

    for entry in json_data:
        _type = entry.pop("_type")

        if _type == "SeiyuuItem":
            _seiyuu = items.SeiyuuItem()
            _seiyuu.update(entry)
            seiyuu_scrapy_items.append(_seiyuu)

        if _type == "AnimeItem":
            _anime = items.AnimeItem()
            _anime.update(entry)
            anime_scrapy_items.append(_anime)

        if _type == "CharacterItem":
            _character = items.CharacterItem()
            _character.update(entry)
            character_scrapy_items.append(_character)

    new_scrapy_items = list()

    duplicate = pipelines.DuplicatesPipeline()
    create_item = pipelines.SeiyuuPipeline()
    all_items = [anime_scrapy_items, seiyuu_scrapy_items, character_scrapy_items]
    for sub_list in all_items:
        for item in sub_list:
            try:
                new_item = duplicate.process_item(item, "")
                create_item.process_item(new_item, "")
            except DropItem:
                print("Ignore %r" % item)
                pass
