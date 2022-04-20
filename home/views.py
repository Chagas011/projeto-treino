from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Video

# Create your views here.


def home(request):
    videos = get_list_or_404(Video, publicado=True)
    messages.success(request, 'Welcome')
    return render(request, 'home/pages/home.html', context={
        'videos': videos
    })


def video(request, id):
    video = get_object_or_404(Video, publicado=True, pk=id)

    return render(request, 'home/pages/video.html', context={
        'videos': video
    })


def categoria(request, categoria_id):
    categoria = get_list_or_404(
        Video, publicado=True, categoria__id=categoria_id)

    return render(request, 'home/pages/categoria.html', context={
        'videos': categoria
    })


def search(request):
    search_term = request.GET.get('search', '').strip()
    if not search_term:
        raise Http404()

    messages.success(request, 'Busca encontrada')
    videos = Video.objects.filter(
        Q(
            Q(titulo__icontains=search_term) |
            Q(descricao__icontains=search_term),
        ),
        publicado=True
    ).order_by('-id')

    return render(request, 'home/pages/search.html', context={
        'search_term': search_term,
        'videos': videos
    })
