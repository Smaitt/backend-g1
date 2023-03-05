from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoList, Todo
from .serializers import TodoListSerializer, TodoSerializer

@api_view(['GET'])
def get_todo_lists(request):
    todo_lists = TodoList.objects.all()
    serializer = TodoListSerializer(todo_lists, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_todo_list(request):
    serializer = TodoListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_todo_list(request, pk):
    try:
        todo_list = TodoList.objects.get(pk=pk)
        serializer = TodoListSerializer(todo_list)
        return Response(serializer.data)
    except TodoList.DoesNotExist:
        return Response(status=404)

@api_view(['PUT'])
def update_todo_list(request, pk):
    try:
        todo_list = TodoList.objects.get(pk=pk)
        serializer = TodoListSerializer(todo_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except TodoList.DoesNotExist:
        return Response(status=404)

@api_view(['DELETE'])
def delete_todo_list(request, pk):
    try:
        todo_list = TodoList.objects.get(pk=pk)
        todo_list.delete()
        return Response(status=204)
    except TodoList.DoesNotExist:
        return Response(status=404)

@api_view(['GET'])
def get_todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    except Todo.DoesNotExist:
        return Response(status=404)

@api_view(['PUT'])
def update_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    except Todo.DoesNotExist:
        return Response(status=404)