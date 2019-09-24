# -*- coding:utf-8 -*-
__author__ = 'sean'
__date__ = '2019/7/17 下午3:55'


import xadmin
from .models import Data,Addgroup,Addsystemname,Zhuanzhebushi,Yewuzerenbumen,czyylx,Zhuanze
from import_export import resources, widgets, fields
from import_export.admin import ImportExportMixin

class DataResource(resources.ModelResource):
    I6000 = fields.Field(column_name='I6000', attribute='I6000')
    class Meta:
        fields = ('I6000')



class DataAdmin(ImportExportMixin,object):
    list_display = ['groupname','system_name','I6000','xtjslx','bslx','ywbs','ywzrbs','yunxingzhuangtai','url','xtsxsj','xtxxsj','ip','xunijiqunip','date']
    search_fields = ['system_name__name','ip']
    list_filter = ['groupname__name']
    resources_class = DataResource

class AddgroupAdmin(object):
    search_fields = ['name']

xadmin.site.register(Data,DataAdmin)
xadmin.site.register(Addgroup,AddgroupAdmin)
xadmin.site.register(Addsystemname)
xadmin.site.register(Zhuanzhebushi)
xadmin.site.register(Yewuzerenbumen)
xadmin.site.register(czyylx)
xadmin.site.register(Zhuanze)

