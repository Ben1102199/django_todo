from django.db.models import fields
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.
class tasklist(ListView):
    model = Task
    context_object_name ='tasks'

class Taskdetail(DetailView):
    model =Task
    context_object_name ='task'
    template_name ='base/task.html'

class TaskCreateview(CreateView):
    model=Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class Task_Update(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')