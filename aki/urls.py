#!/usr/bin/env python
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = (
    # path(r'^admin/', include("admin.site.urls")),
    path(r'^seiyuu/', include("seiyuu_mgr.urls")),
    path(r'^$', RedirectView.as_view(url="/seiyuu/",), name="home"),
)
