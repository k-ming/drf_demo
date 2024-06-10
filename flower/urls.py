#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-04-16 11:34:35
# @Author  : kingming388 (zh88168@yeah.net)
# @Link    : https://k-ming.github.io/
# @Version : $Id$

from django.urls import path, include
from .views1 import FlowerListApiView, FlowerListDetailApiView
from .import views2
from rest_framework.urlpatterns import format_suffix_patterns
from .views3 import FlowerMixinsList, FlowerMixinsDetail,\
					 FlowerMixedList, FlowerMixedDetail,\
					 UserList, UserDetail
from .viewset_view import UserViewSet, FlowerViewSet
from rest_framework.schemas import get_schema_view   # 使用coreapi 来生成接口文档
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
	path('list/', FlowerListApiView.as_view()),
	path('list/<int:pk>', FlowerListDetailApiView.as_view()),
	path('base_list/', views2.flower_list),
	path('base_list/<int:pk>', views2.flower_detail),
	path('mixins_list/', FlowerMixinsList.as_view()),
	path('mixins_list/<int:pk>', FlowerMixinsDetail.as_view()),
	path('mixed_list/', FlowerMixedList.as_view()),
	path('mixed_list/<int:pk>', FlowerMixedDetail.as_view()),
	path('users/', UserList.as_view()),
	path('users/<int:pk>', UserDetail.as_view()),
	path('users_set/', UserViewSet.as_view({'get': 'list'})),
	path('users_set/<int:pk>', UserViewSet.as_view({'get': 'retrieve'})),
	path('doc/', schema_view)
]


urlpatterns = format_suffix_patterns(urlpatterns)

# 使用路由器 router 绑定ModelViewSet视图
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'', FlowerViewSet)
urlpatterns +=[
	path('model_list/', include(router.urls))
]