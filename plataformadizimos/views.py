from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Dizimos, Membros
from django.http import JsonResponse


# Registrar dízimo.
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

    membros = Membros.objects.filter(pastor=request.user)
    dizimos = Dizimos.objects.filter(membro__pastor=request.user).order_by("-data_dizimo")

    return render(request, "dizimos.html", {"membros": membros, "dizimos": dizimos})

@login_required(login_url='/usuarios/login')
def editar_dizimo(request, id):
    dizimo = get_object_or_404(Dizimos, id=id)
    if request.method == 'POST':
        # Atualiza os campos do dízimo com os dados enviados
        dizimo.nome = request.POST.get('nome')
        dizimo.valor = request.POST.get('valor')
        dizimo.data = request.POST.get('data')
        dizimo.save()
        return JsonResponse({'status': 'success', 'message': 'Dízimo atualizado com sucesso!'})
    else:
        # Retorna os dados do dízimo para preencher o modal
        return JsonResponse({
            'id': dizimo.id,
            'nome': dizimo.nome,
            'valor': str(dizimo.valor),  # DecimalField precisa ser convertido para string
            'data': dizimo.data.strftime('%Y-%m-%d')  # Formata a data para o input type="date"
        })