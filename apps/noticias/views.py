from django.shortcuts import render
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'lista_noticias.html', {'noticias': noticias})

# Create your views here.
