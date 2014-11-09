#!/usr/bin/env python
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webfw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^seiyuu/', include("webfw.seiyuu_mgr.urls", "seiyuu_mgr", "seiyuu_mgr"))
)
