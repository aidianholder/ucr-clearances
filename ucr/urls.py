"""ucr urls config"""

from django.conf.urls import url

from . import views

app_name = 'ucr'
urlpatterns = [
    url(r'^(?P<ori>WA[0-9]{5})/(?P<year>[0-9]{4})/$', views.single_year, name='single_year_ori'),
    url(r'^(?P<lea>[A-Z_\']+)/(?P<year>[0-9]{4})/$', views.single_year, name='single_year_lea'),
    url(r'^(?P<lea>[A-Z_\']+)/(?P<startyear>[0-9]{4})/(?P<endyear>[0-9]{4})/$', views.multi_year, name='multi_year_lea'),
    url(r'^(?P<lea>[A-Z_\']+)/(?P<startyear>[0-9]{4})/(?P<endyear>[0-9]{4})/(?P<crime>[a-z_]+)/$', views.multi_year, name='multi_year_lea_crime'),
    url(r'^(?P<ori>WA[0-9]{5})/(?P<startyear>[0-9]{4})/(?P<endyear>[0-9]{4})/$', views.multi_year, name='multi_year_ori'),
    url(r'^(?P<ori>WA[0-9]{5})/(?P<startyear>[0-9]{4})/(?P<endyear>[0-9]{4})/(?P<crime>[a-z_]+)/$', views.multi_year,
        name='multi_year_ori_crime')
]