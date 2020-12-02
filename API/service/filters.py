from django_filters import rest_framework as filters
from API.models import Workplace
from API.models import (
    RestHeader,
)


class WorkPlaceFilter(filters.FilterSet):
    ou = filters.CharFilter(field_name='ou__name')

    class Meta:
        model = Workplace
        fields = ['ou']


class RestsFilter(filters.FilterSet):
    type = filters.CharFilter(field_name='type')

    class Meta:
        model = RestHeader
        fields = ['type']
