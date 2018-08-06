from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout
from weCheck import models
from django.http import JsonResponse
from HTML5project import settings
import base64
import os
from django.contrib.auth import authenticate



def login(request):
    error = []
    if request.is_ajax() and request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        userlogin = models.user.objects.filter(username=username)
        if user is not None:
            if check_password(password, userlogin.passwd):
                token = base64.b32encode(os.urandom(20))
                models.userToken.userTokenObject(username,token)
                request.session['token'] = token
                request.session['username'] = username
                request.session['SESSION_KEY'] = user._meta.pk.value_to_string(user)
                return JsonResponse({
                                     'status':200,
                                    })
            else:
                error.append('WRONG password')
        else:
            error.append('USER not exist')
    else:
        error.append('WRONG request method')
    return JsonResponse({
                            'status':202,
                            'message':error
                                        })





def logout(request):

    logout(request)

    return JsonResponse({
        'status': 200,
    })


def register(request):
    error = []
    if request.is_ajax() and request.method == 'POST':
        username = request.POST['username']
        if models.user.objects.filter(username=username) is None:

            passwd = make_password(request.POST['password'])
            name = request.POST['name']
            img = request.FILES['profile']
            userType = request.POST['userType']
            profile = settings.STATIC_URL+'weCheck/'+username+'.jpg'

            with open(os.path.join(settings.STATIC_ROOT,'weCheck/img'+username+'.jpg'),'wb') as f:
                f.write(img)

            models.user.userObject(username,passwd,name,profile,userType)

            return JsonResponse({
                                 'status':200,
                                            })
        else:
            error.append('REAPEAT of username')
    else:
        error.append('WRONG request method')
    return JsonResponse({
        'status':202,
        'message':error,
    })

def user(request):
    error = []
    if request.is_ajax() and request.method == 'POST':


def group(request):
    pass

def grouplist(request):
    pass

def groupadd(request):
    pass


def groupjoin(request):
    pass


def groupquit(request):
    pass


def groupupdate(request):
    pass


def groupdelete(request):
    pass


def checkstatus(request):
    pass


def checkcheck(request):
    pass


def checkenable(request):
    pass


def checkdisable(request):
    pass


def schedule(request):
    pass


def scheduleadd(request):
    pass


def scheduleupdate(request):
    pass


def scheduledelete(request):
    pass

