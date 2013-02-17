from django.shortcuts import render_to_response
from djangor.models import Post

# Create your views here.

def page(*args, **kwargs):
    for key in kwargs:
        page = kwargs[key]
    post = Post.objects.get(pk=page)
    return render_to_response('post/detail.html', {'title': post.title, 'body': post.body, 'date': post.created})
