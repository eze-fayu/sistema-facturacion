from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, \
    SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, \
    MarcaView, MarcaNew, MarcaEdit, marca_inactivar, UmNew, UmView, UmEdit, \
    um_inactivar, MarcaDel, UmDel, categoria_inactivar, subcategoria_inactivar

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),
    path('categorias/inactivar/<int:id>', categoria_inactivar, name='categoria_inactivar'),
    
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubCategoriaDel.as_view(), name='subcategoria_del'),
    path('subcategorias/inactivar/<int:id>', subcategoria_inactivar, name='subcategoria_inactivar'),
    
    path('marca/', MarcaView.as_view(), name='marca_list'),
    path('marca/new', MarcaNew.as_view(), name='marca_new'),
    path('marca/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path('marca/inactivar/<int:id>', marca_inactivar, name='marca_inactivar'),  #las funciones no llevan el as_view()
    path('marca/delete/<int:pk>', MarcaDel.as_view(), name='marca_del'),

    path('um/', UmView.as_view(), name='um_list'),
    path('um/new', UmNew.as_view(), name='um_new'),
    path('um/edit/<int:pk>', UmEdit.as_view(), name='um_edit'),
    path('um/inactivar/<int:id>', um_inactivar, name='um_inactivar'),
    path('um/delete/<int:pk>', UmDel.as_view(), name='um_del'),
    
]