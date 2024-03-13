# Generated by Django 5.0.2 on 2024-03-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_remove_venda_preco_unitario"),
    ]

    operations = [
        migrations.AddField(
            model_name="venda",
            name="preco_venda",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
