from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Colaborador, TipoPonto, LancamentoAvaliacao, Liga, Departamento
from .forms import LancamentoAvaliacaoForm, TipoPontoForm, LigaForm, ColaboradorForm, DepartamentoForm
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

    avaliacoes = LancamentoAvaliacao.objects.all()

    data = {
        'colaborador': colaborador,
        'avaliacoes': avaliacoes
    }

    return render(request, 'app_maxliga/lista_avaliacoes.html', data)


@login_required
def cadastrar_avaliacao(request):

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

            colaborador_avaliado = Colaborador.objects.get(id=post.colaborador.id)
            print('colaborador_avaliado', colaborador_avaliado)

            colaborador_avaliado.pontuacao += post.tipo_ponto.qtd_ponto
            colaborador_avaliado.save()

            post.avaliador = colaborador

            post.save()
            return redirect('lista_avaliacoes')


    form = LancamentoAvaliacaoForm

    data = {
        'form': form,
        'colaborador': colaborador
    }

    return render(request, 'app_maxliga/nova_avaliacao.html', data)


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

    ligas = Liga.objects.all()

    print(ligas)

    data = {
        'colaborador': colaborador,
        'ligas': ligas
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


@login_required
def cadastro_colaborador(request):
    form = ColaboradorForm

    # Recupera o ID do usuáio autenticado
    user = request.user.id
    print('Usuário logado', user)

    # Recupera a instancia do funcionário buscando pelo o usuário logado
    colaborador = Colaborador.objects.get(usuario=user)
    print('Id Colaborador logado = ', colaborador.id)

    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_liga')

        else:
            form = ColaboradorForm
    return render(request, 'app_maxliga/cadastro_colaborador.html', {'form': form, 'colaborador': colaborador})


@login_required
def lista_departamentos(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    departamentos = Departamento.objects.all()

    print(departamentos)

    data = {
        'colaborador': colaborador,
        'departamentos': departamentos
    }
    return render(request, 'app_maxliga/lista_departamentos.html', data)


def cadastro_departamento(request):
    form = DepartamentoForm

    # Recupera o ID do usuáio autenticado
    user = request.user.id
    print('Usuário logado', user)

    # Recupera a instancia do funcionário buscando pelo o usuário logado
    colaborador = Colaborador.objects.get(usuario=user)
    print('Id Colaborador logado = ', colaborador.id)

    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_liga')

        else:
            form = DepartamentoForm
    return render(request, 'app_maxliga/cadastro_departamento.html', {'form': form, 'colaborador': colaborador})