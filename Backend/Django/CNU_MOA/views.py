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


def basic_get(depart, board, in_year, in_month, in_day):
    event = CrawlingData.objects.filter(depart=depart, board=board, year__gte=in_year)

    value_list = event.values_list('year', flat=True)
    event_list = list()

    for i in range(0, len(value_list)):
        if event[i].year == int(in_year):
            # 게시년도가 같아도 월이 이전이면 삭제
            if event[i].month < int(in_month):
                event_list.append(event[i])

            # 게시월이 같을 경우
            elif event[i].month == int(in_month):
                if event[i].day < int(in_day):
                    event_list.append(event[i])

    # 게시년월일에 따라 최신이 아닌 정보들 제거
    for i in range(0, len(event_list)):
        event_list[i].delete()

    serializer = CrawlingSerializer(event, many=True)

    try:
        print(serializer.data)

        for i in range(0, len(event_list)):
            event_list[i].save()

    except IndexError:
        pass

    return serializer


@api_view(['GET', 'POST'])
def computer_administration_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        serializer = basic_get(depart=1, board=1, in_year=in_year, in_month=in_month, in_day=in_day)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass
        """
        serializer = CrawlingSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        """


@api_view(['GET', 'POST'])
def computer_general_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        serializer = basic_get(depart=1, board=2, in_year=in_year, in_month=in_month, in_day=in_day)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass


@api_view(['GET', 'POST'])
def computer_business_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        serializer = basic_get(depart=1, board=3, in_year=in_year, in_month=in_month, in_day=in_day)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass


@api_view(['GET', 'POST'])
def computer_job_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        serializer = basic_get(depart=1, board=4, in_year=in_year, in_month=in_month, in_day=in_day)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass


@api_view(['GET', 'POST'])
def dormitory_eun_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        serializer = basic_get(depart=2, board=1, in_year=in_year, in_month=in_month, in_day=in_day)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass


@api_view(['GET', 'POST'])
def dormitory_back_notice(request, in_year, in_month, in_day, format=None):
    if request.method == 'GET':
        serializer = basic_get(depart=2, board=2, in_year=in_year, in_month=in_month, in_day=in_day)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass
