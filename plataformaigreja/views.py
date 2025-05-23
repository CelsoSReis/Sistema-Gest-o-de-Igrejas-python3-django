from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from .models import Membros
from igreja.models import Igreja
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from io import BytesIO
from django.core.files.storage import default_storage
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import letter
import os



@login_required(login_url='/usuarios/login')
def dashboard_igreja(request):
    # Renderiza página dashboard
    return render(request, 'dashboard.html')

@login_required(login_url='/usuarios/login')
def controle_membros(request):
    # Renderiza página dashboard
    return render(request, 'controle_memb.html')
    

@login_required(login_url='/usuarios/login')
def membros(request):
    if request.method == "GET":
        # Busca membros do pastor logado
        membros = Membros.objects.filter(pastor=request.user, ativo=True)
        total_membros = membros.count()  # Conta os membros daquele pastor

        return render(request, 'membros.html', {
            'membros': membros,
            'total_membros': total_membros,
        })

    elif request.method == "POST":
        # Obtém os dados do formulário
        nome = request.POST.get('nome', '').strip()
        sexo = request.POST.get('sexo', '').strip()
        email = request.POST.get('email', '').strip()
        telefone = request.POST.get('telefone', '').strip()
        cpf = request.POST.get('cpf', '').strip()
        endereco = request.POST.get('endereco', '').strip()
        foto = request.FILES.get('foto')
        data_batismo = request.POST.get('data_batismo', '').strip()
        data_nascimento = request.POST.get('data_nascimento', '').strip()
        cargo = request.POST.get('cargo', '').strip()

        if not nome or not sexo or not cargo:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos obrigatórios.')
            return redirect('/index/membros/')

        if Membros.objects.filter(nome=nome).exists():
            messages.add_message(request, constants.ERROR, 'O membro já está cadastrado.')
            return redirect('/index/membros/')

        try:
            novo_membro = Membros(
                nome=nome,
                sexo=sexo,
                email=email,
                telefone=telefone,
                cpf=cpf,
                endereco=endereco,
                foto=foto,
                data_batismo=data_batismo or None,
                data_nascimento=data_nascimento or None,
                cargo=cargo,
                pastor=request.user
            )
            novo_membro.save()

            messages.add_message(request, constants.SUCCESS, 'Membro cadastrado com sucesso!')
            return redirect('/index/membros/')
        except Exception as e:
            print(f"Erro ao salvar o membro: {e}")
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar o membro. Tente novamente.')
            return redirect('/index/membros/')


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
            return redirect(f'index/membros/editar/{id}/')

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
            return redirect('/index/membros/')
        except ValidationError as e:
            # Log do erro para fins de depuração (opcional)
            print(f"Erro ao atualizar o membro: {e}")
            messages.add_message(request, messages.ERROR, 'Erro ao atualizar o membro. Verifique os dados.')
            return redirect(f'index/membros/editar/{id}/')
        except Exception as e:
            # Log do erro para fins de depuração (opcional)
            print(f"Erro ao atualizar o membro: {e}")
            messages.add_message(request, messages.ERROR, 'Erro ao atualizar o membro. Tente novamente.')
            return redirect(f'index/membros/editar/{id}/')
        
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
        return redirect('/index/membros/')
    
#Detalhes membro
@login_required(login_url='/usuarios/login')
def detalhes_membro(request, membro_id):
    """Exibe os detalhes de um membro específico, convertendo siglas para nomes completos."""
    membro = get_object_or_404(Membros, id=membro_id)

    # Dicionário de mapeamento de cargos
    cargos_dict = {
        "A": "Auxiliar",
        "C": "Congregado",
        "Cr": "Crianças",
        "Da": "Diaconisa",
        "D": "Diácono",
        "E": "Evangelista",
        "J": "Jovem",
        "Mb": "Membro",
        "Mi": "Missionário(a)",
        "Pr": "Pastor",
        "P": "Presbítero",
    }

    # Dicionário de mapeamento de sexo
    sexo_dict = {
        "M": "Masculino",
        "F": "Feminino",
    }

    # Converter siglas para nomes completos
    membro.cargo_nome = cargos_dict.get(membro.cargo, "Não informado")
    membro.sexo_nome = sexo_dict.get(membro.sexo, "Não informado")

    return render(request, 'detalhes_membro.html', {'membro': membro})


