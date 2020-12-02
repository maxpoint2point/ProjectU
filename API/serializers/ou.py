from rest_framework import serializers
from API.models import OU


class OUDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OU
        fields = "__all__"


class OUListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OU
        fields = ('id', 'name', 'inn',)
