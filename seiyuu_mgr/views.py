#!/usr/bin/env python
import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from seiyuu_mgr import models
from crawl import tools

def seiyuu_list(request, season=None):
    """
    """
    if not season:
        current_season = tools.get_season(datetime.datetime.now(), True)[0]
    else:
        current_season = get_object_or_404(models.Season, label=season)

    seasons = models.Season.objects.all().order_by("starting_date")[:4]
    roles = list()

    seiyuus = models.Seiyuu.objects.filter(
                        character__anime__season=current_season).order_by("first_name")

    for seiyuu in seiyuus.distinct():
        _dict = dict(
            seiyuu=seiyuu,
            role=seiyuu.get_role_for_season(current_season)
        )
        roles.append(_dict)

    context = {"roles":roles,
                "seasons":seasons,
                }
    return render(request, "seiyuu_list.html", context)
