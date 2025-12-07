from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from locations.models import Location
from .models import Rainfall
from .serializers import RainfallSerializer
from .rainfall import fetch_rainfall


class RainfallView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, location_id):
        # Ensure location belongs to user
        try:
            location = Location.objects.get(id=location_id, user=request.user)
        except Location.DoesNotExist:
            return Response({"error": "Location not found"}, status=404)

        # Fetch rainfall data from Open-Meteo
        result = fetch_rainfall(location.latitude, location.longitude)

        if "error" in result:
            return Response({"error": result["error"]}, status=400)

        # Save to DB
        rainfall_record = Rainfall.objects.create(
            user=request.user,
            location=location,
            hourly_rain=result["hourly_rain"],
            daily_rain_sum=result["daily_rain_sum"],
            precipitation_hours=result["precipitation_hours"]
        )

        serializer = RainfallSerializer(rainfall_record)
        return Response(serializer.data, status=200)
