# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0003_auto_20171112_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabalhoatividade',
            name='nota',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
