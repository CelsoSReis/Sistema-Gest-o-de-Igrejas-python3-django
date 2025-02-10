from django.urls import path
from . import views

urlpatterns = [
    path('contas_pagar/', views.contas_pagar, name='contas_pagar'),
]