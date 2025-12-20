from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'latitude', 'longitude', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['name']
    readonly_fields = ['created_at']
