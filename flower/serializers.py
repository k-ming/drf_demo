#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-03-24 15:57:12
# @Author  : kingming388 (zh88168@yeah.net)
# @Link    : https://k-ming.github.io/
# @Version : $Id$

from rest_framework import serializers
from .models import Flower

class FlowerSerializer(serializers.Serializer):
	"""flower 的序列化器"""
	no = serializers.IntegerField(label='编号', read_only=True)
	name = serializers.CharField(label='学名', max_length=20)
	height = serializers.IntegerField(label='高度', required=False)
	product_name = serializers.CharField(label='商品名', required=False)
	bust = serializers.IntegerField(label='胸径', required=False)
	location = serializers.CharField(label='分布', required=False)
	habit = serializers.CharField(label='习性', required=False)
	create_time = serializers.DateTimeField(label='创建日期时间', required=False)
	update_time = serializers.DateTimeField(label='更新日期时间', required=False)
	valid = serializers.IntegerField(label='是否有效', required=False)
	value = serializers.CharField(label='价值', required=False)	

	# class Meta:
	# 	"""定义要展示的字段"""
	# 	fields = ['name', 'location']

	# serializers 并没有实现create和update方法，需要子类实现
	def create(self, validated_data):
		"""
		根据验证的数据创建一个新的Flower实例
		"""
		return Flower.objects.create(**validated_data)

	# 实现update方法
	def update(self, instance, validated_data):
		""" 
		根据验证的数据更新一个实例
		"""
		instance.name = validated_data.get('name', instance.name)
		instance.height = validated_data.get('height')
		instance.product_name = validated_data.get('product_name', instance.product_name)
		instance.bust = validated_data.get('bust', instance.bust)
		instance.location = validated_data.get('location', instance.location)
		instance.habit = validated_data.get('habit', instance.habit)
		instance.value = validated_data.get('value', instance.value)
		instance.create_time =	validated_data.get('create_time', instance.create_time)
		instance.update_time =	validated_data.get('update_time', instance.update_time)
		instance.valid = validated_data.get('valid', instance.valid)
		instance.save()
		return instance