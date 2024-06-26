#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-05-05 15:47:04
# @Author  : ming.zheng (ming.zheng@xinfei.cn)
# @Link    : ${link}
# @Version : $Id$

from rest_framework import generics
from rest_framework import mixins
from .model_serializers import FlowerModelSerializer, UserModelSerializer
from .models import Flower
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class FlowerMixinsList(mixins.ListModelMixin\
						,mixins.CreateModelMixin\
						,generics.GenericAPIView):
	"""
	使用mixins类提供.list()和.create()操作
	使用GenericAPIView 重构试图
	"""
	# 指定查询集
	queryset = Flower.objects.all().filter(valid=1)
	# 指定序列化器
	serializer_class = FlowerModelSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs) # 调用父类ListModelMixin 的list方法，查询列表

	def post(self, request, *args, **kwargs): # 调用父类ListModelMixin 的create方法，新增记录
		return self.create(request, *args, **kwargs)

	"""
	获取请求request中的user,并存入model,实现关联
	"""
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
		
	permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)  # 添加视图所需的权限

class FlowerMixinsDetail(mixins.RetrieveModelMixin\
						,mixins.UpdateModelMixin\
						,mixins.DestroyModelMixin\
						,generics.GenericAPIView):
	"""
	使用类 RetrieveModelMixin 的 retrieve()方法查询单一
	使用类 UpdateModelMixin 的 update() 方法更新单一
	使用 DestroyModelMixin 的 destroy() 方法删除单一
	"""
	# 指定查询集
	queryset = Flower.objects.all().filter(valid=1)
	# 指定序列化器
	serializer_class = FlowerModelSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
	permission_class = (permissions.IsAuthenticatedOrReadOnly,)  # 添加视图所需的权限

class FlowerMixedList(generics.ListCreateAPIView):
	"""
	使用已经混合好list,create方法的generics.ListCreateAPIView类，使代码更简洁
	"""
	# 指定查询集
	queryset = Flower.objects.all().filter(valid=1)
	# 指定序列化器
	serializer_class = FlowerModelSerializer	
	
class FlowerMixedDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	使用已经混合好retrieve,update,destory方法的generics.RetrieveUpdateDestroyAPIView类，使代码更简洁
	"""
	# 指定查询集
	queryset = Flower.objects.all().filter(valid=1)
	# 指定序列化器
	serializer_class = FlowerModelSerializer	
		
class UserList(generics.ListAPIView):
	"""
	创建管理员列表视图，使用通用试图类ListAPIView实现只读
	"""
	queryset = User.objects.all()
	serializer_class = UserModelSerializer

		
class UserDetail(generics.RetrieveAPIView):
	"""
	创建管理员详情视图，使用通用试图类RetrieveAPIView实现只读
	"""
	queryset = User.objects.all()
	serializer_class = UserModelSerializer	
		