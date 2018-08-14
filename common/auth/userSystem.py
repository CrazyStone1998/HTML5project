#coding = utf-8
#Redis

import redis
import datetime
import hashlib
from weCheck import models
from django.contrib.auth.hashers import check_password


re = redis.StrictRedis(host='127.0.0.1',port='6379',db=0)

class userSystem(object):

    def __init__(self,request,response=None,username=None,**kwargs):

        self.request = request
        self.response =response
        self.kwargs = kwargs
        self.username = username
        self.sessionID = None
        self.token = None

    def authentication(self,username,password):
        error = []
        userlogin = models.user.objects.get(username=username)
        if userlogin.exists():

            if check_password(password, userlogin.passwd):

                user = self.setCookieAndSession()

                return error

            else:
                error.append('The password is not right')
        else:
            error.append('The user is not exist')

        return error

    def testCookie(self):
        '''
        在login 中设置 request.session.set_test_cookie()
        如果返回 False 则说明 用户浏览器 关闭了 cookies
        如果返回 True 则说明 用户 浏览器 开启了 cookies
        :return:
        '''
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
            return True
        return False

    def getUserObject(self):
        '''
        返回 用户对象，
            有则说明用户已经登陆，并返回用户对象
            没有 就说明用户没有登陆
        :return:
        '''
        self.sessionID = self.request.COOKIES.get('sessionID')
        self.token = self.request.COOKIES.get('token')
        if re.exists(self.sessionID):
            if re.exists('sessionID_%s' %self.sessionID):
                map = re.hmget('sessionID_%s' %self.sessionID)
                if map.get('token') == self.token:
                    return map
        return None

    def setCookieAndSession(self):
        '''
        设置 cookie and session
        :return:
        '''

        self.sessionID = self.request.COOKIES.get('sessionID')
        if not self.sessionID:
            #set cookie

            hash = hashlib.md5()
            hash.update(datetime.datetime.now())
            token = hashlib.md5()
            token.update(datetime.datetime.now())
            hashID =hash.hexdigest()
            tokenID = token.hexdigest()

            self.response.set_cookie('sessionID',hashID)
            self.response.set_cookie('token',tokenID)
            self.sessionID = hashID
            self.token = tokenID

        if not re.exists('sessionID_%s' %self.sessionID):
            #set session
            re.hset('sessionID_%s' %self.sessionID,'username',self.username,'token',self.token)
        return True



