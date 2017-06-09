from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from jxweb import config


from blog import ajax


# Create your views here.

def detail(request, burl):
    
    template_values = {
        'frame': 'frame.html',
        'config': config,
    }
    response = render(request, 'blog/blog.html', template_values)
    return response