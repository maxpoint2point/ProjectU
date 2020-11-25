from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView

from UTMWatch.models import Workplace
from UTMWatch.serializers import WorkplaceCreateSerializer, WorkplaceDetailSerializer, WorkplaceListSerializer
from UTMWatch.service.filters import WorkPlaceFilter
from UTMWatch.tasks import exchange
from rest_framework.response import Response


class WorkPlaceCreateView(generics.CreateAPIView):
    """Создание рабочего места"""
    serializer_class = WorkplaceCreateSerializer
    queryset = Workplace.objects.all()


class WorkPlaceListView(generics.ListAPIView):
    """Список рабочих мест"""
    serializer_class = WorkplaceListSerializer
    queryset = Workplace.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WorkPlaceFilter


class WorkPlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Подробности рабочего места"""
    serializer_class = WorkplaceDetailSerializer
    queryset = Workplace.objects.all()


class Exchange(APIView):
    """Запуск обмена с УТМ"""
    def get(self, request, pk):
        workplace = Workplace.objects.get(pk=pk)
        exchange.delay(workplace.utm_host, workplace.utm_port)
        return Response()
