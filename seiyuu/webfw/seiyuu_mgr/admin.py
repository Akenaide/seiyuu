from django.contrib import admin

from webfw.seiyuu_mgr.models import Seiyuu
from webfw.seiyuu_mgr.models import Anime
from webfw.seiyuu_mgr.models import Character


class SeiyuuAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name",)

admin.site.register(Seiyuu, SeiyuuAdmin)

