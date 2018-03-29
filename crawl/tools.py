#!/usr/bin/env python
import os
import requests
import urlparse
import datetime

from dateutil import parser, relativedelta
from faker import Factory

from seiyuu_mgr import models

GOOGLE_CACHE_URL = "http://webcache.googleusercontent.com/search?q=cache:%s"

fake = Factory.create()
# session = requests.Session()
def get_google_cache(url):
    """
    take a url and seek it in google cache
    """
    parsed = urlparse.urlparse(url)
    req_url = parsed.hostname + parsed.path
    google_cache = GOOGLE_CACHE_URL % req_url
    headers = {'user-agent':fake.user_agent()}

    return requests.get(google_cache, headers=headers).url

def get_season(starting_date, return_django_obj=False):
    """
    Guess in which season the given date is
    :type date: datetime
    """

    doy = starting_date.timetuple().tm_yday

    # "day of year" ranges for the northern hemisphere
    spring = xrange(80, 172)
    summer = xrange(172, 264)
    fall = xrange(264, 355)
    # winter = everything else

    if doy in spring:
        season = 'spring'
        season_doy = 80
    elif doy in summer:
        season = 'summer'
        season_doy = 172
    elif doy in fall:
        season = 'fall'
        season_doy = 264
    else:
        season = 'winter'
        season_doy = 356

    label = "%s%i" % (season, starting_date.year)
    if not return_django_obj:
        return label

    season_date = datetime.date(starting_date.year, 1, 1)
    season_date += relativedelta.relativedelta(yearday=season_doy)

    django_obj = models.Season.objects.get_or_create(label=label,
                        starting_date=season_date)

    return django_obj
