# CNU_MOA/admin.py
from django.contrib import admin
from .models import CrawlingData


class CrawlingAdmin(admin.ModelAdmin):
    list_display = ('depart', 'board', 'title', 'writer', 'link', 'views', 'year', 'month', 'day')


# Register your models here.
admin.site.register(CrawlingData)