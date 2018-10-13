# CNU_MOA/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CrawlingData

from .serializers import CrawlingSerializer


@api_view(['GET', 'POST'])
def all_notice(request, format=None):
    if request.method == 'GET':
        event = CrawlingData.objects.all()
        serializer = CrawlingSerializer(event, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CrawlingSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def computer_administration_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        event = CrawlingData.objects.filter(depart=1, board=1, year__gte=in_year)

        value_list = event.values_list('year', flat=True)

        for i in range(0, len(value_list)):
            if int(value_list[i]) == int(in_year):
                if int(event[i].month) < int(in_month):
                    print("1")

        serializer = CrawlingSerializer(event, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CrawlingSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def computer_general_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        event = CrawlingData.objects.filter(depart=1, board=2, year__gte=in_year)
        serializer = CrawlingSerializer(event, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CrawlingSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def computer_business_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        event = CrawlingData.objects.filter(depart=1, board=3, year__gte=in_year)
        serializer = CrawlingSerializer(event, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CrawlingSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def computer_job_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        event = CrawlingData.objects.filter(depart=1, board=4, year__gte=in_year)
        serializer = CrawlingSerializer(event, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CrawlingSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def dormitory_eun_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        event = CrawlingData.objects.filter(depart=2, board=1, year__gte=in_year)
        serializer = CrawlingSerializer(event, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CrawlingSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def dormitory_back_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        event = CrawlingData.objects.filter(depart=2, board=2, year__gte=in_year)
        serializer = CrawlingSerializer(event, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CrawlingSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

