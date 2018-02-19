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
