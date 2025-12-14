from django.contrib import admin
from .models import Categoria, Noticia, Comentario

# Register your models here.

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha', 'texto', 'activo', 'categoria', 'imagen', 'publicado')
    
admin.site.register(Categoria)
admin.site.register(Comentario)