from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import ProfilepicSerializer, UserSerializer, ProfileApiKeySerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import Profile, Profilepic
from .auth import HasProfileAPIKey
from .models import ProfileAPIKey
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfilepicViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Profilepic.objects.all()
    serializer_class = ProfilepicSerializer

class ProfilepicByProfile(generics.ListAPIView):
    def get_queryset(self):
        queryset = Profilepic.objects.filter(profile=self.kwargs["pk"])
        return queryset
    serializer_class = ProfilepicSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user_id'
class ProfileAPIKeyView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        queryset = ProfileAPIKey.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer_class = ProfileApiKeySerializer(queryset, many=True, context=serializer_context)
        return Response(serializer_class.data)

