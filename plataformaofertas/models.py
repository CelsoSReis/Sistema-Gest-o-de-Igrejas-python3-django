from django.db import models
from django.contrib.auth.models import User

class Oferta(models.Model):

    pastor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_oferta = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255, default="Oferta Diversa")  # Atualizado para "descrição"
    def __str__(self):
        return f"{self.descricao} - R$ {self.valor} ({self.data_oferta})"