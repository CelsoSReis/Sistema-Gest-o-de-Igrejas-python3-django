from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin

#from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
##import listas view
from django.views.generic.list import ListView
# import models
from .models import PastorPresidente, Pastores, Tesoureiro, Secretarios, Igrejas, Cargos, Membros
# import redirecionamnto
from django.urls import reverse_lazy
# Create your views here.
from django.shortcuts import render

###########cREATE##########

#@method_decorator(login_required, name='dispatch')
class PastorPresidenteCreate(CreateView):
    model = PastorPresidente
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formpastorpre.html'
    success_url = reverse_lazy('bispos')
#@method_decorator(login_required, name='dispatch')
class SecretariosCreate(CreateView):
    model = Secretarios
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-secretario')
#@method_decorator(login_required, name='dispatch')
class TesoureiroCreate(CreateView):
    model = Tesoureiro
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-tesoureiro')
#@method_decorator(login_required, name='dispatch')
class PastoresCreate(CreateView):
    model = Pastores
    fields = ['nome','cpf','endereco','email','data_nascimento','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-pastores')
#@method_decorator(login_required, name='dispatch')
class IgrejasCreate(CreateView):
    model = Igrejas
    fields = ['nome','endereco','email','telefone', 'pastores']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-igrejas')
#@method_decorator(login_required, name='dispatch')
class CargoCreate(CreateView):
    model = Cargos
    fields = ['nome']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-cargos')
#@method_decorator(login_required, name='dispatch')
class MembrosCreate(CreateView):
    model = Membros
    fields = ['nome','cpf','data_nascimento','data_batismo','endereco','email','telefone','cargos' ]
    template_name = 'cadastros/formmembros.html'
    success_url = reverse_lazy('cadastrar-membros')

######### update #########

#@method_decorator(login_required, name='dispatch')    
class PastorPresidenteUpdate(UpdateView):
    model = PastorPresidente
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formpastorpre.html'
    success_url = reverse_lazy('bispos')
#@method_decorator(login_required, name='dispatch')
class SecretariosUpdate(UpdateView):
    model = Secretarios
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-secretario')
#@method_decorator(login_required, name='dispatch')
class TesoureiroUpdate(UpdateView):
    model = Tesoureiro
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-tesoureiro')
#@method_decorator(login_required, name='dispatch')
class PastoresUpdate(UpdateView):
    model = Pastores
    fields = ['nome','cpf','endereco','email','data_nascimento','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-pastores')
#@method_decorator(login_required, name='dispatch')
class IgrejasUpdate(UpdateView):
    model = Igrejas
    fields = ['nome','endereco','email','telefone', 'pastores']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-igrejas')
#@method_decorator(login_required, name='dispatch')
class CargoUpdate(UpdateView):
    model = Cargos
    fields = ['nome']
    template_name = 'cadastros/formcargos.html'
    success_url = reverse_lazy('listar-cargos')
#@method_decorator(login_required, name='dispatch')
class MembrosUpdate(UpdateView):
    model = Membros
    fields = ['nome','cpf','data_nascimento','data_batismo','endereco','email','telefone','cargos' ]
    template_name = 'cadastros/formmembros.html'
    success_url = reverse_lazy('cadastrar-membros')

############## DELETE VIEW ###################

#@method_decorator(login_required, name='dispatch')    
class PastorPresidenteDelete(DeleteView):
    model = PastorPresidente
    template_name = 'cadastros/formpastorpre.html'
    success_url = reverse_lazy('bispos')
#@method_decorator(login_required, name='dispatch')
class SecretariosDelete(DeleteView):
    model = Secretarios
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-secretario')
#@method_decorator(login_required, name='dispatch')
class TesoureiroDelete(DeleteView):
    model = Tesoureiro
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-tesoureiro')
#@method_decorator(login_required, name='dispatch')
class PastoresDelete(DeleteView):
    model = Pastores
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-pastores')
#@method_decorator(login_required, name='dispatch')
class IgrejasDelete(DeleteView):
    model = Igrejas
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-igrejas')
#@method_decorator(login_required, name='dispatch')
class CargoDelete(DeleteView):
    model = Cargos
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-cargos')
#@method_decorator(login_required, name='dispatch')
class MembrosDelete(DeleteView):
    model = Membros
    template_name = 'cadastros/formmembros.html'
    success_url = reverse_lazy('cadastrar-membros')

############## LISTAS VIEW ###################

class SecretariosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Secretarios
    template_name = 'cadastros/listas/listasecretarios.html'



class PastorPresidenteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = PastorPresidente
    template_name = 'cadastros/formpastorpre.html'
    success_url = reverse_lazy('bispos')

class TesoureiroList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tesoureiro
    template_name = 'cadastros/listas/formtesoureiro.html'
#@login_required    
#def TesoureiroList(request):
   # tesoureiro = Tesoureiro.objects.all()
   # contexto = {'tesoureiro': tesoureiro}
   # return render(request, 'cadastros/listas/formtesoureiro.html', contexto)
class PastoresList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Pastores
    template_name = 'cadastros/listas/listapastores.html'

class IgrejasList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Igrejas
    template_name = 'cadastros/listas/listaigrejas.html'

class CargoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"usuarios"
    login_url = reverse_lazy('login')
    model = Cargos
    template_name = 'cadastros/listas/listacargo.html'

#@method_decorator(login_required, name='dispatch')
class MembrosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"usuarios"
    model = Membros
    template_name = 'cadastros/formmembros.html'
    success_url = reverse_lazy('cadastrar-membros')
