#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-04-29 20:28:15
# @Author  : ming.zheng (ming.zheng@xinfei.cn)
# @Link    : ${link}
# @Version : $Id$ 

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Flower
from .model_serializers import FlowerModelSerializer

class JSONResponse(HttpResponse):
	"""parse body data"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def flower_list(request):
	""" 列表操作 """
	if request.method == 'GET':
		flower = Flower.objects.all()
		serializer = FlowerModelSerializer(flower, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = FlowerModelSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def flower_detail(request, pk):
	""" 详情操作 """
	try:
		flower = Flower.objects.get(pk=pk)
	except Flower.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = FlowerModelSerializer(flower)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = FlowerModelSerializer(instance=flower, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		# flower.delete()
		flower.valid = 0 #这种写法有问题，数据无法更新
		flower.save()
		return HttpResponse(status=204)