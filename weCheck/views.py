#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from HTML5project import settings
from django.db.models import F,Q
from weCheck import models
from common.auth.userSystem import userSystem
from common.decorator.ajax_post_only import ajax_post_only
import os
import time
import datetime
import string,random

def imgRescource(request):
    '''
    # 获取用户 大脸照
    :param request:
    :return:
    '''
    path = settings.STATIC_ROOT+'/weCheck/img/'+request.path
    with open(path,'rb') as f:
        img = f.read()
    return HttpResponse(img, content_type='image/jpg')

@ajax_post_only
def login(request):
    '''
    登陆函数
    :param request:
    :return:
    '''

    # 获取用户 账户 和 密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 获取user对象
    user = userSystem(request)
    # user登陆 认证
    # 判定新用户登陆 顶替旧的用户
    if user.getUsername() != username:
        user.delCache()
        # 清理 session
        request.session.flush()

    error = user.authentication(username=username,password=password)
    # error为空 则登陆成功
    # error不为空 则登陆不成功
    if not error:
        return JsonResponse({
            'status':200,
            'message':'OK',
        })
    else:
        return JsonResponse({
                            'status':202,
                            'message':error
                                        })

@ajax_post_only
def logout(request):
    '''
    账号 登出
    :param request:
    :return:
    '''
    # 清理缓存
    user = userSystem(request)
    user.delCache()
    # 清理 session
    request.session.flush()

    return JsonResponse({
        'status': 200,
        'message':'OK',
    })


@ajax_post_only
def register(request):
    # 错误信息列表
    error = []
    # 后台获取并判断用户名和密码 是否为空
    username = request.POST.get('username')
    passwd = request.POST.get('password')
    if username is None or passwd is None:
        error.append('The username&passwd cannot be empty')
        # 获取并判断 用户名是否存在
    elif not models.user.objects.filter(Q(username=username)&Q(isDelete=False)).exists():

        passwd   = make_password(passwd)
        name     = request.POST.get('name')
        img      = request.FILES.get('profile')
        userType = request.POST.get('userType')
        profile  = settings.ICON_URL+''+username+'.jpg'
        # 将 用户 大脸照 写入 本地文件中
        imgPath  = os.path.join(settings.STATIC_ROOT,'weCheck','img',username+'.jpg')
        # 判断用户 大脸照 是否存在 若存在 重写
        if os.path.exists(imgPath):
            os.remove(imgPath)
        with open(imgPath,'wb+') as f:
            for chunk in img.chunks():
                f.write(chunk)
        # 调用 model类的 新建对象方法 存储用户对象
        models.user.userObject(username,passwd,name,profile,userType,)
        # 返回 json
        return JsonResponse({
                             'status':200,
                             'message':'OK'
                                        })
    else:
        error.append('Username already exists')
    return JsonResponse({
            'status':202,
            'message':error,
        })


def user_splitter(request,GET=None,POST=None):
    '''
    获取用户信息 分流器
    根据 request.method 分配方法
    GET:view.userGET
    POST:view.userPOST
    :param request:
    :return:
    '''
    # 错误信息列表
    error = []
    if request.method == 'GET' and GET is not None:
        return GET(request)
    elif request.method == 'POST' and POST is not None:
        return POST(request)
    else:
        error.append('request.method is WRONG')


def userGET(request):
    '''
    显示用户信息
    :param request:
    :return:
    '''
    # 错误信息列表
    error = []
    assert request.method == 'GET'
    # 获取用户对象
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())

    if user is not None:

        return JsonResponse({

            'status': 200,
            'message': 'success',
            'data': {
                'username': user.username,
                'profile': user.profile,
                'name': user.name

            }
        })
    else:
        error.append('user is not exist')
        return JsonResponse({
            'status': 202,
            'message': error
        })


def userPOST(request):
    '''
    修改用户信息
    :param request:
    :return:
    '''
    # 错误信息列表
    error = []
    assert request.method == 'POST'

    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())

    user.name = request.POST.get('name',user.name)

    img = request.FILES.get('profile')
    if img:
        # 修改 大脸照
        user.profile = settings.ICON_URL + '' + user.username + '.jpg'
        # 将 用户 大脸照 写入 本地文件中
        imgPath = os.path.join(settings.STATIC_ROOT, 'weCheck', 'img', user.username + '.jpg')
        # 判断用户 大脸照 是否存在 若存在 重写
        if os.path.exists(imgPath):
            os.remove(imgPath)
        with open(imgPath, 'wb+') as f:
            for chunk in img.chunks():
                f.write(chunk)
    # 保存 修改
    user.save()

    return JsonResponse({
        'status':200,
        'message':'success'
    })



