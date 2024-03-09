from django.views.generic.edit import CreateView, UpdateView
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
    template_name = 'cadastros/formtesoureiro.html'
    success_url = reverse_lazy('cadastrar-tesoureiro')

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
    template_name = 'cadastros/formtesoureiro.html'
    success_url = reverse_lazy('cadastrar-tesoureiro')

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