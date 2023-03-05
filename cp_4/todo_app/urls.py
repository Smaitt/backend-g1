from django.urls import path
from rest_framework.decorators import api_view
from . import views

urlpatterns = [
    path('api/todo-lists', api_view(views.todo_lists), name='todo_lists'),
    path('api/todo-lists/<int:id>', api_view(views.todo_list_detail), name='todo_list_detail'),
    path('api/todo-lists/<int:id>/todos', api_view(views.todos_in_list), name='todos_in_list'),
    path('api/todos', api_view(views.todos), name='todos'),
    path('api/todos/<int:id>', api_view(views.todo_detail), name='todo_detail'),
    path('todo-lists', views.todo_lists_html, name='todo_lists_html'),
    path('todo-lists/<int:id>', views.todo_list_detail_html, name='todo_list_detail_html'),
]