#!/usr/bin/env python

import os
import json
os.environ['DJANGO_SETTINGS_MODULE'] = 'webfw.settings'

from scrapy.exceptions import DropItem

from crawl import items
from crawl import pipelines

def main():
    """
    """
    json_data = json.load(open("items_seiyuu_5.json", "r"))

    scrapy_items = list()

    for entry in json_data:
        _type = entry.pop("_type")

        if _type == "AnimeItems":
            _anime = items.AnimeItems()
            _anime.update(entry)
            scrapy_items.append(_anime)

        if _type == "AnimeItems":
            _anime = items.AnimeItems()
            _anime.update(entry)
            scrapy_items.append(_anime)

        if _type == "AnimeItems":
            _anime = items.AnimeItems()
            _anime.update(entry)
            scrapy_items.append(_anime)

    new_scrapy_items = list()

    duplicate = pipelines.DuplicatesPipeline()
    for items in scrapy_items:
        try:
            new_scrapy_items.append(duplicate.process_item(items, ""))
        except DropItem:
            pass

if __name__ == "__main__":
    main()
