# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import *
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from .models import *


def single_year(request, year, lea=None, ori=None):
    if lea:
        lea_cleaned = lea.replace('_', ' ').upper()
        agency = Agency.objects.get(department=lea_cleaned)
    if ori:
        agency = Agency.objects.get(ori=ori)
        lea_cleaned = agency.department.replace('_', ' ').upper()
    try:
        agency_stats = IncidentsClearances.objects.filter(ori=agency.ori).get(year=year)
    except:
        return render(request, 'nodata.html')
    group_stats = GroupRates.objects.filter(pop_group = agency_stats.population).get(year=year)
    index_crimes = ['homicide', 'rape', 'robbery', 'aggravated_assault', 'burglary', 'larceny', 'gta']
    incidents = {}
    for crime in index_crimes:
        no_incidents = getattr(agency_stats, crime)
        try:
            r_incidents = (Decimal(no_incidents)/Decimal(agency_stats.pop_group)) * 100000
            r_incidents = r_incidents.quantize(Decimal('10.01'))
        except DivisionByZero or InvalidOperation:
            r_incidents = 'NA'
        no_clearances = getattr(agency_stats, "clearance_" + crime)
        try:
            clearance_rate = Decimal(no_clearances)/Decimal(no_incidents) * 100
            clearance_rate = clearance_rate.quantize(Decimal('10.01'))
        except:
            clearance_rate = 'NA'
        r_group = getattr(group_stats, "r_" + crime)
        group_clearance_rate = getattr(group_stats, "cl_" + crime)
        incidents[crime] = [no_incidents, r_incidents, r_group, no_clearances, clearance_rate, group_clearance_rate]
    context = {"jurisdiction":lea_cleaned, "year":year, "incidents":incidents}
    return render(request, 'single_year.html', context)


def multiple_year(request, startyear, endyear, lea=None, ori=None):
    years = range(int(startyear), int(endyear) + 1)
    if lea:
        lea_cleaned = lea.replace('_', ' ').upper()
        agency = Agency.objects.get(department=lea_cleaned)
    else:
        agency = Agency.objects.get(ori=ori)
        lea_cleaned = agency.department.replace('_', ' ').upper()
    try:
        agency_stats = IncidentsClearances.objects.filter(ori=agency.ori).filter(year__in=years)
    except:
        return render(request, 'nodata.html')
    years_reported = []
    for ucr in agency_stats:
        #years_reported.append(ucr.year)
        #sum and then calc rate for violent crime
        violent_crime = ucr.homicide + ucr.rape + ucr.robbery + ucr.aggravated_assault
        violent_crime_rate = (Decimal(violent_crime) / Decimal(ucr.pop_group)) * 100000
        violent_crime_rate = violent_crime_rate.quantize(Decimal('10.1'))
        violent_clearances = ucr.clearance_homicide + ucr.clearance_rape + ucr.clearance_robbery + ucr.clearance_aggravated_assault
        violent_clearance_rate = Decimal(violent_clearances)/Decimal(violent_crime) * 100
        violent_clearance_rate = violent_clearance_rate.quantize(Decimal('10.01'))
        property_crime = ucr.burglary + ucr.larceny + ucr.gta
        property_clearances = ucr.clearance_burglary + ucr.clearance_larceny + ucr.clearance_gta
        property_crime_rate = (Decimal(property_crime)/Decimal(ucr.pop_group)) * 100000
        property_crime_rate = property_crime_rate.quantize(Decimal('10.1'))
        property_clearance_rate = Decimal(property_clearances)/Decimal(property_crime) *100
        property_clearance_rate = property_clearance_rate.quantize(Decimal('10.01'))
        group_stats = GroupRates.objects.filter(year=ucr.year).get(pop_group=ucr.population)
        agency_stats = [ucr.year, {'avt': violent_crime, 'av': violent_crime_rate, 'avc': violent_clearance_rate, 'apt': property_crime, 'ap': property_crime_rate, 'apc': property_clearance_rate, 'gv':group_stats.r_violent, 'gvc':group_stats.cl_violent, 'gp':group_stats.r_property, 'gpc':group_stats.cl_property}]
        years_reported.append(agency_stats)
    context = {"jurisdiction":lea_cleaned, 'crime_stats':years_reported, 'year_list':years}
    return render(request, 'multi_year.html', context)


