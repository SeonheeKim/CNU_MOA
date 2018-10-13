# CNU_MOA/models.py
from django.db import models


class CrawlingData(models.Model):
    depart = models.IntegerField(default=-1)
    board = models.IntegerField(default=0)
    title = models.CharField(max_length=90)
    writer = models.CharField(max_length=20)
    link = models.CharField(null=True, max_length=300)
    views = models.IntegerField(default=0)
    year = models.IntegerField(default=2000)
    month = models.IntegerField(default=1)
    day = models.IntegerField(default=1)