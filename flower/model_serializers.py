#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-04-29 15:59:25
# @Author  : ming.zheng (ming.zheng@xinfei.cn)
# @Link    : ${link}
# @Version : $Id$

from rest_framework import serializers
from  .models import Flower

class FlowerModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flower
		fields = '__all__'

			
		
