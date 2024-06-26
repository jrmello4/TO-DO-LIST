from django.urls import path
from . import views

urlpatterns = [
    path("", views.TodoView.as_view(), name="index"),
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    path("list/<int:list_id>/create/", views.CreateTask.as_view(), name="task-create"),
    path("list/<int:list_id>/update/<int:pk>/", views.UpdateTask.as_view(), name="task-update"),
]
