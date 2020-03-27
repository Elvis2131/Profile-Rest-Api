from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer

# Create your views here.
class HelloApiView(APIView):
    """Testing the APIView
    """

    def get(self,request,format=None):
        
        an_apiview = [
            'Uses HTTP.',
            'similar to a django view'
        ]

        return Response({'message': 'Hello', 'to_say':an_apiview})

    def post(self,request):
        """ Create a hello message"""
        serializer = serializer.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello name"
            return Response({'message': message})

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        