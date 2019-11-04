from django.urls import path
from .views import (
    cadastrar_avaliacao, home, base, lista_avaliacoes, lista_tipo_ponto,
    cadastro_tipo_ponto, lista_liga, cadastro_liga, lista_colaboradores,
    cadastro_colaborador, lista_departamentos, cadastro_departamento,
    minhas_avaliacoes, minhas_ligas, atualizar_avaliacao, excluir_avaliacao,
    atualizar_tipo_ponto, excluir_tipo_ponto, atualizar_liga, excluir_liga,
    atualizar_colaborador, excluir_colaborador, atualizar_departamento,
    excluir_departamento, ranking_liga
    )


urlpatterns = [
    path('', home, name='home'),
    path('base/', base),
    path('avaliacoes/', lista_avaliacoes, name='lista_avaliacoes'),
    path('avaliacoes/nova-avaliacao/', cadastrar_avaliacao, name='cadastrar_avaliacao'),
    path('avaliacoes/atualizar-avaliacao/<int:id>/', atualizar_avaliacao, name='atualizar_avaliacao'),
    path('avaliacoes/excluir-avaliacao/<int:id>/', excluir_avaliacao, name='excluir_avaliacao'),
    path('avaliacoes/minhas-avaliacoes/', minhas_avaliacoes, name='minhas_avaliacoes'),
    path('tipo-ponto/', lista_tipo_ponto, name='lista_tipo_ponto'),
    path('tipo-ponto/novo-tipo-ponto/', cadastro_tipo_ponto, name='cadastro_tipo_ponto'),
    path('tipo-ponto/atualizar-tipo-ponto/<int:id>/', atualizar_tipo_ponto, name='atualizar_tipo_ponto'),
    path('tipo-ponto/excluir-tipo-ponto/<int:id>/', excluir_tipo_ponto, name='excluir_tipo_ponto'),
    path('liga/', lista_liga, name='lista_liga'),
    path('liga/nova-liga/', cadastro_liga, name='cadastro_liga'),
    path('liga/atualizar-liga/<int:id>/', atualizar_liga, name='atualizar_liga'),
    path('liga/excluir-liga/<int:id>/', excluir_liga, name='excluir_liga'),
    path('colaboradores/', lista_colaboradores, name='lista_colaboradores'),
    path('colaboradores/novo-colaborador', cadastro_colaborador, name='cadastro_colaborador'),
    path('colaboradores/atualizar-colaborador/<int:id>/', atualizar_colaborador, name='atualizar_colaborador'),
    path('colaboradores/excluir-colaborador/<int:id>/', excluir_colaborador, name='excluir_colaborador'),
    path('departamentos/', lista_departamentos, name='lista_departamentos'),
    path('departamentos/novo-departamento/', cadastro_departamento, name='cadastro_departamento'),
    path('departamentos/atualizar-departamento/<int:id>/', atualizar_departamento, name='atualizar_departamento'),
    path('departamentos/excluir-departamento/<int:id>/', excluir_departamento, name='excluir_departamento'),
    path('minhas-ligas', minhas_ligas, name='minhas_ligas'),
    path('minhas-ligas/liga/<int:id>/', ranking_liga, name='ranking_liga'),
]
