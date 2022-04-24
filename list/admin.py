from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'complete', 'user']
    list_filter = ['created', 'user']
    search_fields = ['title']
