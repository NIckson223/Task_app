from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tasks', views.task, name='tasks'),
    path('create', views.create_task, name="create"),
    path('delete_tasks', views.delete_tasks, name="delete_tasks")

]
