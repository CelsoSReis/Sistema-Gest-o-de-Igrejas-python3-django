from django.urls import path
# importa as views que foram criadas
from .views import PaginaInicial, SobreView, HomeView, PastoresView

# padrão django urls
urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre' ),
    path('home/', HomeView.as_view(), name='home' ),
    path('pastores/', PastoresView.as_view(), name='pastores' ),
]