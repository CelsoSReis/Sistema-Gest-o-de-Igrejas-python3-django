from django.urls import path
from . import views

urlpatterns = [
    path('membros/', views.membros, name='membros'),
    path('membros/editar/<int:id>/', views.atualizar_membro, name='editar_membro'),
]