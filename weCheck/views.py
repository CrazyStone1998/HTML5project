#!/usr/bin/python
# -*- coding: UTF-8 -*-
from weCheck.common import  BaiduAPI
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from HTML5project import settings
from django.db.models import F,Q
from weCheck import models
from common.auth.userSystem import userSystem
from common.decorator.ajax_post_only import ajax_post_only
from django.views.decorators.cache import never_cache
from weCheck.common import ScheduleThread
from weCheck.common.ScheduleThread import leaveUpdate
import math
import os
import time
import datetime
import string,random

@never_cache
def hasLoggedIn(request):
    if request.method == 'GET':

        if request.session.has_key('sessionID') and request.session.has_key('token'):
            # 用户拥有session，登陆验证
            user = userSystem(request)
            if not user.getUserObject():
                return JsonResponse(
                    {
                        'status':200,
                        'message':'OK',
                        'data':False
                    }
                )
            else:
                return JsonResponse(
                        {
                            'status':200,
                            'message':'OK',
                            'data':True

                        }
                    )
        else:
            return JsonResponse(
                {
                    'status': 200,
                    'message': 'OK',
                    'data': False
                }
            )
    else:
        return JsonResponse(
            {
                'status':202,
                'message':'request.method is not GET.'
            }
        )
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

    error,userType = user.authentication(username=username,password=password)
    # error为空 则登陆成功
    # error不为空 则登陆不成功
    if not error:
        return JsonResponse({
            'status':200,
            'message':'OK',
            'data':{
                'userType': userType
            }

        })
    else:
        return JsonResponse({
                            'status':202,
                            'message':error,
                            'data':{
                                'userType': userType
                            }
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
    error = ''
    # 后台获取并判断用户名和密码 是否为空
    username = request.POST.get('username')
    passwd = request.POST.get('password')
    if username is None or passwd is None:
        error = 'The username&passwd cannot be empty'
        # 获取并判断 用户名是否存在
    else:
        img = request.FILES.get('profile')
        # 检测用户 大脸照是否为人脸
        result = BaiduAPI.facerecognize(img.read())
        # 用户大脸照 判定成功
        if result['result'] == 'SUCCESS':
            if not models.user.objects.filter(Q(username=username)&Q(isDelete=False)).exists():

                passwd   = make_password(passwd)
                name     = request.POST.get('name')
                userType = request.POST.get('userType')
                profile  = settings.ICON_URL+'static/weCheck/img/'+username+'.jpg'
                # 将 用户 大脸照 写入 本地文件中
                imgPath  = os.path.join(settings.BASE_DIR,'static','weCheck','img',username+'.jpg')
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
                error = 'Username already exists'
        else:
            # 用户大脸照 判定失败
            error = result['msg']
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
    error = ''
    if request.method == 'GET' and GET is not None:
        return GET(request)
    elif request.method == 'POST' and POST is not None:
        return POST(request)
    else:
        error = 'request.method is WRONG'

@never_cache
def userGET(request):
    '''
    显示用户信息
    :param request:
    :return:
    '''
    # 错误信息列表
    error = ''
    assert request.method == 'GET'
    # 获取用户对象
    username = request.GET.get('id')
    if username:
        user = models.user.objects.get_or_none(username=username)
    else:
        user = models.user.objects.get_or_none(username=userSystem(request).getUsername())

    if user is not None:

        return JsonResponse({

            'status': 200,
            'message': 'success',
            'data': {
                'username': user.username,
                'profile': user.profile,
                'name': user.name,
                'userType':user.userType

            }
        })
    else:
        error = 'user is not exist'
        return JsonResponse({
            'status': 202,
            'message': error
        })

@never_cache
def userPOST(request):
    '''
    修改用户信息
    :param request:
    :return:
    '''
    # 错误信息列表
    error = ''
    assert request.method == 'POST'

    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())

    user.name = request.POST.get('name',user.name)

    img = request.FILES.get('profile')
    if img:
        # 修改 大脸照
        user.profile = settings.ICON_URL + 'static/weCheck/img/' + user.username + '.jpg'
        # 将 用户 大脸照 写入 本地文件中
        imgPath = os.path.join(settings.BASE_DIR,'static', 'weCheck', 'img', user.username + '.jpg')
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

@never_cache
def group(request):
    id = request.GET.get('id')
    group = models.group.objects.get_or_none(groupID=id)
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())

    if group is not None:
        groupID = group.groupID
        name = group.name
        owner = group.owner.username
        members = group.member.split()
        needLocation = group.needLocation
        needFace = group.needFace
        role = 0
        if user.username == owner:
            role = 2
            #找到当前计划
            checks = models.check.objects.filter(groupID=groupID)
           # anyLeave = False
            if checks.count()!=0:
                # checkID_List = []
                # for check in checks:
                #     checkID_List.append(check.checkID)
                # for checkID in checkID_List:
                #     leaves = models.leave.objects.filter(checkId=checkID)
                #     if leaves is not None:
                #         anyLeave = True
                #         break
                for check in checks:
                    state = check.enable
                    if state == True:
                        member_message = []
                        for member in members:
                            mem = models.user.objects.get_or_none(username=member)
                            state_mem = mem.username in check.results
                            member_user = {'username':mem.username,'name':mem.name,'state':state_mem}
                            member_message.append(member_user)
                        if needLocation == True:
                            lng = group.lng
                            lat = group.lat
                            effectiveDistance = group.effectiveDistance
                            locations = {'lng':lng,'lat':lat,'effectiveDistance':effectiveDistance}
                            return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'members': member_message,
                                     'role': role,
                                     'state': state,
                                     'needLocation':needLocation,
                                     'location':locations,
                                     'needFace':needFace,
                                     #'anyLeave':anyLeave
                                 }
                                 })
                        return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'members': member_message,
                                     'role': role,
                                     'state': state,
                                     'needLocation':needLocation,
                                     'needFace':needFace,
                                    # 'anyLeave': anyLeave
                                     }
                                 })
                #当前没有开启的签到计划
                member_message = []
                for member in members:
                    mem = models.user.objects.get_or_none(username=member)
                    state_mem = False
                    member_user = {'username': mem.username, 'name': mem.name, 'state': state_mem}
                    member_message.append(member_user)
                if needLocation == True:
                    lng = group.lng
                    lat = group.lat
                    effectiveDistance = group.effectiveDistance
                    locations = {'lng': lng, 'lat': lat, 'effectiveDistance': effectiveDistance}
                    return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'members': member_message,
                                     'role': role,
                                     'state': False,
                                     'needLocation':needLocation,
                                     'needFace':needFace,
                                     'location':locations,
                                  #   'anyLeave':anyLeave
                                 }
                                 })
                return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'members': member_message,
                                     'role': role,
                                     'state': False,
                                     'needLocation':needLocation,
                                     'needFace':needFace,
                                    # 'anyLeave': anyLeave
                                     }
                                 })

            #当前群组还没有计划
            else:
                state = False
                member_message = []
                for member in members:
                    mem = models.user.objects.get_or_none(username=member)
                    state_mem = False
                    member_user = {'username': mem.username, 'name': mem.name, 'state': state_mem}
                    member_message.append(member_user)
                if needLocation == True:
                    lng = group.lng
                    lat = group.lat
                    effectiveDistance = group.effectiveDistance
                    locations = {'lng': lng, 'lat': lat, 'effectiveDistance': effectiveDistance}
                    return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'members': member_message,
                                     'role': role,
                                     'state': state,
                                     'needLocation': needLocation,
                                     'needFace': needFace,
                                     'location': locations,
                                     #'anyLeave':False
                                 }
                                 })
                return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'members': member_message,
                                     'role': role,
                                     'state': state,
                                     'needLocation': needLocation,
                                     'needFace': needFace,
                                     #'anyLeave': False
                                 }
                                 })
        elif user.username in group.member:
            role = 1
            checks = models.check.objects.filter(groupID=groupID)
            if checks.count()!=0 :
                for check in checks:
                    state = check.enable
                    if state == True:
                        if user.username in check.results:
                            checked = True
                        else:
                            checked =  False
                        return JsonResponse({'status': 200,
                                 'message': 'success',
                                 'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'role': role,
                                     'state': state,
                                     'checked': checked,
                                     'needLocation':needLocation,
                                     'needFace':needFace
                                 }
                                 })

                state =  False
                return JsonResponse({'status': 200,
                                 'message': 'success',
                                 'data': {
                                     'id': groupID,
                                     'name': name,
                                     'owner': owner,
                                     'role': role,
                                     'state': state,
                                     'needLocation':needLocation,
                                     'needFace':needFace
                                 }
                                 })
            else:
                return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': {
                                         'id': groupID,
                                         'name': name,
                                         'owner': owner,
                                         'role': role,
                                         'state': False,
                                         'needLocation':needLocation,
                                         'needFace':needFace
                                     },
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
        return JsonResponse({
            'status': 202,
            'message':'group is not exist'
        })


