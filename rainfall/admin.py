from django.contrib import admin
from .models import Rainfall

@admin.register(Rainfall)
class RainfallAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'location', 'created_at']
    list_filter = ['created_at', 'user', 'location']
    readonly_fields = ['created_at']
