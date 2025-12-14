from django.urls import path
from .views import lista_noticias

urlpatterns = [
    path('', lista_noticias, name='lista_noticias'),  
]