from UTMWatch.models import WorkPlace, OU
from rest_framework import generics
from .serializers import WorkplaceCreateSerializer, WorkplaceSerializer, OUSerializer


class OUCreateView(generics.CreateAPIView):
    serializer_class = OUSerializer
    queryset = OU.objects.all()


class OUListView(generics.ListAPIView):
    serializer_class = OUSerializer
    queryset = OU.objects.all()


class WorkPlaceCreateView(generics.CreateAPIView):
    serializer_class = WorkplaceCreateSerializer
    queryset = WorkPlace.objects.all()


class WorkPlaceListView(generics.ListAPIView):
    serializer_class = WorkplaceSerializer
    queryset = WorkPlace.objects.all()
