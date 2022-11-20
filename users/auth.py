from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import BaseHasAPIKey, KeyParser
from users.models import ProfileAPIKey
from rest_framework import permissions
from .models import ProfileAPIKey

class HasProfileAPIKey(permissions.BasePermission):
    def has_permission(self, request, view):
        api_key = request.GET.get("api_key")
        keys = ProfileAPIKey.objects.all()
        for key in keys:
            if str(key) == str(api_key):
                return True


    #/?api_key=ffL1pu6c.WAkqHfWFUrKOqTdVFhEOuv98yaJ0QCAx
    #7zbtYFuW.4BVF7nk5As6oBPnbSHhY2gbH4mMszV9c