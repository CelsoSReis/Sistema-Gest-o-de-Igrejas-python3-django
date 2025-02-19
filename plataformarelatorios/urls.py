from django.urls import path
from .views import gerar_relatorio_membros, gerar_relatorio_dizimos, gerar_relatorio_contas

urlpatterns = [
    path('membros/', gerar_relatorio_membros, name='relatorio_membros'),
    path('dizimosrel/', gerar_relatorio_dizimos, name='relatorio_dizimos'),
    path('contas/', gerar_relatorio_contas, name='relatorio_contas'),
]
