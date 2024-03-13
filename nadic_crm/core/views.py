# Importa funções para renderizar templates, redirecionar URLs e obter objetos do banco de dados ou retornar 404 se não encontrado.
from django.shortcuts import render, redirect, get_object_or_404

# Importa uma classe para redirecionar o usuário para uma nova URL.
from django.http import HttpResponseRedirect

# Importa funções para reverter nomes de URL para retornar um caminho para uma visualização.
from django.urls import reverse

# Importa funções e objetos para realizar operações no banco de dados, como somar valores e referenciar campos de modelo.
from django.db.models import Sum, F

# Importa funcionalidades para controlar transações de banco de dados.
from django.db import transaction

# Importa os formulários definidos no arquivo forms.py.
from .forms import ProdutoForm, VendaForm

# Importa os modelos de banco de dados definidos no arquivo models.py.
from .models import Produto, Venda

# Importa o módulo models para usar em consultas ao banco de dados.
from .models import models


def index(request):
    """
    Função de visualização para renderizar a página inicial.
    """
    return render(request, 'core/index.html')


def editar(request):
    """
    Função de visualização para renderizar a página de edição de produtos.
    """
    produtos = Produto.objects.all()  # Obtém todos os objetos Produto do banco de dados.
    # Renderiza o template editar.html, passando os produtos como contexto.
    return render(request, 'core/editar.html', {'produtos': produtos})


def update(request, id):
    """
    Função de visualização para atualizar informações de um produto.
    """
    produto = get_object_or_404(
        Produto, id=id)  # Obtém o objeto Produto com o id fornecido ou retorna um erro 404 se não encontrado.
    if request.method == 'POST':
        # Preenche o formulário com os dados da requisição e do objeto Produto.
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        # Cria um formulário com os dados do objeto Produto.
        form = ProdutoForm(instance=produto)
    # Renderiza o template update.html, passando o formulário como contexto.
    return render(request, 'core/update.html', {'form': form})


def sucesso(request):
    """
    Função de visualização para renderizar a página de sucesso.
    """
    return render(request, 'core/sucesso.html')


def cadastrar(request):
    """
    Função de visualização para cadastrar um novo produto.
    """
    if request.method == 'POST':
        # Preenche o formulário com os dados da requisição.
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = ProdutoForm()  # Cria um formulário em branco.
    # Renderiza o template cadastro.html, passando o formulário como contexto.
    return render(request, 'core/cadastro.html', {'form': form})


def deletar(request, id):
    """
    Função de visualização para deletar um produto.
    """
    produto = get_object_or_404(
        Produto, id=id)  # Obtém o objeto Produto com o id fornecido ou retorna um erro 404 se não encontrado.
    produto.delete()  # Exclui o objeto Produto do banco de dados.
    # Redireciona para a visualização editar.
    return HttpResponseRedirect(reverse('editar'))


@transaction.atomic
def add_venda(request):
    """
    Função de visualização para adicionar uma nova venda.
    """
    if request.method == 'POST':
        # Preenche o formulário com os dados da requisição.
        form = VendaForm(request.POST)
        if form.is_valid():
            # Salva os dados do formulário no banco de dados, sem efetivar a transação.
            venda = form.save(commit=False)
            produto = venda.produto
            quantidade_vendida = venda.quantidade
            # Verifica se há estoque suficiente para a venda.
            if produto.quantidade_estoque >= quantidade_vendida:
                produto.quantidade_estoque -= quantidade_vendida
                produto.save()
                venda.preco_venda = produto.preco
                venda.save()
                return redirect('sucesso')
            else:
                pass
    else:
        form = VendaForm()  # Cria um formulário em branco.
    # Renderiza o template add_venda.html, passando o formulário como contexto.
    return render(request, 'core/add_venda.html', {'form': form})


def faturamento(request):
    """
    Função de visualização para calcular e exibir o faturamento total.
    """
    total_faturamento = Venda.objects.aggregate(
        total_faturamento=Sum(F('preco_venda') * F('quantidade'),
                              output_field=models.DecimalField())
    )['total_faturamento']  # Calcula o faturamento total das vendas.

    vendas = Venda.objects.all()  # Obtém todas as vendas do banco de dados.

    # Renderiza o template faturamento.html, passando as vendas e o total de faturamento como contexto.
    return render(request, 'core/faturamento.html', {'vendas': vendas, 'total_faturamento': total_faturamento})