@login_required(login_url='/usuarios/login')
def exportar_carteirinha_membro(request, id):
    # Busca o membro pelo ID e verifica se pertence ao pastor logado
    membro = get_object_or_404(Membros, id=id, pastor=request.user)

    # Tamanho da carteirinha: 8,5 x 5,5 cm (em pontos)
    largura = 242.65
    altura = 155.91

    # Caminho para a imagem de fundo (ajuste conforme a estrutura do seu projeto)
    fundo_path = os.path.join('templates','static', 'imagens', 'fundo_carteirinha1.jpg')  # Ajuste o caminho conforme necessário

    # Criação do PDF em memória
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=(largura, altura))

    # Adiciona a imagem de fundo (se existir)
    if os.path.exists(fundo_path):
        p.drawImage(fundo_path, 0, 0, width=largura, height=altura)

    # Define margens
    margem = 10

    # Configurações do PDF (sem borda, pois temos fundo)
    p.setStrokeColor(colors.black)
    p.setLineWidth(1)


    # Foto 3x4 (proporção ajustada)
    if membro.foto:
        foto_path = default_storage.path(membro.foto.name)
        p.drawImage(foto_path, margem - 2, altura - 118, width=55, height=65, mask='auto')

    # Dados do membro
    p.setFont("Helvetica", 8)
    p.drawString(68, altura - 56, f"{membro.nome}")
    p.setFont("Helvetica", 6.5)
    p.drawString(68.6, altura - 75, f"{membro.cpf}")
    p.drawString(68.6, altura - 117, f"{membro.data_nascimento.strftime('%d/%m/%Y') if membro.data_nascimento else '00/00/0000'}")
    p.drawString(162, altura - 117, f"{membro.data_batismo.strftime('%d/%m/%Y') if membro.data_batismo else '00/00/0000'}")
    p.drawString(68.6, altura - 95, f"{membro.get_cargo_display()}")

    # Finaliza o PDF
    p.showPage()
    p.save()

    # Configura a resposta como PDF
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="carteirinha_{membro.nome}.pdf"'
    return response

@login_required(login_url='/usuarios/login')
def exportar_todas_carteirinhas(request):
    """Gera um PDF com todas as carteirinhas (8 por página, 4 linhas x 2 colunas)."""
    
    # Busca todos os membros cadastrados pelo usuário logado
    membros = Membros.objects.filter(pastor=request.user, ativo=True)

    # Se não houver membros, retorna erro
    if not membros.exists():
        return HttpResponse("Nenhum membro encontrado.", status=400)

    # Tamanho da página A4 (pontos)
    largura_pagina, altura_pagina = letter

    # Tamanho da carteirinha: 8,5 x 5,5 cm (convertido para pontos)
    largura_carteirinha = 242.65
    altura_carteirinha = 155.91

    # Posições das carteirinhas na página (2 colunas x 4 linhas)
    espacamento_horizontal = 30  # Margem à esquerda
    espacamento_vertical = 20    # Margem no topo
    posicoes = [
        (espacamento_horizontal, altura_pagina - 170), (290, altura_pagina - 170),  # Primeira linha
        (espacamento_horizontal, altura_pagina - 340), (290, altura_pagina - 340),  # Segunda linha
        (espacamento_horizontal, altura_pagina - 510), (290, altura_pagina - 510),  # Terceira linha
        (espacamento_horizontal, altura_pagina - 680), (290, altura_pagina - 680)   # Quarta linha
    ]

    # Caminho para a imagem de fundo
    fundo_path = os.path.join('templates', 'static', 'imagens', 'fundo_carteirinha.jpg')

    # Criação do PDF em memória
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Contador de carteirinhas na página
    count = 0

    for membro in membros:
        # Determinar posição na página
        x, y = posicoes[count]

        # Adicionar imagem de fundo
        if os.path.exists(fundo_path):
            p.drawImage(fundo_path, x, y, width=largura_carteirinha, height=altura_carteirinha)

        # Foto 3x4 (se houver)
        if membro.foto:
            foto_path = default_storage.path(membro.foto.name)
            p.drawImage(foto_path, x + 6, y + 38, width=55, height=65, mask='auto')

        # Dados do membro
        p.setFont("Helvetica", 8)
        p.drawString(x + 68, y + 100, f"{membro.nome}")
        p.setFont("Helvetica", 6.5)
        p.drawString(x + 68.6, y + 81, f"{membro.cpf}")
        p.drawString(x + 68.6, y + 39, f"{membro.data_nascimento.strftime('%d/%m/%Y') if membro.data_nascimento else '00/00/0000'}")
        p.drawString(x + 162, y + 39, f"{membro.data_batismo.strftime('%d/%m/%Y') if membro.data_batismo else '00/00/0000'}")
        p.drawString(x + 68.6, y + 61, f"{membro.get_cargo_display()}")

        # Atualiza o contador de carteirinhas
        count += 1

        # Se já preencheu 8 carteirinhas, cria uma nova página
        if count == 8:
            p.showPage()
            count = 0  # Reseta contador para a nova página

    # Finaliza o PDF
    p.save()

    # Configura a resposta como PDF
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="todas_carteirinhas.pdf"'
    return response
    
