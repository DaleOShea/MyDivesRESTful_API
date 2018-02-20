from rest_framework import serializers
from . import models


class LocationSerializer(serializers.Serializer):
    diveLocation = serializers.CharField(min_length = 5, max_length = 70, allow_blank = False)


class LocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocationInfo
        fields = ('id', 'LocType', 'location', 'latitude', 'longitude', 'details')
