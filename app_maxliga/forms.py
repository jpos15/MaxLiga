from django import forms
from .models import LancamentoAvaliacao, TipoPonto, Liga, Colaborador, Departamento


class LancamentoAvaliacaoForm(forms.ModelForm):

    class Meta:
        model = LancamentoAvaliacao
        fields = ('colaborador', 'tipo_ponto', 'descricao',)
        widgets = {
            'colaborador': forms.Select(attrs={'class': 'form-control'}),
            'tipo_ponto': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }


class TipoPontoForm(forms.ModelForm):
    class Meta:
        model = TipoPonto
        fields = ('nome', 'qtd_ponto', 'qtd_maxcoins',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'qtd_ponto': forms.NumberInput(attrs={'class': 'form-control'}),
            'qtd_maxcoins': forms.NumberInput(attrs={'class': 'form-control'})
        }


class LigaForm(forms.ModelForm):
    class Meta:
        model = Liga
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ('usuario', 'nome', 'departamento', 'liga',)
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'liga': forms.Select(attrs={'class': 'form-control'})
        }


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('nome', 'admin')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'admin': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
        }