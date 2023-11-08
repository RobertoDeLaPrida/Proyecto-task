from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm

def task_list(request):

    tasks = Task.objects.all()

    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form= TaskForm()
    return render(request, 'task/task_list.html', {'tasks': tasks,'form':form})