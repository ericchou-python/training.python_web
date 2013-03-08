from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', 'openshift.views.test', name='test'),
    url(r'^esmee/', include('esmee.urls')),
    url(r'inventory/', include('inventory.urls')),
    url(r'orderPipeline/', include('orderPipeline.urls')),
)
