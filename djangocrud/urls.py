"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='Tareas'), #vista de tareas
    path('tasks_completed', views.tasks_completed, name='tasks_completed'), #vista de tareas completadas
    path('tasks/create/', views.crear_task, name='crear_tareas'), #vista crear tareas
    path('tasks/<int:tarea_id>/', views.task_detalles, name='detalle_tareas'), #le agregamos un dato dinamico aqui y en views.py
    path('tasks/<int:tarea_id>/complete', views.complete_task, name='complete_task'), #agregamos la seccion de copmletado
    path('tasks/<int:tarea_id>/delete', views.delete_task, name='delete_task'), #agregamos la opcion de eliminar la tarea
    path('logout/', views.closeSesion, name='Cerrar Sesion'),
    path('signin/', views.autenticar, name='Signin')

]
