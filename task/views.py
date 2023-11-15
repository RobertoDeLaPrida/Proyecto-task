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
    
class TaskDetail(View):
    nombre_template = 'task/task_detail.html'
    def get(self,request,pk):  
        task = Task.objects.get(id=pk)
        return render(request, self.nombre_template, {'task': task})
    
class TaskCreate(View):
    nombre_template = 'task/task_create.html'
    def get(self,request):
        form=TaskForm()
        return render(request, self.nombre_template, {'tasks': Task.objects.all(),'form':form})
    
    def post(self,request):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, self.nombre_template, {'tasks': Task.objects.all(),'form':form})

class TaskEdit(View):
    nombre_template = 'task/task_edit.html'
    def get(self,request,pk):
        task=Task.objects.get(id=pk)
        form=TaskForm(instance=task)
        return render(request, self.nombre_template, {'task': task,'form':form})
    
    def post(self,request,pk):
        task=Task.objects.get(id=pk)
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, self.nombre_template, {'task': task,'form':form})