from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout
from weCheck import models
from django.http import JsonResponse
from HTML5project import settings
import base64
import os
import time
import datetime
from django.db.models import F,Q
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

@authenticate
def checkstatus(request):
    user = models.user.objects.filter(username=request.session.get('username'))
    if user is not None:
        username=user.username
        nowdate=datetime.date.today()


        doneList=models.check.objects.filter(members__contains=username).filter(startDate__exact=nowdate).filter(results__contains=username)
        doneList_request=[]

        for done in doneList:
            s ={
                "groupId":done.groupID,
                "startUpTime":done.startUpTime
            }
            doneList_request.append(s)


        missedList= models.check.objects.filter(members__contains=username).filter(startDate__exact=nowdate).filter(enable__exact=False).filter(~Q(results__contains=username))
        missedList_request=[]
        for miss in missedList:
            s={
                "groupId": miss.groupID,
                "startUpTime": miss.startUpTime
            }
            missedList_request.append(s)

        openList=models.check.objects.filter(members__contains=username).filter(enable__exact=True)
        openList_request=[]
        for open in openList:
            s={
                "groupId": open.groupID,
                "startUpTime": open.startUpTime
            }
            openList_request.append(s)

        weekdate=str(nowdate.weekday()+1)
        belong_group=models.group.objects.filter(member__contains=username)#用户所属小组
        nowtime = str(time.strftime('%H:%M', time.localtime(time.time())))#将现在的时间格式化为hh:mm
        s1 = "20160916" + nowtime + ":00"#为了能与startuptime相比较 两者必须放到同一天 再转化为日期类型
        t1 = time.strptime(s1, '%Y%m%d%H:%M:%S')
        time1 = time.mktime(t1)

        futureList=models.checkPlan.objects.filter(groupID__in=belong_group).filter(enable__exact=True).filter(repeat__contains=weekdate)
        #以上future并没有一时间为条件过滤，因为时间是字符串类型，在上述语句中不好操作
        futureList_request=[]
        for future in futureList:
            #将startup time转化为日期类型方便比较
            check_time=future.startUpTime
            s2 = "20160916" + check_time + ":00"
            t2 = time.strptime(s2, '%Y%m%d%H:%M:%S')
            time2 = time.mktime(t2)
            if(time2>time1):
                s={
                    "groupId": future.groupID,
                    "startUpTime": future.startUpTime
                }
                futureList_request.append(s)

        return JsonResponse({
            "status": 200,
            "message": 'success',
            "data": {
                "done":doneList_request,
                "missed":missedList_request,
                "open":openList_request,
                "future":futureList_request
            }
        })


@ajax_post_only
def checkcheck(request):
    erro=[]
    user = models.user.objects.filter(username=request.session.get('username'))
    username=user.username
    groupid=request.POST.get('id')
    group=models.group.objects.filter(groupID__exact=groupid).filter(member__contains=username)
    check=models.check.objects.get(groupID=group)
    if group is not None:
        if check.enable is False:
            erro.append("The group is not checking")
            return JsonResponse({
                "status": 202,
                "message": erro
            })
        else:
            m = check.members
            m = m+","+username
            check.members = m
            check.save()
            return JsonResponse({
                "status": 200,
                "message": "ok"
            })

    else:
        erro.append("group is not exist or you are not the member of the group")
        return JsonResponse({
            "status": 202,
            "message": erro
        })

#开启即时签到
@ajax_post_only
def checkenable(request):
    erroe=[]
    user = models.user.objects.filter(username=request.session.get('username'))
    ownerID=user.username
    groupid = request.POST.get('id')
    group=models.group.objects.filter(groupID__exact=groupid).filter(owner__exact=ownerID)#查看该用户是否为该群组的所有者
    if group is not  None:#是该群组的所有者
        check=models.check.objects.filter(groupID__exact=group).filter(enable__exact=True)#查看该群组是否还在开启签到中，保证一个群组同一时间只能开启一次签到
        if check is None:#该群组没有处于签到中
            models.check.checkObject(groupid)#创建新的签到对象
            return JsonResponse({
                "status": 200,
                "message": 'ok'
            })
        else:#该群组上一次签到还没有结束
            erroe.append("the group is checking")
    else:#是该群组的所有者
        erroe.append("you are not the owner of the group or the group not exists")
        return JsonResponse({
            "status": 202,
            "message": erroe
        })


#结束即时签到
def checkdisable(request):
    erroe = []
    user = models.user.objects.filter(username=request.session.get('username'))
    ownerID = user.username
    groupid = request.POST.get('id')
    group = models.group.objects.filter(groupID__exact=groupid).filter(owner__exact=ownerID)
    if group is not None:
        check=models.check.objects.filter(groupID__exact=group).filter(enable__exact=True)#找到该群组正在进行的签到，接着结束他
        if check is not None:
            check.enable = False
            check.save()
            return JsonResponse({
                "status": 200,
                "message": "ok"
            })
        else:
            erroe.append("该群组没有正在进行的签到")
            return JsonResponse({
                "status": 202,
                "message": erroe
            })
    else:
        erroe.append("you are not the owner of the group or the group not exists")
        return JsonResponse({
            "status": 202,
            "message": erroe
        })





