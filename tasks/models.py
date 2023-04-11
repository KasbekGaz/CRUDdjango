from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    #nombre del campo/modelo tipo de dato/caracteristica del tipo de dato
    titulo = models.CharField(max_length=200) #Titulo
    descripcion = models.TextField(blank=True) #Descripcion
    Fcreado = models.DateTimeField(auto_now_add=True) #para asignar en automatico la fecha y hora en archivo
    Fcompletado = models.DateTimeField(null=True, blank=True) #fecha de completado el blank es para pasar el dato vacio el admin
    importante = models.BooleanField(default=False) #asignar si es importante
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #id usuario

    def __str__(self) -> str:
        return self.titulo + ' - Esta tarea es de: -' + self.user.username
    
