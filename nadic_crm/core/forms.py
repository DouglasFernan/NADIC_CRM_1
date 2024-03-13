from django import forms
from .models import Produto, Venda, Faturamento


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'quantidade_estoque', 'preco']


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['produto', 'quantidade']


class FaturamentoForm(forms.ModelForm):
    class Meta:
        model = Faturamento
        fields = ['valor_total']
