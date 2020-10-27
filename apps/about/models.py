from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    title = models.CharField(max_length = 100, verbose_name = 'Title', help_text = "It's not used, it's only referential.")
    # description = models.TextField(verbose_name = 'Description', help_text = 'Description')
    description = RichTextField(verbose_name = 'Description')
    status = models.BooleanField(default = True, verbose_name = 'Status')    
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.title