@never_cache
def grouplist(request):
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    data = []
    group_message = {}
    if user is not None:
        if user.userType == 1:
            groups = models.group.objects.filter(owner=user)
            if groups.count()!=0:
                for group in groups:
                    flag = 0
                    groupID = group.groupID
                    name = group.name
                    owner = group.owner
                    members = group.member.split()
                    needLocation = group.needLocation
                    needFace = group.needFace
                    checks = models.check.objects.filter(groupID=groupID)
                    #anyLeave = False
                    #group 的 member 信息
                    member_message = []
                    #查找当前计划
                    if checks.count()!=0:
                        # checkID_List = []
                        # for check in checks:
                        #     checkID_List.append(check.checkID)
                        # for checkID in checkID_List:
                        #     leaves = models.leave.objects.filter(checkId=checkID)
                        #     if leaves is not None:
                        #         anyLeave = True
                        #         break
                        for check in checks:
                            state = check.enable
                            if state == True:
                                flag = 1
                                for member in members:
                                    mem = models.user.objects.get_or_none(username=member)
                                    state_mem = mem.username in check.results
                                    member_user = {'username': mem.username, 'name': mem.name, 'state': state_mem}
                                    member_message.append(member_user)
                                #基于位置的签到开启时
                                if needLocation == True:
                                    lng = group.lng
                                    lat = group.lat
                                    effectiveDistance = group.effectiveDistance
                                    location = {'lng':lng,'lat':lat,'effectiveDistance':effectiveDistance}
                                    group_message = {'id':groupID,'name':name,'owner':owner.username,'members':member_message,
                                                     'state':state,'role':2,'needLocation':needLocation,
                                                     'location':location,'needFace':needFace,}
                                    data.append(group_message)
                                    break
                                #不开启基于位置的签到
                                group_message = {'id': groupID, 'name': name, 'owner': owner.username,
                                                     'members': member_message,
                                                     'state': state, 'role': 2, 'needLocation': needLocation,
                                                     'needFace': needFace,}
                                data.append(group_message)
                        #没有当前计划时
                        if flag == 0:
                            for member in members:
                                mem = models.user.objects.get_or_none(username=member)
                                state_mem = False
                                member_user = {'username': mem.username, 'name': mem.name, 'state': state_mem}
                                member_message.append(member_user)
                            if needLocation == True:
                                flag = 1
                                lng = group.lng
                                lat = group.lat
                                effectiveDistance = group.effectiveDistance
                                location = {'lng': lng, 'lat': lat, 'effectiveDistance': effectiveDistance}
                                group_message = {'id': groupID, 'name': name, 'owner': owner.username,
                                                 'members': member_message,
                                                 'state': False, 'role': 2, 'needLocation': needLocation,
                                                 'location': location, 'needFace': needFace,}
                                data.append(group_message)
                            if flag == 0:
                                group_message = {'id': groupID, 'name': name, 'owner': owner.username, 'members': member_message,
                                         'state': False,
                                         'role': 2,'needLocation': needLocation,'needFace': needFace,}
                                data.append(group_message)
                    #check中没有当前group的计划
                    else:
                        for member in members:
                            mem = models.user.objects.get_or_none(username=member)
                            state_mem = False
                            member_user = {'username': mem.username, 'name': mem.name, 'state': state_mem}
                            member_message.append(member_user)
                        if needLocation == True:
                            flag = 1
                            lng = group.lng
                            lat = group.lat
                            effectiveDistance = group.effectiveDistance
                            location = {'lng': lng, 'lat': lat, 'effectiveDistance': effectiveDistance}
                            group_message = {'id': groupID, 'name': name, 'owner': owner.username,
                                             'members': member_message,
                                             'state': False, 'role': 2, 'needLocation': needLocation,
                                             'location': location, 'needFace': needFace,}
                            data.append(group_message)
                        if flag == 0:
                            group_message = {'id': groupID, 'name': name, 'owner': owner.username, 'members': member_message,'state':False,
                                     'role': 2,'needLocation': needLocation,'needFace': needFace,}
                            data.append(group_message)
                return     JsonResponse({'status':200,
                                 'message':'success',
                                 'data':data
                                 })
            #当前monitor没有创建群组
            else:
                return JsonResponse({'status': 200,
                                     'message': 'success',
                                     'data': data
                                     })
        else:
            groups = models.group.objects.filter(member__contains=user.username)
            if groups.count()!=0:
                for group in groups :
                    flag = 0
                    groupID = group.groupID
                    name = group.name
                    owner = group.owner
                    needLocation = group.needLocation
                    needFace = group.needFace
                    checks = models.check.objects.filter(groupID=groupID)
                    if checks.count()!=0:
                        for check in checks:
                            state = check.enable
                            if state == True:
                                if user.username in check.results:
                                    checked = True
                                else:
                                    checked = False
                                flag = 1
                                group_message = {'id': groupID, 'name': name, 'owner': owner.username,
                                                     'state': state, 'role': 1,'checked':checked,
                                                     'needLocation': needLocation, 'needFace': needFace
                                                     }
                                data.append(group_message)
                                break

                        if flag == 0:

                            group_message = {'id': groupID, 'name': name, 'owner': owner.username,  'state': False,'role': 1,
                                             'needLocation': needLocation,'needFace': needFace
                                             }
                            data.append(group_message)
                    else:

                        group_message = {'id': groupID, 'name': name, 'owner': owner.username, 'state': False,
                                         'role': 1,'needLocation': needLocation,'needFace': needFace}
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
        return JsonResponse({'status':202,
                             'message':"user not exist "
                             })

