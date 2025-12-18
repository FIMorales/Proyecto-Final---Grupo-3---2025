from django.shortcuts import render ,redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Noticia, Comentario, Categoria
from .forms import ComentarioForm, CrearNoticiaForm, NuevaCategoriaForm



# Create your views here.

#def noticias(request):
#    noticias = Noticia.objects.all()
#    return render (request, 'noticas.html', {'noticias' : noticias})

## Vista basada en clases
class NoticiaListView(ListView):
    model = Noticia
    template_name = "noticias/noticias.html"
    context_object_name = 'noticias'
    

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = "noticias/noticia_individual.html"
    context_object_name = 'noticias'
    pk_url_kwarg = 'id'
    queryset = Noticia.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(noticias_id = self.kwargs['id'])
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit = False)
            comentario.usuario = request.user
            comentario.noticias_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.noticias:noticia_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        
        
class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/agregarComentario.html' 
    success_url = 'comentario/comentarios/'  
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.noticias_id = self.kwargs['noticias_id']
        return super().form_valid(form)  
    


class NoticiaCreateView(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = CrearNoticiaForm  
    template_name = 'noticias/crear_noticia.html'
    success_url = reverse_lazy('apps.noticias:noticias')
    
class CategoriaCreateView(LoginRequiredMixin ,CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name= 'noticias/crear_categoria.html'
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('apps.noticias:crear_noticia')

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'noticias/categoria_list.html' 
    context_object_name = 'categorias' 
    
class CategoriaDeleteView(LoginRequiredMixin ,DeleteView):
    model = Categoria
    template_name = 'noticias/categoria_confirm_delete.html'
    success_url = reverse_lazy('apps.noticias:categoria_list')   
    

class NoticiaUpdateViews(LoginRequiredMixin, UpdateView):
    model = Noticia
    form_class = CrearNoticiaForm
    template_name = 'noticias/modificar_noticia.html'
    success_url = reverse_lazy('apps.noticias:noticias')
    
class NoticiaDeleteViews(LoginRequiredMixin, DeleteView):
    model = Noticia
    template_name = 'noticias/eliminar_noticia.html'
    success_url = reverse_lazy('apps.noticias:noticias' )
    
    

## vista de filtrar noticia por categoria   
def noticias_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    noticias = Noticia.objects.filter(
        categoria=categoria,
        activo=True
    )

    return render(request, 'noticias/noticias_por_categoria.html', {
        'categoria': categoria,
        'noticias': noticias
    })
    

    
    

def like_noticia(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    noticia = get_object_or_404(Noticia, pk=pk)

    if request.user in noticia.likes.all():
        noticia.likes.remove(request.user)
    else:
        noticia.likes.add(request.user)

    return redirect('apps.noticias:noticia_individual', id=noticia.id)


## Buscador de noticias
class BuscarNoticiasView(ListView):
    model = Noticia
    template_name = "noticias/buscar.html"
    context_object_name = "noticias"

    def get_queryset(self):
        query = self.request.GET.get("q")

        if query:
            return Noticia.objects.filter(
                Q(titulo__icontains=query) |
                Q(texto__icontains=query)
            )

        return Noticia.objects.none()
