from django.urls import path
from .views import RainfallForLocation

urlpatterns = [
    path('<int:location_id>/today/', RainfallForLocation.as_view(), name='today-rainfall'),
]
