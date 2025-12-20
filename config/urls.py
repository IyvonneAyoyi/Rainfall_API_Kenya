"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework.views import APIView

class HealthCheckView(APIView):
    """Health check endpoint"""
    permission_classes = []
    
    def get(self, request):
        return Response({"status": "ok", "message": "Rainfall API is running"})

urlpatterns = [
    path('', HealthCheckView.as_view(), name='health-check'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/', include('locations.urls')),

    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/rainfall/', include('rainfall.urls')),
    path("api/", include("api_logs.urls")),

]
