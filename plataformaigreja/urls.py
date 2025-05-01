from django.urls import path
from . import views

urlpatterns = [
    path('membros/', views.membros, name='membros'),
    path('controle_membros/', views.controle_membros, name='controle_membros'),
    path('membros/editar/<int:id>/', views.atualizar_membro, name='editar_membro'),
    path('membros/excluir/<int:id>/', views.excluir_membro, name='excluir_membro'),
    path('dashboard_igreja/', views.dashboard_igreja, name='dashboard_igreja'),
    path('membros/exportar_carteirinha/<int:id>/', views.exportar_carteirinha_membro, name='exportar_carteirinha_membro'),
    path('exportar_todas_carteirinhas/', views.exportar_todas_carteirinhas, name='exportar_todas_carteirinhas'),
    path('membros/<int:membro_id>/', views.detalhes_membro, name='detalhes_membro'),
    path('selecionar_carteirinhas/', views.selecionar_carteirinhas, name='selecionar_carteirinhas'),
    path('imprimir_carteirinhas/', views.imprimir_carteirinhas, name='imprimir_carteirinhas'),
    path('controle_transf/', views.controle_transf, name='controle_transf'),
    path('controle_financeiro', views.controle_financeiro, name='controle_financeiro'),
    path('detalhes_transf/<int:membro_id>/', views.detalhes_transf, name='detalhes_transf'),
]