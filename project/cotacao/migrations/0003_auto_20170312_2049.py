# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0002_auto_20170227_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='dataCriacao',
            field=models.DateField(auto_now_add=True),
        ),
    ]