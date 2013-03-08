from django.shortcuts import render_to_response

def esmee(request, *args, **kwargs):
    return render_to_response('esmee/index.html')
