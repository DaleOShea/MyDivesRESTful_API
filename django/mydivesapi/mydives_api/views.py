from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
# Create your views here.

class ListLocations(APIView):

    serializer = serializers.LocationSerializer

    def get(self, request, format = None):

        sampleDictionaryLocation = [
            'One',
            'Two',
            'Three',
            'Four',
            'Five',
        ]

        return Response({'Location' : sampleDictionaryLocation})


    def post(self, request, format = None):
        serializer = serializers.LocationSerializer(data = request.data)

        if serializer.is_valid():
            userMessage_dataIsValid = 'Location Added!'
            return Response({'userMessage' : userMessage})
        else: 
            userMessage_dataIsValid = 'Please try again '
            return Response({'userMessage_dataIsValid' : userMessage_dataIsValid})
