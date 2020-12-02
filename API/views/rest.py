from API.models import RestHeader
from rest_framework import generics
from API.serializers import RestHeaderListSerializer, RestHeaderDetailSerializer, RestHeaderCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend

from API.service.filters import RestsFilter


class RestListView(generics.ListAPIView):
    """Список запрошенных остатков"""
    serializer_class = RestHeaderListSerializer
    queryset = RestHeader.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RestsFilter


class RestDetailView(generics.RetrieveDestroyAPIView):
    """Остатки алкогольной продукции"""
    serializer_class = RestHeaderDetailSerializer
    queryset = RestHeader.objects.all()


class RestCreateView(generics.CreateAPIView):
    """Запрос остатков"""
    serializer_class = RestHeaderCreateSerializer
    queryset = RestHeader.objects.all()
