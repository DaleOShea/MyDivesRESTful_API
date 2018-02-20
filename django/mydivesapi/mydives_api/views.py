from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets
from . import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication



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

    def list(self, request):

        sampleViewSetTestingDictionary = [
            'One_View',
            'Two_View',
            'Three_View',
            'Four_View',
            'Five_View',
        ]

        return Response({'ViewSet' :sampleViewSetTestingDictionary})


    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationInfoSerializer
    queryset = models.LocationInfo.objects.all()

    filter_backends = (filters.SearchFilter,)
    search_fields = ('LocType', 'location', 'details')

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.allowAccessToUserOwnContent)
