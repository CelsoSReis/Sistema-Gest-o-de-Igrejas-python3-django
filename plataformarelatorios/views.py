from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
from plataformadizimos.models import Dizimos
from plataformaigreja.models import Membros
from plataformacontas.models import ContaPagar
from django.core.files.storage import default_storage
from io import BytesIO
import os


@login_required(login_url='/usuarios/login')
def visualizar_relatorio_membros(request):
    """Exibe os membros em um template antes de gerar o PDF."""
    membros = Membros.objects.filter(pastor=request.user).order_by("nome")
    return render(request, 'relatorio_membros.html', {'membros': membros})

def desenhar_cabecalho(c, titulo):
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 800, titulo)
    c.line(50, 790, 550, 790)  # Linha horizontal abaixo do título

def desenhar_tabela_membros(c, membros):
    x_inicial, y_inicial = 50, 750
    espacamento_linha = 20
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x_inicial, y_inicial, "Nome")
    c.drawString(x_inicial + 200, y_inicial, "Email")
    c.drawString(x_inicial + 350, y_inicial, "Telefone")
    
    c.setFont("Helvetica", 10)
    y_atual = y_inicial - espacamento_linha
    
    for membro in membros:
        c.drawString(x_inicial, y_atual, membro.nome[:25])  # Nome truncado para caber
        c.drawString(x_inicial + 200, y_atual, membro.email[:30])  # Email truncado
        c.drawString(x_inicial + 350, y_atual, membro.telefone)
        y_atual -= espacamento_linha
        
        if y_atual < 50:  # Quebra de página se necessário
            c.showPage()
            desenhar_cabecalho(c, "Relatório de Membros")
            y_atual = y_inicial - espacamento_linha

@login_required(login_url='/usuarios/login')
def gerar_relatorio_membros(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_membros.pdf"'
    
    c = canvas.Canvas(response, pagesize=A4)
    desenhar_cabecalho(c, "Relatório de Membros")
    
    membros = Membros.objects.filter(pastor=request.user).order_by("nome")
    desenhar_tabela_membros(c, membros)
    
    c.showPage()
    c.save()
    
    return response

@login_required(login_url='/usuarios/login')
def gerar_relatorio_dizimos(request):
    """Gera um relatório de dízimos por mês"""
    
    # Obtém os parâmetros do mês e ano da URL (ou usa o mês/ano atual)
    mes = request.GET.get('mes', datetime.now().month)
    ano = request.GET.get('ano', datetime.now().year)

    # Filtra os dízimos do pastor logado por mês e ano
    dizimos = Dizimos.objects.filter(
        data_dizimo__month=mes, 
        data_dizimo__year=ano, 
    ).order_by('data_dizimo')

    # Criar resposta do tipo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="relatorio_dizimos_{mes}_{ano}.pdf"'

    # Criar o documento PDF
    p = canvas.Canvas(response, pagesize=A4)
    largura, altura = A4
    y_position = altura - 50  # Margem superior

    # Título do relatório
    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, y_position, f"Relatório de Dízimos - {mes}/{ano}")
    y_position -= 30  # Espaço após título

    # Cabeçalhos da tabela
    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, y_position, "Nome do Membro")
    p.drawString(250, y_position, "Data")
    p.drawString(350, y_position, "Valor (R$)")
    p.line(50, y_position - 5, 500, y_position - 5)  # Linha separadora
    y_position -= 20

    total = 0  # Para somar os valores

    p.setFont("Helvetica", 10)
    for dizimo in dizimos:
        if y_position < 50:  # Verifica se precisa de nova página
            p.showPage()
            y_position = altura - 50  # Reseta a posição

        p.drawString(50, y_position, dizimo.membro.nome)
        p.drawString(250, y_position, dizimo.data_dizimo.strftime("%d/%m/%Y"))
        p.drawString(350, y_position, f"R$ {dizimo.valor:.2f}")
        y_position -= 20
        total += dizimo.valor  # Soma dos valores

    # Linha final
    p.line(50, y_position, 500, y_position)
    y_position -= 20

    # Total
    p.setFont("Helvetica-Bold", 12)
    p.drawString(250, y_position, "Total: ")
    p.drawString(350, y_position, f"R$ {total:.2f}")

    # Finaliza o PDF
    p.showPage()
    p.save()

    return response
# Gera Relatórios de Dízimos
#@login_required(login_url='/usuarios/login')
#def pagina_relatorio_dizimos(request):
 #   """Exibe a página com o formulário para gerar relatório de dízimos."""
  #  ano_atual = datetime.now().year
   # anos_disponiveis = range(ano_atual - 2, ano_atual + 1)  # Últimos 2 anos

    #return render(request, 'relatorio_dizimos.html', {'anos_disponiveis': anos_disponiveis})

