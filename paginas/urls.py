from django.urls import path
# importa as views que foram criadas
from .views import PaginaInicial
# padrão django urls
urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
]