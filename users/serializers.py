from django.contrib.auth.models import User
from rest_framework import serializers

from images.serializers import ImageSerializer
from .models import Profile, Profilepic, ProfileAPIKey


class UserSerializer(serializers.HyperlinkedModelSerializer):
    author = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email',
                  'is_staff', 'first_name', 'last_name', 'author']


class ProfilepicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profilepic
        fields = ['id', 'pic', 'profile', 'selected']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    profilepic = ProfilepicSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['id','profilepic', 'user']
        lookup_field = 'user_id'
        extra_kwargs = {
            'url': {'lookup_field': 'user_id'}
        }

    
class ProfileApiKeySerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(many=False)

    class Meta:
        model = ProfileAPIKey
        fields = ['apiKey', 'profile']
        lookup_field = 'slug'
