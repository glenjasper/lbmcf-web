from django.contrib import admin
from .models import (
    Project,
    Protocol,
    File
)

class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'financer',
        'date',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class ProtocolAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'type',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class FileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'type',
        'status',
    ]
    readonly_fields = ['created', 'updated']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Protocol, ProtocolAdmin)
admin.site.register(File, FileAdmin)
