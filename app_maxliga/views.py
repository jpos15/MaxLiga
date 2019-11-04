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
def atualizar_avaliacao(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        avaliacao = LancamentoAvaliacao.objects.get(id=id)
        form = LancamentoAvaliacaoForm(request.POST or None, instance=avaliacao)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_avaliacoes')

        data = {
            'colaborador': colaborador,
            'form': form,
            'avaliacao':avaliacao,
        }
        return render(request, 'app_maxliga/nova_avaliacao.html', data)
    return redirect('home')


@login_required
def excluir_avaliacao(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        avaliacao = LancamentoAvaliacao.objects.get(id=id)
        form = LancamentoAvaliacaoForm(request.POST or None, instance=avaliacao)

        if request.method == 'POST':

            colaborador_avaliado = Colaborador.objects.get(id=avaliacao.colaborador.id)

            colaborador_avaliado.pontuacao -= avaliacao.tipo_ponto.qtd_ponto
            colaborador_avaliado.save()

            colaborador_avaliado.maxcoins -= avaliacao.tipo_ponto.qtd_maxcoins
            colaborador_avaliado.save()

            avaliacao.delete()
            return redirect('lista_avaliacoes')

        data = {
            'colaborador': colaborador,
            'form': form,
            'avaliacao': avaliacao,
        }
        return render(request, 'app_maxliga/delete_avaliacao_confirm.html', data)
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

        data = {
            'form': form,
            'colaborador': colaborador
        }
        return render(request, 'app_maxliga/cadastro_tipo_ponto.html', data)
    else:
        return redirect('home')


@login_required
def atualizar_tipo_ponto(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        tipo_ponto = TipoPonto.objects.get(id=id)
        form = TipoPontoForm(request.POST or None, instance=tipo_ponto)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_tipo_ponto')

        data = {
            'colaborador': colaborador,
            'form': form,
            'tipo_ponto':tipo_ponto,
        }
        return render(request, 'app_maxliga/cadastro_tipo_ponto.html', data)
    return redirect('home')


@login_required
def excluir_tipo_ponto(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:
        tipo_ponto = TipoPonto.objects.get(id=id)

        if request.method == 'POST':
            tipo_ponto.delete()
            return redirect('lista_tipo_ponto')

        data = {
            'colaborador': colaborador,
            'tipo_ponto': tipo_ponto,
        }
        return render(request, 'app_maxliga/delete_tipo_ponto_confirm.html', data)
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
def atualizar_liga(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        liga = Liga.objects.get(id=id)
        form = LigaForm(request.POST or None, instance=liga)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_liga')

        data = {
            'colaborador': colaborador,
            'form': form,
            'liga':liga,
        }
        return render(request, 'app_maxliga/cadastro_liga.html', data)
    return redirect('home')


@login_required
def excluir_liga(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:
        liga = Liga.objects.get(id=id)

        if request.method == 'POST':
            liga.delete()
            return redirect('lista_liga')

        data = {
            'colaborador': colaborador,
            'liga': liga,
        }
        return render(request, 'app_maxliga/delete_liga_confirm.html', data)
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
                return redirect('lista_colaboradores')

            else:
                form = ColaboradorForm
        return render(request, 'app_maxliga/cadastro_colaborador.html', {'form': form, 'colaborador': colaborador})
    else:
        return redirect('home')


@login_required
def atualizar_colaborador(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        colaborador_colaborador = Colaborador.objects.get(id=id)
        form = ColaboradorForm(request.POST or None, instance=colaborador_colaborador)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_colaboradores')

        data = {
            'colaborador': colaborador,
            'form': form,
            'colaborador_colaborador':colaborador_colaborador,
        }
        return render(request, 'app_maxliga/cadastro_colaborador.html', data)
    return redirect('home')


@login_required
def excluir_colaborador(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:
        colaborador_colaborador = Colaborador.objects.get(id=id)

        if request.method == 'POST':
            colaborador_colaborador.delete()
            return redirect('lista_colaboradores')

        data = {
            'colaborador': colaborador,
            'colaborador_colaborador': colaborador_colaborador,
        }
        return render(request, 'app_maxliga/delete_colaborador_confirm.html', data)
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
                return redirect('lista_departamentos')

            else:
                form = DepartamentoForm
        return render(request, 'app_maxliga/cadastro_departamento.html', {'form': form, 'colaborador': colaborador})
    else:
        return redirect('home')


@login_required
def atualizar_departamento(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:

        departamento = Departamento.objects.get(id=id)
        form = DepartamentoForm(request.POST or None, instance=departamento)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_departamentos')

        data = {
            'colaborador': colaborador,
            'form': form,
            'departamento':departamento,
        }
        return render(request, 'app_maxliga/cadastro_departamento.html', data)
    return redirect('home')


@login_required
def excluir_departamento(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    # Para validar se o colaborador que está logado tem permissão de acessar a tela
    if colaborador.departamento.admin == True:
        departamento = Departamento.objects.get(id=id)

        if request.method == 'POST':
            departamento.delete()
            return redirect('lista_departamentos')

        data = {
            'colaborador': colaborador,
            'departamento': departamento,
        }
        return render(request, 'app_maxliga/delete_departamento_confirm.html', data)
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

    data = {
        'colaborador': colaborador
    }
    return render(request, 'app_maxliga/minhas_ligas.html', data)


@login_required
def ranking_liga(request, id):
    user = request.user.id
    colaborador = Colaborador.objects.get(usuario=user)

    ranking = Colaborador.objects.filter(liga=id).order_by('-pontuacao')
    lista_ranking = []
    cont = 1

    for posicao in ranking:
        lista_posicao = [cont, posicao.nome, posicao.pontuacao]
        lista_ranking.append(lista_posicao)
        cont +=1

    data = {
        'colaborador': colaborador,
        'ranking': ranking,
        'lista_ranking': lista_ranking
    }
    return render(request, 'app_maxliga/ranking_liga.html', data)
