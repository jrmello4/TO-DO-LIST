from django.contrib import admin
from .models import Task, TodoList


admin.site.register(Task)
admin.site.register(TodoList)
