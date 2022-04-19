from django.contrib import admin

from .models import Categoria, Video

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Video, VideoAdmin)
