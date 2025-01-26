from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from .models import Membros

@login_required(login_url='/usuarios/login')
def membros(request):
    if request.method == "GET":
        #busca membros do pastor logado
        membros = Membros.objects.filter(pastor=request.user)
        #{'membros': membros} dicionário para atribuir a chave 'membros' os dados do banco de dados
        return render(request, 'membros.html', {'membros': membros})

    elif request.method == "POST":
        # Obtém os dados do formulário
        nome = request.POST.get('nome', '').strip()
        sexo = request.POST.get('sexo', '').strip()
        email = request.POST.get('email', '').strip()
        telefone = request.POST.get('telefone', '').strip()
        cpf = request.POST.get('cpf', '').strip()
        endereco = request.POST.get('endereco', '').strip()
        foto = request.FILES.get('foto')  # Obtém arquivo via request.FILES
        data_batismo = request.POST.get('data_batismo', '').strip()
        data_nascimento = request.POST.get('data_nascimento', '').strip()
        cargo = request.POST.get('cargo', '').strip()

        # Valida campos obrigatórios
        if not nome or not sexo or not cargo:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos obrigatórios.')
            return redirect('/membros/')

        # Checa se o membro já está cadastrado (baseado no CPF ou outro identificador único)
        if Membros.objects.filter(cpf=cpf).exists():
            messages.add_message(request, constants.ERROR, 'O membro já está cadastrado.')
            return redirect('/membros/')

        # Tenta salvar o membro
        try:
            novo_membro = Membros(
                nome=nome,
                sexo=sexo,
                email=email,
                telefone=telefone,
                cpf=cpf,
                endereco=endereco,
                foto=foto,
                data_batismo=data_batismo or None,  # Tratar caso seja vazio
                data_nascimento=data_nascimento or None,  # Tratar caso seja vazio
                cargo=cargo,
                pastor=request.user
            )
            novo_membro.save()

            messages.add_message(request, constants.SUCCESS, 'Membro cadastrado com sucesso!')
            return redirect('/membros/')
        except Exception as e:
            # Log do erro para fins de depuração (opcional)
            print(f"Erro ao salvar o membro: {e}")
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar o membro. Tente novamente.')
            return redirect('/membros/')