@login_required(login_url='/usuarios/login')
def gerar_relatorio_dizimos(request):
    """Gera um relatório de dízimos por mês e ano filtrados"""

    # Obtém os parâmetros do mês e ano da URL ou formulário
    mes = request.GET.get('mes')
    ano = request.GET.get('ano')

    # Se não forem fornecidos, utiliza o mês e ano atuais
    if not mes or not ano:
        mes = datetime.now().month
        ano = datetime.now().year

    # Converte para inteiro para o filtro funcionar corretamente
    mes = int(mes)
    ano = int(ano)

    # Filtra os dízimos registrados pelo usuário atual (pastor logado) com base no mês e ano selecionados
    dizimos = Dizimos.objects.filter(
        data_dizimo__month=mes,
        data_dizimo__year=ano,
        membro__pastor=request.user  # Ajuste: filtra pelo pastor do membro
    ).order_by('data_dizimo')

    # Criar resposta do tipo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="relatorio_dizimos_{mes}_{ano}.pdf"'

    # Criar o documento PDF
    p = canvas.Canvas(response, pagesize=A4)
    largura, altura = A4
    y_position = altura - 50  # Margem superior

    # Título do relatório
    p.setFont("Helvetica-Bold", 14)
    p.drawString(180, y_position, f"Relatório de Dízimos - {mes:02d}/{ano}")
    y_position -= 30  # Espaço após título

    # Cabeçalhos da tabela
    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, y_position, "Nome do Membro")
    p.drawString(250, y_position, "Data")
    p.drawString(350, y_position, "Valor (R$)")
    p.line(50, y_position - 5, 500, y_position - 5)  # Linha separadora
    y_position -= 20

    total = 0  # Para somar os valores

    p.setFont("Helvetica", 10)
    for dizimo in dizimos:
        if y_position < 50:  # Verifica se precisa de nova página
            p.showPage()
            y_position = altura - 50  # Reseta a posição

        p.drawString(50, y_position, dizimo.membro.nome)
        p.drawString(250, y_position, dizimo.data_dizimo.strftime("%d/%m/%Y"))
        p.drawString(350, y_position, f"R$ {dizimo.valor:.2f}")
        y_position -= 20
        total += dizimo.valor  # Soma dos valores

    # Linha final
    p.line(50, y_position, 500, y_position)
    y_position -= 20

    # Total
    p.setFont("Helvetica-Bold", 12)
    p.drawString(250, y_position, "Total: ")
    p.drawString(350, y_position, f"R$ {total:.2f}")

    # Finaliza o PDF
    p.showPage()
    p.save()

    return response

@login_required(login_url='/usuarios/login')
def pagina_relatorio_dizimos(request):
    """Exibe a página com o formulário para escolher mês e ano do relatório de dízimos."""
    ano_atual = datetime.now().year
    anos_disponiveis = range(ano_atual - 2, ano_atual + 1)  # Últimos 2 anos
    meses_disponiveis = [
        (1, "Janeiro"), (2, "Fevereiro"), (3, "Março"), (4, "Abril"),
        (5, "Maio"), (6, "Junho"), (7, "Julho"), (8, "Agosto"),
        (9, "Setembro"), (10, "Outubro"), (11, "Novembro"), (12, "Dezembro")
    ]
    return render(request, 'relatorio_dizimos.html', {
        'anos_disponiveis': anos_disponiveis,
        'meses_disponiveis': meses_disponiveis
    })




# Gera um relatório de contas pagas
@login_required(login_url='/usuarios/login')
def gerar_relatorio_contas_pagas(request):
    """Gera um PDF com as contas pagas do mês atual."""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_contas_pagas_mes_atual.pdf"'

    pdf = canvas.Canvas(response, pagesize=A4)
    pdf.setTitle("Relatório de Contas Pagas")

    # Obtém o mês e ano atuais
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Filtra contas pagas do mês atual
    contas_pagas = ContaPagar.objects.filter(
        status=1,
        pastor=request.user,
        data_vencimento__month=mes_atual,
        data_vencimento__year=ano_atual
    ).order_by('data_vencimento')  # Ordena por data de vencimento

    # Configuração inicial do PDF
    y = 800
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(180, y, f"Relatório de Contas Pagas - {mes_atual}/{ano_atual}")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y - 50, "-----------------------------------------")

    y -= 80  # Ajuste da posição inicial para listar as contas

    # Cabeçalho da tabela
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Nome da Conta")
    pdf.drawString(250, y, "Data de Vencimento")
    pdf.drawString(400, y, "Valor Pago")
    y -= 20

    # Linhas da tabela
    pdf.setFont("Helvetica", 12)
    total = 0  # Variável para somar os valores pagos

    for conta in contas_pagas:
        pdf.drawString(50, y, conta.fornecedor)
        pdf.drawString(250, y, conta.data_vencimento.strftime('%d/%m/%Y') if conta.data_vencimento else 'N/A')
        pdf.drawString(400, y, f"R$ {conta.valor:.2f}")
        total += conta.valor  # Soma dos valores pagos
        y -= 20

        # Adiciona uma nova página se a lista ultrapassar o limite
        if y < 100:
            pdf.showPage()
            y = 800  # Reinicia a posição vertical

    # Exibe o total pago
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(250, y - 20, "Total Pago:")
    pdf.drawString(400, y - 20, f"R$ {total:.2f}")

    pdf.save()
    return response
