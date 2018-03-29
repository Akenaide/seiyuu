#!/usr/bin/env python
from django.conf.urls import include, url
from django.urls import path

from seiyuu_mgr import views

urlpatterns = ('seiyuu_mgr.views',
    path(r'^(?P<season>\w+)?$', views.seiyuu_list, name="seiyuu_list"),
)
