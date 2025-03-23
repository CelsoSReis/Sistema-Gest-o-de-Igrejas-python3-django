from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_igreja, name='igreja_cadastro'),
]