
from django.urls import path, include

from .views import ImagesViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'images', ImagesViewSet, basename='images')

router.register(r'category', CategoryViewSet, basename='category')
urlpatterns = router.urls