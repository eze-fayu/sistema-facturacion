from django.contrib import admin

# Register your models here.
from .models import Categoria, SubCategoria

admin.site.register(Categoria)
admin.site.register(SubCategoria)