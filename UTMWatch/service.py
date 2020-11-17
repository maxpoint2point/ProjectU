from django_filters import rest_framework as filters
from UTMWatch.models import Workplace
from UTMDriver.connector import Connector
from .models import Queue
from UTMDriver.generic.documents.rests import storeRest
from .models import RestHeader, StockPosition, FA, FB, Alcohol, VCode, Producer
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
                    rest = StockPosition(
                        quantity=pos.StockPositionQuantity,
                        fa=FA.objects.get_or_create(reg_id=pos.StockPositionInformARegId)[0],
                        fb=FB.objects.get_or_create(reg_id=pos.StockPositionInformBRegId)[0],
                        header=header,
                        alcohol=Alcohol.objects.get_or_create(
                            reg_id=pos.ProductAlcCode,
                            defaults={
                                'full_name': pos.ProductFullName,
                                'short_name': pos.ProductFullName,
                                'capacity': pos.ProductCapacity,
                                'volume': pos.ProductAlcVolume,
                                'v_code': VCode.objects.get_or_create(vcode=pos.ProductVCode)[0],
                                'producer': Producer.objects.get_or_create(
                                    reg_id=pos.ProducerClientRegId,
                                    defaults={
                                        'inn': pos.ProducerINN,
                                        'kpp': pos.ProducerKPP,
                                        'full_name': pos.ProducerFullName,
                                        'short_name': pos.ProducerShortName,
                                        'country': pos.addressCountry,
                                        'region_code': pos.addressRegionCode,
                                        'address': pos.addressDescription,
                                    }
                                )[0],
                            }
                        )[0],
                    )
                    rest.save()
                document.status = True
                document.save()
