from django.urls import path, include

from .views import ProveedorView,ProveedorNew, ProveedorEdit, \
    proveedorInactivar, ProveedorDel, ComprasView, compras, ComprasDetDelete



urlpatterns = [
    path('proveedores/',ProveedorView.as_view(), name="proveedor_list"),
    path('proveedores/new',ProveedorNew.as_view(), name="proveedor_new"),
    path('proveedores/edit/<int:pk>',ProveedorEdit.as_view(), name="proveedor_edit"),
    path('proveedores/inactivar/<int:id>',proveedorInactivar, name="proveedor_inactivar"),
    path('proveedores/delete/<int:pk>', ProveedorDel.as_view(), name='proveedor_del'),
    
    path('compras/',ComprasView.as_view(), name="compras_list"),
    path('compras/new',compras, name='compras_new'),
    path('compras/edit/<int:compra_id>',compras, name="compras_edit"),
    # path('proveedores/inactivar/<int:id>',proveedorInactivar, name="proveedor_inactivar"),
    # path('proveedores/delete/<int:pk>', ProveedorDel.as_view(), name='proveedor_del'),
    path('compras/<int:compra_id>/delete/<int:pk>',ComprasDetDelete.as_view(), name="compras_del"),
]