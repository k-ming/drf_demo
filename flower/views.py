from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework import status
from .models import Flower
from .serializers import FlowerSerializer

# Create your views here.

class FlowerListApiView(APIView):
	"""列表操作"""
	def get(self, request, format=None):
		flower = Flower.objects.filter()
		serializer = FlowerSerializer(flower, many=True)
		return Response(serializer.data)

	def post(self, request):
		"""插入记录"""
		# 1、序列化，传入data
		serializer = FlowerSerializer(data=request.data)

		# 2、校验数据
		if serializer.is_valid(raise_exception=True):
			# 3、存储数据
			serializer.save()

			# 4、返回响应内容和 code
			return Response(serializer.data, status=HTTP_201_CREATED)

		# 5、异常返回
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

		
class FlowerListDetailApiView(APIView):
	"""详情操作"""
	def get_object(self, pk):
		try:
			# 过滤出valid=1的记录，再查询pk存在的记录
			return Flower.objects.filter(valid=1).get(no=pk)
		except Flower.DoesNotExist:
			raise HTTP_400_BAD_REQUEST

	def get(self, request, pk, format=None):
		flower = self.get_object(pk)
		serializer = FlowerSerializer(flower)
		return Response(serializer.data, status=HTTP_200_OK)

	def put(self, request, pk, format=None):
		flower = self.get_object(pk)
		serializer = FlowerSerializer(flower, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		flower = self.get_object(pk)
		# 物理删除
		# flower.delete()

		# 逻辑删除
		flower.valid = 0
		flower.save()
		return Response(status=HTTP_204_NO_CONTENT)