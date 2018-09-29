# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-29 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CNU_MOA', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crawlingdata',
            name='content',
        ),
        migrations.RemoveField(
            model_name='crawlingdata',
            name='viewCount',
        ),
        migrations.AddField(
            model_name='crawlingdata',
            name='board',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='crawlingdata',
            name='depart',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='crawlingdata',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crawlingdata',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='crawlingdata',
            name='title',
            field=models.CharField(max_length=90),
        ),
    ]
