from django.db import IntegrityError
from rest_framework import generics, permissions, serializers
from rest_framework.permissions import IsAuthenticated
from .models import Location
from .serializers import LocationSerializer
from .services import geocode_location, reverse_geocode_location

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

        # Convert coordinates to float if provided
        try:
            latitude = float(latitude) if latitude is not None else None
            longitude = float(longitude) if longitude is not None else None
        except (ValueError, TypeError):
            raise serializers.ValidationError(
                {"error": "Latitude and longitude must be numeric values."}
            )

        # Geocode: Name provided but no coordinates
        if name and (latitude is None or longitude is None):
            latitude, longitude = geocode_location(name)
            if latitude is None or longitude is None:
                raise serializers.ValidationError(
                    {"error": "Could not geocode the location name."}
                )

        # Reverse Geocode: Coordinates provided but no name
        if (latitude is not None and longitude is not None) and not name:
            name = reverse_geocode_location(latitude, longitude)
            if not name:
                raise serializers.ValidationError(
                    {"error": "Could not reverse geocode the coordinates."}
                )

        # Save with logged-in user and coordinates
        try:
            serializer.save(
                user=self.request.user,
                name=name,
                latitude=latitude,
                longitude=longitude
            )
        except IntegrityError:
            raise serializers.ValidationError(
                {"error": "You have already added this location."}
            )


# Retrieve, Update, Delete view for a single Location
class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
