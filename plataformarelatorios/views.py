from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

from plataformaigreja.models import Membros

@login_required(login_url='/usuarios/login')
def visualizar_relatorio_membros(request):
    """Exibe os membros em um template antes de gerar o PDF."""
    membros = Membros.objects.filter(pastor=request.user).order_by("nome")
    return render(request, 'relatorio_membros.html', {'membros': membros})

@login_required(login_url='/usuarios/login')
def gerar_relatorio_membros(request):
    """Gera um PDF dos membros cadastrados."""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_membros.pdf"'
    
    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []
    
    styles = getSampleStyleSheet()
    title = Paragraph("Relatório de Membros", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    data = [["Nome", "Email", "Telefone"]]  # Cabeçalhos da tabela
    
    membros = Membros.objects.filter(pastor=request.user).order_by("nome")
    for membro in membros:
        data.append([membro.nome, membro.email, membro.telefone])
    
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ]))
    
    elements.append(table)
    doc.build(elements)
    
    return response
