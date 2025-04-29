from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from igreja.models import Igreja
from plataformaigreja.models import Membros

class TransferenciaMembros(models.Model):
    membro = models.ForeignKey(Membros, on_delete=models.CASCADE, related_name='transferencias')
    igreja_origem = models.ForeignKey(Igreja, on_delete=models.SET_NULL, null=True, blank=True, related_name='transferencias_origem')
    igreja_destino = models.ForeignKey(Igreja, on_delete=models.SET_NULL, null=True, blank=True, related_name='transferencias_destino')
    data_transferencia = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Transferência de {self.membro} para {self.igreja_destino}'
class Transferencia(models.Model):
    membro = models.ForeignKey(Membros, on_delete=models.CASCADE)
    igreja_origem = models.ForeignKey('igreja.Igreja', related_name='igreja_origem', on_delete=models.CASCADE)
    igreja_destino = models.ForeignKey('igreja.Igreja', related_name='igreja_destino', on_delete=models.CASCADE)
    data_transferencia = models.DateTimeField(auto_now_add=True)