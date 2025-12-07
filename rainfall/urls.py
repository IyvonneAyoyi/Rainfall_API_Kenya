from django.urls import path
from .views import RainfallView

urlpatterns = [
    path('<int:location_id>/', RainfallView.as_view(), name='rainfall'),
]
