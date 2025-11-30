from rest_framework import generics, permissions, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from .services import geocode_location

# List and Create view for Locations
class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Get input data
        name = self.request.data.get("name")
        latitude = self.request.data.get("latitude")
        longitude = self.request.data.get("longitude")

        # If user provided a location name but no lat/lng, geocode it
        if name and (not latitude or not longitude):
            latitude, longitude = geocode_location(name)
            if latitude is None or longitude is None:
                raise serializers.ValidationError(
                    {"error": "Could not geocode the location name."}
                )

        # Save with logged-in user and geocoded coordinates if available
        serializer.save(
            user=self.request.user,
            latitude=latitude if latitude is not None else self.request.data.get("latitude"),
            longitude=longitude if longitude is not None else self.request.data.get("longitude")
        )


# Retrieve, Update, Delete view for a single Location
class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
