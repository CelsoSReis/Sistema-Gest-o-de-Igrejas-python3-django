from django.db import models

# Create your models here.

# PASTOR PRESIDENTE
class PastorPresidente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=20, verbose_name='CPF')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    def __str__(self): ##define método
        return "{}".format(self.nome,self.cpf, self.endereco, self.email, self.telefone)
    
# TESOUREIRO
class Tesoureiro(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=20, verbose_name='CPF')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    def __str__(self): ##define método
        return "{}".format(self.nome,self.cpf, self.endereco, self.email, self.telefone)
    
# SECRETÁRIOS
class Secretarios(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=20, verbose_name='CPF')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    def __str__(self): ##define método
        return "{}".format(self.nome,self.cpf, self.endereco, self.email, self.telefone)
    
# PASTORES
class Pastores(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=20, verbose_name='CPF')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    def __str__(self): ##define método
        return "{}".format(self.nome,self.cpf, self.endereco, self.email, self.data_nascimento, self.telefone)

# IGREJAS
class Igrejas(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')

    pastores = models.ForeignKey(Pastores, on_delete=models.PROTECT)

    def __str__(self): ##define método
        return "{} ({})".format(self.nome, self.endereco, self.email, self.telefone, self.pastores.nome)

# CARGOS
class Cargos(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')

    def __str__(self): ##define método
        return "{} ()".format(self.nome)

    
#MEMBROS
class Membros(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=20, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    data_batismo = models.DateField(verbose_name='Data de Batismo')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    
    cargos = models.ForeignKey(Cargos, on_delete=models.PROTECT)
    
    def __str__(self): ##define método
        return "{} ({})".format(self.nome, self.endereco, self.email, self.telefone, self.cargos.nome)