def schedule(request):
    erro=[]
    user = models.user.objects.filter(username=request.session.get('username'))
    username=user.username#获取该用户的用户名称
    groupid = request.POST.get('id')
    group = models.group.objects.filter(groupID__exact=groupid).filter(member__contains=username)#获取该群组，并且检查是否包含该用户
    if group is not None:
        planlist=models.checkPlan.objects.filter(groupID__exact=group)
        planlist_request=[]
        for plan in planlist:
            s={
                "scheduleId":plan.planID,
                "startUpTime":plan.startUpTime,
                "duration":plan.duration,
                "enable":plan.enable,
                "repeat":plan.repeat
            }
            planlist_request.append(s)
        return JsonResponse({
            "status": 200,
            "message": "ok",
            "data":planlist_request
        })
    else:
        erro.append("you are not the member of the group or the group is not exists")
        return JsonResponse({
            "status": 202,
            "message": erro
        })


@ajax_post_only
def scheduleadd(request):
    error=[]
    user = models.user.objects.filter(username=request.session.get('username'))

    username=user.useranme
    groupid = request.POST.get('id')
    group = models.group.objects.filter(groupID__exact=groupid).filter(owner__exact=username)
    duration = request.POST.get('duration')
    startUpTime = request.POST.get('startUpTime')
    repeat = request.POST.get('repeat')
    duration = request.POST.get('duration')
    enable = request.POST.get('enable')
    if group is not None:

        if enable is False:#计划关闭状态可以加入
            a=models.checkPlan.checkPlanObejct(groupid,startUpTime,duration,repeat,enable)
            return JsonResponse({
                "status": 200,
                "message": 'ok',
                "data":a.planID
            })

        else:#计划开启状态
            #查找与之相冲突的计划
            #先查找改组现在开启的计划
            checkList = models.checkPlan.objects.filter(groupID__exact=group).filter(enable__exact=True)#这是本群开启的其他计划
            flag = False#假设这些计划都不冲突
            #如果这些计划冲突必须满足点：1.有相同的周天 2.当前计划的开启时间+持续时间>原有计划的开始时间 或者原有计划的开始时间+持续时间>当前计划的开始时间
            weekday=repeat.split(",")
            for w in weekday:
                for che in checkList:
                    if(w in che.repeat):#条件一
                        #进行时间的计算
                        #矛盾关系是  -当前持续时间<当前开始时间-以有开始时间<已有持续时间
                        s1="20160916"+startUpTime+":00"
                        t1 = time.strptime(s1, '%Y%m%d%H:%M:%S')
                        time1 = time.mktime(t1)
                        s2="20160916"+che.startUpTime+":00"
                        t2 = time.strptime(s2, '%Y%m%d%H:%M:%S')
                        time2 = time.mktime(t2)
                        current_duration_second=duration*60*-1#负的当前计划持续的秒数
                        check_duration_second=che.duration*60
                        if(current_duration_second<=time1-time2<=check_duration_second):
                            flag = True#表示由计划与当前计划矛盾
                            break
                if(flag==True):
                    break
            if(flag==True):
                error.append("您当前为该群组设置的签到计划，与该群已有签到计划冲突")
                return JsonResponse({
                    "status": 202,
                    "message": error
                })
            else:#与计划没有冲突，查看与开启的签到有没有冲突
                nowdate = datetime.date.today()
                weekdate = str(nowdate.weekday() + 1)
                if weekdate in repeat:
                    check_thisday=models.check.objects.filter(enable__exact=True)
                    if check_thisday is not None:
                        nowtime=str(time.strftime('%H:%M', time.localtime(time.time())))
                        s1="20160916"+nowtime+":00"
                        t1 = time.strptime(s1, '%Y%m%d%H:%M:%S')
                        ti1=time.mktime(t1)
                        s2="20160916"+startUpTime+":00"
                        t2 = time.strptime(s2, '%Y%m%d%H:%M:%S')
                        ti2=time.mktime(t2)
                        if ti1>ti2 :
                            a = models.checkPlan.checkPlanObejct(groupid, startUpTime, duration, repeat, enable)
                            return  JsonResponse({
                                "status": 200,
                                "message": "ok",
                                "data": a.planID
                            })
                        else:
                            error.append("您当前为该群组设置的签到计划,与该群当前开启的签到可能存在冲突")
                            return  JsonResponse({
                                "status": 202,
                                "message":error
                            })



                    else:
                        a = models.checkPlan.checkPlanObejct(groupid, startUpTime, duration, repeat, enable)
                        return  JsonResponse({
                            "status":200,
                            "message":"ok",
                            "data":a.planID
                        })

                else:
                    a = models.checkPlan.checkPlanObejct(groupid, startUpTime, duration, repeat, enable)
                    return JsonResponse({
                        "status":200,
                        "message":"ok",
                        "data":a.planID
                    })




    else:
        error.append("you are not the owner of the group or the group is not exist")
        return JsonResponse({
            "status": 202,
            "message": error
        })


