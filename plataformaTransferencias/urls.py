from django.urls import path
from . import views

urlpatterns = [
    path('transferir/<int:membro_id>/', views.transferir_membro, name='transferir_membro'),
    path('controle_transferidos/', views.controle_transferidos, name='controle_transferidos'),
    path('reativar-membro/<int:membro_id>/', views.reativar_membro, name='reativar_membro'),
    path('transferencias/carta-transferencia/<int:membro_id>/', views.gerar_carta_transferencia, name='gerar_carta_transferencia'),
]
