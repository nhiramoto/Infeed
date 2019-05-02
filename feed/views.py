from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import RedirectView

from .models import Source, SourceList


def index(request, success_message=None, error_message=None):
    source_lists = SourceList.objects.all()
    return render(request, 'feed/index.html', {
        'source_lists': source_lists,
        'sucess_message': success_message,
        'error_message': error_message
    })


def lists_add(request):
    source_lists = SourceList.objects.all()
    try:
        name = request.POST['name']
        if len(name) == 0:
            raise KeyError
        source_list = SourceList(name=name)
        source_list.save()
    except KeyError:
        return render(request, 'feed/index.html', {
            'source_lists': source_lists,
            'error_message': 'Name not provided.'
        })
    else:
        return render(request, 'feed/index.html', {
            'source_lists': source_lists,
            'success_message': f'List "{name}" successfully added.'
        })


def sources_add(request):
    source_lists = SourceList.objects.all()
    try:
        name = request.POST['name']
        description = request.POST['description']
        source_list_id = request.POST['source_list_id']
        url = request.POST['url']
        if len(name) == 0 or len(url) == 0:
            raise KeyError
        source_list = get_object_or_404(SourceList, pk=source_list_id)
        source_list.source_set.create(name=name, description=description,
                                      url=url)
        source_list.save()
    except KeyError:
        return render(request, 'feed/index.html', {
            'source_lists': source_lists,
            'error_message': 'Title or URL not provided.'
        })
    else:
        return render(request, 'feed/index.html', {
            'source_lists': source_lists,
            'success_message': f'Source "{name}" successfully added.'
        })
