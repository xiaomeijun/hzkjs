from import_export.admin import ImportExportMixin
from django.contrib import admin
from import_export import resources, widgets, fields
from .models import Addgroup,Addsystemname,Zhuanzhebushi,Yewuzerenbumen,czyylx,Zhuanze,Data
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
# Register your models here.

class DataResource(resources.ModelResource):
    groupname = fields.Field( widget=widgets.ForeignKeyWidget(Addgroup, 'name'))
    system_name = fields.Field(column_name='system_name', attribute='system_name', widget=widgets.ForeignKeyWidget(Addsystemname, 'name'))
    I6000 = fields.Field(column_name='I6000', attribute='I6000')
    class Meta:
        fields = ('groupname','system_name','I6000')

class DataAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['groupname','system_name','I6000','xtjslx','bslx','ywbs','ywzrbs','yunxingzhuangtai','url','xtsxsj','xtxxsj','ip','xunijiqunip','date']
    resources_class = DataResource


admin.site.register(Data,DataAdmin)