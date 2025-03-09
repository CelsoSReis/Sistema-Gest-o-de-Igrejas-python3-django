from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Documento

# Upload de documentos
@login_required(login_url='/usuarios/login')
def upload_documento(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        arquivo = request.FILES.get('arquivo')
        if titulo and arquivo:
            Documento.objects.create(pastor=request.user, titulo=titulo, arquivo=arquivo)
            messages.success(request, 'Documento enviado com sucesso!')
            return redirect('listar_documentos')
        else:
            messages.error(request, 'Por favor, preencha todos os campos!')
    return render(request, 'upload_documento.html')

# Listagem de documentos
@login_required(login_url='/usuarios/login')
def listar_documentos(request):
    documentos = Documento.objects.filter(pastor=request.user)
    return render(request, 'listar_documentos.html', {'documentos': documentos})

# Exclusão de documentos
@login_required(login_url='/usuarios/login')
def excluir_documento(request, id):
    documento = get_object_or_404(Documento, id=id, pastor=request.user)
    if request.method == 'POST':
        documento.delete()
        messages.success(request, 'Documento excluído com sucesso!')
        return redirect('listar_documentos')
    return render(request, 'confirmar_exclusao.html', {'documento': documento})
