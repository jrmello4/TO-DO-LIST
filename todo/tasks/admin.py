from django.contrib import admin
from .models import tasks, todo_list


admin.site.register(tasks)
admin.site.register(todo_list)
