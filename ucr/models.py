# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Agency(models.Model):
    ori = models.CharField(max_length=7, primary_key=True)
    department = models.CharField(max_length=50)
    county = models.CharField(max_length=50, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return '%s' % (self.department)


@python_2_unicode_compatible
class IncidentsClearances(models.Model):
    ori = models.ForeignKey("Agency", on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    homicide = models.PositiveSmallIntegerField()
    rape = models.PositiveSmallIntegerField()
    robbery = models.PositiveSmallIntegerField()
    aggravated_assault = models.PositiveSmallIntegerField()
    burglary = models.PositiveSmallIntegerField()
    larceny = models.PositiveSmallIntegerField()
    gta = models.PositiveSmallIntegerField()
    violent = models.PositiveSmallIntegerField()
    property = models.PositiveIntegerField()
    clearance_homicide = models.PositiveIntegerField()
    clearance_rape = models.PositiveSmallIntegerField()
    clearance_robbery = models.PositiveSmallIntegerField()
    clearance_aggravated_assault = models.PositiveSmallIntegerField()
    clearance_burglary = models.PositiveSmallIntegerField()
    clearance_larceny = models.PositiveSmallIntegerField()
    clearance_gta = models.PositiveSmallIntegerField()
    clearance_violent = models.PositiveSmallIntegerField()
    clearance_property = models.PositiveSmallIntegerField()
    population = models.PositiveIntegerField()
    pop_group = models.PositiveIntegerField()

    def __str__(self):
        return '%s %s' % (self.ori.department, self.year)


@python_2_unicode_compatible
class GroupRates(models.Model):
    pop_group = models.PositiveIntegerField()
    year = models.PositiveSmallIntegerField()
    cl_violent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cl_property = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cl_homicide = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    cl_rape = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    cl_robbery = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    cl_aggravated_assault = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    cl_burglary = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    cl_larceny = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    cl_gta = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    r_violent = models.DecimalField(max_digits=6,decimal_places=1,default=0)
    r_property = models.DecimalField(max_digits=6,decimal_places=1,default=0)
    r_homicide = models.DecimalField(max_digits=6,decimal_places=1,default=0)
    r_rape = models.DecimalField(max_digits=6,decimal_places=1,default=0)
    r_robbery = models.DecimalField(max_digits=6,decimal_places=1,default=0)
    r_aggravated_assault = models.DecimalField(max_digits=6,decimal_places=1,default=0)
    r_burglary = models.DecimalField(max_digits=6,decimal_places=1,default=0)
    r_larceny = models.DecimalField(max_digits=6,decimal_places=1,default=0)
    r_gta = models.DecimalField(max_digits=6,decimal_places=1,default=0)


    def __str__(self):
        return '%s %s' % (self.pop_group, self.year)

