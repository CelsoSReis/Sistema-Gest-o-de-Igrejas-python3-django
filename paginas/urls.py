from django.urls import path
# importa as views que foram criadas
from .views import PaginaInicial, SobreView
# padrão django urls
urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre' ),
]