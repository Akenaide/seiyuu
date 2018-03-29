#!/usr/bin/env python
from django.conf.urls import include, url
from django.urls import path

from seiyuu_mgr import views

app_name = "seiyuu_mgr"
urlpatterns = (
        path('', views.seiyuu_list, name="seiyuu_list_default"),
        path('<str:season>/', views.seiyuu_list, name="seiyuu_list"),
)
