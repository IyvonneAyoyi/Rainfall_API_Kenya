from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Location
from .serializers import LocationSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # automatically associate the logged-in user with the location
        serializer.save(user=self.request.user)
# Retrieve, Update, Delete view for a single Location
class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
