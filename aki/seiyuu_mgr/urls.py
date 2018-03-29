#!/usr/bin/env python
from django.conf.urls import patterns, include, url

from seiyuu_mgr import views

urlpatterns = patterns('seiyuu_mgr.views',
    url(r'^(?P<season>\w+)?$', "seiyuu.seiyuu_list", name="seiyuu_list"),
)
