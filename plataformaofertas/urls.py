from django.urls import path
from . import views  # Importe as views do seu aplicativo

urlpatterns = [
    path("ofertas/", views.ofertas, name="ofertas"),
]