from django import forms
from .models import LancamentoPontuacao


class LancamentoPontuacaoForm(forms.ModelForm):

    class Meta:
        model = LancamentoPontuacao
        fields = ('colaborador', 'tipo_ponto', 'descricao')