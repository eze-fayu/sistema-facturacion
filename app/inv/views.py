from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Categoria, SubCategoria, Marca, Um, Productos
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UmForm, ProductosForm
from django.urls import reverse_lazy
from django.http import HttpResponse #, JsonResponse
# import json
from bases.views import SinPrivilegios
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.


# ################# CATEGORIA ####################

class CategoriaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required='inv.view_categoria'
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class CategoriaNew(SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, generic.CreateView):
    permission_required='inv.add_categoria'
    model = Categoria
    template_name='inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'
    success_message='Categoría creada exitosamente'
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
      
class CategoriaEdit(SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, generic.UpdateView):
    permission_required='inv.change_categoria'
    model = Categoria
    template_name='inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'
    success_message='Categoría editada exitosamente'
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class CategoriaDel(SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, generic.DeleteView):
    permission_required='inv.delete_categoria'
    model = Categoria
    template_name='inv/catalogo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')
    success_message='Categoría eliminada exitosamente'
    
def categoria_inactivar(request, id):
    categoria = Categoria.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_inac.html"
        
    if not categoria:
        return redirect("inv:categoria_list")
    
    if request.method=="GET":
        contexto={'obj':categoria}
        
    if request.method=="POST":
        if categoria.estado==False:
            categoria.estado=True
            categoria.save()
            # messages.success(request, 'Categoria Activada.')     
            return redirect("inv:categoria_list")
        else:
            categoria.estado=False
            categoria.save()     
            # messages.error(request, 'Categoria Desactivada.') 
            return redirect("inv:categoria_list")
        
    return render(request,template_name,contexto)
    
    
# ################# SUBCATEGORIA ####################
    
    
class SubCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required='inv.view_subcategoria'
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class SubCategoriaNew(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required='inv.add_subcategoria'
    model = SubCategoria
    template_name='inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'
    success_message='Subcategoría creada exitosamente'
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class SubCategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required='inv.change_subcategoria'
    model = SubCategoria
    template_name='inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'
    success_message='Subcategoría editada exitosamente'
    
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class SubCategoriaDel(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required='inv.delete_subcategoria'
    model = SubCategoria
    template_name='inv/catalogo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategoria_list')
    success_message='Subcategoría eliminada exitosamente'
    
def subcategoria_inactivar(request, id):
    subcategoria = SubCategoria.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_inac.html"
        
    if not subcategoria:
        return redirect("inv:subcategoria_list")
    
    if request.method=="GET":
        contexto={'obj':subcategoria}
        
    if request.method=="POST":
        if subcategoria.estado==False:
            subcategoria.estado=True
            subcategoria.save()  
            # messages.success(request, 'Subcategoria Activada.')     
            return redirect("inv:subcategoria_list")
        else:
            subcategoria.estado=False
            subcategoria.save() 
            # messages.error(request, 'Subcategoria Desactivada.')      
            return redirect("inv:subcategoria_list")
        
    return render(request,template_name,contexto)
    
# ################# MARCA ####################

class MarcaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required='inv.view_marca'
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class MarcaNew(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required='inv.add_marca'
    model = Marca
    template_name='inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'
    success_message='Marca creada exitosamente'
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class MarcaEdit(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required='inv.change_marca'
    model = Marca
    template_name='inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'
    success_message='Marca editada exitosamente'
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class MarcaDel(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required='inv.delete_marca'
    model = Marca
    template_name='inv/catalogo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:marca_list')
    success_message='Marca eliminada exitosamente'
    
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_inac.html"
        
    if not marca:
        return redirect("inv:marca_list")
    
    if request.method=="GET":
        contexto={'obj':marca}
        
    if request.method=="POST":
        if marca.estado==False:
            marca.estado=True
            marca.save()  
            # messages.success(request, 'Marca Activada.')     
            return redirect("inv:marca_list")
        else:
            marca.estado=False
            marca.save()
            # messages.error(request, 'Marca Desactivada.')       
            return redirect("inv:marca_list")
        
    return render(request,template_name,contexto)


# ################# UNIDAD MEDIDA ####################

class UmView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required='inv.view_um'
    model = Um
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class UmNew(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required='inv.add_um'
    model = Um
    template_name='inv/um_form.html'
    context_object_name = 'obj'
    form_class = UmForm
    success_url = reverse_lazy('inv:um_list')
    login_url = 'bases:login'
    success_message='Unidad de Medida creada exitosamente'
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class UmEdit(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required='inv.change_um'
    model = Um
    template_name='inv/um_form.html'
    context_object_name = 'obj'
    form_class = UmForm
    success_url = reverse_lazy('inv:um_list')
    login_url = 'bases:login'
    success_message='Unidad de Medida editada exitosamente'
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class UmDel(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required='inv.delete_um'
    model = Um
    template_name='inv/catalogo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:um_list')
    success_message='Unidad de Medida borrada exitosamente'
    
def um_inactivar(request, id):
    um = Um.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_inac.html"
        
    if not um:
        return redirect("inv:um_list")
    
    if request.method=="GET":
        contexto={'obj':um}
        
    if request.method=="POST":
        if um.estado==False:
            um.estado=True
            um.save()      
            # messages.success(request, 'Unidad de Medida Activada.') 
            return redirect("inv:um_list")
        else:
            um.estado=False
            um.save()      
            # messages.error(request, 'Unidad de Medida Desactivada.') 
            return redirect("inv:um_list")
        
    return render(request,template_name,contexto)

# ################# PRODUCTO ####################

class ProductosView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required='inv.view_productos'
    model = Productos
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class ProductosNew(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required='inv.add_productos'
    model = Productos
    template_name='inv/producto_form_popup.html'
    context_object_name = 'obj'
    form_class = ProductosForm
    success_url = reverse_lazy('inv:productos_list')
    login_url = 'bases:login'
    success_message='Producto creada exitosamente'
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class ProductosEdit(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required='inv.change_productos'
    model = Productos
    template_name='inv/producto_form_popup.html'
    context_object_name = 'obj'
    form_class = ProductosForm
    success_url = reverse_lazy('inv:productos_list')
    login_url = 'bases:login'
    success_message='Producto editado exitosamente'
    
    def form_valid(self, form):
        form.instance.producto = self.request.user.id
        return super().form_valid(form)
    
class ProductosDel(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required='inv.delete_productos'
    model = Productos
    template_name='inv/catalogo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:productos_list')
    success_message='Producto eliminado exitosamente'
    
def productos_inactivar(request, id):
    producto = Productos.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_inac.html"
        
    if not producto:
        return redirect("inv:productos_list")
    
    if request.method=="GET":
        contexto={'obj':producto}
        
    if request.method=="POST":
        if producto.estado==False:
            producto.estado=True
            producto.save()      
            # messages.success(request, 'Producto Activado.') 
            return redirect("inv:productos_list")
        else:
            producto.estado=False
            producto.save()      
            # messages.error(request, 'Producto Desactivado.') 
            return redirect("inv:productos_list")
        
    return render(request,template_name,contexto)