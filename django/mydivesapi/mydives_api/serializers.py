from rest_framework import serializers


class Location(serializers.Seializer):
    diveLocation = serializers.CharField(min_length = 5, max_length = 70, allow_blank = False)
