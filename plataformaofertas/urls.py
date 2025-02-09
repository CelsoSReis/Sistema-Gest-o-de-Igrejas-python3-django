from django.urls import path
from . import views  # Importe as views do seu aplicativo

urlpatterns = [
    path("ofertas/", views.ofertas, name="ofertas"),
    path('ofertas/excluir/<int:oferta_id>/', views.excluir_oferta, name='excluir_oferta'),
    path('ofertas/editar/<int:oferta_id>/', views.editar_oferta, name='editar_oferta'),
    path('ofertas/', views.listar_ofertas, name='listar_ofertas'),

]