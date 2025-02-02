from django.db import models
from django.contrib.auth.models import User
from plataformaigreja.models import Membros


class Dizimo(models.Model):
    membro = models.ForeignKey(Membros, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_dizimo = models.DateField(auto_now_add=True)  # Data do dízimo (preenchida automaticamente)

    def __str__(self):
        return f"Dízimo de {self.membro.nome} - R$ {self.valor}"
