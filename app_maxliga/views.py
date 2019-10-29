from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Colaborador, TipoPonto, LancamentoAvaliacao, Liga
from .forms import LancamentoAvaliacaoForm, TipoPontoForm, LigaForm
from django.contrib.auth.decorators import login_required, permission_required


@login_required
def home(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    qtd_avaliacoes = LancamentoAvaliacao.objects.filter(colaborador = colaborador.id).count()
    print('qtd_avaliacoes', qtd_avaliacoes)

    qtd_avaliacoes_realizadas = LancamentoAvaliacao.objects.filter(avaliador=colaborador.id).count()
    print('qtd_avaliacoes_realizadas', qtd_avaliacoes_realizadas)

    pontuaca_atual = colaborador.pontuacao
    print('pontuaca_atual' , pontuaca_atual)

    maxcoins_atual = colaborador.pontuacao
    print('maxcoins_atual', maxcoins_atual)

    data = {
        'colaborador': colaborador,
        'qtd_avaliacoes': qtd_avaliacoes,
        'pontuaca_atual': pontuaca_atual,
        'maxcoins_atual': maxcoins_atual,
        'qtd_avaliacoes_realizadas': qtd_avaliacoes_realizadas
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
def nova_avaliacao(request):

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


@login_required
def lista_tipo_ponto(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    tipo_ponto = TipoPonto.objects.all()

    print(tipo_ponto)

    data = {
        'colaborador': colaborador,
        'tipo_ponto': tipo_ponto
    }

    return render(request, 'app_maxliga/lista_tipo_ponto.html', data)


@login_required
def cadastro_tipo_ponto(request):
    form = TipoPontoForm

    # Recupera o ID do usuáio autenticado
    user = request.user.id
    print('Usuário logado', user)

    # Recupera a instancia do funcionário buscando pelo o usuário logado
    colaborador = Colaborador.objects.get(usuario=user)
    print('Id Colaborador logado = ', colaborador.id)

    if request.method == 'POST':
        form = TipoPontoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_tipo_ponto')

        else:
            form = TipoPontoForm
    return render(request, 'app_maxliga/cadastro_tipo_ponto.html', {'form': form, 'colaborador': colaborador})


@login_required
def lista_liga(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    liga = Liga.objects.all()

    print(liga)

    data = {
        'colaborador': colaborador,
        'liga': liga
    }
    return render(request, 'app_maxliga/lista_liga.html', data)


@login_required
def cadastro_liga(request):
    form = LigaForm

    # Recupera o ID do usuáio autenticado
    user = request.user.id
    print('Usuário logado', user)

    # Recupera a instancia do funcionário buscando pelo o usuário logado
    colaborador = Colaborador.objects.get(usuario=user)
    print('Id Colaborador logado = ', colaborador.id)

    if request.method == 'POST':
        form = LigaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_liga')

        else:
            form = LigaForm
    return render(request, 'app_maxliga/cadastro_liga.html', {'form': form, 'colaborador': colaborador})


@login_required
def lista_colaboradores(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    colaboradores = Colaborador.objects.all()

    print(colaboradores)

    data = {
        'colaborador': colaborador,
        'colaboradores': colaboradores
    }
    return render(request, 'app_maxliga/lista_colaboradores.html', data)