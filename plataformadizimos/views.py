from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Dizimos, Membros
# Biblioteca para soma dizimo dentro do mês 
from django.db.models import Sum
from datetime import datetime

@login_required(login_url='/usuarios/login')
def dizimos(request):
    if request.method == "POST":
        membro_id = request.POST.get("membro")
        valor = request.POST.get("valor")

        if not membro_id or not valor:
            messages.error(request, "Preencha todos os campos.")
            return redirect("/dizimos/")

        membro = get_object_or_404(Membros, id=membro_id, pastor=request.user)
        Dizimos.objects.create(membro=membro, valor=valor)

        messages.success(request, "Dízimo registrado com sucesso!")
        return redirect("/dizimos/")
    # Obtém a data atual
    data_atual = datetime.now()
    mes_atual = data_atual.month
    ano_atual = data_atual.year

    # Filtra os dízimos do pastor logado no mês atual
    dizimos = Dizimos.objects.filter(membro__pastor=request.user).order_by("-data_dizimo")

    # Soma dos dízimos no mês atual
    total_dizimos = Dizimos.objects.filter(
        membro__pastor=request.user,
        data_dizimo__month=mes_atual,
        data_dizimo__year=ano_atual
    ).aggregate(Sum('valor'))['valor__sum'] or 0

    membros = Membros.objects.filter(pastor=request.user)

    return render(request, "dizimos.html", {
        "membros": membros,
        "dizimos": dizimos,
        "total_dizimos": total_dizimos,
        "data_atual": data_atual,
    })


#EDITAR DÍZIMOS
@login_required(login_url='/usuarios/login')
def editar_dizimo(request, dizimo_id):
    dizimo = get_object_or_404(Dizimos, id=dizimo_id, membro__pastor=request.user)

    if request.method == "POST":
        membro_id = request.POST.get("membro")
        valor = request.POST.get("valor")

        if not membro_id or not valor:
            messages.error(request, "Preencha todos os campos.")
            return redirect(f"/dizimos/editar/{dizimo_id}/")

        membro = get_object_or_404(Membros, id=membro_id, pastor=request.user)

        dizimo.membro = membro
        dizimo.valor = float(valor)
        dizimo.save()

        messages.success(request, "Dízimo atualizado com sucesso!")
        return redirect("/dizimos/")

    membros = Membros.objects.filter(pastor=request.user)
    return render(request, "editar_dizimo.html", {"dizimo": dizimo, "membros": membros})

#EXCLUIR DÍZIMO

@login_required(login_url='/usuarios/login')
def excluir_dizimo(request, dizimo_id):
    dizimo = get_object_or_404(Dizimos, id=dizimo_id, membro__pastor=request.user)
    
    if request.method == "POST":
        dizimo.delete()
        messages.success(request, "Dízimo excluído com sucesso!")
        return redirect("/dizimos/")
    
    messages.error(request, "Erro ao excluir o dízimo.")
    return redirect("/dizimos/")
