#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-06-10 22:43:49
# @Author  : King ming (zh88168@yeah.net)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : $Id$

"""
使用viewset重构视图
"""

from  rest_framework import viewsets
from .models import Flower
from django.contrib.auth.models import User
from .model_serializers import FlowerModelSerializer, UserModelSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import  Response

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""使用viewset只读视图,此视图自动提供list 和 detail"""
	queryset = User.objects.all()
	serializer_class = UserModelSerializer

class FlowerViewSet(viewsets.ModelViewSet):
	"""使用ModelViewSet, 此视图提供list create detail update delete"""
	queryset = Flower.objects.all()
	serializer_class = FlowerModelSerializer
	permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)



