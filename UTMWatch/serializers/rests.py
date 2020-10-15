from rest_framework import serializers
from UTMWatch.models import RestHeader, ShopPosition, StockPosition


class ShopPositionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopPosition
        fields = "__all__"


class StockPositionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPosition
        fields = "__all__"


class RestHeaderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestHeader
        fields = ("date", "type", "status")


class RestHeaderDetailSerializer(serializers.ModelSerializer):
    stock = StockPositionDetailSerializer(many=True, read_only=True)
    shop = ShopPositionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = RestHeader
        fields = "__all__"


class RestHeaderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestHeader
        fields = ("type", "workplace")
