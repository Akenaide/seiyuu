#!/usr/bin/env python
from django.contrib import admin

from seiyuu_mgr.models import Seiyuu
from seiyuu_mgr.models import Anime
from seiyuu_mgr.models import Character
from seiyuu_mgr.models import Season


class SeiyuuAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name",)
    search_fields = ("first_name", "last_name")

admin.site.register(Seiyuu, SeiyuuAdmin)

class AnimeAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "season")
    search_fields = ("name",)

admin.site.register(Anime, AnimeAdmin)

class CharacterAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name")
    search_fields = ("first_name", "last_name")

admin.site.register(Character, CharacterAdmin)

class SeasonAdmin(admin.ModelAdmin):
    list_display = ("label",)

admin.site.register(Season, SeasonAdmin)
