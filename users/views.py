from django.shortcuts import render

from users.forms import LoginForm

def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', dict(form=form))

def signup(request):
    return render(request, 'users/signup.html')
