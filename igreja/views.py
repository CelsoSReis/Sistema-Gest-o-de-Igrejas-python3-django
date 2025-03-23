from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Igreja

@login_required(login_url='/usuarios/login')
def cadastrar_igreja(request):
    if hasattr(request.user, "igreja"):
        messages.warning(request, "Você já cadastrou uma igreja!")
        return redirect("editar_igreja")

    if request.method == "POST":
        nome = request.POST.get("nome")
        endereco = request.POST.get("endereco")
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")
        logo = request.FILES.get("logo")
        fundo_carteirinha = request.FILES.get("fundo_carteirinha")

        igreja = Igreja(
            pastor=request.user,
            nome=nome,
            endereco=endereco,
            telefone=telefone,
            email=email,
            logo=logo,
            fundo_carteirinha=fundo_carteirinha,
        )
        igreja.save()
        messages.success(request, "Igreja cadastrada com sucesso!")
        return redirect("igreja_cadastro")

    return render(request, "cadastrar_igreja.html")
