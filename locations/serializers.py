from rest_framework import serializers
from django.utils.timezone import localtime
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['id', 'user', 'name', 'latitude', 'longitude', 'created_at']
        read_only_fields = ['id', 'created_at', 'user']

    def get_created_at(self, obj):
        # Convert UTC to local timezone (Africa/Nairobi)
        return localtime(obj.created_at).strftime("%Y-%m-%d %H:%M:%S")