def group(request):
    error = []
    id = request.GET.get('id')
    group = models.group.objects.get_or_none(groupID=id)
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())

    if group is not None:
        groupID = group.groupID
        name = group.name
        owner = group.owner.username
        member = group.member
        role = 0

        if user.username == owner:
            role = 2
            check = models.check.objects.get_or_none(groupID=groupID)
            if check is not None:
                state = check.enable

            else:
                state = False
            return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'member': member,
                                     'role': role
                                 },
                                 'state':state
                                 })


        elif user.username in group.member:
            role = 1
            check = models.check.objects.get_or_none(groupID=groupID)
            if check is not None:
                state = check.enable
                if state == True:
                    if user.username in check.members:
                        checked = True
                    else:
                        checked =  False
                    return JsonResponse({'status': 200,
                                 'message': 'success',
                                 'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'role': role
                                 },
                                 'state': state,
                                 'checked':checked
                                 })

                elif state ==  False:
                    return JsonResponse({'status': 200,
                                 'message': 'success',
                                 'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'role': role
                                 },
                                 'state': state
                                 })
            else:
                return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': {
                                         'id': groupID,
                                         'name': name,
                                         'owner': owner,
                                         'role': role
                                     },
                                     'state': False
                                     })
        else:
            return JsonResponse({'status': 200,
                                 'message': 'success',
                                 'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'role': role
                                 },
                                 })
    else:
        error.append('group is not exist')
        return JsonResponse({
            'status': 202,
            'message': error
        })



def grouplist(request):
    error = []
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    data = []
    group_message = {}
    if user is not None:
        if user.userType == 1:
            groups = models.group.objects.filter(owner=user)
            if groups.count()!=0:
                for group in groups:
                    groupID = group.groupID
                    name = group.name
                    owner = group.owner
                    member = group.member
                    check = models.check.objects.get_or_none(groupID=groupID)
                    if check is not None:
                        state = check.enable
                        group_message = {'id':groupID,'name':name,'owner':owner.username,'member':member,'state':state,'role':2}
                        data.append(group_message)
                    else:
                        group_message = {'id': groupID, 'name': name, 'owner': owner.username, 'member': member,'state':False,
                                     'role': 2}
                        data.append(group_message)
                return     JsonResponse({'status':200,
                                 'message':'success',
                                 'data':data
                                 })
            else:
                return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': data
                                     })
        else :
            groups = models.group.objects.filter(member__contains=user.username)
            if groups.count()!=0:
                for group in groups :
                    groupID = group.groupID
                    name = group.name
                    owner = group.owner

                    check = models.check.objects.get_or_none(groupID=groupID)
                    if check is not None:
                        state = check.enable
                        if state == True:
                            if user.username in check.members:
                                checked = True
                            else:
                                checked = False
                            group_message = {'id': groupID, 'name': name, 'owner': owner.username,  'state': state,'role': 1,'checked':checked}
                            data.append(group_message)
                        else:
                            group_message = {'id': groupID, 'name': name, 'owner': owner.username,  'state': state,'role': 1}
                            data.append(group_message)
                    else:
                        group_message = {'id': groupID, 'name': name, 'owner': owner.username, 'state': False,
                                         'role': 1}
                        data.append(group_message)
                return JsonResponse({'status':200,
                                 'message':'success',
                                 'data':data
                                 })
            else:
                return JsonResponse({'status': 200,
                              'message': 'success',
                              'data': data
                              })

    else:
        error.append("user not exist ")
        return JsonResponse({'status':202,
                             'message':error,
                             'data':group_message
                             })



# 创建group
def groupadd(request):
    error = []
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    if user.userType == 1:
        name = request.POST.get('name')
        id = ''.join(random.sample(string.ascii_letters+string.digits,6))

        #生成6位的随机口令由大写小写字母和数字随机组成，多达21亿多种结果,基本不能重复
        newGroup,flag=models.group.objects.get_or_create(groupID=id,name=name,member='',owner=user,isDelete=False)
        if newGroup is not None:
            return JsonResponse({'status':200,
                                 'message':'OK',
                                 'data':id,
            })
        else:
            error.append('group id repeat,create group fault')
            return JsonResponse({
                'status':202,
                'message':error
            })
    else:
        error.append('user type error,must be monitor')
        return JsonResponse({
            'status':403,
            'message':error
        })


