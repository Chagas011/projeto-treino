from django.shortcuts import get_list_or_404, render, get_object_or_404

# Create your views here.


def home(request):
    return render(request, 'home/pages/home.html', context={
    })


def video(request):
    return render(request, 'home/pages/video.html', context={
        'range': range(10)
    })
