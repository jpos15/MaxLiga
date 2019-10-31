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

    maxcoins_atual = colaborador.maxcoins
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

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        avaliacoes = LancamentoAvaliacao.objects.all()

        data = {
            'colaborador': colaborador,
            'avaliacoes': avaliacoes
        }

        return render(request, 'app_maxliga/lista_avaliacoes.html', data)
    else:
        return redirect('home')


@login_required
def cadastrar_avaliacao(request):

    # Recupera o ID do usuáio autenticado
    user = request.user.id
    print('Usuário logado', user)

    # Recupera a instancia do funcionário buscando pelo o usuário logado
    colaborador = Colaborador.objects.get(usuario=user)
    print('Id Colaborador logado = ', colaborador.id)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        if request.method == 'POST':
            form = LancamentoAvaliacaoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)

                colaborador_avaliado = Colaborador.objects.get(id=post.colaborador.id)
                print('colaborador_avaliado', colaborador_avaliado)
                print('colaborador_avaliado.pontuacao', colaborador_avaliado.pontuacao)
                print('colaborador_avaliado.maxcoins', colaborador_avaliado.maxcoins)

                colaborador_avaliado.pontuacao += post.tipo_ponto.qtd_ponto
                colaborador_avaliado.save()

                colaborador_avaliado.maxcoins += post.tipo_ponto.qtd_maxcoins
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
    else:
        return redirect('home')


@login_required
def lista_tipo_ponto(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        tipo_ponto = TipoPonto.objects.all()

        print(tipo_ponto)

        data = {
            'colaborador': colaborador,
            'tipo_ponto': tipo_ponto
        }

        return render(request, 'app_maxliga/lista_tipo_ponto.html', data)
    return redirect('home')


@login_required
def cadastro_tipo_ponto(request):
    form = TipoPontoForm

    user = request.user.id

    colaborador = Colaborador.objects.get(usuario=user)

    #Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        if request.method == 'POST':
            form = TipoPontoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('lista_tipo_ponto')

            else:
                form = TipoPontoForm
        return render(request, 'app_maxliga/cadastro_tipo_ponto.html', {'form': form, 'colaborador': colaborador})
    else:
        return redirect('home')


@login_required
def lista_liga(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        ligas = Liga.objects.all()

        print(ligas)

        data = {
            'colaborador': colaborador,
            'ligas': ligas
        }
        return render(request, 'app_maxliga/lista_liga.html', data)
    else:
        return redirect('home')


@login_required
def cadastro_liga(request):
    form = LigaForm

    user = request.user.id

    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        if request.method == 'POST':
            form = LigaForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('lista_liga')

            else:
                form = LigaForm
        return render(request, 'app_maxliga/cadastro_liga.html', {'form': form, 'colaborador': colaborador})
    else:
        return redirect('home')


@login_required
def lista_colaboradores(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    colaboradores = Colaborador.objects.all()

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        data = {
            'colaborador': colaborador,
            'colaboradores': colaboradores
        }
        return render(request, 'app_maxliga/lista_colaboradores.html', data)
    else:
        return redirect('home')


@login_required
def cadastro_colaborador(request):
    form = ColaboradorForm

    user = request.user.id

    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        if request.method == 'POST':
            form = ColaboradorForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('lista_liga')

            else:
                form = ColaboradorForm
        return render(request, 'app_maxliga/cadastro_colaborador.html', {'form': form, 'colaborador': colaborador})
    else:
        return redirect('home')


@login_required
def lista_departamentos(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        departamentos = Departamento.objects.all()

        data = {
            'colaborador': colaborador,
            'departamentos': departamentos
        }
        return render(request, 'app_maxliga/lista_departamentos.html', data)
    else:
        return redirect('home')


@login_required
def cadastro_departamento(request):
    form = DepartamentoForm

    user = request.user.id

    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        if request.method == 'POST':
            form = DepartamentoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('lista_liga')

            else:
                form = DepartamentoForm
        return render(request, 'app_maxliga/cadastro_departamento.html', {'form': form, 'colaborador': colaborador})
    else:
        return redirect('home')


@login_required
def minhas_avaliacoes(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    avaliacoes = LancamentoAvaliacao.objects.filter(colaborador=colaborador)

    data = {
        'colaborador': colaborador,
        'avaliacoes': avaliacoes
    }

    return render(request, 'app_maxliga/minhas_avaliacoes.html', data)


@login_required
def minhas_ligas(request):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    ranking_liga = Colaborador.objects.filter(liga=1).order_by('-pontuacao')
    print(ranking_liga)

    data = {
        'colaborador': colaborador,
        'ranking_liga': ranking_liga
    }

    return render(request, 'app_maxliga/minhas_ligas.html', data)
