from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Video

# Create your views here.


def home(request):
    videos = get_list_or_404(Video, publicado=True)

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
