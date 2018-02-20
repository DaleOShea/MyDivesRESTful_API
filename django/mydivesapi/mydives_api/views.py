from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets


class ListLocations(APIView):

    serializer_class = serializers.LocationSerializer

    def get(self, request, format = None):

        sampleDictionaryLocation = [
            'One',
            'Two',
            'Three',
            'Four',
            'Five',
        ]

        return Response({'Location' : sampleDictionaryLocation})


    def post(self, request):
        serializer = serializers.LocationSerializer(data = request.data)

        if serializer.is_valid():
            userMessage_dataIsValid = 'Location Added!'
            return Response({'userMessage' : userMessage_dataIsValid})
        else:
            userMessage_dataIsNotValid = 'Please try again'
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk = None):
        return Response(status = status.HTTP_204_N0_CONTENT)

class MyDivesViewSet(viewsets.ViewSet):
    
