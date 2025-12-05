from django.urls import path
from .views import listar_contacto

urlpatterns = [
    path('', listar_contacto, name="inicio")
]

