from django.contrib import admin

# Register your models here.
from .models import Categoria, SubCategoria, Marca, Um, Productos

admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Marca)
admin.site.register(Um)
admin.site.register(Productos)