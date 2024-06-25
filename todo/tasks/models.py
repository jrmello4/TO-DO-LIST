from django.db import models
from django.urls import reverse


class todo_list(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    todo_list = models.ForeignKey(todo_list, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return self.title
