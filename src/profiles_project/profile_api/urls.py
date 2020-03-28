from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewset,LoginViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='helloviewset')
router.register('profile', UserProfileViewset)
router.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls))
]