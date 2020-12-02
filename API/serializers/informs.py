from rest_framework import serializers
from API.models import FA, FB


class FADetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FA
        exclude = ("id",)


class FBDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FB
        exclude = ("id",)
