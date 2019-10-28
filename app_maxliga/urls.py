from django.urls import path
from .views import lancamento_pontuacao, home


urlpatterns = [
        path('', home),
    path('novo/', lancamento_pontuacao, name='novo'),
]
