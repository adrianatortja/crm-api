from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'client', 'status', 'source', 'created_at')
    list_filter = ('status', 'source', 'created_at')
    search_fields = ('title', 'client__name', 'source')
    
