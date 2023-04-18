from django.shortcuts import render

from users.forms import LoginForm, SignupForm

def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', dict(form=form))

def signup(request):
    form = SignupForm()
    return render(request, 'users/signup.html', dict(form=form))
