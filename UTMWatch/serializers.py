from rest_framework import serializers
from UTMWatch.models import WorkPlace, OU


class OUSerializer(serializers.ModelSerializer):
    class Meta:
        model = OU
        fields = "__all__"


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = "__all__"


class WorkplaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        exclude = ("fsrar",)
