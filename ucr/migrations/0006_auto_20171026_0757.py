# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucr', '0005_auto_20171026_0537'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountyClearances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=15)),
                ('year', models.PositiveSmallIntegerField()),
                ('homicide', models.PositiveSmallIntegerField()),
                ('rape', models.PositiveSmallIntegerField()),
                ('robbery', models.PositiveSmallIntegerField()),
                ('aggravated_assault', models.PositiveSmallIntegerField()),
                ('burglary', models.PositiveSmallIntegerField()),
                ('larceny', models.PositiveSmallIntegerField()),
                ('gta', models.PositiveSmallIntegerField()),
                ('clearance_homicide', models.PositiveIntegerField()),
                ('clearance_rape', models.PositiveSmallIntegerField()),
                ('clearance_robbery', models.PositiveSmallIntegerField()),
                ('clearance_aggravated_assault', models.PositiveSmallIntegerField()),
                ('clearance_burglary', models.PositiveSmallIntegerField()),
                ('clearance_larceny', models.PositiveSmallIntegerField()),
                ('clearance_gta', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='agency',
            name='county',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
