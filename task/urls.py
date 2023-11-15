from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate , TaskEdit

urlpatterns = [

path('', TaskList.as_view(), name='task_list'),
path('task/<int:pk>',TaskDetail.as_view(), name='task_detail'),
path('create',TaskCreate.as_view(),name='task_create'),
path('edit/<int:pk>',TaskEdit.as_view(),name="task_edit")

]