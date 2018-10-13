
# CNU_MOA/serializers.py
from rest_framework import serializers

from .models import CrawlingData


class CrawlingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrawlingData
        fields = ('depart', 'board', 'title', 'writer', 'link', 'views', 'year', 'month', 'day')

        def create(self, validated_data):
            return CrawlingData.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.depart = validated_data.get('depart', instance.depart)
            instance.board = validated_data.get('board', instance.board)
            instance.title = validated_data.get('title', instance.title)
            instance.writer = validated_data.get('writer', instance.writer)
            instance.link = validated_data.get('link', instance.link)
            instance.views = validated_data.get('views', instance.views)
            instance.year = validated_data.get('year', instance.year)
            instance.month = validated_data.get('month', instance.month)
            instance.day = validated_data.get('day', instance.day)
            instance.save()
            return instance
