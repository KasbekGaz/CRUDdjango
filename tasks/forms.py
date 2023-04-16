from django import forms
from .models import Task #importamos el modelo que vamos usar


class TaskForm(forms.ModelForm):  #creamos las clase
    class Meta:   #introducimos una clase meta para procesar datos
        model = Task  #referenciamos el modelo tarea.
        fields = ['titulo', 'descripcion', 'importante']
        widgets = { #esto es un diccionario para mandar un formulario en la vista create_tasks.html
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo de la tarea.'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Describe la tarea.'}),
            #No logramos poner el checkbox desde aqui
            #'importante': forms.CheckboxInput(attrs={'class':'form-control'}),
            #Lo que hizo fue poner otra clase
            'importante': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

