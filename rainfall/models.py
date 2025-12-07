from django.db import models
from django.contrib.auth import get_user_model
from locations.models import Location

User = get_user_model()

class Rainfall(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    daily_rain_sum = models.JSONField(null=True, blank=True)
    precipitation_hours = models.JSONField(null=True, blank=True)
    hourly_rain = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rainfall for {self.location.name} at {self.created_at}"
