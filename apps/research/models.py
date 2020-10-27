from django.db import models
from apps.core.models import Financer

class Project(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Project name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Project summary')
    financer = models.ForeignKey(to = Financer, on_delete = models.CASCADE, verbose_name = 'Financer name')
    date = models.DateField(help_text = 'project start date', verbose_name = 'Start date')
    image = models.ImageField(upload_to = "research", verbose_name = "Reference image")
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-date"]

    def __str__(self):
        return self.title
