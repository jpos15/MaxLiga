from django.shortcuts import render
from django.http import HttpResponse
from .forms import LancamentoPontuacaoForm
from .models import Colaborador, TipoPonto
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'base.html')


@login_required
def lancamento_pontuacao(request):

    # Recupera o ID do usuáio autenticado
    user = request.user.id
    print('Usuário logado', user)

    # Recupera a instancia do funcionário buscando pelo o usuário logado
    colaborador = Colaborador.objects.get(usuario=user)
    print('Id Colaborador logado = ', colaborador.id)


    if request.method == 'POST':
        form = LancamentoPontuacaoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            print('Id user colaborador selecionado', post.colaborador.usuario.id)
            print('Id colaborador selecionado', post.colaborador.id)
            print('Qtd pontos colaborador selecionado', post.colaborador.pontuacao)
            print(post.tipo_ponto.qtd_ponto)

    form = LancamentoPontuacaoForm
    return render(request, 'app_maxliga/form.html', {'form': form})