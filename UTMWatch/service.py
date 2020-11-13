from django_filters import rest_framework as filters
from UTMWatch.models import Workplace
from UTMDriver.connector import Connector
from .models import Queue
from UTMDriver.generic.documents.rests import storeRest
from .models import RestHeader, StockPosition, FA, FB, Alcohol
from django.core.exceptions import ObjectDoesNotExist


class WorkPlaceFilter(filters.FilterSet):
    ou = filters.CharFilter(field_name='ou__name')

    class Meta:
        model = Workplace
        fields = ['ou']


def exchange(host, port):
    utm = Connector(host, port)
    documents = Queue.objects.filter(status=False)
    for document in documents:
        d = utm.getByReplyId(document.reply_id)
        for r in d:
            if type(r) == storeRest.StoreRest:
                header = RestHeader.objects.get(request_id=document.reply_id)
                header.status = RestHeader.LOADED
                header.save()
                for pos in r.Position:
                    fa = FA.get_or_create(pos.StockPositionInformARegId)
                    fb = FB.get_or_create(pos.StockPositionInformBRegId)
                    alcohol = Alcohol.get_or_create(pos)
                    rest = StockPosition(
                        quantity=pos.StockPositionQuantity,
                        fa=fa,
                        fb=fb,
                        header=header,
                        alcohol=alcohol,
                    )
                    rest.save()
                document.status = True
                document.save()
