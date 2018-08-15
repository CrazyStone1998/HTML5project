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
        '''
        用户 登陆 认 证
        :param username:
        :param password:
        :return:
        '''
        error = []
        userlogin = models.user.objects.get(username=username)
        if userlogin is not None:

            if check_password(password, userlogin.passwd):

                self.setCookieAndSession()

                return error

            else:
                error.append('The password is not right')
        else:
            error.append('The user is not exist')

        return error

    def getUsername(self):
        '''
        获取用户 username
        :return:
        '''
        self.sessionID = self.request.session.get('sessionID')

        if re.exists('sessionID_%s' % self.sessionID):

            return re.hget('sessionID_%s' %self.sessionID,'username').decode()

        else:
            return None

    def delCache(self):
        '''
        清楚 缓存 session登陆信息
        :return:
        '''
        if self.request.session.has_key('sessionID') and self.request.session.has_key('token'):
            sessionID = self.request.session.get('sessionID')

            if re.exists('sessionID_%s' % sessionID):
                re.hdel('sessionID_%s' % sessionID,['username','token'])
            return True
        return False
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
        self.sessionID = self.request.session.get('sessionID')
        self.token = self.request.session.get('token')

        if re.exists('sessionID_%s' %self.sessionID):
            token_redis = re.hget('sessionID_%s' %self.sessionID,'token').decode()
            username_redis = re.hget('sessionID_%s' %self.sessionID,'username').decode()

            if token_redis == self.token:
                return username_redis
        return None

    def setCookieAndSession(self):
        '''
        设置 cookie and session
        :return:
        '''

        self.sessionID = self.request.session.get('sessionID')
        if not self.sessionID:
            #set cookie

            hash = hashlib.md5()
            token = hashlib.md5()
            hashID =hash.hexdigest()
            tokenID = token.hexdigest()

            self.request.session['sessionID'] = hashID
            self.request.session['token'] = tokenID
            self.sessionID = hashID
            self.token = tokenID

        if not re.exists('sessionID_%s' %self.sessionID):
            #set session
            re.hmset('sessionID_%s' %self.sessionID,{'username':self.username,'token':self.token})
        return True



