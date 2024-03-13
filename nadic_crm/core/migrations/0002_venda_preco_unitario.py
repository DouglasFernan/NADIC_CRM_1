# Generated by Django 5.0.2 on 2024-03-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="venda",
            name="preco_unitario",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
