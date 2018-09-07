# coding=utf-8

from weCheck.models import check
import datetime
import time
import threading
import inspect
import ctypes

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)



# 定义线程类
class scheduleThread(threading.Thread):

    def __init__(self,name,group,startUpTime,duration,repeat):
        threading.Thread.__init__(self)
        self.name = name
        self.group = group
        self.startUpTime = startUpTime
        self.duration = duration
        self.repeat = [(b - 1) for b in [int(a) for a in repeat.split(',')]]


    def run(self):

        self.open_check()

    def open_check(self):

        # 当前时间
        now = datetime.datetime.strptime(time.strftime('%Y%m%d%H:%M'), '%Y%m%d%H:%M')
        # 计算天数
        weekNow = datetime.datetime.now().weekday()
        day = self.caclulate(weekNow, self.repeat)
        # 获取当天 签到开启时间
        dateTarget = time.strftime('%Y%m%d') + self.startUpTime
        dateTarget = datetime.datetime.strptime(dateTarget, '%Y%m%d%H:%M')
        # 计算 日期
        # 计算时间 偏差

        if (dateTarget-now).days < 0 and weekNow in self.repeat:
            dateTarget = dateTarget+datetime.timedelta(days=day)

        while True:
            print('lll')
            if time.strftime('%Y%m%d%H:%M') == dateTarget.strftime('%Y%m%d%H:%M'):

                self.check_open_close(self.group, self.duration)
                break
            else:
                time.sleep(1)

        while True:

            # 计算天数
            weekNow = datetime.datetime.now().weekday()
            day = self.caclulate(weekNow, self.repeat)

            # 获取下次 签到开启时间
            dateTarget = time.strftime('%Y%m%d') + self.startUpTime
            dateTarget = datetime.datetime.strptime(dateTarget,'%Y%m%d%H:%M')+datetime.timedelta(days=day)

            while True:

                if datetime.datetime.now() == dateTarget.strftime('%Y%m%d%H:%M'):
                    print('success')
                    self.check_open_close(self.group, self.duration)
                    break
                else:
                    time.sleep(5)
        #
        # # 计算时间 偏差
        # d = (target - now).days
        # if d < 0:
        #     s = day * 24 * 60 * 60 - (now - target).seconds
        #
        # else:
        #     if weekNow in self.repeat:
        #         s = (target - now).seconds
        #     else:
        #         s = day * 24 * 60 * 60 + (target - now).seconds
        #
        # print('沉睡时间%s' % s)
        # # 沉睡
        # time.sleep(s)
        #
        # # 唤醒后创建 check
        # self.check_open_close(self.group, self.duration)
        #
        # while True:
        #
        #     now = datetime.strptime(time.strftime('%H:%M'),'%H:%M')
        #     target = datetime.strptime(self.startUpTime, '%H:%M')
        #
        #     # 计算天数
        #     weekNow = datetime.now().weekday()
        #
        #     day = self.caclulate(weekNow,self.repeat)
        #
        #     # 计算时间 偏差
        #     d = (target-now).days
        #     if d < 0 :
        #         s = day*24*60*60 - (now-target).seconds
        #
        #     else:
        #
        #         s = day*24*60*60 + (target-now).seconds
        #
        #     print('沉睡时间%s' % s)
        #     #沉睡
        #     time.sleep(s)
        #
        #     #唤醒后创建 check
        #     self.check_open_close(self.group,self.duration)


    def caclulate(self,weekday,repeat):

        count = 1
        while True:
            weekday = (weekday+1) % 7
            if weekday not in repeat:
                count = count + 1
            else:
                break
        return count


    def check_open_close(self,group,duration):
        # 开启一个 新的签到
        new = check.checkObject(group=group, duration=duration)
        # 当前时间
        now = datetime.datetime.strptime(time.strftime('%Y%m%d%H:%M'), '%Y%m%d%H:%M')
        dateTarget = now + datetime.timedelta(minutes=int(duration))
        while True:
            if time.strftime('%Y%m%d%H:%M') == dateTarget.strftime('%Y%m%d%H:%M'):
                new.enable = False
                new.save()
                break
            else:
                time.sleep(5)



def addScheduleThread(name,group,startUpTime,duration,repeat):

    thread1 = scheduleThread(name=name,group=group,startUpTime=startUpTime,duration=duration,repeat=repeat)
    thread1.start()

def deleteScheduleThread(name):

    for thread in threading.enumerate():
        if thread.getName() == name:
            stop_thread(thread)

