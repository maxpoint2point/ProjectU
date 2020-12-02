from API.models import OU
from rest_framework import generics

from API.serializers import OUDetailSerializer, OUListSerializer


class OUCreateView(generics.CreateAPIView):
    """Создание организации"""
    serializer_class = OUDetailSerializer
    queryset = OU.objects.all()


class OUDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Подробности об организации"""
    serializer_class = OUDetailSerializer
    queryset = OU.objects.all()


class OUListView(generics.ListAPIView):
    """Список организаций"""
    serializer_class = OUListSerializer
    queryset = OU.objects.all()
