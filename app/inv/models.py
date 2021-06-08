from django.db import models
from bases.models import ClaseModelo

# Create your models here.

class Categoria(ClaseModelo):
    # el campo id lo crea por defecto django
    descripcion = models.CharField(max_length=100, help_text='Descripción de la Categoría', unique=True)
    
    # sobreescribo el metodo str para que cambie lo que muestra
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    # sobreescribo el metodo save para que la descripcion este toda en mayuscula.
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
    
    # como se va a llamar cuando es plural
    class Meta:
        verbose_name_plural = 'Categorias'