@login_required(login_url='/usuarios/login')
def selecionar_carteirinhas(request):
    """Página para selecionar quais carteirinhas imprimir (exibe apenas os membros cadastrados pelo usuário)."""
    membros = Membros.objects.filter(pastor=request.user, ativo=True)  # Filtra pelo usuário logado
    return render(request, 'selecionar_carteirinhas.html', {'membros': membros})

@login_required(login_url='/usuarios/login')
def imprimir_carteirinhas(request):
    """Gera um PDF com até 8 carteirinhas por página dos membros selecionados (apenas os cadastrados pelo usuário)."""
    if request.method == "POST":
        membros_ids = request.POST.getlist('membros_selecionados')

        # Filtra apenas os membros cadastrados pelo usuário logado
        membros = Membros.objects.filter(id__in=membros_ids, pastor=request.user)

        # Se não houver membros correspondentes, retorna erro
        if not membros.exists():
            return HttpResponse("Nenhum membro selecionado.", status=400)

        # Tamanho da página A4 (pontos)
        largura_pagina, altura_pagina = letter

        # Tamanho da carteirinha: 8,5 x 5,5 cm (convertido para pontos)
        largura_carteirinha = 242.65
        altura_carteirinha = 155.91

        # Posições das carteirinhas na página (2 colunas x 4 linhas)
        espacamento_horizontal = 30  # Margem à esquerda
        espacamento_vertical = 20    # Margem no topo
        posicoes = [
            (espacamento_horizontal, altura_pagina - 170), (290, altura_pagina - 170),  # Primeira linha
            (espacamento_horizontal, altura_pagina - 340), (290, altura_pagina - 340),  # Segunda linha
            (espacamento_horizontal, altura_pagina - 510), (290, altura_pagina - 510),  # Terceira linha
            (espacamento_horizontal, altura_pagina - 680), (290, altura_pagina - 680)   # Quarta linha
        ]

        # Caminho para a imagem de fundo
        fundo_path = os.path.join('templates', 'static', 'imagens', 'fundo_carteirinha.jpg')

        # Criação do PDF em memória
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        # Contador de carteirinhas na página
        count = 0

        for membro in membros:
            # Determinar posição na página
            x, y = posicoes[count]

            # Adicionar imagem de fundo
            if os.path.exists(fundo_path):
                p.drawImage(fundo_path, x, y, width=largura_carteirinha, height=altura_carteirinha)

            # Foto 3x4 (se houver)
            if membro.foto:
                foto_path = default_storage.path(membro.foto.name)
                p.drawImage(foto_path, x + 6, y + 38, width=55, height=65, mask='auto')

            # Dados do membro
            p.setFont("Helvetica", 8)
            p.drawString(x + 68, y + 100, f"{membro.nome}")
            p.setFont("Helvetica", 6.5)
            p.drawString(x + 68.6, y + 81, f"{membro.cpf}")
            p.drawString(x + 68.6, y + 39, f"{membro.data_nascimento.strftime('%d/%m/%Y') if membro.data_nascimento else '00/00/0000'}")
            p.drawString(x + 162, y + 39, f"{membro.data_batismo.strftime('%d/%m/%Y') if membro.data_batismo else '00/00/0000'}")
            p.drawString(x + 68.6, y + 61, f"{membro.get_cargo_display()}")

            # Atualiza o contador de carteirinhas
            count += 1

            # Se já preencheu 8 carteirinhas, cria uma nova página
            if count == 8:
                p.showPage()
                count = 0  # Reseta contador para a nova página

        # Finaliza o PDF
        p.save()

        # Configura a resposta como PDF
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="carteirinhas_selecionadas.pdf"'
        return response

    return HttpResponse("Erro ao gerar carteirinhas.", status=400)

