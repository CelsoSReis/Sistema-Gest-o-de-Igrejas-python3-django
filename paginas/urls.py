from django.urls import path
# importa as views que foram criadas
#from .views import PaginaInicial, SobreView, HomeView #PastoresView, UsuariosView, IgrejasView, BisposView, TesoureirosView, SecretariosView, CargosView, FrequenciasView, PatrimoniosView
from paginas import views


# padrão django urls
urlpatterns = [
    path('index/', views.PaginaInicial, name='index'),
    path('sobre/', views.SobreView, name='sobre'),
    path('home/', views.HomeView, name='home'),
    path('pastores/', views.PastoresView, name='pastores' ),
    path('igrejas/', views.IgrejasView, name='igrejas' ),
    path('tesoureiros/', views.TesoureirosView, name='tesoureiros' ),

    #path('usuarios/', UsuariosView.as_view(), name='usuarios' ),
    #path('igrejas/', IgrejasView.as_view(), name='igrejas' ),
    #path('bispos/', BisposView.as_view(), name='bispos' ),
    #path('tesoureiros/', TesoureirosView.as_view(), name='tesoureiros' ),
    #path('secretarios/', SecretariosView.as_view(), name='secretarios' ),
    #path('cargos/', CargosView.as_view(), name='cargos' ),
    #path('frequencias/', FrequenciasView.as_view(), name='frequencias' ),
    #path('patrimonios/', PatrimoniosView.as_view(), name='patrimonios' ),
]