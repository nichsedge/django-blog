from django.urls import path

from cerita9.views import *

urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', index, name='index'),
]
