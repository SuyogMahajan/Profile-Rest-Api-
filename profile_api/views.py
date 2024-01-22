from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        "This is it",
        "I am sleepy",
        "I am trying to learn something new",
        "I have knowledge of AWS"
        ]

        return Response({'message':'Hello API !!','an_apiview':an_apiview})
