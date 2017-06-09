from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.db.models import Q
from core.models import *
import json

@csrf_exempt
def signin(request):
    error = None
    if not request.method == u'POST':
        error = "Request is not POST"

    if not error:
        username = request.POST.get('username', '')
        if not username:
            error = "username is required"
    if not error:
        password = request.POST.get('password', '')
        if not password:
            error = 'password is required'
    if not error:
        gender = request.POST.get('gender', '')
        if not gender:
            error = 'gender is required'
    if not error:
        email = request.POST.get('email', '')
        if not email:
            error = 'email is required'
    if not error:
        phonenum = request.POST.get('phonenum', '')
        if not phonenum:
            error = 'phonenum is required'
    if not error:
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        icon = request.POST.get('icon', '')
        description = request.POST.get('description', '')
        qq = request.POST.get('qq', '')
        wechat = request.POST.get('wechat', '')
        city = request.POST.get('city', '')
        birthday = request.POST.get('birthday', None)
    
    if not error:
        jxuser = JXUser.objects.filter(username=username)
        if jxuser:
            error = 'username is already exist'
    if not error:
        jxuser = JXUser.objects.filter(phonenum=phonenum)
        if jxuser:
            error = 'phonenum is already exist'
    if not error:
        JXUser(
            username = username,
            password = password,
            gender = gender,
            email = email,
            phonenum = phonenum,
            firstname = firstname,
            lastname = lastname,
            icon = icon,
            description = description,
            qq = qq,
            wechat = wechat,
            city = city,
            birthday = birthday,
            isblogger = 0,
            isstaff = 0,
            removed = 0,
        ).save()

    response = {}
    if error:
        response['error'] = error
    else:
        response['script'] = "signinDone(obj)"

    return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def login(request):
    error = None
    if not request.method == u'POST':
        error = "Request is not POST"
    if not error:
        username = request.POST.get('username', '')
        if not username:
            error = 'username is required'
    if not error:
        password = request.POST.get('password', '')
        if not password:
            error = 'password is required'
    if not error:
        try:
            jxuser = JXUser.objects.get(username=username)
        except ObjectDoesNotExist:
            error = 'username is not exist'
    if not error:
        if jxuser.password != password:
            error = 'Password error'

    response = {}
    if error:
        response['error'] = error
    else:
        response['jxuser'] = jxuser.serializeForJson()
        response['script'] = "loginDone(obj)"
        response['test'] = 'test'
    
    return HttpResponse(json.dumps(response), content_type="application/json")