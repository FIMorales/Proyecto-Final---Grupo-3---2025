from django.shortcuts import render
from apps.noticias.models import Noticia

def index(request):
    ultimas_noticias = Noticia.objects.order_by('-fecha')[:5]
    return render(request, 'index.html', {
        'ultimas_noticias': ultimas_noticias
    })


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')