
from django.urls import path, include

from .views import ImagesViewSet, ImagesDetailViewSet, CategoryViewSet


urlpatterns = [
    path('', ImagesViewSet.as_view(), name='images'),
    path('category/<int:pk>/', CategoryViewSet().as_view(), name='category_view'),
    path('<int:pk>/', ImagesDetailViewSet.as_view(), name='imagesdetail'),
]