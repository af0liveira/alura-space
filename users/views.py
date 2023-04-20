from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from users.forms import LoginForm, SignupForm

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form['login_name'].value()
            password = form['password'].value()

            user = auth.authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                return redirect('login')

    return render(request, 'users/login.html', dict(form=form))

def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():

            if form['password'].value() != form['password_confirmation'].value():
                return redirect('signup')

            username = form['login_name'].value()
            password = form['password'].value()
            email = form['email'].value()

            if User.objects.filter(username=username).exists():
                return redirect('signup')

            new_user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )

            new_user.save()
            return redirect('login')
    
    return render(request, 'users/signup.html', dict(form=form))
