from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_documento, name='upload_documento'),
    path('listar/', views.listar_documentos, name='listar_documentos'),
    path('excluir/<int:id>/', views.excluir_documento, name='excluir_documento'),
]
