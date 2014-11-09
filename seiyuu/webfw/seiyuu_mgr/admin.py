#!/usr/bin/env python
from django.contrib import admin

from webfw.seiyuu_mgr.models import Seiyuu
from webfw.seiyuu_mgr.models import Anime
from webfw.seiyuu_mgr.models import Character
from webfw.seiyuu_mgr.models import Season


class SeiyuuAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name",)

admin.site.register(Seiyuu, SeiyuuAdmin)

class AnimeAdmin(admin.ModelAdmin):
    list_display = ("pk", "name",)

admin.site.register(Anime, AnimeAdmin)

class CharacterAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name")
admin.site.register(Character, CharacterAdmin)

class SeasonAdmin(admin.ModelAdmin):
    list_display = ("label",)

admin.site.register(Season, SeasonAdmin)
