
from django.test import TestCase
from django.urls import reverse


class ProjetoUrlTest(TestCase):
    def test_projeto_url_home(self):
        home_ulr = reverse('polls:home')
        self.assertEqual(home_ulr, '/')

    def test_projeto_url_video(self):
        video_url = reverse('polls:v', kwargs={'id': 1})
        self.assertEqual(video_url, '/home/video/1/')

    def test_projeto_url_categoria(self):
        categoria_ulr = reverse('polls:categoria', kwargs={'categoria_id': 1})
        self.assertEqual(categoria_ulr, '/home/categoria/1/')
