from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/usuarios/login')
def dizimos(request):
    if request.method == "GET":
        #busca membros do pastor logado
        #membros = Membros.objects.filter(pastor=request.user)
        #{'membros': membros} dicionário para atribuir a chave 'membros' os dados do banco de dados
        return render(request, 'dizimos.html')