#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-04-16 11:34:35
# @Author  : kingming388 (zh88168@yeah.net)
# @Link    : https://k-ming.github.io/
# @Version : $Id$

from django.urls import path
from .views import FlowerListApiView, FlowerListDetailApiView

urlpatterns = [
    path('list/', FlowerListApiView.as_view()),
    path('list/<int:pk>', FlowerListDetailApiView.as_view()),
]
