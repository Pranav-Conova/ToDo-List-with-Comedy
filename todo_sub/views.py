from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .utils import generate_comedy_text

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.comedy_text = generate_comedy_text(task.description)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todoapp/add_task.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from .models import Task

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.is_done = not task.is_done
        task.save()
    return redirect('task_list')  # or whatever your main page's URL name is
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoapp/edit_task.html', {'form': form})
  
def delete_task(request, task_id):
  task = get_object_or_404(Task, id=task_id)
  if request.method == 'POST':
      task.delete()
  return redirect('task_list')
