from django.db import models
from django.contrib.auth.models import User


class Departamento(models.Model):
    nome = models.CharField('Nome do departamento', max_length=128)
    admin = models.BooleanField('Departamento Admin')

    def __str__(self):
        return self.nome


class Liga(models.Model):
    nome = models.CharField('Nome da liga', max_length=128)

    def __str__(self):
        return self.nome


class Colaborador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Usuário')
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cargo do colaborador')
    liga = models.ForeignKey(Liga, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Liga do colaborador')
    nome = models.CharField('Nome do funcionário', max_length=128)
    data_cadastro = models.DateTimeField('Data de criação', auto_now_add=True)
    pontuacao = models.FloatField('Pontuação colaborador', blank=True, default=0)
    maxcoins = models.FloatField('MaxCoins colaborador', blank=True, default=0)

    def __str__(self):
        return self.nome


class TipoPonto(models.Model):
    nome = models.CharField('Nome tipo de ponto', max_length=128)
    qtd_ponto = models.FloatField('Quantidade de pontos', blank=True, default=0)
    qtd_maxcoins = models.FloatField('Quantidade de MaxCoins', blank=True, default=0)
    data_cadastro = models.DateTimeField('Data de criação', auto_now_add=True)

    def __str__(self):
        return str(self.nome) + '   - Pontos: ' + str(self.qtd_ponto) + '   - MaxCoins: ' + str(self.qtd_maxcoins)


class LancamentoAvaliacao(models.Model):
    avaliador = models.ForeignKey(Colaborador, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Avaliador', related_name='avaliador_colaborador')
    colaborador = models.ForeignKey(Colaborador, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Colaborador', related_name='colaborador_colaborador')
    tipo_ponto = models.ForeignKey(TipoPonto, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tipo de ponto')
    descricao = models.TextField('Descrição do lançamento', max_length=300)
    data_lancamento = models.DateTimeField('Data de criação', auto_now_add=True)

    def __str__(self):
        return 'Colaborador: ' + str(self.colaborador) + '  - Data lançamento: ' + str(self.data_lancamento)
