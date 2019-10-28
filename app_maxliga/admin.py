from django.contrib import admin
from .models import (Departamento,
                     Liga,
                     Colaborador,
                     TipoPonto,
                     LancamentoAvaliacao)


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
    pass


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    readonly_fields = ('data_cadastro', 'pontuacao', 'maxcoins',)


@admin.register(TipoPonto)
class TipoPontoAdmin(admin.ModelAdmin):
    pass


@admin.register(LancamentoAvaliacao)
class LancamentoAvaliacaoAdmin(admin.ModelAdmin):
    readonly_fields = ('data_lancamento',)