from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'complete', 'created', 'updated']
    list_filter = ['complete', 'created', 'updated']
    search_fields = ['title']
    list_editable = ['complete']
    list_per_page = 10