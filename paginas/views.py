from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#classe PaginaInicial extends TemplateView
class PaginaInicial(TemplateView):
    template_name = "paginas/modelo.html"


class SobreView(TemplateView):
    template_name = "paginas/sobre.html"