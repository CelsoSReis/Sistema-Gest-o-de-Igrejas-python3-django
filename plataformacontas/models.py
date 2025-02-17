from django.db import models
from django.contrib.auth.models import User

class ContaPagar(models.Model):
    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Paga'),
    )
    pastor = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário dono da conta
    fornecedor = models.CharField(max_length=255)  # Nome do fornecedor
    descricao = models.TextField()  # Descrição da conta
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da conta
    data_vencimento = models.DateField()  # Data de vencimento da conta
    quantidade_parcelas = models.PositiveIntegerField(default=1)  # Número de parcelas
    arquivo = models.FileField(upload_to="contas_a_pagar/", blank=True, null=True)  # Upload de arquivo
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)  # Padrão: Pendente

    def __str__(self):
        return f"{self.fornecedor} - {self.get_status_display()}"