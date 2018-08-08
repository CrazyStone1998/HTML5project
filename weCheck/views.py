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


@authenticate
def schedule(request):
    error = []
    if request.is_ajax() and request.method == 'GET':
        id = models.checkPlan.objects.filter(groupID=request.GET.get('id'))
        if id is None:
            error.append('there is no plan for this group')
            return JsonResponse({
                'status':202,
                'message':error,
            })
        else:
            data = []

            for e in id:
                data.append({
                    'planID':e.planID,
                    'startUpTime':e.startUpTime,
                    'duration':e.duration,
                    'enable':e.enable,
                    'repeat':e.repeat,
                })
            return JsonResponse({
                'status':200,
                'message':'OK',
                'data':data,
        })
    else:
        error.append('WRONG method')
        return JsonResponse({
            'status':202,
            'message':error,
        })

@authenticate
@ajax_post_only
def scheduleadd(request):

    groupID = request.POST.get('id')
    startUpTime = request.POST.get('startUpTime')
    duration = request.POST.get('duration')
    repeat = request.POST.get('repeat')
    enable = request.POST.get('enable')

    scheduleId = base64.b32encode(os.urandom(20))

    models.checkPlan.checkPlanObejct(scheduleId,groupID,startUpTime,duration,repeat,enable)

    return JsonResponse({
        'status':200,
        'message':'OK',
        'data':scheduleId

    })

@ajax_post_only
@authenticate
def scheduleupdate(request):
    error = []
    plan = models.checkPlan.objects.filter(scheduleId=request.POST.get('scheduleId'))
    if plan is None:
        error.append('plan is not exist')
    else:
        plan.startUpTime = request.POST.get('startUpTime',plan.startUpTime)
        plan.enable      = request.POST.get('enable',plan.enable)
        plan.duration    = request.POST.get('duration',plan.duration)
        plan.repeat      = request.POST.get('repeat',plan.repeat)

        plan.save()
        return JsonResponse({
            'status':200,
            'message':'OK'
        })
    return JsonResponse({
        'status':202,
        'message':error
    })

@authenticate
@ajax_post_only
def scheduledelete(request):
    error = []
    schedule = models.checkPlan.objects.filter(scheduleId = request.POST.get('scheduleId'))
    if schedule is None:
        error.append('schedule is not exist')
    else:
        schedule.delete()
        return JsonResponse({
            'status':200,
            'message':'OK',
        })
    return JsonResponse({
        'status':202,
        'message':error,
    })