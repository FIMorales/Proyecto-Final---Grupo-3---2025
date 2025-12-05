from django.shortcuts import render

def listar_categorias(request):
    return render(request, 'categorias.html')

