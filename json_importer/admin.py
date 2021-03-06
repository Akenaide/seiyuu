#!/usr/bin/env python
from __future__ import absolute_import

from django.contrib import admin

from json_importer.models import JsonFile

def import_json(modeladmin, request, queryset):
    for obj in queryset:
        json_importer.import_json(obj.json_file.path)

class JsonFileAdmin(admin.ModelAdmin):
    list_display = ("label", "json_file")
    actions = []

admin.site.register(JsonFile, JsonFileAdmin)
