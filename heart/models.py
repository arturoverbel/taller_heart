# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Heart(models.Model):
    registered = models.DateTimeField('date registered')
    dataA = models.FloatField(default=0)
    dataB = models.FloatField(default=0)
