from rest_framework import serializers
from .models import Location 

class LocationSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)

    class Meta:
        model = Location
        fields = ['id', 'user', 'name', 'latitude', 'longitude', 'created_at']
        read_only_fields = ['id', 'created_at', 'user']
