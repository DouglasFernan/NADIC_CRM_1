from django.contrib import admin
from .models import Produto, Venda, Faturamento

# Register your models here.

admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Faturamento)
