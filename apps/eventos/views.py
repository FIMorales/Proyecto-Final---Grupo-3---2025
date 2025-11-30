from django.shortcuts import render

def listar_eventos(request):
    return render(request, 'todos_los_eventos.html')

