from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'main/home/index.html')


def delete_tasks(request):
    Task.objects.all().delete()
    return render(request, 'main/tasks/index.html')


def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = "Incorect form"
    form = TaskForm()
    content = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create/index.html', content)


def task(request):
    tasks = Task.objects.order_by('date')
    return render(request, 'main/tasks/index.html', {'title': 'Home page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about/index.html')