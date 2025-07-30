from django.urls import path

from cerita6.views import *

urlpatterns = [
    path('', listEvent, name='list-all-event'),
    path('add-event', addEvent, name='add-event'),
    path('<pk>/join', joinEvent, name='join-event'),
    path('<pk>/delete', deleteEvent, name='delete-event'),

    path('todo-list', index, name='todo'),
    path('add_todo', add_todo, name='add_todo'),
    path('todo-list/delete/<id>', delete_todo, name='delete-todo'),

]
