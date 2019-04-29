from django.shortcuts import render

from .models import Source


def index(request):
    return render(request, 'feed/index.html')


def sources_add(request):
    try:
        name = request.POST['name']
        description = request.POST['description']
        url = request.POST['url']
        source = Source(name=name, description=description, url=url)
        source.save()
    except (KeyError):
        return render(request, 'feed/index.html', {
            'error_message': 'Title or URL not provided.'
        })
    else:
        return render(request, 'feed/index.html', {
            'success_message': 'Source successfully added.'
        })
