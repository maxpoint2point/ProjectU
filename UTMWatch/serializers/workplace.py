from rest_framework import serializers
from UTMWatch.models import WorkPlace
from UTMWatch.serializers import OUListSerializer


class WorkplaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ("id", "name", "fsrar", "ou")


class WorkplaceDetailSerializer(serializers.ModelSerializer):
    ou = OUListSerializer(read_only=True)

    class Meta:
        model = WorkPlace
        fields = "__all__"


class WorkplaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        exclude = ("fsrar",)
