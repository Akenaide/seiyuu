#!/usr/bin/env python
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^seiyuu/', include("seiyuu_mgr.urls", "seiyuu_mgr", "seiyuu_mgr")),
    url(r'^$', RedirectView.as_view(url="/seiyuu/",), name="home"),
)
