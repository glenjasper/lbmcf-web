from django.contrib import admin
from .models import (
    Project
)

class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'financer',
        'date',
        'status',
    ]
    readonly_fields = ['created', 'updated']

admin.site.register(Project, ProjectAdmin)
