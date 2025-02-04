from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .utils import password_is_valid, email_html
import os
from django.conf import settings
from .models import Ativacao
from hashlib import sha256

# Create your views here.
    
# Funcionalidades de cadastro.
## Função "cadastro", Realiza cadastro de usuários para o sistema
def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        ## Validação senha
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/usuarios/cadastro')
        
        try:
            # Username deve ser único!
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
                is_active=False,
            )
            #cria token para ativação
            token = sha256(f"{username}{email}".encode()).hexdigest()
            ativacao = Ativacao(token=token, user=user)
            ativacao.save()

            path_template = os.path.join(settings.BASE_DIR, 'usuarios/templates/emails/cadastro_confirmado.html')
            email_html(path_template, 'Cadastro confirmado', [email,], username=username, link_ativacao=f"127.0.0.1:8000/usuarios/ativar_conta/{token}")
            messages.add_message(request, constants.SUCCESS, 'Usuário Salvo com sucesso!')
        except:
            messages.add_message(request, constants.ERROR, 'Erro, contate o administrador do sistema!')
            return redirect('/usuarios/cadastro')
        return redirect('/usuarios/login')
    
# Funcionalidade para logar
def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/plataformaigreja/dashboard_igreja')
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
						# Acontecerá um erro ao redirecionar por enquanto
            return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
            return redirect('/usuarios/login')
# Função para deslogar
## LOGOUT
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/usuarios/login')

#ativar conta
def ativar_conta(request, token):
    token = get_object_or_404(Ativacao, token=token)
    if token.ativo:
        messages.add_message(request, constants.WARNING, 'Essa token já foi usado')
        return redirect('/usuarios/login')
    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.ativo = True
    token.save()

    messages.add_message(request, constants.SUCCESS, 'Conta ativa com sucesso')
    return redirect('/usuarios/login')