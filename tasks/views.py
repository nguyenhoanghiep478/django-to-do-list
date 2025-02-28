from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'tasks/tasks.html', {'tasks': tasks, 'form': form})

def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')


def toggle_task(request,id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
