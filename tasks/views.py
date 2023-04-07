from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm  #importamos el modelo de forms para tareas
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
    })
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                #Usuraio registrado
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('Tareas') #nombre de la url es decir el name  path('tasks/', views.tasks, name='Tareas')
                #Se le pone el return para indicar que ahi tiene que terminar.
            except IntegrityError: #para traer un dato en especifico de la base de datos y agregar un error.
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                 })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Contraseña no existen.'
                 })
    
def tasks(request):
    return render(request, 'tasks.html')

def crear_task(request):       #Aqui esta donde va el formulario crear tareas
    if request.method == 'GET':
        return render(request, 'create_task.html',{
            'form': TaskForm #aqui esta la funcion de forms.py
        })
    else:
        print(request.POST)
        return render(request, 'create_task.html',{
            'form': TaskForm #aqui esta la funcion de forms.py
        })

def closeSesion(request):
    logout(request)
    return redirect('home')

def autenticar(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None: #Si el usuario no existe
                return render(request, 'signin.html',{
                    'form': AuthenticationForm,
                    'error': 'Usuario o contraseña incorrecta'
                })
        else: #si SI existe lo reenvia a TASKS
            login(request, user)
            return redirect('Tareas')   
""" Esto ya no es necesario
    return render(request, 'signin.html', {
        'form': AuthenticationForm
    })
"""