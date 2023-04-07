from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
      readonly_fields = ("Fcreado", ) #Le decimos que campos quiero de lectura y se la pasamos a admin.site
#se coloca un espacio despues porque es una tupla.
#Esto quiere decir que no puedo editar este campo puesto que es solo lectura.
admin.site.register(Task, TaskAdmin) #para que pueda modificar en la tabla en la pagina admin.
