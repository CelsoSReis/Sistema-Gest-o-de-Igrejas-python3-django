from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ContaPagar
from datetime import datetime
from django.utils.timezone import now



@login_required(login_url='/usuarios/login')
def contas_pagar(request):
    if request.method == "POST":
        fornecedor = request.POST.get("fornecedor")
        descricao = request.POST.get("descricao")
        valor = request.POST.get("valor")
        data_vencimento = request.POST.get("data_vencimento")
        quantidade_parcelas = request.POST.get("quantidade_parcelas")
        arquivo = request.FILES.get("arquivo")

        if not fornecedor or not descricao or not valor or not data_vencimento or not quantidade_parcelas:
            messages.error(request, "Preencha todos os campos obrigatórios.")
            return redirect("/contas_pagar/")

        ContaPagar.objects.create(
            pastor=request.user,
            fornecedor=fornecedor,
            descricao=descricao,
            valor=valor,
            data_vencimento=data_vencimento,
            quantidade_parcelas=int(quantidade_parcelas),
            arquivo=arquivo
        )

        messages.success(request, "Conta a pagar registrada com sucesso!")
        return redirect("/contas_pagar/")

    contas = ContaPagar.objects.filter(pastor=request.user).order_by("-data_vencimento")

    return render(request, "contas_pagar.html", {"contas": contas})

@login_required(login_url='/usuarios/login')
def contas_vencimento_mes_atual(request):
    # Obtém o mês e ano atual
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Filtra as contas que vencem no mês atual
    contas_vencendo = ContaPagar.objects.filter(
        pastor=request.user,
        data_vencimento__month=mes_atual,
        data_vencimento__year=ano_atual
    ).order_by("data_vencimento")

    return render(request, "contas_vencimento_mes.html", {"contas_vencendo": contas_vencendo})

@login_required(login_url='/usuarios/login')
def contas_vencidas(request):
    # Obtém a data atual
    data_atual = now().date()

    # Filtra as contas vencidas (vencimento antes de hoje)
    contas = ContaPagar.objects.filter(pastor=request.user, data_vencimento__lt=data_atual).order_by("data_vencimento")

    return render(request, "contas_vencidas.html", {"contas": contas})