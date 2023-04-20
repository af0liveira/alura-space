from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

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
                messages.success(request, f"Logado como <bold>{username}</bold>.")
                return redirect('index')
            else:
                messages.error(request, f"Falha ao efetuar login!")
                return redirect('login')

    return render(request, 'users/login.html', dict(form=form))

def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():

            if form['password'].value() != form['password_confirmation'].value():
                messages.error(request, "Senhas não coincidem!")
                return redirect('signup')

            username = form['login_name'].value()
            password = form['password'].value()
            email = form['email'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, f"Usuário <b>{username}</b> já existe!")
                return redirect('signup')

            new_user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )

            new_user.save()
            messages.success(request, f"Usuário <b>{username}</b> cadastrado com sucesso!")
            return redirect('login')
    
    return render(request, 'users/signup.html', dict(form=form))

def logout(request):
    if request.user.is_authenticated:
        username = request.user.username
        auth.logout(request)
        messages.success(request, f"Logout de {username} efetuado com sucesso!")
    return redirect('login')
