#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-04-29 15:59:25
# @Author  : ming.zheng (ming.zheng@xinfei.cn)
# @Link    : ${link}
# @Version : $Id$

from rest_framework import serializers
from  .models import Flower
from django.contrib.auth.models import User

class FlowerModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flower
		owner = serializers.ReadOnlyField(source='owner.username') # 更新关联
		fields = '__all__'
			
class UserModelSerializer(serializers.ModelSerializer):
	"""
	创建 auth.models.User序列化器
	"""
	flower = serializers.PrimaryKeyRelatedField(many=True, queryset=Flower.objects.all()) # 设置主键关联
	class Meta:
		model = User
		# flower 在用户模型中是一个反向关联关系。在使用 ModelSerializer 类时它默认不会被包含，所以我们需要为它添加一个显式字段。
		fields =  ('id', 'username', 'flower') 
