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
        
        
class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField( max_length=100, help_text = 'Descripción de la Categoria', unique = True )
    
    def __str__(self):
        return '{}: {}'.format(self.categoria.descripcion, self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()
    
    class Meta:
        verbose_name_plural = 'SubCategorias'
        unique_together = ('categoria','descripcion')
  
        
class Marca(ClaseModelo):
    # el campo id lo crea por defecto django
    descripcion = models.CharField(max_length=100, help_text='Marca', unique=True)
    
    # sobreescribo el metodo str para que cambie lo que muestra
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    # sobreescribo el metodo save para que la descripcion este toda en mayuscula.
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()
    
    # como se va a llamar cuando es plural
    class Meta:
        verbose_name_plural = 'Marcas'
        
        
class Um(ClaseModelo):
    # el campo id lo crea por defecto django
    descripcion = models.CharField(max_length=50, help_text='Unidad Medida', unique=True)
    
    # sobreescribo el metodo str para que cambie lo que muestra
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    # sobreescribo el metodo save para que la descripcion este toda en mayuscula.
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Um, self).save()
    
    # como se va a llamar cuando es plural
    class Meta:
        verbose_name_plural = 'Unidades de Medida'
        
class Productos(ClaseModelo):
    codigo = models.CharField(max_length=50, help_text='Codigo de Producto', unique=True)
    codigo_barra = models.CharField(max_length=13)
    descripcion = models.CharField(max_length=200, help_text='Desc. del Producto')
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)
    
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(Um, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
       
    # sobreescribo el metodo str para que cambie lo que muestra
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    # sobreescribo el metodo save para que la descripcion este toda en mayuscula.
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Productos, self).save()
    
    # como se va a llamar cuando es plural
    class Meta:
        verbose_name_plural = 'Productos'
        unique_together = ('codigo','codigo_barra')