# -*- coding:utf-8 -*-
__author__ = 'sean'
__date__ = '2019/7/17 下午4:59'
import xadmin
from xadmin import views
from .models import System, Middleware, Database,Url
from django.db.models import Q
from django.shortcuts import render



# 'system_name','group','ip','url','I6000','zhujileixing','jifangxinxi','czyylx','czyymc','ywzzr','lxdh'
class SystemAdmin(object):
    list_display = ['system_name', 'groupname', 'ip', 'I6000', 'xtjslx', 'bslx', 'ywbs', 'ywzrbs', 'yunxingzhuangtai',
                    'zhkx', 'jfxx', 'fwqms', 'yjpp', 'yjxh', 'tyrq', 'usedate', 'czyylx', 'chzyymc',
                    'url', 'ywzzr', 'lxdh', 'zhuanze', 'date']
    search_fields = ['system_name__name', 'ip']
    list_filter = ['groupname__name']


'''
class MiddlewareAdmin(object):
    list_display = ['system_name','group','ip','url','czyylx','czyymc','ywzzr','lxdh','czyybb']
    search_fields = []
    list_filter = []


    def queryset(self):
        qs = super(MiddlewareAdmin,self).queryset()
        qs = qs.filter(czyylx="中间件")
        return qs
'''


class DatabaseAdmin(object):
    list_display = ['system_name', 'czxtlx', 'czxtbb', 'czyylx', 'chzyymc', 'czyybb', 'czyycxazml', 'ywzzr', 'lxdh',
                    'groupname', 'ip', 'date']
    search_fields = ['czyylx__name','chzyymc']
    list_filter = ['czyylx__name']


class UrlAdmin(object):
    object_list_template = 'sean.html'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "华中科技运维管理系统"
    site_footer = "华中科技运维管理系统"
    menu_style = "accordion"


xadmin.site.register(views.CommAdminView, GlobalSetting)

xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(System, SystemAdmin)
# xadmin.site.register(Middleware,MiddlewareAdmin)
xadmin.site.register(Database, DatabaseAdmin)
xadmin.site.register(Url,UrlAdmin)