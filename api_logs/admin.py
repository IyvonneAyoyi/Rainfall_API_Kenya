from django.contrib import admin
from .models import APILog

@admin.register(APILog)
class APILogAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'method', 'path', 'status_code', 'ip_address', 'created_at']
    list_filter = ['method', 'status_code', 'created_at']
    search_fields = ['path', 'ip_address', 'user__username']
    readonly_fields = ['created_at', 'user', 'method', 'path', 'status_code', 'ip_address']