# 创建group
@ajax_post_only
def groupadd(request):
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
            return JsonResponse({
                'status':202,
                'message':'group id repeat,create group fail'
            })
    else:
        return JsonResponse({
            'status':403,
            'message':'user type error,must be monitor'
        })


#加入群组
@ajax_post_only
def groupjoin(request):

    user = models.user.objects.get_or_none(username = userSystem(request).getUsername())
    if user.userType == 0:
        id = request.POST.get('id')
        group = models.group.objects.get_or_none(groupID=id)
        checks = models.check.objects.filter(groupID=id)
        if group.member == '':
            group.member = group.member+user.username
        else:
            group.member = group.member +" "+user.username
        group.save()
        if checks.count()!=0:
            for check in checks:
                if check.enable == True:
                    check.members += ' '+user.username
                    check.save()
                    break
        return JsonResponse({
            'status':200,
            'message':'success'
        })
    else:
        return JsonResponse({
            'status':403,
            'message':'user type error, must be user '
        })

@ajax_post_only
def groupquit(request):
    id = request.POST.get('id')
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    group = models.group.objects.get_or_none(groupID=id)
    if user.userType == 0 and group is not None:
        member = group.member
        index = member.find(user.username)
        if index != -1:
            new_member = member.replace(user.username,'')
            #if group_check is not None:
              #  if group_check.enable == True:
                    #if user.username in group_check.results:
                       # results = group_check.results
                       # if results.find(user.username) != -1:
                           # new_results = results.replace(user.username,'')
                           # group_check.results = new_results
                           # group_check.save()
            group.member = new_member
            group.save()
            return JsonResponse({'status':200,
                                 'message':'success'
                                 })
    else :
        return JsonResponse({'status':202,
                             'message':'user type error you must be user or group id error group not exist'
                             })

@ajax_post_only
def groupupdate(request):
    id = request.POST.get('id')
    group = models.group.objects.get_or_none(groupID=id)
    user = models.user.objects.get_or_none(username = userSystem(request).getUsername())
    if group is not None:
        if user.userType == 1 and group.owner.username == user.username:

            name = request.POST.get('name',group.name)
            needLocation = request.POST.get('needLocation',group.needLocation)
            needFace = request.POST.get('needFace',group.needFace)
            if needLocation == 'true':
                lng = request.POST.get('lng',group.lng)
                lat = request.POST.get('lat',group.lat)
                effectiveDistance = request.POST.get('effectiveDistance',group.effectiveDistance)
                group.lng = lng
                group.lat = lat
                group.effectiveDistance = effectiveDistance
                needLocation=True
            if needLocation == 'false':
                needLocation = False
            if needFace == 'true':
                needFace =True
            if needFace == 'false':
                needFace = False
            group.needLocation = needLocation
            group.needFace = needFace
            group.name = name
            group.save()
            return JsonResponse({'status':200,
                             'message':'success'
                             })
        else:
            return JsonResponse({'status':403,
                                 'message':'user type error,must be group monitor'
                                 })
    else:
        return JsonResponse({'status':202,
                             'message':'group not exist '})

