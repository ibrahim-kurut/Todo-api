from django.urls import path

from .views import (
    todo_list_create,
    todo_detail,
)

# /api/todos/

urlpatterns = [
    # /api/todos/
    path('todos/', todo_list_create),
    
    # /api/todos/:id/
    path('todo/<int:pk>/', todo_detail),
]