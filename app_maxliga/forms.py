from django import forms
from .models import LancamentoAvaliacao


class LancamentoAvaliacaoForm(forms.ModelForm):

    class Meta:
        model = LancamentoAvaliacao
        fields = ('colaborador', 'tipo_ponto', 'descricao')
        widgets = {
            'colaborador': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo_ponto': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }