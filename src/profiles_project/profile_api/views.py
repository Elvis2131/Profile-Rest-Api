from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from .models import *
from .serializers import (HelloSerializer,UserProfileSerilaizer)
from .permissions import *


# Create your views here.
class HelloApiView(APIView):
    """Testing the APIView
    """
    serializer_class = HelloSerializer

    def get(self,request,format=None):
        
        an_apiview = [
            'Uses HTTP.',
            'similar to a django view'
        ]

        return Response({'message': 'Hello', 'to_say':an_apiview})

    def post(self,request):
        serializer = HelloSerializer(data=request.POST)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'message':'put'})

    def patch(self,request,pk=None):
        return Response({'message':'patch'})


    def delete(self,request,pk=None):
        return Response({'message':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Testing API Viewset"""
    serializer_class = HelloSerializer

    def list(self,request):
        return Response({'message':'List created successfully'})

    def create(self,request):
        """Post function for a viewset"""

        serializer = HelloSerializer(data=request.POST)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = "Hello {0}".format(name)

            return Response({'Message':msg})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """ Handles getting an object via the pk"""
        return Response({"Message":'Get an object'})

    def update(self,request,pk=None):
        """Handles updating an object"""
        return Response({"Message":"Updating an object"})

    def partial_update(self,request,pk=None):
        """ Handles the patch http request"""
        return Response({"Message":"Partial updating an object"})

    def destroy(self,request,pk=None):
        """ Handles the destroy function"""
        return Response({"Message":"Deleting an object"})

class UserProfileViewset(viewsets.ModelViewSet):
    """Handles the CRUD function for profiles"""

    serializer_class = UserProfileSerilaizer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self,request):
        """Use the ObtainAuthToken APIView to validate and create a token"""
        return ObtainAuthToken().post(request)