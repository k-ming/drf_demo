#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-04-29 20:28:15
# @Author  : ming.zheng (ming.zheng@xinfei.cn)
# @Link    : ${link}
# @Version : $Id$ 


from .models import Flower
from .model_serializers import FlowerModelSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def flower_list(request, format=None):
	""" 列表操作 """
	if request.method == 'GET':
		flower = Flower.objects.all()
		serializer = FlowerModelSerializer(flower, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif request.method == 'POST':
		serializer = FlowerModelSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def flower_detail(request, pk, format=None):
	""" 详情操作 """
	try:
		flower = Flower.objects.get(pk=pk)
	except Flower.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = FlowerModelSerializer(flower)
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif request.method == 'PUT':
		serializer = FlowerModelSerializer(instance=flower, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

	elif request.method == 'DELETE':
		# flower.delete()
		flower.valid = 0 #这种写法有问题，数据无法更新
		flower.save()
		return Response(status=status.HTTP_204_NO_CONTENT)