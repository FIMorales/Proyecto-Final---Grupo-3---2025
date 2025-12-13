from django.db import models
from django.utils import timezone

# Create your models here.

#le voy a poner cat en vez de categoria, porque categoria ya lo tenemos en eventos, y no quiero borrar nada por las dudas jajaj
class Cat(models.Model):
     nombre = models.CharField(max_length=100, null=False, blank=False)

     def __str__(self):
         return self.nombre
     
class Noticia(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    subtitulo = models.CharField(max_length=300, null=False, blank=False)
    contenido = models.TextField(null=False, blank=False)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    activo = models.BooleanField(default=True)

    categoria = models.ForeignKey(Cat, on_delete=models.SET_NULL,null=True, default='Sin categoria')
    imagen = models.ImageField(upload_to='media', default='static/post_default.png' , null=True, blank=True)    
    
    class Meta:
        ordering = ['-fecha_publicacion']
    def __str__(self):
        return self.titulo
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()
   
