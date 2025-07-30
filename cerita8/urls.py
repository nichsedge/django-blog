from django.urls import path

from cerita8.views import *

urlpatterns = [
    path('list', book_list, name='book_list'),
    path('list/<book_name>', get_books, name='ajax'),

]
