from UTMWatch.models import RestHeader
from rest_framework import generics
from UTMWatch.serializers import RestHeaderListSerializer, RestHeaderDetailSerializer, RestHeaderCreateSerializer


class RestListView(generics.ListAPIView):
    serializer_class = RestHeaderListSerializer
    queryset = RestHeader.objects.all()


class RestDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestHeaderDetailSerializer
    queryset = RestHeader.objects.all()


class RestCreateView(generics.CreateAPIView):
    serializer_class = RestHeaderCreateSerializer
    queryset = RestHeader.objects.all()
