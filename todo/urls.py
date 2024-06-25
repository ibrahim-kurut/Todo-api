from django.urls import path

from .views import (
    todo_list_create,
    todo_detail,

    # from concrete view
    Todo_List_Create,
    Todo_Detail
)

# /api/todos/

urlpatterns = [
    # # /api/todos/
    # path('todos/', todo_list_create),

    # # /api/todos/:id/
    # path('todo/<int:pk>/', todo_detail),


    path('todos/', Todo_List_Create.as_view()),
    path('todo/<int:pk>/', Todo_Detail.as_view()),

]