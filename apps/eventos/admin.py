from django.contrib import admin
from .models import Evento, Categoria

# Register your models here.

class Eventoadmin(admin.ModelAdmin):
    fields = ('titulo','descripcion')
    list_display = ('titulo', 'fecha_inicio')
    search_fields = ('titulo',)


admin.site.register(Categoria)
admin.site.register(Evento)

