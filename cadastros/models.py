from django.db import models

# Create your models here.
#IGREJAS
class Igrejas(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    telefone = models.IntegerField(verbose_name='Telefone')
    def __str__(self): ##define método
        return "{} ({})".format(self.nome, self.endereco, self.email, self.telefone)

#CARGOS
class Cargos(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')

    def __str__(self): ##define método
        return "{} ({})".format(self.nome)

    
#MEMBROS
class Membros(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.IntegerField(verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    data_batismo = models.DateField(verbose_name='Data de Batismo')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    telefone = models.IntegerField(verbose_name='Telefone')
    
    cargos = models.ForeignKey(Cargos, on_delete=models.PROTECT)
    
    def __str__(self): ##define método
        return "{} ({})".format(self.nome, self.endereco, self.email, self.telefone, self.cargos.nome)