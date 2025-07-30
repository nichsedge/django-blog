from django.shortcuts import render, redirect, HttpResponseRedirect

from .forms import formEvent, Todo_Form
from .models import Event, Member, Todo


# Create your views here.
def listEvent(request):
    context = {}
    event = Event.objects.all()

    context['events'] = event

    return render(request, "list-AllEvent.html", context)


def addEvent(request):
    if request.method == 'POST':
        form = formEvent(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add-event')

    else:
        form = formEvent(request.POST)

    return render(request, "add-Event.html", {'form': form})


def joinEvent(request, pk):
    context = {}
    event = Event.objects.get(pk=pk)
    context['pk'] = pk

    if request.method == 'POST':
        name = request.POST['name']
        if name.isspace() or name == "":
            return redirect('join-event', pk)

        try:
            member = Member.objects.get(name=name)
        except:
            member = Member.objects.create(name=name)

        if member not in event.member.all():
            event.member.add(member)

    return render(request, "join-event.html", context)

def deleteEvent(request, pk):
    event = Event.objects.get(pk=pk)
    event.delete()

    return redirect('list-all-event')

## 
response = {}


def index(request):
    response['author'] = "Al"
    todo = Todo.objects.all()
    response['todo'] = todo
    html = 'lab_5/lab_5.html'
    response['todo_form'] = Todo_Form
    return render(request, html, response)


def add_todo(request):
    form = Todo_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        response['title'] = request.POST['title']
        response['description'] = request.POST['description']
        todo = Todo(title=response['title'], description=response['description'])
        todo.save()
        return HttpResponseRedirect('todo-list')
    else:
        return HttpResponseRedirect('todo-list')

def delete_todo(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('todo')
