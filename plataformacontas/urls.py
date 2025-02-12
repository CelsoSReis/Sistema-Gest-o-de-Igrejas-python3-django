from django.urls import path
from . import views

urlpatterns = [
    path('contas_pagar/', views.contas_pagar, name='contas_pagar'),
    path('contas/vencimento-mes/', views.contas_vencimento_mes_atual, name='contas_vencimento_mes_atual'),
    path('contas/vencidas/', views.contas_vencidas, name='contas_vencidas'),

]