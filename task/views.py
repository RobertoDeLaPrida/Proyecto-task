from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.views import View

# def task_list(request):

#     tasks = Task.objects.all()

#     if request.method == 'POST':
#         form=TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#     else:
#         form= TaskForm()
#     return render(request, 'task/task_list.html', {'tasks': tasks,'form':form})


class TaskList(View):

#    tasks = Task.objects.all()
    nombre_template = 'task/task_list.html'
    
    def get(self,request):
        form=TaskForm()
        return render(request, self.nombre_template, {'tasks': Task.objects.all(),'form':form})
    
    def post(self,request):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, self.nombre_template, {'tasks': Task.objects.all(),'form':form})