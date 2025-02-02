from django.db import models
from django.contrib.auth.models import User

class Membros(models.Model):
    choices_sexo = (('F', 'Feminino'),
                    ('M', 'Masculino'))
    choices_cargo = (('A', 'Auxiliar'),
                     ('C', 'Congregado'),
                     ('Cr', 'Crianças'),
                     ('Da', 'Diaconisa'),
                     ('D', 'Diácono'),
                     ('E', 'Evangelista'),
                     ('J', 'Jovem'),
                     ('Mb', 'Membro'),
                     ('Mi', 'Missionário(a)'),
                     ('Pr', 'Pastor'),
                     ('P', 'Presbítero'))
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=19, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to="img_membros", null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    data_batismo = models.DateField(null=True, blank=True)
    cargo = models.CharField(max_length=2, choices=choices_cargo)
    pastor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome
