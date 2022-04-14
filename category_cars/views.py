from django.shortcuts import render
from rest_framework import response, generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser, ]


# class CreateCategory(APIView):
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return response.Response(serializer.data)

# class CreateCategory(generics.CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAdminUser, ]
#
#
# class ListCategory(generics.ListAPIView):
#     permission_classes = [AllowAny, ]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class DetailCategory(generics.RetrieveAPIView):
#     permission_classes = [AllowAny, ]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class UpdateCategory(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAdminUser, ]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


