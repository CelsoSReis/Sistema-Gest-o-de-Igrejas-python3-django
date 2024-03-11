from django.views.generic.edit import CreateView, UpdateView, DeleteView
##import listas view
from django.views.generic.list import ListView
# import models
from .models import PastorPresidente, Pastores, Tesoureiro, Secretarios, Igrejas, Cargos, Membros
# import redirecionamnto
from django.urls import reverse_lazy
# Create your views here.
class PastorPresidenteCreate(CreateView):
    model = PastorPresidente
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formpastorpre.html'
    success_url = reverse_lazy('bispos')

class SecretariosCreate(CreateView):
    model = Secretarios
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formsecretarios.html'
    success_url = reverse_lazy('cadastrar-secretario')

class TesoureiroCreate(CreateView):
    model = Tesoureiro
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-tesoureiro')

class PastoresCreate(CreateView):
    model = Pastores
    fields = ['nome','cpf','endereco','email','data_nascimento','telefone']
    template_name = 'cadastros/formpastores.html'
    success_url = reverse_lazy('cadastrar-pastores')

class IgrejasCreate(CreateView):
    model = Igrejas
    fields = ['nome','endereco','email','telefone', 'pastores']
    template_name = 'cadastros/formigrejas.html'
    success_url = reverse_lazy('cadastrar-igrejas')

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
    template_name = 'cadastros/formsecretarios.html'
    success_url = reverse_lazy('cadastrar-secretario')

class TesoureiroUpdate(UpdateView):
    model = Tesoureiro
    fields = ['nome','cpf','endereco','email','telefone']
    template_name = 'cadastros/formcadastro.html'
    success_url = reverse_lazy('listar-tesoureiro')

class PastoresUpdate(UpdateView):
    model = Pastores
    fields = ['nome','cpf','endereco','email','data_nascimento','telefone']
    template_name = 'cadastros/formpastores.html'
    success_url = reverse_lazy('cadastrar-pastores')

class IgrejasUpdate(UpdateView):
    model = Igrejas
    fields = ['nome','endereco','email','telefone', 'pastores']
    template_name = 'cadastros/formigrejas.html'
    success_url = reverse_lazy('cadastrar-igrejas')

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
    template_name = 'cadastros/formsecretarios.html'
    success_url = reverse_lazy('cadastrar-secretario')

class TesoureiroDelete(DeleteView):
    model = Tesoureiro
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-tesoureiro')

class PastoresDelete(DeleteView):
    model = Pastores
    template_name = 'cadastros/formpastores.html'
    success_url = reverse_lazy('cadastrar-pastores')

class IgrejasDelete(DeleteView):
    model = Igrejas
    template_name = 'cadastros/formigrejas.html'
    success_url = reverse_lazy('cadastrar-igrejas')

class CargoDelete(DeleteView):
    model = Cargos
    template_name = 'cadastros/formcargos.html'
    success_url = reverse_lazy('cadastrar-cargos')

class MembrosDelete(DeleteView):
    model = Membros
    template_name = 'cadastros/formmembros.html'
    success_url = reverse_lazy('cadastrar-membros')



############## LISTAS VIEW ###################
    
class PastorPresidenteList(ListView):
    model = PastorPresidente
    template_name = 'cadastros/formpastorpre.html'
    success_url = reverse_lazy('bispos')

class SecretariosList(ListView):
    model = Secretarios
    template_name = 'cadastros/formsecretarios.html'
    success_url = reverse_lazy('cadastrar-secretario')

class TesoureiroList(ListView):
    model = Tesoureiro
    template_name = 'cadastros/listas/formtesoureiro.html'
    

class PastoresList(ListView):
    model = Pastores
    template_name = 'cadastros/formpastores.html'
    success_url = reverse_lazy('cadastrar-pastores')

class IgrejasList(ListView):
    model = Igrejas
    template_name = 'cadastros/formigrejas.html'
    success_url = reverse_lazy('cadastrar-igrejas')

class CargoList(ListView):
    model = Cargos
    template_name = 'cadastros/formcargos.html'
    success_url = reverse_lazy('cadastrar-cargos')

class MembrosList(ListView):
    model = Membros
    template_name = 'cadastros/formmembros.html'
    success_url = reverse_lazy('cadastrar-membros')
