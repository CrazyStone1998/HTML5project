# coding=utf-8
from __future__ import absolute_import
import redis
import time
from HTML5project.celery import app
from celery.schedules import crontab
from celery.task import periodic_task
from weCheck.models import check
# redis 对象 cache
re = redis.StrictRedis(host='127.0.0.1',port='6379',db=0)

@app.task
def schedule_open_check(scheduleId,group,startUpTime,duration,repeat):
    '''
    函数 用于 周期开启签到
                关闭签到
    :param scheduleId:
    :param group:
    :param startUpTime:
    :param duration:
    :param repeat:
    :return:
    '''
    # 设置 cache 记录任务id
    re.set(scheduleId, schedule_open_check.request.id)
    print("------id------%s" % schedule_open_check.request.id)
    print('------id------%s' % re.get(scheduleId))
    # 设置 任务周期时间
    t = startUpTime.split(':')
    hour = int(t[0])
    minute = int(t[1])
    day_of_week = [b%7 for b in [int(a) for a in repeat.split(',')]]
    # 定义 周期函数
    @periodic_task(run_every=crontab(minute=minute,hour=hour,day_of_week=day_of_week))
    def open_check():
        # 开启签到
        new = check.checkObject(group=group,duration=duration)
        # 等待签到结束
        time.sleep(int(duration)*60)
        # 关闭签到
        new.enable = False
        new.save()
    # 返回函数
    return open_check

@app.task
def schedule_close_check(scheduleId):
    '''
    关闭当前 开启的签到计划周期函数
    :param scheduleId:
    :return:
    '''
    # 获取 周期任务函数id
    id = re.get(scheduleId)
    # 停止 周期任务函数
    app.control.revoke(id=id,terminate=True)





