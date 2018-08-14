# coding=utf-8


from django.conf import settings
from common.auth.userSystem import userSystem
from django.http import JsonResponse


class authenticationMiddleWare(object):
    #判断登陆 权限控制
    def process_request(self,request):
        '''
        Request 预处理函数
        :param request:
        :return:
        '''
        context = []
        if request.method == 'GET':
            requestData = request.GET
        else:
            requestData = request.POST
        request.session['errmsg'] = ''
        #如果用户没有认证，限制访问
        if not request.session.has_key('sessionID') and not request.session.has_key('token') \
                and 'register' not in request.path and 'login' not in request.path:
            context.append('Please login')
            return JsonResponse({
                'status':403,
                'message':context,
            })
        elif request.session.has_key('sessionID') and request.session.has_key('token') \
                and 'register' not in request.path and 'logout' not in request.path:
            try:

                user = userSystem(request)
                if not user.getUserObject():
                    context.append('Please login')
                    return JsonResponse({
                        'status': 403,
                        'message': context,
                    })
                '''
                
                权限管理
                
                pass
            
            
            '''
            except Exception as e:
                context.append('somthing is wrong')
                return JsonResponse({
                    'status': 202,
                    'message': context,
                })

        # 用户已登录，而且url是login,将转到首页
        if request.session.has_key('sessionID') and request.session.has_key('token') and 'login' in request.path:
                context.append('Repeat login')
                return JsonResponse({
                    'status': 202,
                    'message': context,
                })



