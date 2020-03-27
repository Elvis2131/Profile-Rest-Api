from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewset

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='helloviewset')
router.register('profile', UserProfileViewset)

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls))
]