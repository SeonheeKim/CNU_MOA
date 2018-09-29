from django.db import models

# Create your models here.


class CrawlingData(models.Model):
    depart = models.IntegerField(default=-1)
    board = models.IntegerField(default=0)
    title = models.CharField(max_length=90)
    writer = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    link = models.CharField(null=True, max_length=300)
    views = models.IntegerField(default=0)
