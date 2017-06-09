from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.db.models import F
from jxweb import config

from blog import ajax
import random

# Create your views here.

def index(request):
    # canvas_num = random.randrange(1, 8)
    # canvas = 'canvas' + str(canvas_num)

    template_values = {
        
    }
    # response = render(request, 'core/'+canvas+'.html', template_values)
    response = render(request, 'core/index.html', template_values)
    return response
def login(request):
    template_values = {
        'frame': 'frame.html',
        'config': config
    }
    response = render(request, 'core/login.html', template_values)
    return response