from django.contrib import admin
from django.urls import re_path,include,path
from weCheck import views

app_name = 'weCheck'
urlpatterns = [

    re_path(r'^hasLoggedIn/*$',     views.hasLoggedIn,    name='hasLoggedIn'),
    re_path(r'^login/*$',           views.login,          name='login'),           # access: all
    re_path(r'^logout/*$',          views.logout,         name='logout'),          # access: all
    re_path(r'^register/*$',        views.register,       name='register'),        # access: all
    re_path(r'^user/*$',            views.user_splitter, {'GET': views.userGET, 'POST': views.userPOST}, name='user'),            # access: all
    re_path(r'^group/*$',           views.group,          name='group'),           # access: all
    re_path(r'^group/list/*$',      views.grouplist,      name='grouplist'),       # access: all
    re_path(r'^group/add/*$',       views.groupadd,       name='groupadd'),        # access: manager
    re_path(r'^group/join/*$',      views.groupjoin,      name='groupjoin'),       # access: user
    re_path(r'^group/quit/*$',      views.groupquit,      name='groupquit'),       # access: user
    re_path(r'^group/update/*$',    views.groupupdate,    name='groupupdate'),     # access: manager
    re_path(r'^group/delete/*$',    views.groupdelete,    name='groupdelete'),     # access: manager
    re_path(r'^check/status/*$',    views.checkstatus,    name='checkstatus'),     # access: user
    re_path(r'^check/check/*$',     views.checkcheck,     name='checkcheck'),      # access: user
    re_path(r'^check/enable/*$',    views.checkenable,    name='checkenable'),     # access: manager
    re_path(r'^check/disable/*$',   views.checkdisable,   name='checkdiable'),     # access: manager
    re_path(r'^schedule/*$',        views.schedule,       name='schedule'),      # access: manager
    re_path(r'^schedule/add/*$',    views.scheduleadd,    name='scheduleadd'),     # access: manager
    re_path(r'^schedule/update/*$', views.scheduleupdate, name='scheduleupdate'),  # access: manager
    re_path(r'^schedule/delete/*$', views.scheduledelete, name='scheduledelete'),  # access: manager
    re_path(r'^group/leave/*$',     views.groupleave,     name='groupleave'),
    re_path(r'^leave/*$',           views.leave,          name='leave'),

    re_path(r'^group/(?P<groupID>[\d\w]{6})/user/(?P<username>.+)/*$', views.userhistory, name='userhistory'),# access:user
    re_path(r'^history/(?P<id>[\d\w]{6}/*$)', views.history, name='history'),  # access : all
    re_path(r'^record/(?P<checkID>[\d]+)/*$',views.record,name='record'),# access: manager


]
