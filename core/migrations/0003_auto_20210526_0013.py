# Generated by Django 3.1.7 on 2021-05-26 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210526_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_envio',
            field=models.DateTimeField(verbose_name='Data do Envio'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_pagamento',
            field=models.DateTimeField(verbose_name='Data do Pagamento'),
        ),
        migrations.AlterField(
            model_name='pedidoorigem',
            name='data_envio',
            field=models.DateTimeField(verbose_name='Data do Envio'),
        ),
        migrations.AlterField(
            model_name='pedidoorigem',
            name='data_pagamento',
            field=models.DateTimeField(verbose_name='Data do Pagamento'),
        ),
    ]
