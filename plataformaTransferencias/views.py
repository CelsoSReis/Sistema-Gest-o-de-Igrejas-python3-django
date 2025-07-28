from django.shortcuts import render, redirect, get_object_or_404
from plataformaigreja.models import Membros
from igreja.models import Igreja
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Transferencia
from reportlab.lib.pagesizes import A4
import io
from datetime import datetime
from io import BytesIO

# Gera carta de Transferência

@login_required(login_url='/usuarios/login')
def gerar_carta_transferencia(request, membro_id):
    membro = get_object_or_404(Membros, id=membro_id, pastor=request.user)

    if request.method == "POST":
        data_transferencia = request.POST.get("data_transferencia")
        # Formata a data
        data_formatada = datetime.strptime(data_transferencia, "%Y-%m-%d").strftime("%d/%m/%Y")

        igreja_destino = request.POST.get("igreja_destino")

        # Pega dados da igreja do usuário atual
        try:
            igreja_origem = Igreja.objects.get(pastor=request.user)
        except Igreja.DoesNotExist:
            return HttpResponse("Igreja não cadastrada para este usuário.", status=404)

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)

        # Layout simples da carta
        largura, altura = A4
        p.setFont("Helvetica", 14)

        p.drawString(100, altura - 100, f"Declaração de Transferência de Membro")
        p.setFont("Helvetica", 12)

        corpo = f"""
Declaramos que o membro {membro.nome}, pertencente à {igreja_origem.nome_igreja},
foi transferido(a) em {data_formatada} para a seguinte igreja:

{igreja_destino}

Agradecemos pelo período em que esteve conosco e desejamos bênçãos em sua nova jornada.

Atenciosamente,
{igreja_origem.nome_igreja}
Endereço: {igreja_origem.endereco}
"""

        text_object = p.beginText(50, altura - 140)
        for linha in corpo.splitlines():
            text_object.textLine(linha.strip())
        p.drawText(text_object)

        p.showPage()
        p.save()

        buffer.seek(0)
        return HttpResponse(buffer, content_type='application/pdf')

    return render(request, 'transferencias/modal_transferencia.html', {
        'membro': membro
    })



# Função para realizar transferência de membro / após transferência de membro o mesmo fica inativo no banco
@login_required(login_url='/usuarios/login')
def transferir_membro(request, membro_id):
    membro = get_object_or_404(Membros, id=membro_id)

    if request.method == 'POST':
        membro.ativo = False
        membro.save()

        messages.success(request, f'{membro.nome} foi marcado como transferido (inativo).')
        return redirect('controle_transferidos')

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

