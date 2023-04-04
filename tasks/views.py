from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
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
            except IntegrityError:
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