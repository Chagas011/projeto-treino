
from django.test import TestCase
from django.urls import reverse


class ProjetoUrlTest(TestCase):
    def test_projeto_url_home(self):
        home_ulr = reverse('polls:home')
        self.assertEqual(home_ulr, '/')

    def test_projeto_url_video(self):
        home_ulr = reverse('polls:video', kwargs={'id': 1})
        self.assertEqual(home_ulr, '/home/video/1')
