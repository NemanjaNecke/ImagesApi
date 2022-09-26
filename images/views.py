from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer, CategorySerializer
from .models import Images, Category
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Images.objects.filter(category=self.kwargs["pk"])
        return queryset

    serializer_class = ImageSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()

    serializer_class = ImageSerializer

# class ImagesDetailViewSet(generics.RetrieveDestroyAPIView):
#     queryset = Images.objects.all()
#     serializer_class = ImageSerializer
