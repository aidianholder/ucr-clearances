# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ucr', '0003_aggregaterates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidents15', models.IntegerField(blank=True, null=True)),
                ('incidents14', models.IntegerField(blank=True, null=True)),
                ('incidents13', models.IntegerField(blank=True, null=True)),
                ('incidents12', models.IntegerField(blank=True, null=True)),
                ('incidents11', models.IntegerField(blank=True, null=True)),
                ('incidents10', models.IntegerField(blank=True, null=True)),
                ('clearances15', models.IntegerField(blank=True, null=True)),
                ('clearances14', models.IntegerField(blank=True, null=True)),
                ('clearances13', models.IntegerField(blank=True, null=True)),
                ('clearances12', models.IntegerField(blank=True, null=True)),
                ('clearances11', models.IntegerField(blank=True, null=True)),
                ('clearances10', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Burglary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidents15', models.IntegerField(blank=True, null=True)),
                ('incidents14', models.IntegerField(blank=True, null=True)),
                ('incidents13', models.IntegerField(blank=True, null=True)),
                ('incidents12', models.IntegerField(blank=True, null=True)),
                ('incidents11', models.IntegerField(blank=True, null=True)),
                ('incidents10', models.IntegerField(blank=True, null=True)),
                ('clearances15', models.IntegerField(blank=True, null=True)),
                ('clearances14', models.IntegerField(blank=True, null=True)),
                ('clearances13', models.IntegerField(blank=True, null=True)),
                ('clearances12', models.IntegerField(blank=True, null=True)),
                ('clearances11', models.IntegerField(blank=True, null=True)),
                ('clearances10', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GTA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidents15', models.IntegerField(blank=True, null=True)),
                ('incidents14', models.IntegerField(blank=True, null=True)),
                ('incidents13', models.IntegerField(blank=True, null=True)),
                ('incidents12', models.IntegerField(blank=True, null=True)),
                ('incidents11', models.IntegerField(blank=True, null=True)),
                ('incidents10', models.IntegerField(blank=True, null=True)),
                ('clearances15', models.IntegerField(blank=True, null=True)),
                ('clearances14', models.IntegerField(blank=True, null=True)),
                ('clearances13', models.IntegerField(blank=True, null=True)),
                ('clearances12', models.IntegerField(blank=True, null=True)),
                ('clearances11', models.IntegerField(blank=True, null=True)),
                ('clearances10', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Larceny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidents15', models.IntegerField(blank=True, null=True)),
                ('incidents14', models.IntegerField(blank=True, null=True)),
                ('incidents13', models.IntegerField(blank=True, null=True)),
                ('incidents12', models.IntegerField(blank=True, null=True)),
                ('incidents11', models.IntegerField(blank=True, null=True)),
                ('incidents10', models.IntegerField(blank=True, null=True)),
                ('clearances15', models.IntegerField(blank=True, null=True)),
                ('clearances14', models.IntegerField(blank=True, null=True)),
                ('clearances13', models.IntegerField(blank=True, null=True)),
                ('clearances12', models.IntegerField(blank=True, null=True)),
                ('clearances11', models.IntegerField(blank=True, null=True)),
                ('clearances10', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Murder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidents15', models.IntegerField(blank=True, null=True)),
                ('incidents14', models.IntegerField(blank=True, null=True)),
                ('incidents13', models.IntegerField(blank=True, null=True)),
                ('incidents12', models.IntegerField(blank=True, null=True)),
                ('incidents11', models.IntegerField(blank=True, null=True)),
                ('incidents10', models.IntegerField(blank=True, null=True)),
                ('clearances15', models.IntegerField(blank=True, null=True)),
                ('clearances14', models.IntegerField(blank=True, null=True)),
                ('clearances13', models.IntegerField(blank=True, null=True)),
                ('clearances12', models.IntegerField(blank=True, null=True)),
                ('clearances11', models.IntegerField(blank=True, null=True)),
                ('clearances10', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PopGroupNames',
            fields=[
                ('pop_group', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=26)),
                ('group_classification', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='PopGroupRates',
            fields=[
                ('pop_group', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('murder2015', models.DecimalField(decimal_places=2, max_digits=5)),
                ('murder2014', models.DecimalField(decimal_places=2, max_digits=5)),
                ('murder2013', models.DecimalField(decimal_places=2, max_digits=5)),
                ('murder2012', models.DecimalField(decimal_places=2, max_digits=5)),
                ('murder2011', models.DecimalField(decimal_places=2, max_digits=5)),
                ('murder2010', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rape2015', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rape2014', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rape2013', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rape2012', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rape2011', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rape2010', models.DecimalField(decimal_places=2, max_digits=5)),
                ('robbery2015', models.DecimalField(decimal_places=2, max_digits=5)),
                ('robbery2014', models.DecimalField(decimal_places=2, max_digits=5)),
                ('robbery2013', models.DecimalField(decimal_places=2, max_digits=5)),
                ('robbery2012', models.DecimalField(decimal_places=2, max_digits=5)),
                ('robbery2011', models.DecimalField(decimal_places=2, max_digits=5)),
                ('robbery2010', models.DecimalField(decimal_places=2, max_digits=5)),
                ('assault2015', models.DecimalField(decimal_places=2, max_digits=5)),
                ('assault2014', models.DecimalField(decimal_places=2, max_digits=5)),
                ('assault2013', models.DecimalField(decimal_places=2, max_digits=5)),
                ('assault2012', models.DecimalField(decimal_places=2, max_digits=5)),
                ('assault2011', models.DecimalField(decimal_places=2, max_digits=5)),
                ('assault2010', models.DecimalField(decimal_places=2, max_digits=5)),
                ('burglary2015', models.DecimalField(decimal_places=2, max_digits=5)),
                ('burglary2014', models.DecimalField(decimal_places=2, max_digits=5)),
                ('burglary2013', models.DecimalField(decimal_places=2, max_digits=5)),
                ('burglary2012', models.DecimalField(decimal_places=2, max_digits=5)),
                ('burglary2011', models.DecimalField(decimal_places=2, max_digits=5)),
                ('burglary2010', models.DecimalField(decimal_places=2, max_digits=5)),
                ('larceny2015', models.DecimalField(decimal_places=2, max_digits=5)),
                ('larceny2014', models.DecimalField(decimal_places=2, max_digits=5)),
                ('larceny2013', models.DecimalField(decimal_places=2, max_digits=5)),
                ('larceny2012', models.DecimalField(decimal_places=2, max_digits=5)),
                ('larceny2011', models.DecimalField(decimal_places=2, max_digits=5)),
                ('larceny2010', models.DecimalField(decimal_places=2, max_digits=5)),
                ('GTA2015', models.DecimalField(decimal_places=2, max_digits=5)),
                ('GTA2014', models.DecimalField(decimal_places=2, max_digits=5)),
                ('GTA2013', models.DecimalField(decimal_places=2, max_digits=5)),
                ('GTA2012', models.DecimalField(decimal_places=2, max_digits=5)),
                ('GTA2011', models.DecimalField(decimal_places=2, max_digits=5)),
                ('GTA2010', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Rape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidents15', models.IntegerField(blank=True, null=True)),
                ('incidents14', models.IntegerField(blank=True, null=True)),
                ('incidents13', models.IntegerField(blank=True, null=True)),
                ('incidents12', models.IntegerField(blank=True, null=True)),
                ('incidents11', models.IntegerField(blank=True, null=True)),
                ('incidents10', models.IntegerField(blank=True, null=True)),
                ('clearances15', models.IntegerField(blank=True, null=True)),
                ('clearances14', models.IntegerField(blank=True, null=True)),
                ('clearances13', models.IntegerField(blank=True, null=True)),
                ('clearances12', models.IntegerField(blank=True, null=True)),
                ('clearances11', models.IntegerField(blank=True, null=True)),
                ('clearances10', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Robbery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidents15', models.IntegerField(blank=True, null=True)),
                ('incidents14', models.IntegerField(blank=True, null=True)),
                ('incidents13', models.IntegerField(blank=True, null=True)),
                ('incidents12', models.IntegerField(blank=True, null=True)),
                ('incidents11', models.IntegerField(blank=True, null=True)),
                ('incidents10', models.IntegerField(blank=True, null=True)),
                ('clearances15', models.IntegerField(blank=True, null=True)),
                ('clearances14', models.IntegerField(blank=True, null=True)),
                ('clearances13', models.IntegerField(blank=True, null=True)),
                ('clearances12', models.IntegerField(blank=True, null=True)),
                ('clearances11', models.IntegerField(blank=True, null=True)),
                ('clearances10', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='aggregaterates',
            name='ori',
        ),
        migrations.RemoveField(
            model_name='crime2012',
            name='ori',
        ),
        migrations.RemoveField(
            model_name='crime2013',
            name='ori',
        ),
        migrations.RemoveField(
            model_name='crime2014',
            name='ori',
        ),
        migrations.RemoveField(
            model_name='crime2015',
            name='ori',
        ),
        migrations.RemoveField(
            model_name='crime2016',
            name='ori',
        ),
        migrations.DeleteModel(
            name='GroupRates2012',
        ),
        migrations.DeleteModel(
            name='GroupRates2013',
        ),
        migrations.DeleteModel(
            name='GroupRates2014',
        ),
        migrations.DeleteModel(
            name='GroupRates2015',
        ),
        migrations.DeleteModel(
            name='GroupRates2016',
        ),
        migrations.AddField(
            model_name='agency',
            name='agency_group',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='covered_by',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='msa',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='agency',
            name='pop10',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='agency',
            name='pop11',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='agency',
            name='pop12',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='agency',
            name='pop13',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='agency',
            name='pop14',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='agency',
            name='pop15',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='agency',
            name='county',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='agency',
            name='department',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='agency',
            name='ori',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='AggregateRates',
        ),
        migrations.DeleteModel(
            name='Crime2012',
        ),
        migrations.DeleteModel(
            name='Crime2013',
        ),
        migrations.DeleteModel(
            name='Crime2014',
        ),
        migrations.DeleteModel(
            name='Crime2015',
        ),
        migrations.DeleteModel(
            name='Crime2016',
        ),
        migrations.AddField(
            model_name='robbery',
            name='ori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucr.Agency'),
        ),
        migrations.AddField(
            model_name='rape',
            name='ori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucr.Agency'),
        ),
        migrations.AddField(
            model_name='murder',
            name='ori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucr.Agency'),
        ),
        migrations.AddField(
            model_name='larceny',
            name='ori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucr.Agency'),
        ),
        migrations.AddField(
            model_name='gta',
            name='ori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucr.Agency'),
        ),
        migrations.AddField(
            model_name='burglary',
            name='ori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucr.Agency'),
        ),
        migrations.AddField(
            model_name='assault',
            name='ori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucr.Agency'),
        ),
    ]
