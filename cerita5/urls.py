from django.urls import path

from cerita5.views import *

urlpatterns = [
    path('', detail_all_course, name='list-all'),
    path('tambah', add_course, name='add_course'),
    path('delete', remove_course, name='remove_course'),
    path('<code>', detail_course, name='detail-course'),
]
