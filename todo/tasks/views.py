from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task, TodoList
from django.contrib.auth.mixins import LoginRequiredMixin

class TodoView(LoginRequiredMixin, ListView):
    model = TodoList
    template_name = 'index.html'

class ItemListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "todo_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        list_id = self.kwargs.get("list_id")
        return Task.objects.filter(todo_list_id=list_id, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_id = self.kwargs.get("list_id")
        context["todo_list"] = TodoList.objects.get(id=list_id)
        return context

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed', 'todo_list']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list', kwargs={'list_id': self.object.todo_list.id})

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed']

    def get_success_url(self):
        return reverse_lazy('list', kwargs={'list_id': self.object.todo_list.id})

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('list', kwargs={'list_id': self.object.todo_list.id})
