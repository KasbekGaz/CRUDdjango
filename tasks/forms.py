from django.forms import ModelForm
from .models import Task #importamos el modelo que vamos usar


class TaskForm(ModelForm):  #creamos las clase
    class Meta:   #introducimos una clase meta para procesar datos
        model = Task  #referenciamos el modelo tarea.
        fields = ['titulo', 'descripcion', 'importante']

