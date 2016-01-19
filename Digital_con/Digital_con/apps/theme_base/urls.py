from django.conf.urls import patterns, url

urlpatterns = patterns('Digital_con.apps.theme_base.views',
					 url(r'^$', 'index_view', name="index"),
					 )