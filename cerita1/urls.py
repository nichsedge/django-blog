from django.urls import path

from cerita1.views import home, about

urlpatterns = [
    # story 1
    path('', home, name='home'),

    # story 4
    path('about', about, name='about'),
]
