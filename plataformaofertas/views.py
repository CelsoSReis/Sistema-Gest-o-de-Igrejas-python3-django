from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Oferta
from datetime import datetime

@login_required(login_url='/usuarios/login')
def ofertas(request):
    if request.method == "POST":
        data_oferta = request.POST.get("data_oferta")
        valor = request.POST.get("valor")
        descricao = request.POST.get("descricao")  # Atualizado para "descrição"

        if not data_oferta or not valor or not descricao:
            messages.error(request, "Preencha todos os campos.")
            return redirect("/ofertas/")

        Oferta.objects.create(
            pastor=request.user,
            data_oferta=data_oferta,
            valor=valor,
            descricao=descricao  # Atualizado para "descrição"
        )

        messages.success(request, "Oferta registrada com sucesso!")
        return redirect("/ofertas/")

    ofertas = Oferta.objects.filter(pastor=request.user).order_by("-data_oferta")

    return render(request, "ofertas.html", {"ofertas": ofertas})
