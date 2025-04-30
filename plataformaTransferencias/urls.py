from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_transferencias, name='listar_transferencias'),
    path('transferir/<int:membro_id>/', views.transferir_membro, name='transferir_membro'),
    path('controle_transferidos/', views.controle_transferidos, name='controle_transferidos'),
]
