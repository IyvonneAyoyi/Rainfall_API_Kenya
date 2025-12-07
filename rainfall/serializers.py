from rest_framework import serializers

class RainfallSerializer(serializers.Serializer):
    location = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    rainfall_today_mm = serializers.FloatField(allow_null=True)
