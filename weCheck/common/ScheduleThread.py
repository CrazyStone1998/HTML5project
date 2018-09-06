# coding=utf-8

from weCheck.models import check
from datetime import datetime
import time
import threading
import inspect
import ctypes


# 线程中止
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

        now = datetime.strptime(time.strftime('%H:%M'), '%H:%M')
        target = datetime.strptime(self.startUpTime, '%H:%M')

        # 计算天数
        weekNow = datetime.now().weekday()

        day = self.caclulate(weekNow, self.repeat)

        # 计算时间 偏差
        d = (target - now).days
        if d < 0:
            s = day * 24 * 60 * 60 - (now - target).seconds

        else:
            if weekNow in self.repeat:
                s = (target - now).seconds
            else:
                s = day * 24 * 60 * 60 + (target - now).seconds

        print('沉睡时间%s' % s)
        # 沉睡
        time.sleep(s)

        # 唤醒后创建 check
        self.check_open_close(self.group, self.duration)

        while True:

            now = datetime.strptime(time.strftime('%H:%M'),'%H:%M')
            target = datetime.strptime(self.startUpTime, '%H:%M')

            # 计算天数
            weekNow = datetime.now().weekday()

            day = self.caclulate(weekNow,self.repeat)

            # 计算时间 偏差
            d = (target-now).days
            if d < 0 :
                s = day*24*60*60 - (now-target).seconds

            else:

                s = day*24*60*60 + (target-now).seconds

            print('沉睡时间%s' % s)
            #沉睡
            time.sleep(s)

            #唤醒后创建 check
            self.check_open_close(self.group,self.duration)


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
        print('success')
        # 开启一个 新的签到
        new = check.checkObject(group=group, duration=duration)
        time.sleep(int(duration)*60)
        new.enable = False
        new.save()


def addScheduleThread(name,group,startUpTime,duration,repeat):

    thread1 = scheduleThread(name=name,group=group,startUpTime=startUpTime,duration=duration,repeat=repeat)
    print('-------------%s' % thread1.getName())
    thread1.start()
    print(threading.enumerate())

def deleteScheduleThread(name):

    for thread in threading.enumerate():
        if thread.getName() == name:
            stop_thread(thread)

