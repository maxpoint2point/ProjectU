from django_filters import rest_framework as filters
from UTMWatch.models import Workplace


class WorkPlaceFilter(filters.FilterSet):
    ou = filters.CharFilter(field_name='ou__name')

    class Meta:
        model = Workplace
        fields = ['ou']