#加入群组
def groupjoin(request):
    error = []

    user = models.user.objects.get_or_none(username = userSystem(request).getUsername())
    if user.userType == 0:
        id = request.POST.get('id')
        group = models.group.objects.get_or_none(groupID=id)
        if group.member == '':
            group.member = group.member+user.username
        else:
            group.member = group.member +" "+user.username
        group.save()

        return JsonResponse({
            'status':200,
            'message':'success'
        })
    else:
        error.append('user type error, must be user ')
        return JsonResponse({
            'status':403,
            'message':error
        })


def groupquit(request):
    error = []
    id = request.POST.get('id')
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    group = models.group.objects.get_or_none(groupID=id)
    group_check = models.check.objects.get_or_none(groupID=id)
    if user.userType == 0 and group is not None:
        member = group.member
        index = member.find(user.username)
        if index != -1:
            new_member = member.replace(user.username,' ')
            if group_check is not None:
                if group_check.enable == True:
                    if user.username in group_check.members:
                        members = group_check.members
                        if members.find(user.username) != -1:
                            new_members = members.replace(user.username,'')
                            group_check.members = new_members
                            group_check.save()
            group.member = new_member
            group.save()
            return JsonResponse({'status':200,
                                 'message':'success'
                                 })
    else :
        error.append('user type error you must be user or group id error group not exist')
        return JsonResponse({'status':202,
                             'message':error
                             })
def groupupdate(request):
    error = []
    id = request.POST.get('id')
    group = models.group.objects.get_or_none(groupID=id)
    user = models.user.objects.get_or_none(username = userSystem(request).getUsername())
    if group is not None:
        if user.userType == 1 and group.owner.username == user.username:
            owner_name = request.POST.get('owner')
            if owner_name is not None:
                owner = models.user.objects.get(username=owner_name)
                if owner is not None:
                    if owner.userType == 1:
                        group.owner = owner
            member = request.POST.get('member',group.member)
            name = request.POST.get('name',group.name)
            group.member = member
            group.name = name
            group.save()
            return JsonResponse({'status':200,
                             'message':'success'
                             })
        else:
            error.append('user type error,must be group monitor')
            return JsonResponse({'status':403,
                                 'message':error
                                 })
    else:
        error.append('group not exist ')
        return JsonResponse({'status':202,
                             'message':error})
def groupdelete(request):
    error = []
    id = request.POST.get('id')
    group = models.group.objects.get_or_none(groupID=id)
    user = models.user.objects.get_or_none(username = userSystem(request).getUsername())
    if group is not None:
        if user.userType == 1 and group.owner == user:
            group.delete()
            return JsonResponse({'status':200,
                                 'message':'success'})
        else:
            error.append('user type error ,must be group monitor')
            return JsonResponse({
                'status':403,
                'message':error
            })
    else:
        error.append('group not exist')
        return JsonResponse({
            'status':202,
            'message':error
        })


def checkstatus(request):
    user = models.user.objects.get_or_none(username= userSystem(request).getUsername())
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
    error=[]
    user = models.user.objects.get_or_none(username=userSystem(request).getUserObject())
    username=user.username
    groupid=request.POST.get('id')
    group=models.group.objects.filter(groupID__exact=groupid).filter(member__contains=username)
    check=models.check.objects.get_or_none(groupID=group)
    if group is not None:
        if check.enable is False:
            error.append("The group is not checking")
            return JsonResponse({
                "status": 202,
                "message": error
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
        error.append("group is not exist or you are not the member of the group")
        return JsonResponse({
            "status": 202,
            "message": error
        })

#开启即时签到
@ajax_post_only
def checkenable(request):
    error=[]
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
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
            error.append("the group is checking")
    else:#是该群组的所有者
        error.append("you are not the owner of the group or the group not exists")
        return JsonResponse({
            "status": 202,
            "message": error
        })


#结束即时签到
def checkdisable(request):
    error = []
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
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
            error.append("该群组没有正在进行的签到")
            return JsonResponse({
                "status": 202,
                "message": error
            })
    else:
        error.append("you are not the owner of the group or the group not exists")
        return JsonResponse({
            "status": 202,
            "message": error
        })





def schedule(request):
    error=[]
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
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
                "repeat":plan.repeat,
            }
            planlist_request.append(s)
        return JsonResponse({
            "status": 200,
            "message": "ok",
            "data":planlist_request
        })
    else:
        error.append("you are not the member of the group or the group is not exists")
        return JsonResponse({
            "status": 202,
            "message": error
        })


@ajax_post_only
def scheduleadd(request):
    error=[]
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())

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
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    username = user.useranme
    scheduleId= request.POST.get('scheduleId')
    check_plan = models.checkPlan.objects.get_or_none(planID=scheduleId)
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
                            "message":"OK",
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
