from django.shortcuts import render
from django.http import JsonResponse

from crud.models import Todo
from django.template.loader import render_to_string
from django.http import HttpResponse


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}

    print(todos)
    return render(request, "index.html", context)


def delete(request):
    return render(request, "index.html")


def add_todo(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Todo.objects.create(content=content)
        todos = Todo.objects.all()
        return render(request, 'todo_list_items.html', {'todos': todos})
    else:
        return JsonResponse({'success': False, 'error': 'POST method expected'})