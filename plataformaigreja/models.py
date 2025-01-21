from django.db import models
from django.contrib.auth.models import User

class Membros(models.Model):
    choices_sexo = (('F', 'Feminino'),
                    ('M', 'Maculino'))
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    cpf = models.CharField(max_length=20)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    endereco = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="img_membros", null=True, blank=True)
    data_cadastro = models.DateField()
    data_nascimento = models.DateField()
    obs = models.TextField(max_length=200)
    data_batismo = models.DateField()
    cargo = models.CharField(max_length=50)
    ativo = models.CharField(max_length=6)
    pastor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
