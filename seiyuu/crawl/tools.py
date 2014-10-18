
import os
import requests
import urlparse

GOOGLE_CACHE_URL = "http://webcache.googleusercontent.com/search?q=cache:%s"
def get_google_cache(url):
    """
    take a url and seek it in google cache
    """
    parsed = urlparse.urlparse(url)
    req_url = parsed.hostname + parsed.path
    google_cache = GOOGLE_CACHE_URL % req_url

    return requests.get(google_cache).url
