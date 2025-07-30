import datetime

from django.shortcuts import render


# Create your views here.
def home(request):
    context = {'today': datetime.datetime.now()}

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')
