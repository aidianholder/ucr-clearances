# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ucr', '0002_auto_20170927_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='AggregateRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_violent_16', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='violent crime rate')),
                ('r_property_16', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='property crime rate')),
                ('r_violent_15', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='violent crime rate')),
                ('r_property_15', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='property crime rate')),
                ('r_violent_14', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='violent crime rate')),
                ('r_property_14', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='property crime rate')),
                ('r_violent_13', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='violent crime rate')),
                ('r_property_13', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='property crime rate')),
                ('r_violent_12', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='violent crime rate')),
                ('r_property_12', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='property crime rate')),
                ('ori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucr.Agency')),
            ],
        ),
    ]
