from django.db import models

# Create your models here.
class Igrejas(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    foto = models.ImageField()
    telefone = models.CharField(max_length=20, verbose_name='Telefone')