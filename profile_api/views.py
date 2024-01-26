from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from profile_api import serializers
# Create your views here.

class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        "This is it",
        "I am sleepy","3ew",
        "I have knowledge of AWS"
        ]

        return Response({'message':'Hello API !!','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data )

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle partial updating an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Handle Deleting an object"""
        return Response({'method':'DELETE'})

class HelloViewSets(viewsets.ViewSet):
    """Test View Set"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello Message"""
        a_view = [
            'Uses actions (lists, retrieve, create, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]

        return Response({ 'message':'Hello', 'a_viewset': a_view })
    
    def create(self, request):
        """Create a new hello function"""
        serializer = self.serializer_class(data=request.data )

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, request, pk=None):
        """Handle getting an object by its id """
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle partial updation of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle deletion of an object"""
        return Response({'http_method':'DELETE'})
        