@ajax_post_only
def groupdelete(request):
    id = request.POST.get('id')
    group = models.group.objects.get_or_none(groupID=id)
    user = models.user.objects.get_or_none(username = userSystem(request).getUsername())
    if group is not None:
        if user.userType == 1 and group.owner == user:
            group.delete()
            return JsonResponse({'status':200,
                                 'message':'success'})
        else:
            return JsonResponse({
                'status':403,
                'message':'user type error ,must be group monitor'
            })
    else:
        return JsonResponse({
            'status':202,
            'message':'group not exist'
        })

def history(request,id):
    uname = userSystem(request).getUsername()
    user = models.user.objects.get_or_none(username=uname)
    group = models.group.objects.get_or_none(groupID=id)
    checks = models.check.objects.filter(groupID=id).order_by('-checkID')
    history_message = []
    if group is not None:
        if checks.count()==0:
            return JsonResponse({
                'status':200,
                'message':'OK',
                'data':history_message
                }
                )
        else :
            if group.owner.username == user.username:
                for check in checks:
                    message={
                    'id':check.checkID,
                    'startUpDateTime':str(check.startDate)+'T'+check.startUpTime+'Z',
                    'duration':check.duration,
                    }
                    history_message.append(message)
                return JsonResponse({
                'status':200,
                'message':'OK',
                'data':history_message
                }
                )
            if user.username in group.member:
                for check in checks:
                    leaves = models.leave.objects.get_or_none(username=uname,checkID=check.checkID,status=1)
                    message = {
                        'id': check.checkID,
                        'startUpDateTime': str(check.startDate)+'T'+check.startUpTime+'Z',
                        'duration': check.duration,
                        'checked':user.username in check.results,
                        'leave': True if leaves is not None else False
                    }
                    history_message.append(message)
                return JsonResponse({
                    'status':200,
                    'message':'OK',
                    'data':history_message
                }
                )
            else:
                return JsonResponse({
                'status': 200,
                'message': 'you are not the monitor or member of this group'
            }
            )
    else:
        return JsonResponse({
            'status': 200,
            'message': 'group is not exist'
        }
        )

def userhistory(request,groupID,username):
    user = models.user.objects.get_or_none(username=username)
    group = models.group.objects.get_or_none(groupID=groupID)
    checks = models.check.objects.filter(groupID=groupID).order_by('-checkID')
    history_message = []
    if group is not None:
        if checks.count() == 0:
            return JsonResponse({
                'status': 200,
                'message': 'OK',
                'data': history_message
            }
            )
        else:
            if user.username in group.member:
                for check in checks:
                    leaves = models.leave.objects.get_or_none(username=username, checkID=check.checkID,status=1)
                    message = {
                        'id': check.checkID,
                        'startUpDateTime': str(check.startDate)+'T'+check.startUpTime+'Z',
                        'duration': check.duration,
                        'checked': user.username in check.results,
                        'leave':True if leaves is not None else False
                    }
                    history_message.append(message)
                return JsonResponse({
                    'status': 200,
                    'message': 'OK',
                    'data': history_message
                }
                )
            else:
                return JsonResponse({
                    'status': 200,
                    'message': 'you are not the  member of this group'
                }
                )
    else:
            return JsonResponse({
                'status': 200,
                'message': 'group is not exist'
            }
            )

@never_cache
def checkstatus(request):
    user = models.user.objects.get_or_none(username= userSystem(request).getUsername())
    if user is not None:
        username=user.username
        nowdate=datetime.date.today()
        doneList=models.check.objects.filter(members__contains=username).filter(startDate__exact=nowdate).filter(results__contains=username)
        doneList_request=[]
        for done in doneList:
            s ={
                "groupId":str(done.groupID.groupID),
                "groupName":str(done.groupID.name),
                "startUpTime":str(done.startUpTime),
            }
            doneList_request.append(s)

        missedList= models.check.objects.filter(members__contains=username).filter(startDate__exact=nowdate).filter(enable__exact=False).filter(~Q(results__contains=username))
        missedList_request=[]
        for miss in missedList:

            s1={
                "groupId": str(miss.groupID.groupID),
                "groupName": str(miss.groupID.name),
                "startUpTime": str(miss.startUpTime),
            }
            missedList_request.append(s1)

        openList=models.check.objects.filter(members__contains=username).filter(enable__exact=True)
        openList_request=[]
        for open in openList:
            if username not in open.results:
                s = {
                    "groupId": str(open.groupID.groupID),
                    "groupName": str(open.groupID.name),
                    "startUpTime": str(open.startUpTime),
                }
                openList_request.append(s)

        weekdate=str(nowdate.weekday()+1)
        belong_group=models.group.objects.filter(member__contains=username)#用户所属小组
        belong_group_id=[]
        for a in belong_group:
            belong_group_id.append(a.groupID)
        nowtime = str(time.strftime('%H:%M', time.localtime(time.time())))#将现在的时间格式化为hh:mm
        s1 = "20160916" + nowtime + ":00"#为了能与startuptime相比较 两者必须放到同一天 再转化为日期类型
        t1 = time.strptime(s1, '%Y%m%d%H:%M:%S')
        time1 = time.mktime(t1)

        futureList=models.checkPlan.objects.filter(enable__exact=True).filter(Q(repeat__contains=weekdate) | Q(repeat__exact=""))

        #以上future并没有一时间为条件过滤，因为时间是字符串类型，在上述语句中不好操作
        futureList_request=[]
        for future in futureList:
            #将startup time转化为日期类型方便比较
            check_time=future.startUpTime
            s2 = "20160916" + check_time + ":00"
            t2 = time.strptime(s2, '%Y%m%d%H:%M:%S')
            time2 = time.mktime(t2)
            if (time2>time1) and (future.groupID.groupID in belong_group_id):
                s={

                    "groupId": str(future.groupID.groupID),
                    "startUpTime": str(future.startUpTime),
                    'groupName':str(future.groupID.name),
                }
                futureList_request.append(s)

        return JsonResponse({
            "status": 200,
            "message": 'success',
            "data": {
                "done":doneList_request,
                "missed":missedList_request,
                "open":openList_request,
                "future":futureList_request,
            }
        })