def multi_year(request, startyear, endyear, lea=None, ori=None, crime="violent"):
    years = range(int(startyear), int(endyear) + 1)
    if lea:
        lea_cleaned = lea.replace('_', ' ').upper()
        agency = Agency.objects.get(department = lea_cleaned)
    if ori:
        agency = Agency.objects.get(ori=ori)
        lea_cleaned = agency.department
    try:
        agency_stats = IncidentsClearances.objects.filter(ori=agency.ori).filter(year__in=years)
    except:
        return render(request, 'nodata.html')
    years_reported = []
    for ucr in agency_stats:
        year = ucr.year
        incidents = getattr(ucr, crime)
        clearances = getattr(ucr, "clearance_" + crime)
        tot_incidents = 0
        tot_clearances = 0
        crime_rate = (Decimal(incidents)/Decimal(ucr.pop_group)) * 100000
        crime_rate = crime_rate.quantize(Decimal('10.1'))
        try:
            clearance_rate = Decimal(clearances)/Decimal(incidents)
            clearance_rate = clearance_rate.quantize(Decimal('.0001'))
        except DivisionByZero or InvalidOperation:
            clearance_rate = None
        group_stats = GroupRates.objects.filter(year=year).get(pop_group=ucr.population)
        group_rate = getattr(group_stats, "r_" + crime)
        group_clearance_rate = getattr(group_stats, "cl_" + crime)
        if clearance_rate:
            chart_data = [year, clearance_rate, group_clearance_rate/100, crime_rate, group_rate]
            years_reported.append(chart_data)
    if crime == "violent" or "property":
        crime = crime + " crime"
    elif crime == "gta" or "GTA":
        crime = "vehicle theft"
    context = {'jurisdiction':lea_cleaned, 'crime':crime, 'crime_stats':years_reported, 'years':str(years[0]) + "-" + str(years[-1])}
    return render(request, 'chart.html', context)


"""        if crime == 'violent':
            crime = ucr.homicide + ucr.rape + ucr.robbery + ucr.aggravated_assault
        elif crime = 'property':
    for ucr in agency_stats:
        violent_crime = ucr.homicide + ucr.rape + ucr.robbery + ucr.aggravated_assault
        violent_clearances = ucr.clearance_homicide + ucr.clearance_rape + ucr.clearance_robbery + ucr.clearance_aggravated_assault
        violent_clearance_rate = Decimal(violent_clearances) / Decimal(violent_crime) * 100
        violent_clearance_rate = violent_clearance_rate.quantize(Decimal('10.01'))
        property_crime = ucr.burglary + ucr.larceny + ucr.gta
        property_clearances = ucr.clearance_burglary + ucr.clearance_larceny + ucr.clearance_gta
        property_clearance_rate = Decimal(property_clearances) / Decimal(property_crime) * 100
        property_clearance_rate = property_clearance_rate.quantize(Decimal('10.01'))"""


def crimes_and_clearances(request, county, lea=None, startyear='2005', endyear='2015'):
    if startyear == endyear:
        years = [int(startyear)]
    else:
        years = range(int(startyear), int(endyear) + 1)
    county_cleaned = county.replace('_', ' ').upper()
    if not lea:
        agencies = Agency.objects.filter(county=county_cleaned)
        jurisdiction = county_cleaned + " COUNTY"
    else:
        lea_cleaned = lea.replace('_', ' ').upper()
        agencies = Agency.objects.filter(department=lea_cleaned)
        jurisdiction = lea_cleaned
    cc = IncidentsClearances.objects.filter(ori__in=agencies).filter(year__in=years)
    index_crimes = ['homicide', 'rape', 'robbery', 'aggravated_assault', 'burglary', 'larceny', 'gta']
    incidents = {}
    for crime in index_crimes:
        #no_of_incidents = cc.aggregate(Sum(crime))[crime + '__sum']
        i = cc.aggregate(Sum(crime))
        t = crime + '__sum'
        tt = i[t]
        no_of_incidents = tt
        cl = "clearance_" + crime
        c = cc.aggregate(Sum(cl))
        ct = cl + '__sum'
        ctt = c[ct]
        no_of_clearances = ctt
        try:
            r = Decimal(no_of_clearances)/Decimal(no_of_incidents)
            r = r.quantize(Decimal('1.01'))
        except DivisionByZero or InvalidOperation:
            r = 'NA'
        incidents[crime] = [no_of_incidents, no_of_clearances, r]
    context = {'jurisdiction': jurisdiction, 'years':years, 'incidents': incidents}
    return render(request, 'details.html', context)




"""def agency_detail(request, county, department, startyear, endyear):
    department_cleaned = department.replace('_', ' ')
    department_cleaned = department_cleaned.upper()
    agency = Agency.objects.get(department=department_cleaned)
    if startyear == endyear:
        years = [int(startyear)]
    else:
        years = range(int(startyear), int(endyear))
    cc = IncidentsClearances.objects.filter(ori__in=agency).filter(year__in=years)
    
    context = {'agency': agency}
    return render(request, 'ucr/agency_detail.html', context)

    rates = {agency.ori.r_violent_16}
    data_years = [Crime2012, Crime2013, Crime2014, Crime2015, Crime2016]
    for year in data_years:
        c = agency.year_set.all()
    c_2016 = agency.crime2016_set.all()
    v_16 = c_2016.r_violent_crime
    p_16 = c_2016.r_property_crime
    c_2015 ="""