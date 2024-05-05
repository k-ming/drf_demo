#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-05-05 15:47:04
# @Author  : ming.zheng (ming.zheng@xinfei.cn)
# @Link    : ${link}
# @Version : $Id$

from rest_framework import generics
from rest_framework import mixins
from .model_serializers import FlowerModelSerializer
from .models import Flower

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
		