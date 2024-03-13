from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade_estoque = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_venda = models.DateTimeField(auto_now_add=True)
    preco_venda = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)


class Faturamento(models.Model):
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
