from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from .models import Dizimos, Membros



# Create your views here.
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