from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Todo

from .serializers import TodoSerializer


# Create && Get all todo
@api_view(['GET', 'POST'])
def todo_list_create(request):

    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message": "Todo created successfully"
            }
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get & update & delete Single todo
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    todo = get_object_or_404(Todo, id=pk)

    #? get todo by id
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    #? update todo by id
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message": "Todo updated successfully"
                }
            return Response(message, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #? delete todo by id    
    elif request.method == 'DELETE':
        todo.delete()
        message = {
            "message": "Todo deleted successfully"
            }
        return Response(message, status=status.HTTP_200_OK)
