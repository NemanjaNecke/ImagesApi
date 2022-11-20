from django.urls import path, include
from .views import ProfilepicByProfile, ProfilepicViewSet, UserViewSet, ProfileAPIKeyView, ProfileViewSet
from rest_framework import routers
from dj_rest_auth.registration.views import VerifyEmailView

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'profile-pic', ProfilepicViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'auth/', include('dj_rest_auth.urls')),
    path(r'auth/registration/', include('dj_rest_auth.registration.urls')),
    path(r'api-key/', ProfileAPIKeyView.as_view()),
    path(r'profile-pic-profile/<int:pk>/', ProfilepicByProfile.as_view())

]
#(?P<key>.+)/