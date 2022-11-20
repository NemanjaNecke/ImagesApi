from rest_framework import serializers
from .models import Images, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ImageSerializer(serializers.ModelSerializer):
    #category = CategorySerializer(many=True)
    
    class Meta:
        model = Images
        fields = ['id', 'category', 'title', 'alt', 'created', 'author', 'status', 'image']