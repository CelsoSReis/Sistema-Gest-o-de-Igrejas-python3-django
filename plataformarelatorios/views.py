from django.http import HttpResponse
from django.contrib.auth.models import User
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from plataformaofertas.models import Oferta  # Importando modelo de contas
from plataformadizimos.models import Dizimos  # Importando modelo de dízimos
from datetime import datetime

# 📄 Relatório de Membros
def gerar_relatorio_membros(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_membros.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 40, "Relatório de Membros")

    y_position = height - 80
    p.setFont("Helvetica", 12)

    membros = User.objects.all().order_by("first_name")

    for membro in membros:
        p.drawString(50, y_position, f"{membro.first_name} {membro.last_name} - {membro.email}")
        y_position -= 20

    p.showPage()
    p.save()
    return response


# 📄 Relatório de Dízimos
def gerar_relatorio_dizimos(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_dizimos.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 40, "Relatório de Dízimos")

    y_position = height - 80
    p.setFont("Helvetica", 12)

    dizimos = Dizimos.objects.all().order_by("-data")

    for dizimo in dizimos:
        p.drawString(50, y_position, f"{Dizimos.membro.first_name} {Dizimos.membro.last_name} - R$ {Dizimos.valor} - {Dizimos.data}")
        y_position -= 20

    p.showPage()
    p.save()
    return response


# 📄 Relatório de Contas
def gerar_relatorio_contas(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_contas.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 40, "Relatório de Contas")

    y_position = height - 80
    p.setFont("Helvetica", 12)

    contas = ContaPagar.objects.all().order_by("data_vencimento")

    for conta in contas:
        p.drawString(50, y_position, f"{conta.fornecedor} - {conta.descricao} - R$ {conta.valor} - {conta.get_status_display()}")
        y_position -= 20

    p.showPage()
    p.save()
    return response
