from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm  #importamos el modelo de forms para tareas
from .models import Task #importamos el modelo de tareas para consultarlas y listarlas.

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
    
def tasks(request): #aqui se listan las tareas para hacer una consulta.
    tasks = Task.objects.filter(user = request.user, Fcompletado__isnull = True) #para ver la consulta de tareas solo del usuario logeado
    #tasks = Task.objects.all() #devuelve todas las tareas de la base de datos.
    return render(request, 'tasks.html', {'tasks':tasks})

def crear_task(request):       #Aqui esta donde va el formulario crear tareas
    if request.method == 'GET':
        return render(request, 'create_task.html',{
            'form': TaskForm #aqui esta la funcion de forms.py
        })
    else:
        try:
            #print(request.POST)  # locomentamos porque queremos ver como guardar el dato en forms
            form = TaskForm(request.POST)
            nueva_tarea = form.save(commit=False) #se pone asi porque solo queremos los datos del formulario.
            nueva_tarea.user = request.user #para que la tarea sea enlazada con la id del usuario en las cookies
            nueva_tarea.save() #ahora si la guardamos.
            return redirect('Tareas') #y que me mande a la pagina de tareas.
            #print(nueva_tarea)
            #print(form) #y lo mandamos a consola pa verlo
            #return render(request, 'create_task.html',{
            #    'form': TaskForm #aqui esta la funcion de forms.py
            #})
        except:
            return render(request, 'create_task.html', {
                'form':TaskForm,
                'error': 'Porfavor verifique sus datos e intente de nuevo.'
            })

def task_detalles(request, tarea_id):   #agregamos el dato dinamico que pusimos en urls
    tarea = get_object_or_404(Task, pk=tarea_id) #pasamos el modelo de consulta
    #tarea = Task.objects.get(pk=tarea_id)
    # print(tarea_id)  #lo imprimimos
    return render(request, 'tasks_detalles.html', {'task': tarea})



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
    #Esto ya no es necesario
    #return render(request, 'signin.html', {
    #    'form': AuthenticationForm
    #})


