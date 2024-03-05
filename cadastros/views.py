from django.views.generic.edit import CreateView
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