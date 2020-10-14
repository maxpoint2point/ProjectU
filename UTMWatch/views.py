from .models import WorkPlace, OU
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    WorkplaceCreateSerializer,
    WorkplaceDetailSerializer,
    OUDetailSerializer,
    OUListSerializer,
    WorkplaceListSerializer
)
from .service import WorkPlaceFilter


class OUCreateView(generics.CreateAPIView):
    serializer_class = OUDetailSerializer
    queryset = OU.objects.all()


class OUDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OUDetailSerializer
    queryset = OU.objects.all()


class OUListView(generics.ListAPIView):
    serializer_class = OUListSerializer
    queryset = OU.objects.all()


class WorkPlaceCreateView(generics.CreateAPIView):
    serializer_class = WorkplaceCreateSerializer
    queryset = WorkPlace.objects.all()


class WorkPlaceListView(generics.ListAPIView):
    serializer_class = WorkplaceListSerializer
    queryset = WorkPlace.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WorkPlaceFilter


class WorkPlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkplaceDetailSerializer
    queryset = WorkPlace.objects.all()
