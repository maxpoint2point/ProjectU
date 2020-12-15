from rest_framework import generics
from API.models import Tasks
from API.serializers import PeriodicTaskDetailSerializer, PeriodicTaskListSerializer


class PeriodicTaskCreateView(generics.CreateAPIView):
    """Создание переодических задач"""
    serializer_class = PeriodicTaskDetailSerializer
    queryset = Tasks.objects.all()


class PeriodicTaskRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    """Изменение переодических задач"""
    serializer_class = PeriodicTaskDetailSerializer
    queryset = Tasks.objects.all()


class PeriodicTaskListView(generics.ListAPIView):
    serializer_class = PeriodicTaskListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Tasks.objects.filter(workplace__id=pk)
