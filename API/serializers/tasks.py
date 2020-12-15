from rest_framework import serializers
from django_celery_beat.models import IntervalSchedule
from API.models import Tasks


class IntervalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = ("every", "period")


class PeriodicTaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"


class PeriodicTaskListSerializer(serializers.ModelSerializer):
    interval = IntervalDetailSerializer()

    class Meta:
        model = Tasks
        fields = ("id", "name", "task", "interval")
