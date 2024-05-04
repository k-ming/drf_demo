#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-04-16 11:34:35
# @Author  : kingming388 (zh88168@yeah.net)
# @Link    : https://k-ming.github.io/
# @Version : $Id$

from django.urls import path
from .api_views import FlowerListApiView, FlowerListDetailApiView
from .import base_views

urlpatterns = [
    path('list/', FlowerListApiView.as_view()),
    path('list/<int:pk>', FlowerListDetailApiView.as_view()),
    path('base_list/', base_views.flower_list),
    path('base_list/<int:pk>', base_views.flower_detail)
]
