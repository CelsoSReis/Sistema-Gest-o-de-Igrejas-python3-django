from django.urls import path
from .views import visualizar_relatorio_membros, gerar_relatorio_membros, pagina_relatorio_dizimos, gerar_relatorio_dizimos, gerar_relatorio_contas_pagas

urlpatterns = [
    path('membrosrel/', visualizar_relatorio_membros, name='visualizar_relatorio_membros'),
    path('membrosrel/pdf/', gerar_relatorio_membros, name='gerar_relatorio_membros'),
    path('dizimos/relatorio/', pagina_relatorio_dizimos, name='pagina_relatorio_dizimos'),
    path('dizimos/gerar-relatorio/', gerar_relatorio_dizimos, name='gerar_relatorio_dizimos'),
    path('contas_pagas/relatorio/', gerar_relatorio_contas_pagas, name='relatorio_contas_pagas'),
]
