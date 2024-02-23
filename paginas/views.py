from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#classe PaginaInicial extends TemplateView
class PaginaInicial(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"

class HomeView(TemplateView):
    template_name = "paginas/home.html"

class PastoresView(TemplateView):
    template_name = "paginas/pastores.html"

class UsuariosView(TemplateView):
    template_name = "paginas/usuarios.html"

class IgrejasView(TemplateView):
    template_name = "paginas/igrejas.html"

class BisposView(TemplateView):
    template_name = "paginas/bispos.html"

class TesoureirosView(TemplateView):
    template_name = "paginas/tesoureiros.html"

class SecretariosView(TemplateView):
    template_name = "paginas/secretarios.html"

class CargosView(TemplateView):
    template_name = "paginas/cargos.html"

class FrequenciasView(TemplateView):
    template_name = "paginas/frequencias.html"