from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Categoria(models.Model):
    genero = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.genero


class Video(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField(max_length=165, blank=True)
    tempo = models.IntegerField()
    publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)
    imagem = models.ImageField(upload_to='home/covers/%Y/%m/%d/')
    data_criacao = models.DateTimeField(auto_now_add=True)
    autualizacao_criacao = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.titulo
