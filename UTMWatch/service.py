from django_filters import rest_framework as filters
from UTMWatch.models import WorkPlace


class WorkPlaceFilter(filters.FilterSet):
    ou = filters.CharFilter(field_name='ou__name')

    class Meta:
        model = WorkPlace
        fields = ['ou']
