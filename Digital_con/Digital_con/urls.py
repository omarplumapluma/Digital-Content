from django.conf.urls import include, url
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('Digital_con.apps.theme_base.urls')),
    url(r'^company/', include('Digital_con.apps.company.urls')),
    url(r'^company_content/', include('Digital_con.apps.company_content.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
        name='digital_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('index')}, name='digital_logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
