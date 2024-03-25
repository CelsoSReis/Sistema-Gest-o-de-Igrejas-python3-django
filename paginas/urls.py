from django.urls import path
# importa as views que foram criadas
from .views import PaginaInicial, SobreView, HomeView #PastoresView, UsuariosView, IgrejasView, BisposView, TesoureirosView, SecretariosView, CargosView, FrequenciasView, PatrimoniosView
from paginas import views
# padrão django urls
urlpatterns = [
    #path('', views.PaginaInicial, name='index'),
    #path('', views.SobreView, name='sobre'),
    #path('', views.HomeView, name='home'),

    #path('', PaginaInicial.as_view(), name='index'),
    #path('sobre/', SobreView.as_view(), name='sobre' ),
    #path('home/', HomeView.as_view(), name='home' ),
    #path('pastores/', PastoresView.as_view(), name='pastores' ),
    #path('usuarios/', UsuariosView.as_view(), name='usuarios' ),
    #path('igrejas/', IgrejasView.as_view(), name='igrejas' ),
    #path('bispos/', BisposView.as_view(), name='bispos' ),
    #path('tesoureiros/', TesoureirosView.as_view(), name='tesoureiros' ),
    #path('secretarios/', SecretariosView.as_view(), name='secretarios' ),
    #path('cargos/', CargosView.as_view(), name='cargos' ),
    #path('frequencias/', FrequenciasView.as_view(), name='frequencias' ),
    #path('patrimonios/', PatrimoniosView.as_view(), name='patrimonios' ),
]