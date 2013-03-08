from django.conf.urls import patterns, url
from django.http import HttpResponse

def stub(request, *args, **kwargs):
    return HttpResponse('This is the stub view', mimetype="text/plain")

urlpatterns = patterns('', 
    url(r'^$',
        'esmee.views.esmee', 
        ),
)

