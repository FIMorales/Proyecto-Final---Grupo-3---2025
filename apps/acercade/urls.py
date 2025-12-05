from django.urls import path
from .views import listar_acercade

urlpatterns = [
    path('',listar_acercade, name="inicio")
]
