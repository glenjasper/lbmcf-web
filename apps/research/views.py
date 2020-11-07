from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView
)
from .models import (
    Project,
    Protocol,
    File
)

class ProjectView(ListView):
    model = Project
    queryset = Project.objects.all().filter(status = True)
    template_name = "research/projects.html"
    context_object_name = "context_projects"

class ProtocolView(ListView):
    model = Protocol
    queryset = Protocol.objects.all().filter(status = True)

    _queryset = {}
    for item in queryset:
        protocol_type = item.type.name
        protocol_description = item.type.description

        protocol_item_name = item.name
        protocol_item_description = item.description
        protocol_item_pdf = item.pdf

        _protocol = {'name': protocol_item_name,
                     'description': protocol_item_description,
                     'pdf': protocol_item_pdf}

        if protocol_type not in _queryset:
            _queryset.update({protocol_type: {'description': protocol_description,
                                              'items': [_protocol]}})
        else:
            _current = _queryset[protocol_type].copy()
            _current['items'].append(_protocol)
            _queryset.update({protocol_type: _current})
    queryset = _queryset

    template_name = "research/protocols.html"
    context_object_name = "context_protocols"

class FileView(ListView):
    model = File
    queryset = File.objects.all().filter(status = True)

    _queryset = {}
    for item in queryset:
        file_type = item.type.name
        file_description = item.type.description

        file_item_name = item.name
        file_item_description = item.description
        file_item_pdf = item.pdf

        _file = {'name': file_item_name,
                     'description': file_item_description,
                     'pdf': file_item_pdf}

        if file_type not in _queryset:
            _queryset.update({file_type: {'description': file_description,
                                              'items': [_file]}})
        else:
            _current = _queryset[file_type].copy()
            _current['items'].append(_file)
            _queryset.update({file_type: _current})
    queryset = _queryset

    template_name = "research/files.html"
    context_object_name = "context_files"
