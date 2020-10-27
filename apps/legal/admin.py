from django.contrib import admin
from .models import (
    Legal
)

class LegalAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'order',
        'status',
    ]
    readonly_fields = ['created', 'updated']

    class Media:
        css = {
            'all': ('css/custom_ckeditor.css',)
        }

admin.site.register(Legal, LegalAdmin)
