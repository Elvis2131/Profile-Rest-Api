from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer

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


class HelloViewSet(viewsets.Viewset):
    """Testing API Viewset"""

    def list(self,request):
        return Response({'message':'List created successfully'})