@ajax_post_only
def checkcheck(request):
    error=''
    user = models.user.objects.get_or_none(username=userSystem(request).getUserObject())
    username=str(user.username)
    groupid=request.POST.get('id')
    group=models.group.objects.filter(groupID__exact=groupid).filter(member__contains=username)
    g=None
    for i in group:
        g=i
    if group.count() != 0:
        check = models.check.objects.filter(groupID__exact=g.groupID)
        flag = False
        c = None
        for ch in check:
            if ch.enable is True:
                flag = True
                c = ch
                break
        if flag is False:
            error = "The group is not checking"
            return JsonResponse({
                "status": 202,
                "message": error
             })
        else:

            m = c.results
            if username in m:
                error = "you have already checked"
                return JsonResponse({
                    "status": 202,
                    "message": error
                })
            else:

                if g.needLocation==False and g.needFace == False:
                    m = m + "," + username
                    c.results = m
                    c.save()

                    #签到时 将请假信息清除
                    leavevalid(c, user)

                    return JsonResponse({
                        "status": 200,
                        "message": "ok"
                    })
                else :
                    if g.needLocation==True:
                        lng_now = float(request.POST.get('lng'))*math.pi/180.0
                        lat_now = float(request.POST.get('lat'))*math.pi/180.0
                        lng_base = float(g.lng)*math.pi/180.0
                        lat_base = float(g.lat)*math.pi/180.0
                        a = lat_base - lat_now
                        b = lng_base - lng_now
                        effectiveDistance = float(g.effectiveDistance)
                        s = math.asin(math.sqrt(
                            math.pow(math.sin(a / 2), 2) + math.cos(lat_base) * math.cos(lat_now) * math.pow(
                                math.sin(b / 2), 2)))
                        s = 2 * s * 6371000
                        s = round(s * 10000) / 10000
                        if s <= effectiveDistance:
                            m = m + "," + username
                            c.results = m
                            c.save()

                            # 签到时 将请假信息清除
                            leavevalid(c, user)
                            return JsonResponse({
                                "status": 200,
                                "message": "ok"
                            })
                        else:
                            error = "you are not in the area of checking "
                            return JsonResponse({
                                "status": 202,
                                "message": error
                            })
                    if g.needFace==True:
                        imgPath = os.path.join(settings.BASE_DIR,'static', 'weCheck', 'img', username + '.jpg')
                        face_now = request.FILES.get('face').read()
                        with open(imgPath, 'rb') as f:
                            face_base = f.read()

                        face_result = BaiduAPI.faceContrast(face_now, face_base)


                        if  face_result['result'] == "SUCCESS":
                            m = m + "," + username
                            c.results = m
                            c.save()

                            # 签到时 将请假信息清除
                            leavevalid(c, user)

                            return JsonResponse({
                                "status": 200,
                                "message": "ok"
                            })
                        else:
                            error = face_result['msg']
                            return JsonResponse({
                                "status": 202,
                                "message": error
                            })


    else:
        error = "group is not exist or you are not the member of the group"
        return JsonResponse({
            "status": 202,
            "message": error
        })

@ajax_post_only
def checkenable(request):
    '''
    开启即时签到
    :param request:
    :return:
    '''
    error = ''
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    if user is not None:
        ownerID=user.username
        groupid = request.POST.get('id')
        group=models.group.objects.filter(groupID__exact=groupid).filter(owner__exact=ownerID)#查看该用户是否为该群组的所有者
        if group.count()!=0:#是该群组的所有者
            g=None
            for i in group:
                g=i

            check=models.check.objects.filter(groupID__exact=g).filter(enable__exact=True)#查看该群组是否还在开启签到中，保证一个群组同一时间只能开启一次签到
            if check.count()==0:#该群组没有处于签到中
                models.check.checkObject(g,startUpTime=time.strftime('%H:%M'))#创建新的签到对象
                return JsonResponse({
                    "status": 200,
                    "message": 'ok'
                })
            else:#该群组上一次签到还没有结束
                error = "the group is checking"
                return JsonResponse({
                    "status": 202,
                    "message": error
                })
        else:#是该群组的所有者
            error = "you are not the owner of the group or the group not exists"
            return JsonResponse({
                "status": 202,
                "message": error
            })
    else:
        error = "user is not exist"
        return JsonResponse({
            "status": 202,
            "message": error
        })

#结束即时签到
def checkdisable(request):
    error = ''
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    ownerID = user.username
    groupid = request.POST.get('id')
    group = models.group.objects.filter(groupID__exact=groupid).filter(owner__exact=ownerID)
    g=None
    if group.count()!=0:
        for i in group :
            g=i
        check=models.check.objects.filter(groupID__exact=g).filter(enable__exact=True)#找到该群组正在进行的签到，接着结束他
        if check.count()!=0:
            c=None
            for i in check:
                c=i
            c.enable = False
            c.save()
            # 签到关闭 请假请求后处理
            leaveUpdate(c.checkID)

            return JsonResponse({
                "status": 200,
                "message": "ok"
            })
        else:
            error = "There is no sign in progress in the group"
            return JsonResponse({
                "status": 202,
                "message": error
            })
    else:
        error = "you are not the owner of the group or the group not exists"
        return JsonResponse({
            "status": 202,
            "message": error
        })




