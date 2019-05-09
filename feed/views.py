from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import RedirectView

from .models import Source, List


def login(request, error_message=None):
    """
    Login page.
    """
    return render(request, 'feed/login.html', {
        'error_message': error_message
    })


def user_login(request):
    """
    Authenticate user.
    """
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'feed/all.html')
        else:
            return render(request, 'feed/login.html', {
                'error_message': 'User not found.'
            })
    except KeyError:
        return render(request, 'feed/login.html', {
            'error_message': 'User name or password not provided.'
        })


def all(request, success_message=None, error_message=None):
    """
    Default page: list items from all sources.
    """
    source_lists = List.objects.all()
    return render(request, 'feed/all.html', {
        'source_lists': source_lists,
        'sucess_message': success_message,
        'error_message': error_message
    })


def lists_add(request):
    source_lists = List.objects.all()
    try:
        name = request.POST['name']
        if len(name) == 0:
            raise KeyError
        source_list = List(name=name)
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
    source_lists = List.objects.all()
    try:
        name = request.POST['name']
        description = request.POST['description']
        source_list_id = request.POST['source_list_id']
        url = request.POST['url']
        if len(name) == 0 or len(url) == 0:
            raise KeyError
        source_list = get_object_or_404(List, pk=source_list_id)
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
