from django.db import models

# Create your models here.

class Task(models.Model):
    #nombre del campo/modelo tipo de dato/caracteristica del tipo de dato
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    Fcreado = models.DateTimeField(auto_now_add=True) #para asignar en automatico la fecha y hora en archivo
    Fcompletado = models.DateTimeField(null=True)
    importante = models.BooleanField(default=False)
    # user = 
