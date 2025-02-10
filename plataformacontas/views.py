from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ContaPagar

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
