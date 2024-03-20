from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# classe PaginaInicial extends TemplateView

def PaginaInicial(request):
    return render(request, 'paginas/index.html')

def SobreView(request):
    return render(request, 'paginas/sobre.html')

def HomeView(request):
    return render(request, 'paginas/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Mensagem de erro de login inválido
            return render(request, 'login.html', {'error': 'Login inválido'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

#class PaginaInicial(TemplateView):
#    template_name = "paginas/index.html"

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
