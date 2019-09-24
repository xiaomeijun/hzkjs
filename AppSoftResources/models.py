# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Addgroup(models.Model):
    name = models.CharField(u'工作组', max_length=20)
    class Meta:
        verbose_name_plural = '添加工作组'
    def __unicode__(self):
        return self.name


class Addsystemname(models.Model):
    name = models.CharField(u'系统名称', max_length=20)
    class Meta:
        verbose_name_plural = '添加系统名称'
    def __unicode__(self):
        return self.name

class Zhuanzhebushi(models.Model):
    name = models.CharField(u'运维责任部室', max_length=20)
    class Meta:
        verbose_name_plural = '添加运维责任部室'
    def __unicode__(self):
        return self.name

class Yewuzerenbumen(models.Model):
    name = models.CharField(u'业务责任部门', max_length=20)
    class Meta:
        verbose_name_plural = '添加业务责任部门'
    def __unicode__(self):
        return self.name


class czyylx(models.Model):
    name = models.CharField(u'承载应用类型', max_length=20)
    class Meta:
        verbose_name_plural = '添加应用类型'
    def __unicode__(self):
        return self.name

class Zhuanze(models.Model):
    name = models.CharField(u'专责', max_length=20)
    class Meta:
        verbose_name_plural = '添加专责'
    def __unicode__(self):
        return self.name



class Data(models.Model):
    groupname = models.ForeignKey(Addgroup, verbose_name="工作组")
    system_name = models.ForeignKey(Addsystemname, verbose_name="系统名称")
    I6000 = models.CharField(max_length=10, choices=(('yes', u'是'), ('no', u'否')))
    xtjslx = models.CharField(max_length=10, choices=(('tt', u'统推 '), ('zj', u'自建')), verbose_name="系统建设类型")
    bslx = models.CharField(max_length=20, verbose_name="部署类型")
    ywbs = models.ForeignKey(Zhuanzhebushi, verbose_name="运维责任部室")
    ywzrbs = models.ForeignKey(Yewuzerenbumen, verbose_name="业务责任部门")
    yunxingzhuangtai = models.CharField(max_length=10, choices=(('jsz', u'建设中 '), ('zy', u'在运')), verbose_name="业务责任部门")
    url = models.CharField(u'应用访问URL', max_length=100, blank=True, null=True)
    xtsxsj = models.DateField(u'系统上线时间', blank=True, null=True)
    xtxxsj = models.DateField(u'系统下线时间', blank=True, null=True)
    ip = models.CharField(u'IP地址', max_length=100)
    xunijiqunip = models.CharField(u'集群IP', max_length=100,blank=True,null=True)
    xitongsuoshuwangluo = models.CharField(max_length=10,choices=(('jsz',u'内网'),('zy',u'外网')),verbose_name="系统所属网络")
    zjczzb = models.CharField(u'主机承载指标项', max_length=100)
    zhkx = models.CharField(max_length=10,choices=(('wlj',u'物理机'),('xnj',u'虚拟机')),verbose_name="主机类型")
    jfxx = models.CharField(u'机房信息', max_length=100, blank=True, null=True)
    fwqms = models.CharField(u'服务器描述', max_length=100, blank=True, null=True)
    yjpp = models.CharField(u'硬件品牌', max_length=100, blank=True, null=True)
    yjxh = models.CharField(u'硬件型号', max_length=100, blank=True, null=True)
    tyrq = models.DateField(u'投运日期', blank=True, null=True)
    usedate = models.CharField(u'使用年限', max_length=100, blank=True, null=True)
    czxtlx = models.CharField(max_length=10, verbose_name="操作系统类型")
    czxtbb = models.CharField(u'操作系统版本', max_length=100)
    czyylx = models.ForeignKey(czyylx, verbose_name="承载应用类型")
    chzyymc = models.CharField(u'承载应用名称', max_length=100)
    czyybb = models.CharField(u'承载应用版本', max_length=100, blank=True, null=True)
    czyycxazml = models.CharField(u'承载应用程序安装目录', max_length=100, blank=True, null=True)
    fwdkqd = models.CharField(u'服务端口清单', max_length=100)
    ywzzr = models.CharField(u'运维责任人', max_length=100)
    lxdh = models.CharField(u'联系电话', max_length=100)
    ywmail = models.CharField(u'邮箱', max_length=100)
    zhuanze = models.ForeignKey(Zhuanze, verbose_name="专责")
    zhuanzephone = models.CharField(u'专责电话', max_length=100)
    zzmail = models.CharField(u'专责邮箱', max_length=100)
    zongbulianxiren = models.CharField(u'总部联系人', max_length=100, blank=True, null=True)
    zongbulianxi = models.CharField(u'总部联系方式', max_length=100, blank=True, null=True)
    youxiang = models.CharField(u'总部邮箱', max_length=100, blank=True, null=True)
    yanfadan = models.CharField(u'研发单位名称', max_length=100, blank=True, null=True)
    beizhu = models.TextField(u'备注', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = '资产信息录入'


class Url(models.Model):
    name = models.CharField(max_length=10)


