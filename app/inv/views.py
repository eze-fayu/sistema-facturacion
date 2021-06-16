from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria, SubCategoria, Marca, Um
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UmForm
from django.urls import reverse_lazy


# Create your views here.


# ################# CATEGORIA ####################

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name='inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    
class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name='inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name='inv/catalogo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')
    
def categoria_inactivar(request, id):
    categoria = Categoria.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_del.html"
        
    if not categoria:
        return redirect("inv:categoria_list")
    
    if request.method=="GET":
        contexto={'obj':categoria}
        
    if request.method=="POST":
        if categoria.estado==False:
            categoria.estado=True
            categoria.save()      
            return redirect("inv:categoria_list")
        else:
            categoria.estado=False
            categoria.save()      
            return redirect("inv:categoria_list")
        
    return render(request,template_name,contexto)
    
    
# ################# SUBCATEGORIA ####################
    
    
class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name='inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name='inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name='inv/catalogo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategoria_list')
    
def subcategoria_inactivar(request, id):
    subcategoria = SubCategoria.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_del.html"
        
    if not subcategoria:
        return redirect("inv:subcategoria_list")
    
    if request.method=="GET":
        contexto={'obj':subcategoria}
        
    if request.method=="POST":
        if subcategoria.estado==False:
            subcategoria.estado=True
            subcategoria.save()      
            return redirect("inv:subcategoria_list")
        else:
            subcategoria.estado=False
            subcategoria.save()      
            return redirect("inv:subcategoria_list")
        
    return render(request,template_name,contexto)
    
# ################# MARCA ####################

class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name='inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name='inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class MarcaDel(LoginRequiredMixin, generic.DeleteView):
    model = Marca
    template_name='inv/catalogo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:marca_list')
    

def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_del.html"
        
    if not marca:
        return redirect("inv:marca_list")
    
    if request.method=="GET":
        contexto={'obj':marca}
        
    if request.method=="POST":
        if marca.estado==False:
            marca.estado=True
            marca.save()      
            return redirect("inv:marca_list")
        else:
            marca.estado=False
            marca.save()      
            return redirect("inv:marca_list")
        
    return render(request,template_name,contexto)


# ################# UNIDAD MEDIDA ####################

class UmView(LoginRequiredMixin, generic.ListView):
    model = Um
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class UmNew(LoginRequiredMixin, generic.CreateView):
    model = Um
    template_name='inv/um_form.html'
    context_object_name = 'obj'
    form_class = UmForm
    success_url = reverse_lazy('inv:um_list')
    login_url = 'bases:login'
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class UmEdit(LoginRequiredMixin, generic.UpdateView):
    model = Um
    template_name='inv/um_form.html'
    context_object_name = 'obj'
    form_class = UmForm
    success_url = reverse_lazy('inv:um_list')
    login_url = 'bases:login'
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class UmDel(LoginRequiredMixin, generic.DeleteView):
    model = Um
    template_name='inv/catalogo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:um_list')
    

def um_inactivar(request, id):
    um = Um.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_del.html"
        
    if not um:
        return redirect("inv:um_list")
    
    if request.method=="GET":
        contexto={'obj':um}
        
    if request.method=="POST":
        if um.estado==False:
            um.estado=True
            um.save()      
            return redirect("inv:um_list")
        else:
            um.estado=False
            um.save()      
            return redirect("inv:um_list")
        
    return render(request,template_name,contexto)