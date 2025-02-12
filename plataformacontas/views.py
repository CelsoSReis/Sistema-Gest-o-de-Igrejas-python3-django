from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ContaPagar
from datetime import datetime
from django.utils.timezone import now
from django.db.models import Sum


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

    # Obtém o mês e ano atuais
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Filtra as contas do mês atual
    contas = ContaPagar.objects.filter(
        pastor=request.user,
        data_vencimento__month=mes_atual,
        data_vencimento__year=ano_atual
    )

    # Calcula o total das contas do mês atual
    total_contas_mes = contas.aggregate(total=Sum('valor'))['total'] or 0

    

    return render(request, "contas_pagar.html", {"contas": contas, "total_contas_mes": total_contas_mes})

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

    # Obtém a data atual
    data_atual = datetime.now().date()

    # Filtra as contas vencidas
    contas_vencidas = ContaPagar.objects.filter(pastor=request.user, data_vencimento__lt=data_atual)

    # Soma total das contas vencidas
    total_contas_vencidas = contas_vencidas.aggregate(total=Sum('valor'))['total'] or 0


    return render(request, "contas_vencidas.html", {"contas": contas, "total_contas_vencidas": total_contas_vencidas})

@login_required(login_url='/usuarios/login')
def excluir_conta(request, conta_id):
    conta = get_object_or_404(ContaPagar, id=conta_id, pastor=request.user)

    if request.method == "POST":
        conta.delete()
        messages.success(request, "Conta excluída com sucesso!")
        return redirect("/contas_pagar/")

    messages.error(request, "Erro ao excluir a conta.")
    return redirect("/contas_pagar/")

@login_required(login_url='/usuarios/login')
def todas_contas(request):
    # Obtém todas as contas do usuário ordenadas por data de criação (mais recente primeiro)
    contas = ContaPagar.objects.filter(pastor=request.user).order_by("-data_criacao")

    # Calcula o total geral de todas as contas
    total_geral = contas.aggregate(Sum('valor'))['valor__sum'] or 0

    return render(request, "todas_contas.html", {
        "contas": contas,
        "total_geral": total_geral
    })
