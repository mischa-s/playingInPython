from __future__ import unicode_literals

from django.db import models

# Create your models here.
class trialapp(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.TextField(max_length=10000, blank=True, null=True)
    auther = models.TextField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=250000, blank=True, null=True)
