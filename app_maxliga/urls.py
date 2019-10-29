from django.urls import path
from .views import (
    cadastrar_avaliacao, home, base, lista_avaliacoes, lista_tipo_ponto,
    cadastro_tipo_ponto, lista_liga, cadastro_liga, lista_colaboradores,
    cadastro_colaborador, lista_departamentos, cadastro_departamento
    )


urlpatterns = [
    path('', home, name='home'),
    path('base/', base),
    path('avaliacoes/minhas-avaliacoes/', lista_avaliacoes, name='lista_avaliacoes'),
    path('avaliacoes/nova-avaliacao/', cadastrar_avaliacao, name='cadastrar_avaliacao'),
    path('tipo-ponto/', lista_tipo_ponto, name='lista_tipo_ponto'),
    path('tipo-ponto/novo-tipo-ponto/', cadastro_tipo_ponto, name='cadastro_tipo_ponto'),
    path('liga/', lista_liga, name='lista_liga'),
    path('liga/nova-liga/', cadastro_liga, name='cadastro_liga'),
    path('colaboradores/', lista_colaboradores, name='lista_colaboradores'),
    path('colaboradores/novo-colaborador', cadastro_colaborador, name='cadastro_colaborador'),
    path('departamentos/', lista_departamentos, name='lista_departamentos'),
    path('departamentos/novo-departamento/', cadastro_departamento, name='cadastro_departamento')
]