@ajax_post_only
def scheduleupdate(request):
    error = []
    user = models.user.objects.filter(username=request.session.get('username'))
    username = user.useranme
    scheduleId= request.POST.get('scheduleId')
    check_plan = models.checkPlan.objects.get(planID=scheduleId)
    groupId=request.POST.get('id',check_plan.group_ID)
    startUpTime = request.POST.get('startUpTime', check_plan.startUpTime)
    duration = request.POST.get('duration', check_plan.duration)
    repeat = request.POST.get('repeat', check_plan.repeat)
    enable = request.POST.get('enable', check_plan.enable)
    group = models.group.objects.filter(groupID__exact=groupId).filter(owner__exact=username)
    if group is not None:
        if enable is False:#计划修改为关闭状态可以修改
            check_plan.groupID=groupId
            check_plan.startUpTime=startUpTime
            check_plan.duration=duration
            check_plan.repeat=repeat
            check_plan.enable=enable
            check_plan.save()
            return JsonResponse({
                "status": 200,
                "message": 'ok',
            })

        else:#计划修改为开启状态
            #查找与之相冲突的计划
            #先查找改组现在开启的计划
            checkList = models.checkPlan.objects.filter(groupID__exact=group).filter(enable__exact=True)#这是本群开启的其他计划
            flag = False#假设这些计划都不冲突
            #如果这些计划冲突必须满足点：1.有相同的周天 2.当前计划的开启时间+持续时间>原有计划的开始时间 或者原有计划的开始时间+持续时间>当前计划的开始时间
            weekday=repeat.split(",")
            for w in weekday:
                for che in checkList:
                    if(w in che.repeat):#条件一
                        #进行时间的计算
                        #矛盾关系是  -当前持续时间<当前开始时间-以有开始时间<已有持续时间
                        s1="20160916"+startUpTime+":00"
                        t1 = time.strptime(s1, '%Y%m%d%H:%M:%S')
                        time1 = time.mktime(t1)
                        s2="20160916"+che.startUpTime+":00"
                        t2 = time.strptime(s2, '%Y%m%d%H:%M:%S')
                        time2 = time.mktime(t2)
                        current_duration_second=duration*60*-1#负的当前计划持续的秒数
                        check_duration_second=che.duration*60
                        if(current_duration_second<=time1-time2<=check_duration_second):
                            flag = True#表示由计划与当前计划矛盾
                            break
                if(flag==True):
                    break
            if(flag==True):
                error.append("您修改后的签到计划，与该群已有签到计划冲突")
                return JsonResponse({
                    "status": 202,
                    "message": error
                })
            else:#与计划没有冲突，查看与开启的签到有没有冲突
                nowdate = datetime.date.today()
                weekdate = str(nowdate.weekday() + 1)
                if weekdate in repeat:
                    check_thisday=models.check.objects.filter(enable__exact=True)
                    if check_thisday is not None:
                        nowtime=str(time.strftime('%H:%M', time.localtime(time.time())))
                        s1="20160916"+nowtime+":00"
                        t1 = time.strptime(s1, '%Y%m%d%H:%M:%S')
                        ti1=time.mktime(t1)
                        s2="20160916"+startUpTime+":00"
                        t2 = time.strptime(s2, '%Y%m%d%H:%M:%S')
                        ti2=time.mktime(t2)
                        if ti1>ti2 :
                            check_plan.groupID=groupId
                            check_plan.startUpTime=startUpTime
                            check_plan.duration=duration
                            check_plan.repeat=repeat
                            check_plan.enable=enable
                            check_plan.save()
                            return  JsonResponse({
                                "status": 200,
                                "message": "ok",
                            })
                        else:
                            error.append("您修改后的签到计划,与该群当前开启的签到可能存在冲突")
                            return  JsonResponse({
                                "status": 202,
                                "message":error
                            })



                    else:
                        check_plan.groupID=groupId
                        check_plan.startUpTime=startUpTime
                        check_plan.duration=duration
                        check_plan.enable=enable
                        check_plan.repeat=repeat
                        check_plan.save()
                        return  JsonResponse({
                            "status":200,
                            "message":"ok",
                        })

                else:
                    check_plan.groupID= groupId
                    check_plan.startUpTime=startUpTime
                    check_plan.duration=duration
                    check_plan.enable=enable
                    check_plan.repeat=repeat
                    check_plan.save()
                    return JsonResponse({
                        "status":200,
                        "message":"ok",
                    })

    else:
        error.append("you are not the owner of the group or the group is not exist")
        return JsonResponse({
            "status": 202,
            "message": error
        })





def scheduledelete(request):
    error=[]
    scheduleId = request.POST.get('scheduleId')
    check_plan = models.checkPlan.objects.filter(planID__exact=scheduleId)
    if check_plan is not None:
        check_plan.delete()
        return JsonResponse({
            "status":200,
            "message":"ok"
        })
    else:
        error.append("该签到计划不存在")
        return JsonResponse({
            "status":202,
            "message":error
        })


