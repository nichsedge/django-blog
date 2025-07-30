from django.urls import path

from cerita7.views import *

urlpatterns = [
    path('', story7, name='story7'),
]
