# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from AppSoftResources.models import Data
# Create your models here.

class System(Data):
    class Meta:
        verbose_name = '应用系统'
        verbose_name_plural = verbose_name
        proxy = True

class Middleware(Data):
    class Meta:
        verbose_name = '中间件'
        verbose_name_plural = verbose_name
        proxy = True

class Database(Data):
    class Meta:
        verbose_name = '应用部署'
        verbose_name_plural = verbose_name
        proxy = True

class Url(models.Model):
    name = models.CharField(max_length=10)