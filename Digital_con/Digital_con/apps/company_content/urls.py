from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('Digital_con.apps.company_content.views',
	url(r'^list/$', 'company_content_listing', name='companies_content_list'),
	url(r'^list-media/$', 'company_media_listing', name='companies_media_list'),
    url(r'^detail/(?P<pk>\d+)/$', 'company_content_detail', name='company_content_detail'),
    url(r'^update/(?P<pk>\d+)/$', CompanyContentUpdate.as_view(), name='company_content_update'),
    url(r'^delete/(?P<pk>\d+)/$', CompanyContentDelete.as_view(), name='company_content_delete'),
    url(r'^companycontentform/$', CompanyContentForm.as_view(), name='company_content_form'),
    url(r'^companymediaform/$', CompanyMediaForm.as_view(), name='company_media_form'),
)