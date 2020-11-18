from rest_framework import serializers
from UTMWatch.models import Producer


class ProducerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        exclude = ("id",)
