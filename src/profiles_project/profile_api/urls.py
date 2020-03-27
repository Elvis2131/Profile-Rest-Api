from django.urls import path,include

from rest_framework.routes import DefaultRouter
from .views import HelloApiView

from .views import HelloViewSet

Router = DefaultRouter
Router.register('hello-viewset', HelloViewSet, base_name='hello_viewset')

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(Router.urls))
]