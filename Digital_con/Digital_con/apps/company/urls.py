from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('Digital_con.apps.company.views',
	url(r'^list/$', 'company_listing', name='companies_list'),
    url(r'^detail/(?P<pk>\d+)/$', 'company_detail', name='company_detail'),
    url(r'^update/(?P<pk>\d+)/$', CompanyUpdate.as_view(), name='company_update'),
    url(r'^delete/(?P<pk>\d+)/$', CompanyDelete.as_view(), name='company_delete'),
    url(r'^companyform/$', CompanyForm.as_view(), name='company_form'),
)