from django.shortcuts import render

def listar_contacto(request):
    return render(request, 'contacto.html')


