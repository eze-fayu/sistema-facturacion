from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)  # agrega solo la fecha actual para cuando se crea
    fm = models.DateTimeField(auto_now=True)    # agrega solo la fecha actual para cuando se modifica
    uc = models.ForeignKey(User, on_delete=models.CASCADE)  # depende de los usuarios, el usuario logeado. relacion de 1 a muchos. CASCADE HACE QUE SI SE VE EL DE ARRIVA SE VA ESTE
    um = models.IntegerField(blank=True, null=True)  # permite que este en blanco o sea nulo
    
    # para que no tome en cuenta el modelo cuando hace las migraciones
    class Meta:
        abstract=True