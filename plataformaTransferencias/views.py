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
"""
@login_required(login_url='/usuarios/login')
def transferir_membro(request, membro_id):
    membro = get_object_or_404(Membros, id=membro_id)
    
    # Pega a igreja que o usuário logado é o pastor
    igreja_origem = get_object_or_404(Igreja, pastor=request.user)

    if request.method == "POST":
        nome_igreja_destino = request.POST.get('igreja_destino')

        # Cria uma nova igreja no banco de dados ou busca se já existir
        igreja_destino, created = Igreja.objects.get_or_create(nome_igreja=nome_igreja_destino)

        Transferencia.objects.create(
            membro=membro,
            igreja_origem=igreja_origem,
            igreja_destino=igreja_destino,
            data_transferencia=timezone.now()
        )

        membro.delete()  # Remove o membro após confirmar a transferência
        messages.success(request, 'Membro transferido com sucesso!')
        return redirect('listar_transferencias')

    return render(request, 'transferencias/transferir_membro.html', {
        'membro': membro,
        'igreja_origem': igreja_origem,
    })
"""
# Função para realizar transferência de membro / após transferência de membro o mesmo fica inativo no banco
@login_required(login_url='/usuarios/login')
def transferir_membro(request, membro_id):
    membro = get_object_or_404(Membros, id=membro_id)

    if request.method == 'POST':
        membro.ativo = False
        membro.save()

        messages.success(request, f'{membro.nome} foi marcado como transferido (inativo).')
        return redirect('controle_transf')

    return redirect('controle_transf')
