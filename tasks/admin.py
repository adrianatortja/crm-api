from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "lead", "title", "status", "due_date", "created_at")
    list_filter = ("status", "due_date", "created_at")
    search_fields = ("title", "description", "lead__title")
    