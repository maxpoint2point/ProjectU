from UTMWatch.models import RestHeader
from rest_framework import generics
from UTMWatch.serializers import RestHeaderListSerializer, RestHeaderDetailSerializer, RestHeaderCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend

from UTMWatch.service import RestsFilter


class RestListView(generics.ListAPIView):
    serializer_class = RestHeaderListSerializer
    queryset = RestHeader.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RestsFilter


class RestDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = RestHeaderDetailSerializer
    queryset = RestHeader.objects.all()


class RestCreateView(generics.CreateAPIView):
    serializer_class = RestHeaderCreateSerializer
    queryset = RestHeader.objects.all()
