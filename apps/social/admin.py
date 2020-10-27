from django.contrib import admin
from .models import (
    LinkSocial
)

class LinkSocialAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'url',
        'status',
    ]
    readonly_fields = ['created', 'updated']

    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name = "regular").exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(LinkSocial, LinkSocialAdmin)
