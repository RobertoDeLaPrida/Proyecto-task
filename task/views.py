from django.shortcuts import render

from django.utils import timezone

from .models import Task

def task_list(request):

    tasks = Task.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'task/task_list.html', {'tasks': tasks})