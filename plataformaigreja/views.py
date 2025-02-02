from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse

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


@login_required(login_url='/usuarios/login')
def atualizar_membro(request, id):
    # Busca o membro pelo ID ou retorna 404 se não existir
    membro = get_object_or_404(Membros, id=id, pastor=request.user)

    if request.method == "GET":
        # Renderiza o formulário de edição com os dados atuais do membro
        return render(request, 'editar_membro.html', {'membro': membro})

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
            messages.add_message(request, messages.ERROR, 'Preencha todos os campos obrigatórios.')
            return redirect(f'/membros/editar/{id}/')

        # Checa se o CPF já está cadastrado para outro membro (exceto o atual)
        if Membros.objects.filter(cpf=cpf).exclude(id=id).exists():
            messages.add_message(request, messages.ERROR, 'O CPF já está cadastrado para outro membro.')
            return redirect(f'/membros/editar/{id}/')

        # Atualiza os dados do membro
        try:
            membro.nome = nome
            membro.sexo = sexo
            membro.email = email
            membro.telefone = telefone
            membro.cpf = cpf
            membro.endereco = endereco
            if foto:  # Atualiza a foto apenas se uma nova foi enviada
                membro.foto = foto
                membro.data_batismo = data_batismo or None  # Tratar caso seja vazio
                membro.data_nascimento = data_nascimento or None  # Tratar caso seja vazio
                membro.cargo = cargo

            # Salva as alterações no banco de dados
            membro.save()

            messages.add_message(request, messages.SUCCESS, 'Membro atualizado com sucesso!')
            return redirect('/membros/')
        except ValidationError as e:
            # Log do erro para fins de depuração (opcional)
            print(f"Erro ao atualizar o membro: {e}")
            messages.add_message(request, messages.ERROR, 'Erro ao atualizar o membro. Verifique os dados.')
            return redirect(f'/membros/editar/{id}/')
        except Exception as e:
            # Log do erro para fins de depuração (opcional)
            print(f"Erro ao atualizar o membro: {e}")
            messages.add_message(request, messages.ERROR, 'Erro ao atualizar o membro. Tente novamente.')
            return redirect(f'/membros/editar/{id}/')
        
@login_required(login_url='/usuarios/login')
def excluir_membro(request, id):
    if request.method == "POST":
        try:
            # Busca o membro pelo ID e verifica se pertence ao pastor logado
            membro = get_object_or_404(Membros, id=id, pastor=request.user)
            
            # Exclui o membro do banco de dados
            membro.delete()
            
            # Mensagem de sucesso
            messages.add_message(request, constants.SUCCESS, 'Membro excluído com sucesso!')
        except Membros.DoesNotExist:
            # Mensagem de erro se o membro não for encontrado
            messages.add_message(request, constants.ERROR, 'Membro não encontrado.')
        except Exception as e:
            # Mensagem de erro genérico
            print(f"Erro ao excluir o membro: {e}")
            messages.add_message(request, constants.ERROR, 'Erro ao excluir o membro. Tente novamente.')
        
        # Redireciona de volta para a lista de membros
        return redirect('/membros/')
    
#Exibir membros em uma modal
@login_required(login_url='/usuarios/login')
def obter_dados_membro(request, id):
    try:
        # Busca o membro pelo ID e verifica se pertence ao pastor logado
        membro = Membros.objects.get(id=id, pastor=request.user)
        
        # Retorna os dados do membro em formato JSON
        data = {
            'id': membro.id,
            'nome': membro.nome,
            'sexo': membro.get_sexo_display(),
            'email': membro.email,
            'telefone': membro.telefone,
            'cpf': membro.cpf,
            'endereco': membro.endereco,
            'foto': membro.foto.url if membro.foto else None,
            'data_nascimento': membro.data_nascimento.strftime('%d/%m/%Y') if membro.data_nascimento else None,
            'data_batismo': membro.data_batismo.strftime('%d/%m/%Y') if membro.data_batismo else None,
            'cargo': membro.get_cargo_display(),
        }
        return JsonResponse(data)
    except Membros.DoesNotExist:
        return JsonResponse({'error': 'Membro não encontrado.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
