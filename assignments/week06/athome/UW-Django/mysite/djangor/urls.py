
from django.conf.urls import patterns, url
from django.http import HttpResponse
from django.views.generic import ListView
from djangor.models import Post

def stub(request, *args, **kwargs):
    return HttpResponse('This is the stub view', mimetype="text/plain")

urlpatterns = patterns('', 
    url(r'^$',
        ListView.as_view(
            model=Post,
            template_name="post/list.html"
        ), 
        name="post_list"),
    url(r'^(?P<pk>\d+)/$', 
        'djangor.views.page'), 
)

