from django.urls import path
from django.contrib.auth import views as auth_views
from .views import TodoView, ItemListView, CreateTask, UpdateTask, DeleteTask
from . import views


urlpatterns = [
    path('', TodoView.as_view(), name='index'),
    path('list/<int:list_id>/', ItemListView.as_view(), name='list'),
    path('task/create/<int:list_id>/', CreateTask.as_view(), name='task_create'),
    path('task/update/<int:pk>/', UpdateTask.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', DeleteTask.as_view(), name='task_delete'),
    path('task/login/', auth_views.LoginView.as_view(), name='login'),
    path('task/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('task/register/', views.register, name='register'),
    path('task/guest_login/', views.guest_login, name='guest_login'),
]
