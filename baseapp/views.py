from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task


class ListAllTasks(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'baseapp/all_tasks.html'


class CreateNewTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'
    