
import os
import requests
import urlparse

from dateutil import parser
from faker import Factory

GOOGLE_CACHE_URL = "http://webcache.googleusercontent.com/search?q=cache:%s"

fake = Factory.create()
session = requests.Session()
def get_google_cache(url):
    """
    take a url and seek it in google cache
    """
    parsed = urlparse.urlparse(url)
    req_url = parsed.hostname + parsed.path
    google_cache = GOOGLE_CACHE_URL % req_url
    session.headers.update({'user-agent':fake.user_agent()})

    return session.get(google_cache).url

def get_season(date):
    """
    Guess in which season the given date is
    :type date: datetime
    """

    doy = date.timetuple().tm_yday

    # "day of year" ranges for the northern hemisphere
    spring = xrange(80, 172)
    summer = xrange(172, 264)
    fall = xrange(264, 355)
    # winter = everything else

    if doy in spring:
        season = 'spring'
    elif doy in summer:
        season = 'summer'
    elif doy in fall:
        season = 'fall'
    else:
        season = 'winter'

    return "%s%i" % (season, date.year)
