from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Oferta
from datetime import datetime
from django.db.models import Sum


# Registrar ofertas
@login_required(login_url='/usuarios/login')
def ofertas(request):
    if request.method == "POST":
        data_oferta = request.POST.get("data_oferta")
        valor = request.POST.get("valor")
        descricao = request.POST.get("descricao")

        if not data_oferta or not valor or not descricao:
            messages.error(request, "Preencha todos os campos.")
            return redirect("/ofertas/")

        Oferta.objects.create(
            pastor=request.user,
            data_oferta=data_oferta,
            valor=valor,
            descricao=descricao
        )

        messages.success(request, "Oferta registrada com sucesso!")
        return redirect("/ofertas/")

    # Obtém a data atual, mês e ano
    data_atual = datetime.now().strftime("%d/%m/%Y")
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year


    # Filtra as ofertas do mês atual
    ofertas = Oferta.objects.filter(
        pastor=request.user,
        data_oferta__month=mes_atual,
        data_oferta__year=ano_atual
    )

    # Soma total das ofertas do mês
    total_ofertas = ofertas.aggregate(total=Sum('valor'))['total'] or 0

    return render(request, "ofertas.html", {
        "ofertas": ofertas,
        "total_ofertas": total_ofertas,
        "data_atual": data_atual
    })



# Excluir ofertas

@login_required(login_url='/usuarios/login')
def excluir_oferta(request, oferta_id):
    oferta = get_object_or_404(Oferta, id=oferta_id, pastor=request.user)

    if request.method == "POST":
        oferta.delete()
        messages.success(request, "Oferta excluída com sucesso!")
        return redirect("/ofertas/")

    messages.error(request, "Erro ao excluir a oferta.")
    return redirect("/ofertas/")

# Editar Oferta
@login_required(login_url='/usuarios/login')
def editar_oferta(request, oferta_id):
    oferta = get_object_or_404(Oferta, id=oferta_id, pastor=request.user)

    if request.method == "POST":
        descricao = request.POST.get("descricao")
        valor = request.POST.get("valor")
        data_oferta = request.POST.get("data_oferta")

        if not descricao or not valor or not data_oferta:
            messages.error(request, "Preencha todos os campos.")
            return redirect(f"/ofertas/editar/{oferta_id}/")

        oferta.descricao = descricao
        oferta.valor = float(valor)
        oferta.data_oferta = data_oferta
        oferta.save()

        messages.success(request, "Oferta atualizada com sucesso!")
        return redirect("/ofertas/")

    return render(request, "editar_oferta.html", {"oferta": oferta})

# Somar oferta
@login_required(login_url='/usuarios/login')
def listar_ofertas(request):
    # Obtém a data atual, mês e ano
    data_atual = datetime.now().strftime("%d/%m/%Y")
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Filtra as ofertas do mês atual
    ofertas = Oferta.objects.filter(
        pastor=request.user,
        data_oferta__month=mes_atual,
        data_oferta__year=ano_atual
    )

    # Soma total das ofertas do mês
    total_ofertas = ofertas.aggregate(total=Sum('valor'))['total'] or 0

    return render(request, 'ofertas.html', {
        'ofertas': ofertas,
        'total_ofertas': total_ofertas,
        'data_atual': data_atual
    })