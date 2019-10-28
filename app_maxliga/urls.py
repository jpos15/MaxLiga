from django.urls import path
from .views import lancamento_pontuacao, home, base, lista_avaliacoes


urlpatterns = [
    path('', home, name='home'),
    path('base/', base),
    path('avaliacoes/minhas-avaliacoes/', lista_avaliacoes, name='lista_avaliacoes'),
    path('avaliacoes/nova-avaliacao/', lancamento_pontuacao, name='nova_avaliacao'),
]
