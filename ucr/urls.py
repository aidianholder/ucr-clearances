"""ucr urls config"""

from django.conf.urls import url

from . import views

app_name = 'ucr'
urlpatterns = [
    url(r'^$', views.county, name='base'),
    url(r'^county/(?P<selected_county>[A-Z\s]+)$', views.department, name='department_select'),
    url(r'^(?P<ori>WA[A-Z0-9]{2}[0-9]{3})/$', views.multi_year, name='multi_year_ori'),
    url(r'^(?P<ori>WA[A-Z0-9]{2}[0-9]{3})/(?P<year>[0-9]{4})/$', views.single_year, name='single_year_ori'),
    url(r'^(?P<ori>WA[A-Z0-9]{2}[0-9]{3})/(?P<crime>[a-z_]+)/$', views.multi_year, name='multi_year_ori_crime'),
    url(r'^(?P<lea>[A-Z_\']+)/(?P<year>[0-9]{4})/$', views.single_year, name='single_year_lea'),
    url(r'^(?P<lea>[A-Z_\']+)/(?P<crime>[a-z_]+)/$', views.multi_year, name='multi_year_lea_crime')
]