@never_cache
def schedule(request):
    error = ''
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())

    username = user.username#获取该用户的用户名称
    groupid = request.GET.get('id')
    group = models.group.objects.filter(groupID__exact=groupid).filter(Q(member__contains=username)  |  Q(owner__exact=username))#获取该群组，并且检查是否包含该用户
    g = None

    for i in group:
        g = i
    if group.count() != 0:
        planlist = models.checkPlan.objects.filter(groupID__exact=g)
        planlist_request = []
        for plan in planlist:
            s = {
                "scheduleId": plan.planID,
                "startUpTime": plan.startUpTime,
                "duration": plan.duration,
                "enable": plan.enable,
                "repeat": plan.repeat,
            }
            planlist_request.append(s)
        return JsonResponse({
            "status": 200,
            "message": "ok",
            "data": planlist_request
        })
    else:
        error = "you are not the member of the group or the group is not exists"
        return JsonResponse({
            "status": 202,
            "message": error
        })


@ajax_post_only
def scheduleadd(request):
    error = ''
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    username = user.username
    groupid = request.POST.get('id')
    group = models.group.objects.filter(groupID__exact=groupid).filter(owner__exact=username)
    g=None
    for i in group:
        g=i
    duration = request.POST.get('duration')
    startUpTime = str(request.POST.get('startUpTime'))
    repeat = request.POST.get('repeat')
    duration = int(request.POST.get('duration'))
    enable = str(request.POST.get('enable'))
    if group.count()!=0:
        if enable=="false":#计划关闭状态可以加入
            a=models.checkPlan.checkPlanObejct(g,startUpTime,duration,repeat,False)
            return JsonResponse({
                "status": 200,
                "message": 'ok',
                "data":a.planID
            })

        else:
            # 计划开启状态
            # 查找与之相冲突的计划
            # 先查找改组现在开启的计划
            checkList = models.checkPlan.objects.filter(groupID__exact=g).filter(enable__exact=True)#这是本群开启的其他计划
            flag = False# 假设这些计划都不冲突
            # 如果这些计划冲突必须满足点：1.有相同的周天 2.当前计划的开启时间+持续时间>原有计划的开始时间 或者原有计划的开始时间+持续时间>当前计划的开始时间
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
                error = "Your current schedule for this group is in conflict with the existing schedule"
                return JsonResponse({
                    "status": 202,
                    "message": error
                })
            else:#与计划没有冲突，查看与开启的签到有没有冲突
                nowdate = datetime.date.today()
                weekdate = str(nowdate.weekday() + 1)
                if weekdate in repeat:
                    check_thisday=models.check.objects.filter(enable__exact=True).filter(duration__exact=1000).filter(groupID__exact=g)
                    if check_thisday.count()!=0:
                        nowtime = str(time.strftime('%H:%M', time.localtime(time.time())))
                        s1 = "20160916"+nowtime+":00"
                        t1 = time.strptime(s1, '%Y%m%d%H:%M:%S')
                        ti1 = time.mktime(t1)
                        s2 = "20160916"+startUpTime+":00"
                        t2 = time.strptime(s2, '%Y%m%d%H:%M:%S')
                        ti2 = time.mktime(t2)
                        if ti1 > ti2:
                            a = models.checkPlan.checkPlanObejct(g, startUpTime, duration, repeat, True)
                            # 开启 周期计划
                            ScheduleThread.addScheduleThread(a.planID, g, startUpTime, duration, repeat)
                            return JsonResponse({
                                "status": 200,
                                "message": "ok",
                                "data": a.planID
                            })
                        else:
                            error = "Your current schedule for this group is in conflict with the ongoing check"
                            return  JsonResponse({
                                "status": 202,
                                "message":error
                            })
                    else:
                        a = models.checkPlan.checkPlanObejct(g, startUpTime, duration, repeat, True)
                        ScheduleThread.addScheduleThread(a.planID, g, startUpTime, duration, repeat)
                        return  JsonResponse({
                            "status":200,
                            "message":"ok",
                            "data":a.planID
                        })

                else:
                    a = models.checkPlan.checkPlanObejct(g, startUpTime, duration, repeat, True)
                    ScheduleThread.addScheduleThread(a.planID, g, startUpTime, duration, repeat)
                    return JsonResponse({
                        "status":200,
                        "message":"ok",
                        "data":a.planID
                    })




    else:
        error = "you are not the owner of the group or the group is not exist"
        return JsonResponse({
            "status": 202,
            "message": error
        })


