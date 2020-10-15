from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from UTMWatch.models import Workplace
from UTMWatch.serializers import WorkplaceCreateSerializer, WorkplaceDetailSerializer, WorkplaceListSerializer
from UTMWatch.service import WorkPlaceFilter


class WorkPlaceCreateView(generics.CreateAPIView):
    serializer_class = WorkplaceCreateSerializer
    queryset = Workplace.objects.all()


class WorkPlaceListView(generics.ListAPIView):
    serializer_class = WorkplaceListSerializer
    queryset = Workplace.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WorkPlaceFilter


class WorkPlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkplaceDetailSerializer
    queryset = Workplace.objects.all()
