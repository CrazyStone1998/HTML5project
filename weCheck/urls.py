from django.contrib import admin
from django.urls import path,include
from weCheck import views

app_name = 'weCheck'
urlpatterns = [
    path('index/',           views.index,          name='index'),
    path('login/',           views.login,          name='login'),           #access: all
    path('logout/',          views.logout,         name='logout'),          #access: all
    path('register/',        views.register,       name='register'),        #access: all
    path('user/',            views.user,           name='user'),            #access: all
    path('group/',           views.group,          name='group'),           #access: all
    path('group/list/',      views.grouplist,      name='grouplist'),       #access: all
    path('group/add/',       views.groupadd,       name='groupadd'),        #access: manager
    path('group/join/',      views.groupjoin,      name='groupjoin'),       #access: user
    path('group/quit/',      views.groupquit,      name='groupquit'),       #access: user
    path('group/update/',    views.groupupdate,    name='groupupdate'),     #access: manager
    path('group/delete/',    views.groupdelete,    name='groupdelete'),     #access: manager
    path('check/status/',    views.checkstatus,    name='checkstatus'),     #access: user
    path('check/check/',     views.checkcheck,     name='checkcheck'),      #access: user
    path('check/enable/',    views.checkenable,    name='checkenable'),     #access: manager
    path('check/disable/',   views.checkdisable,   name='checkdiable'),     #access: manager
    path('schedule/',        views.schedule,       name='schedule'  ),      #access: manager
    path('schedule/add/',    views.scheduleadd,    name='scheduleadd'),     #access: manager
    path('schedule/update/', views.scheduleupdate, name='scheduleupdate'),  #access: manager
    path('schedule/delete/', views.scheduledelete, name='scheduledelete'),  #access: manager

]
