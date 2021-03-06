# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('dataCriacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='cotacao.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('quantidade', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido', to='cotacao.Pedido'),
        ),
        migrations.AddField(
            model_name='item',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto', to='cotacao.Produto'),
        ),
    ]
