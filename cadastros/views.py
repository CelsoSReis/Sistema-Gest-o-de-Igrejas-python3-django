from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView
##import listas view
from django.views.generic.list import ListView
# import models
from .models import PastorPresidente, Pastores, Tesoureiro, Secretarios, Igrejas, Cargos, Membros
# import redirecionamnto
from django.urls import reverse_lazy
# Create your views here.
from django.shortcuts import render


class PastorPresidenteCreate(CreateView):
    model = PastorPresidente
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formpastorpre.html'
    success_url = reverse_lazy('bispos')


class SecretariosCreate(CreateView):
    model = Secretarios
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-secretario')

class TesoureiroCreate(CreateView):
    model = Tesoureiro
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-tesoureiro')

class PastoresCreate(CreateView):
    model = Pastores
    fields = ['nome','cpf','endereco','email','data_nascimento','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-pastores')

class IgrejasCreate(CreateView):
    model = Igrejas
    fields = ['nome','endereco','email','telefone', 'pastores']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-igrejas')

class CargoCreate(CreateView):
    model = Cargos
    fields = ['nome']
    template_name = 'cadastros/formcargos.html'
    success_url = reverse_lazy('cadastrar-cargos')

class MembrosCreate(CreateView):
    model = Membros
    fields = ['nome','cpf','data_nascimento','data_batismo','endereco','email','telefone','cargos' ]
    template_name = 'cadastros/formmembros.html'
    success_url = reverse_lazy('cadastrar-membros')



######### update #########
    
class PastorPresidenteUpdate(UpdateView):
    model = PastorPresidente
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formpastorpre.html'
    success_url = reverse_lazy('bispos')

class SecretariosUpdate(UpdateView):
    model = Secretarios
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-secretario')

class TesoureiroUpdate(UpdateView):
    model = Tesoureiro
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-tesoureiro')

class PastoresUpdate(UpdateView):
    model = Pastores
    fields = ['nome','cpf','endereco','email','data_nascimento','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-pastores')

class IgrejasUpdate(UpdateView):
    model = Igrejas
    fields = ['nome','endereco','email','telefone', 'pastores']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-igrejas')

class CargoUpdate(UpdateView):
    model = Cargos
    fields = ['nome']
    template_name = 'cadastros/formcargos.html'
    success_url = reverse_lazy('cadastrar-cargos')

class MembrosUpdate(UpdateView):
    model = Membros
    fields = ['nome','cpf','data_nascimento','data_batismo','endereco','email','telefone','cargos' ]
    template_name = 'cadastros/formmembros.html'
    success_url = reverse_lazy('cadastrar-membros')

############## DELETE VIEW ###################
    
class PastorPresidenteDelete(DeleteView):
    model = PastorPresidente
    template_name = 'cadastros/formpastorpre.html'
    success_url = reverse_lazy('bispos')

class SecretariosDelete(DeleteView):
    model = Secretarios
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-secretario')

class TesoureiroDelete(DeleteView):
    model = Tesoureiro
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-tesoureiro')

class PastoresDelete(DeleteView):
    model = Pastores
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-pastores')

class IgrejasDelete(DeleteView):
    model = Igrejas
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-igrejas')

class CargoDelete(DeleteView):
    model = Cargos
    template_name = 'cadastros/formcargos.html'
    success_url = reverse_lazy('cadastrar-cargos')

class MembrosDelete(DeleteView):
    model = Membros
    template_name = 'cadastros/formmembros.html'
    success_url = reverse_lazy('cadastrar-membros')



############## LISTAS VIEW ###################
@login_required    
def SecretariosList(request):
    secretarios = Secretarios.objects.all()
    contexto = {'secretarios': secretarios}
    return render(request, 'cadastros/listas/listasecretarios.html', contexto)

class PastorPresidenteList(ListView):
    model = PastorPresidente
    template_name = 'cadastros/formpastorpre.html'
    success_url = reverse_lazy('bispos')

@login_required    
def TesoureiroList(request):
    tesoureiro = Tesoureiro.objects.all()
    contexto = {'tesoureiro': tesoureiro}
    return render(request, 'cadastros/listas/formtesoureiro.html', contexto)
    
@login_required    
def PastoresList(request):
    pastores = Pastores.objects.all()
    contexto = {'pastores': pastores}
    return render(request, 'cadastros/listas/listapastores.html', contexto)

@login_required    
def IgrejasList(request):
    igrejas = Igrejas.objects.all()
    contexto = {'igrejas': igrejas}
    return render(request, 'cadastros/listas/listaigrejas.html', contexto)

@login_required    
def CargoList(request):
    cargos = Cargos.objects.all()
    contexto = {'cargos': cargos}
    return render(request, 'cadastros/listas/listacargo.html', contexto)

#class CargoList(ListView):
 #   cargos = Cargos.objects.all()
  #  template_name = 'cadastros/formcargos.html'
   # success_url = reverse_lazy('cadastrar-cargos')

class MembrosList(ListView):
    model = Membros
    template_name = 'cadastros/formmembros.html'
    success_url = reverse_lazy('cadastrar-membros')
