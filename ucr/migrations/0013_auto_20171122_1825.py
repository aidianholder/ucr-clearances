# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucr', '0012_auto_20171122_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentsclearances',
            name='property',
            field=models.PositiveIntegerField(),
        ),
    ]
