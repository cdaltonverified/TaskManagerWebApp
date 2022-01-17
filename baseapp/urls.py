from django.urls import path
from .views import ListAllTasks, CreateNewTask, UpdateTask, DeleteTask
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('', ListAllTasks.as_view(), name='tasks'),
    path('task-new/', CreateNewTask.as_view(), name='task-new'),
    path('task-edit/<int:pk>/', UpdateTask.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]