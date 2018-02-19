from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    diveLocation = serializers.CharField(min_length = 5, max_length = 70, allow_blank = False)
