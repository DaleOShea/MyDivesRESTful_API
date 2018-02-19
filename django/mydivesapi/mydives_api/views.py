from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ListLocations(APIView):

    def get(self, request, format = None):

        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
