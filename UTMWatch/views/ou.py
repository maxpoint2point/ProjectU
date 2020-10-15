from UTMWatch.models import OU
from rest_framework import generics

from UTMWatch.serializers import OUDetailSerializer, OUListSerializer


class OUCreateView(generics.CreateAPIView):
    serializer_class = OUDetailSerializer
    queryset = OU.objects.all()


class OUDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OUDetailSerializer
    queryset = OU.objects.all()


class OUListView(generics.ListAPIView):
    serializer_class = OUListSerializer
    queryset = OU.objects.all()
