from rest_framework import serializers
from API.models import RestHeader, ShopPosition, StockPosition
from API.serializers.informs import FADetailSerializer, FBDetailSerializer
from API.serializers.alcohol import AlcoholDetailSerializer


class ShopPositionDetailSerializer(serializers.ModelSerializer):
    alcohol = AlcoholDetailSerializer(read_only=True)

    class Meta:
        model = ShopPosition
        fields = "__all__"


class StockPositionDetailSerializer(serializers.ModelSerializer):
    fa = FADetailSerializer(read_only=True)
    fb = FBDetailSerializer(read_only=True)
    alcohol = AlcoholDetailSerializer(read_only=True)

    class Meta:
        model = StockPosition
        fields = "__all__"


class RestHeaderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestHeader
        fields = ("id", "date", "type", "status")


class RestHeaderDetailSerializer(serializers.ModelSerializer):
    restheader_stockposition = StockPositionDetailSerializer(many=True, read_only=True)
    restheader_shopposition = ShopPositionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = RestHeader
        fields = "__all__"


class RestHeaderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestHeader
        fields = ("type", "workplace")
