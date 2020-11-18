from rest_framework import serializers
from UTMWatch.models import Alcohol, VCode
from .producers import ProducerDetailSerializer


class VCodeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VCode
        exclude = ("id",)


class AlcoholDetailSerializer(serializers.ModelSerializer):
    producer = ProducerDetailSerializer(read_only=True)
    v_code = VCodeDetailSerializer(read_only=True)

    class Meta:
        model = Alcohol
        exclude = ("id",)
