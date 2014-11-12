#!/usr/bin/env python

import os
import json
os.environ['DJANGO_SETTINGS_MODULE'] = 'webfw.settings'
import sys
from scrapy.exceptions import DropItem
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from crawl import items
from crawl import pipelines

def main():
    """
    """
    json_data = json.load(open("items_seiyuu_5.json", "r"))

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

    # print("Create : %r" % new_scrapy_items)

if __name__ == "__main__":
    main()
