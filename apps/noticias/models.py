from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.nombre
    


class Noticia(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='sin categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/noticia_default.png')
    publicado = models.DateTimeField(default= timezone.now)
    
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    def total_likes(self):
        return self.likes.count()
    
    class Meta:
        ordering = ('-publicado',)
        
    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()
        

        
class Comentario(models.Model):
    noticias = models.ForeignKey('noticias.Noticia', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios') 
    texto = models.TextField()     
    fecha = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.texto