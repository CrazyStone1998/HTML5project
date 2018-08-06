from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout
from weCheck import models
from django.http import JsonResponse
from HTML5project import settings
import base64
import os

from django.contrib.auth.decorators import login_required

def ajax_post_only(func):
    '''
    装饰器
    过滤掉非ajax post请求

    :param func:
    :return:
    '''
    def wrapper(request,*args,**kwargs):
        error = []
        if request.is_ajax() and request.method == 'POST':
            return func(request,*args,**kwargs)
        else:
            error.append('method error')
            return JsonResponse({
                'status':202,
                'message':error,
            })
    return wrapper


def authenticate(func):
    """
    装饰器
    验证用户登陆状态

    :param func:
    :return:
    """
    def wrapper(request,*args,**kwargs):
        error = []
        session_name = request.session.get('username')
        session_token = request.session.get('token')
        usercheck = models.user.objects.filter(username=session_name)
        if usercheck is not None:
            return func(request,*args,**kwargs)
        else:
            if usercheck is None:
                error.append('user off-line')
            elif usercheck.token == session_token:
                error.append('wrong request')
            return JsonResponse({
                'status': 202,
                'message':error,
            })
    return wrapper()


@ajax_post_only
def login(request):
    error = []
    username = request.POST.get('username')
    password = request.POST.get('password')
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
    return JsonResponse({
                            'status':202,
                            'message':error
                                        })





def logout(request):

    logout(request)

    return JsonResponse({
        'status': 200,
    })

@ajax_post_only
def register(request):
    error = []
    username = request.POST.get('username')
    if models.user.objects.filter(username=username) is None:
        passwd = make_password(request.POST.get('password'))
        name = request.POST.get('name')
        img = request.FILES.get('profile')
        userType = request.POST.get('userType')
        profile = settings.STATIC_URL+'weCheck/'+username+'.jpg'
        with open(os.path.join(settings.STATIC_ROOT,'weCheck/img'+username+'.jpg'),'wb') as f:
            f.write(img)
        models.user.userObject(username,passwd,name,profile,userType,)
        return JsonResponse({
                             'status':200,
                                        })
    else:
        error.append('REAPEAT of username')
    return JsonResponse({
        'status':202,
        'message':error,
    })

@authenticate
def user(request):
    error = []
    if request.method == 'POST':
        user = models.user.objects.filter(username=request.session.get('username'))
        user.username = request.POST.get('username',user.username)
        user.name = request.POST.get('name',user.name)
        img = request.FILES.get('profile')
        if img:
            with open(os.path.join(settings.STATIC_ROOT, 'weCheck/img' + user.username + '.jpg'), 'wb') as f:
                f.write(img)
            user.profile = settings.STATIC_URL + 'weCheck/' + user.username + '.jpg'
        user.save()
        return JsonResponse({
            'status':200,
            'message':'success'
        })


    elif request.method == 'GET':
        user = models.user.objects.filter(username=request.session.get('username'))
        if user is not None:
            username = user.username
            profile = user.profile
            name = user.name
            return JsonResponse({
                'status':200,
                'message':'success',
                'data':{
                    'username':username,
                    'profile':profile,
                    'name':name
                }
            })
        else:
            error.append('user is not exist')
            return JsonResponse({
                'status':202,
                'message':error
            })


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

