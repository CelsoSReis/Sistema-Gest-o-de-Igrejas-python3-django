from django.urls import path
from .views import visualizar_relatorio_membros, gerar_relatorio_membros

urlpatterns = [
    path('membrosrel/', visualizar_relatorio_membros, name='visualizar_relatorio_membros'),
    path('membrosrel/pdf/', gerar_relatorio_membros, name='gerar_relatorio_membros'),
]
