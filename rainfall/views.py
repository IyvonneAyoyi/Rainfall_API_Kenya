from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from locations.models import Location
from .rainfall import get_daily_rainfall
from .serializers import RainfallSerializer


class RainfallForLocation(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, location_id):
        try:
            location = Location.objects.get(id=location_id, user=request.user)
        except Location.DoesNotExist:
            return Response({"error": "Location not found."}, status=404)

        rainfall = get_daily_rainfall(location.latitude, location.longitude)

        data = {
            "location": location.name,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "rainfall_today_mm": rainfall
        }

        serializer = RainfallSerializer(data)
        return Response(serializer.data)
