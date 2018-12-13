#!/usr/bin/env python

import json
import datetime

from django.core.management.base import BaseCommand, CommandError

from seiyuu_mgr import models

class Command(BaseCommand):
    help = "Import json"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str)
        parser.add_argument("season", type=str)

    def handle(self, *args, **options):
        with open(options["json_file"], 'r') as f:
            data = json.load(f)
            for _anime in data:
                season, _ = models.Season.objects.get_or_create(label=_anime["premiered"] or "undefined")
                anime, _ = models.Anime.objects.get_or_create(
                        name=_anime["title"],
                        page_link=_anime["link_canonical"],
                        season=season,
                        image_link=_anime["image_url"],
                        )
                for _character in _anime["characters"]:
                    try:
                        seiyuu_data = [jp_seiyuu for jp_seiyuu in _character["voice_actors"] if jp_seiyuu["language"] == "Japanese"][0]
                    except IndexError:
                        continue
                    seiyuu, _ = models.Seiyuu.objects.get_or_create(
                            page_link=seiyuu_data["url"],
                            image_link=seiyuu_data["image_url"],
                            first_name=seiyuu_data["name"],
                            last_name="",
                            )
                    character, _ = models.Character.objects.get_or_create(
                            status=_character["role"],
                            page_link=_character["url"],
                            image_link=_character["image_url"],
                            first_name=_character["name"],
                            last_name="",
                            )
                    character.seiyuu.add(seiyuu)
                    character.anime.add(anime)

###
