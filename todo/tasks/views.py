from django.shortcuts import render
from django.views.generic import ListView
from .models import tasks, todo_list


class TodoView(ListView):
    model = todo_list
    template_name = 'index.html'


class ItemListView(ListView):
    model = todo_list
    template_name = "todo_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        list_id = self.kwargs.get("list_id")
        return tasks.objects.filter(todo_list_id=list_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_id = self.kwargs.get("list_id")
        context["todo_list"] = todo_list.objects.get(id=list_id)
        return context
