from django.db import models
from django.contrib.auth.models import User

class Documento(models.Model):
    pastor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documentos')
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='documentos/')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
