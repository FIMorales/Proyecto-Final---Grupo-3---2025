from django.contrib import admin
from .models import Cat, Noticia

# Register your models here.
admin.site.register(Noticia)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'subtitulo', 'fecha_publicacion', 'activo', 'categoria', 'imagen', 'contenido')
    list_filter = ('categoria', 'fecha_publicacion')
    search_fields = ('titulo', 'subtitulo', 'contenido')
    ordering = ('-fecha_publicacion',)

admin.site.register(Cat)