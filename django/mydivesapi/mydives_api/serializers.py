from rest_framework import serializers
from . import models


class LocationSerializer(serializers.Serializer):
    diveLocation = serializers.CharField(min_length = 5, max_length = 70, allow_blank = False)


class LocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocationInfo
        fields = ('id', 'LocType', 'location', 'latitude', 'longitude', 'details')


    def create(self, validated_data):
        location = models.LocationInfo(
            LocType = validated_data['LocType'],
            location = validated_data['location'],
            latitude = validated_data['latitude'],
            longitude = validated_data['longitude'],
            details = validated_data['details'],
        )

        location.save()

        return location
