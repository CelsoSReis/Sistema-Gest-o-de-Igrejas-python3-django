from django import forms
from .models import Membros

class MembrosForm(forms.ModelForm):
    class Meta:
        model = Membros
        fields = '__all__'  # Ou liste os campos que você quer incluir no formulário