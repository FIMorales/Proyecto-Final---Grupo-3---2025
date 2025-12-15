from django.urls import path
from .views import *
from .views import like_noticia


app_name = "apps.noticias"

urlpatterns = [
    path('noticias/', NoticiaListView.as_view(), name='noticias'),
    path('noticias/<int:id>/', NoticiaDetailView.as_view(), name='noticia_individual' ),
    path("noticia/",  NoticiaCreateView.as_view(), name="crear_noticia"),
    path("noticia/categoria", CategoriaCreateView.as_view(), name="crear_categoria"),
    path("categoria/", CategoriaListView.as_view(), name="categoria_list"),
    path("categoria/<int:pk>/delete/", CategoriaDeleteView.as_view(), name="categoria_delete"),
    path("noticia/<int:pk>/modificar/", NoticiaUpdateViews.as_view(), name="noticia_update"),
    path("noticia/<int:pk>/eliminar/", NoticiaDeleteViews.as_view(), name="noticia_delete"),
    path('noticia/<int:pk>/like/', like_noticia, name='noticia_like'),
    path('categoria/<int:categoria_id>/',noticias_por_categoria, name='por_categoria'),
]
