from rest_framework import serializers
from .models import Rainfall

class RainfallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rainfall
        fields = [
            'id',
            'user',
            'location',
            'daily_rain_sum',
            'precipitation_hours',
            'hourly_rain',
            'created_at'
        ]
        read_only_fields = ['id', 'user', 'created_at']
