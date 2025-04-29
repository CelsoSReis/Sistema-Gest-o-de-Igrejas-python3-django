from django.db import models
from django.contrib.auth.models import User
from plataformaigreja.models import Membros


class Igreja(models.Model):
    nome_igreja = models.CharField(max_length=255, verbose_name="Nome da Igreja", default="Igreja")
    endereco = models.TextField(verbose_name="Endereço")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(verbose_name="E-mail")
    logo = models.ImageField(upload_to="logos_igreja/", blank=True, null=True, verbose_name="Logo da Igreja")
    fundo_carteirinha = models.ImageField(upload_to="fundos_carteirinha/", blank=True, null=True, verbose_name="Fundo da Carteirinha")
    nome = models.CharField(max_length=255, verbose_name="Nome do Pastor")
    secretario = models.CharField(max_length=255, verbose_name="Nome do Secretário")
    tesoureiro = models.CharField(max_length=255, verbose_name="Nome do Tesoureiro")
    

    pastor = models.ForeignKey(
            User, 
            on_delete=models.CASCADE
        )
    def __str__(self):
        return self.nome
