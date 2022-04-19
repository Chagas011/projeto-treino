from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/search/', views.search, name='search'),
    path('home/video/<int:id>/', views.video, name='v'),
    path('home/categoria/<int:categoria_id>/',
         views.categoria, name='categoria'),

]
