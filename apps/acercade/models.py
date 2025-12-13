from django.db import models

# Create your models here.
from django.db import models

class Acercade(models.Model):
    titulo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Acerca de'
        verbose_name_plural = 'Acerca de'

