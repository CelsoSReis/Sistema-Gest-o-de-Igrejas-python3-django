from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            # Mensagem de erro
            pass
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')



#from django.shortcuts import render, redirect
#from django.views.generic import TemplateView
#from django.contrib.auth import authenticate, login, logout

# Create your views here.

# classe PaginaInicial extends TemplateView

#def PaginaInicial(request):
 #   return render(request, 'paginas/index.html')

#def SobreView(request):
 #   return render(request, 'paginas/sobre.html')

#def HomeView(request):
 #   return render(request, 'contas/home.html')

#def login_view(request):
 #   if request.method == 'POST':
  #      username = request.POST['username']
   ##    user = authenticate(request, username=username, password=password)
     #   if user is not None:
      #      login(request, user)
       #     return redirect('home')
       # else:
        #    # Mensagem de erro de login inválido
         #   return render(request, 'login.html', {'error': 'Login inválido'})
    #return render(request, 'login.html')

#def logout_view(request):
 #   logout(request)
  #  return redirect('login')