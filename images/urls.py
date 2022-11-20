
from django.urls import path, include
from .views import ImagesViewSet, CategoryViewSet, CategoriesView
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'images', ImagesViewSet, basename='images')
router.register(r'categories', CategoriesView)
urlpatterns = [
    path(r'category-image/<int:pk>/', CategoryViewSet.as_view()),
    path('', include(router.urls)),
    ]