from django.urls import path
from . import views

urlpatterns = [
    path('contas_pagar/', views.contas_pagar, name='contas_pagar'),
    path('contas/vencimento-mes/', views.contas_vencimento_mes_atual, name='contas_vencimento_mes_atual'),
    path('contas/vencidas/', views.contas_vencidas, name='contas_vencidas'),
    path('contas/excluir/<int:conta_id>/', views.excluir_conta, name='excluir_conta'),
    path('contas/todas_contas/', views.todas_contas, name='todas_contas'),
    path('contas_pagar/editar/<int:conta_id>/', views.editar_conta, name="editar_conta"),
    path('contas_pagar/pagar/<int:conta_id>/', views.pagar_conta, name="pagar_conta"),
    path('contas_pagas/', views.contas_pagas, name="contas_pagas"),
]