#Controle de transferência de Membros
@login_required(login_url='/usuarios/login')
def controle_transf(request):
    membros = Membros.objects.filter(pastor=request.user, ativo=True)
    return render(request, 'controle_transf.html', {'membros': membros})

#Controle de Financeiro
@login_required(login_url='/usuarios/login')
def controle_financeiro(request):
    # Renderiza página dashboard
    return render(request, 'controle_finan.html')

@login_required
def listar_membros_transferencia(request):
    membros = Membros.objects.filter(pastor=request.user, ativo=True)
    return render(request, 'controle_transf.html', {'membros': membros})

@login_required
def transferir_membro(request, membro_id):
    membro = get_object_or_404(Membro, id=membro_id)

    if request.method == 'POST':
        # Confirma a transferência: deleta o membro
        membro.delete()
        return redirect('controle_membros')  #redirecionar após a transferência

    # Se for GET, gera a carta de transferência
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    texto = f"""
    Carta de Transferência

    Declaramos que {membro.nome} está sendo transferido(a) da igreja {membro.nome_igreja.nome if membro.nome_igreja else 'não especificada'} para outra congregação.

    Data: _____________
    """

    p.drawString(100, 750, "Carta de Transferência")
    p.drawString(100, 700, f"Nome: {membro.nome}")
    if membro.nome_igreja:
        p.drawString(100, 675, f"Igreja de origem: {membro.nome_igreja.nome}")
    else:
        p.drawString(100, 675, "Igreja de origem: Não especificada")
    p.drawString(100, 650, "Data: ___________________")
    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"carta_transferencia_{membro.nome}.pdf")

#Detalhes membro
@login_required(login_url='/usuarios/login')
def detalhes_transf(request, membro_id):
    """Exibe os detalhes de um membro específico, convertendo siglas para nomes completos."""
    membro = get_object_or_404(Membros, id=membro_id)

    # Dicionário de mapeamento de cargos
    cargos_dict = {
        "A": "Auxiliar",
        "C": "Congregado",
        "Cr": "Crianças",
        "Da": "Diaconisa",
        "D": "Diácono",
        "E": "Evangelista",
        "J": "Jovem",
        "Mb": "Membro",
        "Mi": "Missionário(a)",
        "Pr": "Pastor",
        "P": "Presbítero",
    }

    # Dicionário de mapeamento de sexo
    sexo_dict = {
        "M": "Masculino",
        "F": "Feminino",
    }

    # Converter siglas para nomes completos
    membro.cargo_nome = cargos_dict.get(membro.cargo, "Não informado")
    membro.sexo_nome = sexo_dict.get(membro.sexo, "Não informado")

    return render(request, 'controle_transf.html', {'membro': membro})