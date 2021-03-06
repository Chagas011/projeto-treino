# Generated by Django 4.0.3 on 2022-04-01 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=65)),
                ('descricao', models.TextField(blank=True, max_length=165)),
                ('tempo', models.IntegerField()),
                ('publicado', models.BooleanField(default=False)),
                ('imagem', models.ImageField(upload_to='video/covers/%Y/%m/%d/')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('autualizacao_criacao', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.categoria')),
            ],
        ),
    ]
