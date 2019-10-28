from django.shortcuts import render
from django.http import HttpResponse
from .forms import LancamentoAvaliacaoForm
from .models import Colaborador, TipoPonto, LancamentoAvaliacao
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    qtd_avaliacoes = LancamentoAvaliacao.objects.filter(colaborador = colaborador.id).count()
    print('qtd_avaliacoes ', qtd_avaliacoes)

    pontuaca_atual = colaborador.pontuacao
    print('pontuaca_atual' ,  pontuaca_atual)

    maxcoins_atual = colaborador.pontuacao
    print('maxcoins_atual', maxcoins_atual)

    data = {
        'colaborador': colaborador,
        'qtd_avaliacoes': qtd_avaliacoes,
        'pontuaca_atual': pontuaca_atual,
        'maxcoins_atual': maxcoins_atual
    }

    return render(request, 'app_maxliga/home.html', data)


@login_required
def base(request):
    return render(request, 'base.html')


@login_required
def lista_avaliacoes(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    data = {
        'colaborador': colaborador
    }

    return render(request, 'app_maxliga/lista_avaliacoes.html', data)


@login_required
def lancamento_pontuacao(request):

    # Recupera o ID do usuáio autenticado
    user = request.user.id
    print('Usuário logado', user)

    # Recupera a instancia do funcionário buscando pelo o usuário logado
    colaborador = Colaborador.objects.get(usuario=user)
    print('Id Colaborador logado = ', colaborador.id)


    if request.method == 'POST':
        form = LancamentoAvaliacaoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            print('Id user colaborador selecionado', post.colaborador.usuario.id)
            print('Id colaborador selecionado', post.colaborador.id)
            print('Qtd pontos colaborador selecionado', post.colaborador.pontuacao)
            print(post.tipo_ponto.qtd_ponto)

    form = LancamentoAvaliacaoForm
    return render(request, 'app_maxliga/nova_avaliacao.html', {'form': form, 'colaborador': colaborador})