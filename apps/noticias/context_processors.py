# apps/noticias/context_processors.py
from .models import Categoria

def categorias_globales(request):
    return {
        'categorias': Categoria.objects.all()
    }