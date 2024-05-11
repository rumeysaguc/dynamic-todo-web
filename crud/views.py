from django.shortcuts import render
from django.http import JsonResponse

from crud.models import Todo
from django.template.loader import render_to_string
from django.http import HttpResponse
import json

from crud.serializers import TodoListSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response


# Main Page render function
def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    print(todos)
    return render(request, "index.html", context)


# Delete function
@csrf_exempt
def delete(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


# TodoList Api View you can access all todolist data.
class TodoListAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)


# Task done function
@csrf_exempt
def toggle_completion(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.is_completed = not todo.is_completed
        todo.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


# Add Task function.
@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content')
        if content:
            todo = Todo.objects.create(content=content)
            return JsonResponse({'success': True, 'todo_id': todo.id, 'content': todo.content})
    return JsonResponse({'success': False})
