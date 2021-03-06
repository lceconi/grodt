# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='professor',
        ),
        migrations.AddField(
            model_name='empresa',
            name='integrantes',
            field=models.ManyToManyField(to='go.Usuario'),
        ),
        migrations.AddField(
            model_name='turma',
            name='data_fim',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Encerramento'),
        ),
        migrations.AddField(
            model_name='turma',
            name='data_inicio',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de In\xedcio'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='nota',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
