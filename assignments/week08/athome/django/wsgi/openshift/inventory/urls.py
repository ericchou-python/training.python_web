from django.conf.urls import patterns, url
from django.http import HttpResponse

def stub(request, *args, **kwargs):
    return HttpResponse('This is the stub view', mimetype="text/plain")

urlpatterns = patterns('', 
    url(r'^$',
        stub, 
        ),
    url(r'^manufactures/$',
        'inventory.views.display_manufacture'),
    url(r'^manufactures/(.*)/$',
        'inventory.views.display_manu_inventory'),
    url(r'^search-manufacture/$', 'inventory.views.search_manufacture'),
    url(r'^search/$', 'inventory.views.search'),
    url(r'^add_manufacture/$', 'inventory.forms.add_manufacture'),
    url(r'^add_manufacture_submit/$', 'inventory.forms.add_manufacture_submit'),
)

