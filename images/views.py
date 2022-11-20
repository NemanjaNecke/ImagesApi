from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer, CategorySerializer
from .models import Images, Category
from users.auth import HasProfileAPIKey
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CategoriesView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = [IsAuthenticated]
class CategoryViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Images.objects.filter(category=self.kwargs["pk"])
        return queryset
    #permission_classes = [HasProfileAPIKey and IsAuthenticated]
    serializer_class = ImageSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    #permission_classes = [HasProfileAPIKey and IsAuthenticated]
    serializer_class = ImageSerializer

# class ImagesDetailViewSet(generics.RetrieveDestroyAPIView):
#     queryset = Images.objects.all()
#     serializer_class = ImageSerializer
