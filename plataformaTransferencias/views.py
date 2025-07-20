from django.shortcuts import render, redirect, get_object_or_404
from .models import Transferencia
from plataformaigreja.models import Membros
from igreja.models import Igreja
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required(login_url='/usuarios/login')
def listar_transferencias(request):
    transferencias = Transferencia.objects.all()
    return render(request, 'transferencias/listar_transferencias.html', {'transferencias': transferencias})

# Função para realizar transferência de membro / após transferência de membro o mesmo fica inativo no banco
@login_required(login_url='/usuarios/login')
def transferir_membro(request, membro_id):
    membro = get_object_or_404(Membros, id=membro_id)

    if request.method == 'POST':
        membro.ativo = False
        membro.save()

        messages.success(request, f'{membro.nome} foi marcado como transferido (inativo).')
        return redirect('/index/membros/')

    return redirect('/index/membros/')

#Controle de membros transferidos
@login_required(login_url='/usuarios/login')
def controle_transferidos(request):
    membros = Membros.objects.filter(pastor=request.user, ativo=False)
    return render(request, 'transferencias/controle_transferidos.html', {'membros': membros})

# Reativar membro transferido
@login_required(login_url='/usuarios/login')
def reativar_membro(request, membro_id):
    membro = get_object_or_404(Membros, id=membro_id, pastor=request.user)

    if not membro.ativo:
        membro.ativo = True
        membro.save()
        messages.success(request, f'{membro.nome} foi reativado com sucesso.')

    return redirect('controle_transferidos')