@ajax_post_only
def scheduleupdate(request):
    error = ''
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    username = user.username
    scheduleId = request.POST.get('scheduleId')
    check_plan = models.checkPlan.objects.get(planID=scheduleId)
    check_plan_id = check_plan.planID
    groupId=request.POST.get('id',check_plan.groupID.groupID)
    startUpTime = str(request.POST.get('startUpTime', check_plan.startUpTime))
    duration = int(request.POST.get('duration', check_plan.duration))
    repeat = request.POST.get('repeat', check_plan.repeat)
    enable = str(request.POST.get('enable', check_plan.enable))
    group = models.group.objects.filter(groupID__exact=groupId).filter(owner__exact=username)


    g=None
    for i in group:
        g = i

    if group.count()!=0 :
        if (enable == (str(
                check_plan.enable)).lower() and groupId == check_plan.groupID.groupID and startUpTime == check_plan.startUpTime
                and duration == int(check_plan.duration) and repeat == check_plan.repeat):
            error = "You haven't made any changes."
            return JsonResponse({
                "status": 202,
                "message": error
            })
        if enable=="false":#计划修改为关闭状态可以修改
            check_plan.groupID=g
            check_plan.startUpTime=startUpTime
            check_plan.duration=duration
            check_plan.repeat=repeat
            check_plan.enable=False
            check_plan.save()

            # 关闭 周期任务计划
            ScheduleThread.deleteScheduleThread(str(scheduleId)+startUpTime)

            return JsonResponse({
                "status": 200,
                "message": 'ok',
            })

        else:#计划修改为开启状态
            #查找与之相冲突的计划
            #先查找改组现在开启的计划

            checkList = models.checkPlan.objects.filter(groupID__exact=g).filter(enable__exact=True)#这是本群开启的其他计划
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
                            che_id=che.planID
                            if che_id!=check_plan_id:

                                flag = True#表示由计划与当前计划矛盾
                                break
                if(flag==True):
                    break
            if(flag==True):
                error = "Your current schedule for this group is in conflict with the existing schedule"
                return JsonResponse({
                    "status": 202,
                    "message": error
                })
            else:#与计划没有冲突，查看与开启的签到有没有冲突

                nowdate = datetime.date.today()
                weekdate = str(nowdate.weekday() + 1)
                if weekdate in repeat:
                    check_thisday=models.check.objects.filter(enable__exact=True).filter(groupID__exact=g).filter(duration__exact=1000)
                    if check_thisday.count() != 0:
                        nowtime = str(time.strftime('%H:%M', time.localtime(time.time())))
                        s1 = "20160916"+nowtime+":00"
                        t1 = time.strptime(s1, '%Y%m%d%H:%M:%S')
                        ti1 = time.mktime(t1)
                        s2 = "20160916"+startUpTime+":00"
                        t2 = time.strptime(s2, '%Y%m%d%H:%M:%S')
                        ti2 = time.mktime(t2)
                        if ti1 > ti2:
                            check_plan.groupID=g
                            check_plan.startUpTime=startUpTime
                            check_plan.duration=duration
                            check_plan.repeat=repeat
                            check_plan.enable=True
                            check_plan.save()
                            # 开启周期签到计划
                            ScheduleThread.addScheduleThread(scheduleId,g,startUpTime,duration,repeat)

                            return  JsonResponse({
                                "status": 200,
                                "message": "ok",
                            })
                        else:

                            error = "Your current schedule for this group is in conflict with the ongoing check"
                            return  JsonResponse({
                                "status": 202,
                                "message":error
                            })



                    else:

                        check_plan.groupID=g
                        check_plan.startUpTime=startUpTime
                        check_plan.duration=duration
                        check_plan.enable=True
                        check_plan.repeat=repeat
                        check_plan.save()
                        ScheduleThread.addScheduleThread(scheduleId, g, startUpTime, duration, repeat)
                        return  JsonResponse({
                            "status":200,
                            "message":"OK",
                        })

                else:
                    check_plan.groupID= g
                    check_plan.startUpTime=startUpTime
                    check_plan.duration=duration
                    check_plan.enable=True
                    check_plan.repeat=repeat
                    check_plan.save()
                    ScheduleThread.addScheduleThread(scheduleId, g, startUpTime, duration, repeat)
                    return JsonResponse({
                        "status":200,
                        "message":"ok",
                    })

    else:
        error = "you are not the owner of the group or the group is not exist"
        return JsonResponse({
            "status": 202,
            "message": error
        })

def scheduledelete(request):
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    username=user.username
    error = ''
    scheduleId = request.POST.get('scheduleId')
    check_plan = models.checkPlan.objects.filter(planID__exact=scheduleId)
    c=None
    for i in check_plan:
        c = i
    groupID=c.groupID.groupID
    group=models.group.objects.filter(groupID__exact=groupID).filter(owner__exact=username)
    if group.count() != 0:
        if check_plan.count() != 0:
            check_plan.delete()
            return JsonResponse({
                "status":200,
                "message":"ok"
            })
        else:
            error = "The schedule does not exist"
            return JsonResponse({
                "status":202,
                "message":error
            })
    else:
        error = "You are not the owner of the group or the group is not exist"
        return JsonResponse({
            "status": 202,
            "message": error
        })
#获取历史记录中的某条记录的信息(m)
def record(request,checkID):
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    username=user.username
    check= models.check.objects.get(checkID=checkID)
    group = models.group.objects.filter(owner__exact=username).filter(groupID__exact=check.groupID.groupID)
    leaves = models.leave.objects.filter(checkID=checkID,status=1)
    leavenameList = []
    if leaves.count() != 0:
        for leave in leaves:
            leavenameList.append(leave.username.username)
    g=None
    if group.count()!=0:
        if check.enable is True:
            return JsonResponse({
                "status": 202,
                "message": "The sign in is in progress. Please examine later"
            })
        else:
            starttime = str(check.startDate) + "T" + check.startUpTime + "Z"
            if check.members:
                memeber = check.members.split(" ")
                result = check.results.strip(" ,").split(",")
                doneList = []
                missedList = []
                leaveList = []
                for m in memeber:
                    m_name = (models.user.objects.get(username=m)).name
                    s = {
                        "username": m,
                        "name": m_name,
                    }
                    if m in result:
                        doneList.append(s)
                    elif m in leavenameList:
                        leaveList.append(s)
                    else:
                        missedList.append(s)
                return JsonResponse({
                    "status": 200,
                    "message": "OK",
                    "data": {
                        "id": checkID,
                        "startUpTime": starttime,
                        "duration": check.duration,
                        "done": doneList,
                        "missed": missedList,
                        'leave':leaveList
                    }
                })
            else:
                doneList = []
                missedList = []
                leaveList = []
                return JsonResponse({
                    "status": 200,
                    "message": "OK",
                    "data": {
                        "id": checkID,
                        "startUpTime": starttime,
                        "duration": check.duration,
                        "done": doneList,
                        "missed": missedList,
                        'leave': leaveList
                    }
                })
    else:
        return JsonResponse({
            "status": 202,
            "message": "you are not the owner of the group or the groip is not exist"
        })

