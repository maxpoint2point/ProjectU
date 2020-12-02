from rest_framework import serializers
from API.models import Workplace
from API.serializers import OUListSerializer


class WorkplaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = ("id", "name", "fsrar", "ou")


class WorkplaceDetailSerializer(serializers.ModelSerializer):
    ou = OUListSerializer(read_only=True)

    class Meta:
        model = Workplace
        fields = "__all__"


class WorkplaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        exclude = ("fsrar",)
