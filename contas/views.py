# contas/views.py
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, logout

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = login(request, form.cleaned_data['user'])
        return redirect('index')  # Redirecionar para a página inicial
    context = {
        'form': form,
    }
    return render(request, 'contas/templates/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirecionar para a página de login
