from django.contrib import admin
from .models import Interaction


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ("id", "lead", "interaction_type", "subject", "created_at")
    list_filter = ("interaction_type", "created_at")
    search_fields = ("subject", "notes", "lead__name")
    
