from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Mensagem de erro
            pass
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

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


#class SobreView(TemplateView):
#    template_name = "paginas/sobre.html"

#class HomeView(TemplateView):
 #   template_name = "paginas/home.html"

#class PastoresView(TemplateView):
 #   template_name = "paginas/pastores.html"

#class UsuariosView(TemplateView):
 #   template_name = "paginas/usuarios.html"

#class IgrejasView(TemplateView):
 #   template_name = "paginas/igrejas.html"

#class BisposView(TemplateView):
 #   template_name = "paginas/bispos.html"

#class TesoureirosView(TemplateView):
 #   template_name = "paginas/tesoureiros.html"

#class SecretariosView(TemplateView):
 #   template_name = "paginas/secretarios.html"

#class CargosView(TemplateView):
 #   template_name = "paginas/cargos.html"

#class FrequenciasView(TemplateView):
 #   template_name = "paginas/frequencias.html"

#class PatrimoniosView(TemplateView):
 #   template_name = "paginas/patrimonios.html"
