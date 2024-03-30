from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

# classe PaginaInicial extends TemplateView
@login_required
def PaginaInicial(request):
  return render(request, 'paginas/index.html')
@login_required
def SobreView(request):
  return render(request, 'paginas/sobre.html')
@login_required
def HomeView(request):
  return render(request, 'paginas/home.html')
@login_required
def PastoresView(request):
  return render(request, 'paginas/pastores.html')
@login_required
def IgrejasView(request):
  return render(request, 'paginas/igrejas.html')
@login_required
def TesoureirosView(request):
  return render(request, 'paginas/tesoureiros.html')


#class UsuariosView(TemplateView):
 #   template_name = "paginas/usuarios.html"


#class BisposView(TemplateView):
 #   template_name = "paginas/bispos.html"


#class SecretariosView(TemplateView):
 #   template_name = "paginas/secretarios.html"

#class CargosView(TemplateView):
 #   template_name = "paginas/cargos.html"

#class FrequenciasView(TemplateView):
 #   template_name = "paginas/frequencias.html"

#class PatrimoniosView(TemplateView):
 #   template_name = "paginas/patrimonios.html"
