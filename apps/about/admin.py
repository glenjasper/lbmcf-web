from django.contrib import admin
from .models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status'
    ]
    readonly_fields = ['created', 'updated']

    class Media:
        css = {
            'all': ('css/custom_ckeditor.css',)
        }

admin.site.register(About, AboutAdmin)
