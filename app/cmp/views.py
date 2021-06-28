from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import datetime
import json
from bases.views import SinPrivilegios
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Proveedor, ComprasEnc, CompraDetalle
from cmp.forms import ProveedorForm, ComprasEncForm
from inv.models import Productos
# Create your views here.


class ProveedorView(SuccessMessageMixin, SinPrivilegios, generic.ListView):
    permission_required='cmp.view_proveedores'
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    # permission_required="cmp.view_proveedor"

class ProveedorNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class=ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    success_message="Proveedor creado exitosamente"
    # permission_required="cmp.add_proveedor"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)

class ProveedorEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class=ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    success_message="Proveedor Editado exitosamente"
    # permission_required="cmp.change_proveedor"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)
    
class ProveedorDel(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    model = Proveedor
    template_name='cmp/catalogo_cmp_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('cmp:proveedor')
    success_message='Producto eliminado exitosamente'

@login_required(login_url='/login/') #mira q estes logueado
@permission_required('cmp.change_proveedor', login_url='bases:sin_privilegios') # mira que tengas permisos
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
            # messages.success(request, 'Proveedor Activado.') 
            contexto={'obj':'OK'}
            return HttpResponse('Proveedor Inactivado')
        else:
            prv.estado=True
            prv.save()
            # messages.error(request, 'Proveedor Desactivado.') 
            contexto={'obj':'OK'}
            return HttpResponse('Proveedor Activado')

    return render(request,template_name,contexto)

###################### COMPRAS ##############################3

class ComprasView(SuccessMessageMixin, SinPrivilegios, generic.ListView):
    permission_required='cmp.view_comprasenc'
    model = ComprasEnc
    template_name = "cmp/compras_list.html"
    context_object_name = "obj"
    # permission_required="cmp.view_proveedor"
    
@login_required(login_url='/login/') #mira q estes logueado
@permission_required('cmp.view_comprasenc', login_url='bases:sin_privilegios') # mira que tengas permisos
def compras(request, compra_id=None):
    template_name = "cmp/compras.html"
    prod = Productos.objects.filter(estado=True)
    form_compras = {}
    contexto = {}
    
    if request.method == 'GET':
        form_compras = ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()
        
        if enc:
            det = CompraDetalle.objects.filter(compras=enc)
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            e = {
                'fecha_compra':fecha_compra,
                'proveedor': enc.proveedor,
                'observacion':enc.observacion,
                'no_factura':enc.nro_factura,
                'fecha_factura': fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }
            
            form_compras = ComprasEncForm(e)
        else:
            det=None
            
        contexto={'productos':prod, 'encabezado':enc, 'detalle':det, 'form_enc':form_compras}
        
        return render(request, template_name, contexto)