from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'cerita9/index.html')


def signup(request):
    """
    if request.user.is_authenticated:
        user_logout(request)
        return redirect('register')
    """
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save(commit=False)
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    context['form'] = form

    return render(request, 'cerita9/registrasi.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'cerita9/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')
