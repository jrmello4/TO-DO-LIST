from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Task, TodoList

class TodoView(ListView):
    model = TodoList
    template_name = 'index.html'

class ItemListView(ListView):
    model = Task
    template_name = "todo_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        list_id = self.kwargs.get("list_id")
        return Task.objects.filter(todo_list_id=list_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_id = self.kwargs.get("list_id")
        context["todo_list"] = TodoList.objects.get(id=list_id)
        return context

class CreateTask(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed', 'todo_list']

    def get_success_url(self):
        return reverse_lazy('list', kwargs={'list_id': self.object.todo_list.id})

class UpdateTask(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed']

    def get_success_url(self):
        return reverse_lazy('list', kwargs={'list_id': self.object.todo_list.id})

    