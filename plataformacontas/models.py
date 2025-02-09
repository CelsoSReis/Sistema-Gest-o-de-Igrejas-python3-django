from django.db import models
from django.utils import timezone

class ContaPagar(models.Model):
    nome_fornecedor = models.CharField(max_length=255)
    descricao = models.TextField()
    data_vencimento = models.DateField()
    quantidade_parcelas = models.IntegerField()
    anexo = models.FileField(upload_to='contas_anexos/', blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nome_fornecedor} - {self.descricao[:20]}..."
