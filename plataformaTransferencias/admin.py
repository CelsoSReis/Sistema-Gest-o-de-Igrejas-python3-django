from django.contrib import admin
from .models import TransferenciaMembros

@admin.register(TransferenciaMembros)
class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('membro', 'igreja_origem', 'igreja_destino', 'data_transferencia')
    search_fields = ('membro__nome', 'igreja_origem', 'igreja_destino')
