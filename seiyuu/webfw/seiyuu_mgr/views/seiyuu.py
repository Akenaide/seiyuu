from django.http import HttpResponse
from django.shortcuts import render

from webfw.seiyuu_mgr import models

def seiyuu_list(request):
    """
    """
    seasons = models.Season.objects.all()[:4]
    seiyuus = list()

    for season in seasons:
        seiyuus.extend(models.Seiyuu.objects.filter(
                                character__anime__season=season))

    context = {"seiyuus":set(seiyuus),
                "seasons":seasons,
                }
    return render(request, "seiyuu_list.html", context)
