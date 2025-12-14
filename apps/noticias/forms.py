from django import forms
from .models import Comentario,Noticia,Categoria

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        
class CrearNoticiaForm(forms.ModelForm):
    class Meta:
        model=Noticia
        fields = '__all__'
        
class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'