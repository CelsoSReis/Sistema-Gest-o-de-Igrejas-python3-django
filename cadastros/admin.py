from django.contrib import admin

# Importar as classes
from .models import PastorPresidente, Pastores, Tesoureiro, Secretarios, Igrejas, Cargos, Membros

# Register your models here.
admin.site.register(PastorPresidente)
admin.site.register(Pastores)
admin.site.register(Tesoureiro)
admin.site.register(Secretarios)
admin.site.register(Igrejas)
admin.site.register(Cargos)
admin.site.register(Membros)