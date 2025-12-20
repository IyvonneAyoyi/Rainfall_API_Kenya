from rest_framework import generics, permissions
from .models import APILog
from .serializers import APILogSerializer

class APILogListView(generics.ListAPIView):
    queryset = APILog.objects.all().order_by("-created_at")
    serializer_class = APILogSerializer
    permission_classes = [permissions.IsAdminUser]
