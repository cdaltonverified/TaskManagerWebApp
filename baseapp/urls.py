from django.urls import path
from .views import ListAllTasks, CreateNewTask, UpdateTask, DeleteTask

urlpatterns = [
    path('', ListAllTasks.as_view(), name='tasks'),
    path('task-new/', CreateNewTask.as_view(), name='task-new'),
    path('task-edit/<int:pk>/', UpdateTask.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),
]