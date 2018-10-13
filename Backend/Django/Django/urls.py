"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# Django/urls.py
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from CNU_MOA import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.all_notice),
    url(r'^1/1/(?P<in_year>[0-9]+)/(?P<in_month>[0-9]+)/(?P<in_day>[0-9]+)$', views.computer_administration_notice),
    url(r'^1/2/(?P<in_year>[0-9]+)/(?P<in_month>[0-9]+)/(?P<in_day>[0-9]+)$', views.computer_general_notice),
    url(r'^1/3/(?P<in_year>[0-9]+)/(?P<in_month>[0-9]+)/(?P<in_day>[0-9]+)$', views.computer_business_notice),
    url(r'^1/4/(?P<in_year>[0-9]+)/(?P<in_month>[0-9]+)/(?P<in_day>[0-9]+)$', views.computer_job_notice),
    url(r'^2/1/(?P<in_year>[0-9]+)/(?P<in_month>[0-9]+)/(?P<in_day>[0-9]+)$', views.dormitory_eun_notice),
    url(r'^2/2/(?P<in_year>[0-9]+)/(?P<in_month>[0-9]+)/(?P<in_day>[0-9]+)$', views.dormitory_back_notice),
]

urlpatterns = format_suffix_patterns(urlpatterns)