from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
import json

from .models import Proveedor
from cmp.forms import ProveedorForm
# Create your views here.


class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    login_url = 'bases/login'
    # permission_required="cmp.view_proveedor"

class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class=ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    login_url = 'bases/login'
    # success_message="Proveedor Nuevo"
    # permission_required="cmp.add_proveedor"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)


class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class=ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    login_url = 'bases/login'
    # success_message="Proveedor Editado"
    # permission_required="cmp.change_proveedor"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)


def proveedorInactivar(request,id):
    template_name='cmp/inactivar_prv.html'
    contexto={}
    # hace una consulta por el numero de id que le mandamos (va con el boton del click)
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe ' + str(id))

    # si es una peticion get, le pasa el nombre del provvedor en la pregunta
    if request.method=='GET':
        contexto={'obj':prv}

    # si es posta, manda el cambio, lo guarda, y devuelve msj de estado
    if request.method=='POST':
        if prv.estado==True:    
            prv.estado=False
            prv.save()
            contexto={'obj':'OK'}
            return HttpResponse('Proveedor Inactivado')
        else:
            prv.estado=True
            prv.save()
            contexto={'obj':'OK'}
            return HttpResponse('Proveedor Activado')

    return render(request,template_name,contexto)