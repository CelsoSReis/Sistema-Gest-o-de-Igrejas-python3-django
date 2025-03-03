from django.urls import path
from . import views

urlpatterns = [
    path('membros/', views.membros, name='membros'),
    path('membros/editar/<int:id>/', views.atualizar_membro, name='editar_membro'),
    path('membros/excluir/<int:id>/', views.excluir_membro, name='excluir_membro'),
    path('membros/obter-dados/<int:id>/', views.obter_dados_membro, name='obter_dados_membro'),
    path('dashboard_igreja/', views.dashboard_igreja, name='dashboard_igreja'),
    path('membros/exportar_carteirinha/<int:id>/', views.exportar_carteirinha_membro, name='exportar_carteirinha_membro'),
    path('exportar_todas_carteirinhas/', views.exportar_todas_carteirinhas, name='exportar_todas_carteirinhas'),
]