from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView
)
from .models import (
    Project,
)

class ProjectView(ListView):
    model = Project
    queryset = Project.objects.all().filter(status = True)
    template_name = "research/projects.html"
    context_object_name = "context_projects"

class ProtocolView(TemplateView):
    template_name = "research/protocols.html"

class FileView(TemplateView):
    template_name = "research/files.html"