#用户端 请假接口
def groupleave(request):
    '''
    用户发出请假请求，数据库插入请假记录
    :param request:
                    group_id:
                    result:
    :return:
    '''
    user = models.user.objects.get_or_none(username=userSystem(request).getUsername())
    username = user.username

    if request.method == 'POST':

        group_id = request.POST.get('group_id')
        result = request.POST.get('result')

        groupID = models.group.objects.get_or_none(groupID=group_id)
        checkID = models.check.objects.filter(Q(groupID=groupID) & Q(enable=True))[0]


        leave_exist = models.leave.objects.filter(Q(username=user) & Q(checkID=checkID) & Q(status=0))
        new_leave = None
        if leave_exist:
            if leave_exist[0]:

                leave_exist[0].result = result
                leave_exist[0].save()

                return JsonResponse(
                    {
                        'status': 200,
                        'message': 'OK',
                        'data': {
                            'leaveID': leave_exist[0].leaveID,
                        },
                    }
                )

            else:
                new_leave = models.leave.leaveObject(user, checkID, groupID, result)
        else:

            new_leave = models.leave.leaveObject(user, checkID, groupID, result)

        return JsonResponse(
            {
                'status': 200,
                'message': 'OK',
                'data': {
                    'leaveID': new_leave.leaveID,
                },
            }
        )

#老师获取请假请求
@never_cache
def leave(request):
    '''

    :param request:
    :return:
    '''
    leaves = []

    if request.method == 'GET':

        groupID = request.GET.get('group_id')

        leave_list = models.leave.objects.filter(Q(groupID=groupID) & Q(status=0))

        for each in leave_list:
            leaves.append(
                {
                    'leave_id': each.leaveID,

                    'username': each.username.username,
                    'name': each.username.name,
                    'result': each.result,
                }
            )

        return JsonResponse(
            {
                'status': 200,
                'message': 'success',
                'data': {
                    'leaves': leaves,
                }
            }
        )


def leaveresponse(request):
    '''

    :param request:
    :return:
    '''

    if request.method == 'POST':

        leave_id = request.POST.get('leave_id')
        leave_response = request.POST.get('leave_response')
        leave_msg = request.POST.get('leave_msg')

        leaveID = models.leave.objects.get_or_none(leaveID=leave_id)


        if leave_response == 'true':

            leaveID.status = 1
        elif leave_response == 'false':

            leaveID.status = 2

        leaveID.reMsg = leave_msg

        leaveID.save()

    return JsonResponse(
        {
            'status': 200,
            'message': 'OK',
        }
    )

@never_cache
def leavefeedback(request, leaveID):
    '''

    :param request:
    :return:
    '''
    # 获取当前用户
    # 获取当前签到（开启状态）
    leave = models.leave.objects.get_or_none(leaveID=leaveID)

    if leave:

        return JsonResponse(
            {
                'status': 200,
                'message': 'success',
                'data': {
                    'leaveID': leave.leaveID,
                    'leave_status': leave.status,
                    'leave_msg': leave.reMsg,
                    'leave_result': leave.result,
                }
            }
        )
    return JsonResponse(
        {
            'status': 202,
            'message': 'leave is closed'

        }
    )

@never_cache
def datarecord(request, groupID):

    data_raw = {}

    if request.method == 'GET':

        check_data_list = models.check.objects.filter(Q(groupID=groupID))
        members = models.group.objects.get_or_none(groupID=groupID).member

        for each_member in members.split(' '):
            if models.user.objects.get_or_none(username=each_member):
                if not data_raw.get(each_member):
                    data_raw[each_member] = {
                        'username': each_member,
                        'name': models.user.objects.get_or_none(username=each_member).name,
                        'missed': 0,
                        'leave': 0,
                        'sum': 0,
                        'done': 0,
                        'done_percent': '0.00%',
                    }

        for each_check in check_data_list:

            checkID = each_check.checkID

            member_list = each_check.members.split(' ')


            for each_member in member_list:
                if models.user.objects.get_or_none(username=each_member):
                    if not data_raw.get(each_member):
                        data_raw[each_member] = {
                            'username': each_member,
                            'name': models.user.objects.get_or_none(username=each_member).name,
                            'missed': 0,
                            'leave': 0,
                            'sum': 1,
                            'done': 0,
                            'done_percent': '',
                        }
                    else:
                        data_raw[each_member]['sum'] = data_raw[each_member]['sum'] + 1

            leave_list = models.leave.objects.filter(checkID=checkID)


            if leave_list:
                for each_leave in leave_list:
                    if each_leave.valid and each_leave.status == 1 and data_raw.get(each_leave.username.username):
                        data_raw[each_leave.username.username]['leave'] = data_raw[each_leave.username.username]['leave'] + 1

            results_list = each_check.results.split(',')
            for each_result in results_list[1:]:
                if each_result:

                    data_raw[each_result]['done'] = data_raw[each_result]['done'] + 1

        for each_key in data_raw.keys():
            data_raw[each_key]['missed'] = data_raw[each_key]['sum'] - data_raw[each_key]['leave'] - data_raw[each_key]['done']
            if data_raw[each_key]['sum'] != 0:
                data_raw[each_key]['done_percent'] = '{:.2%}'.format(data_raw[each_key]['done'] / data_raw[each_key]['sum'])
        data_raw_sorted = sorted(list(data_raw.values()), key=lambda x: float(x['done_percent'][:-1]),reverse=True)
        return JsonResponse(
            {
                'status': 200,
                'message': 'OK',
                'data': data_raw_sorted,
            }
        )

def leavevalid(check,user):
    '''

    :param check:
    :param user:
    :return:
    '''
    leave_list = models.leave.objects.filter(Q(checkID=check) & Q(username=user) & Q(status=1))
    for each_leave in leave_list:

        each_leave.valid = False

        each_leave.save()
