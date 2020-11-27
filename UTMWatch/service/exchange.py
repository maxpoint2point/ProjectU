from UTMDriver.connector import Connector
from UTMWatch.models import Queue
from UTMDriver.generic.documents.rests import storeRest, shopRest
from UTMDriver.generic.documents.tickets import UTMTickets, EGAISTickets
from UTMWatch.models import (
    RestHeader,
    StockPosition,
    ShopPosition,
    FA,
    FB,
    Alcohol,
    VCode,
    Producer,
)
import logging


# logger = logging.getLogger(__name__)


def store_rests(utm_doc_instance, queue):
    header = RestHeader.objects.get(request_id=queue.reply_id)
    header.status = RestHeader.LOADED
    header.date = utm_doc_instance.RestDate
    header.save()
    for pos in utm_doc_instance.Position:
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
    queue.status = True
    queue.save()
    return True


def shop_rests(utm_doc_instance, queue):
    header = RestHeader.objects.get(request_id=queue.reply_id)
    header.status = RestHeader.LOADED
    header.date = utm_doc_instance.RestDate
    header.save()
    for pos in utm_doc_instance.Position:
        rest = ShopPosition(
            quantity=pos.ShopPositionQuantity,
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
                            'address': pos.addressdescription,
                        }
                    )[0],
                }
            )[0],
        )
        rest.save()
    queue.status = True
    queue.save()


def main_exchange(host, port):
    # logger.debug('Начата загрузка документов из УТМ')
    utm = Connector(host, port)
    for queue in Queue.objects.filter(status=False):
        for utm_doc_instance in utm.getByReplyId(queue.reply_id):
            if type(utm_doc_instance) == storeRest.StoreRest:
                store_rests(utm_doc_instance, queue)
            if type(utm_doc_instance) == shopRest.ShopRest:
                shop_rests(utm_doc_instance, queue)
            if type(utm_doc_instance) == UTMTickets.UTMTicket:
                if utm_doc_instance:
                    pass
                else:
                    if utm_doc_instance.DocType == 'QueryRests' or utm_doc_instance.DocType == 'QueryRestsShop_v2':
                        header = RestHeader.objects.get(request_id=queue.reply_id)
                        header.status = RestHeader.ERROR
                        header.message = utm_doc_instance.Comments
                        header.save()
                        queue.status = True
                        queue.save()
            # if type(utm_doc_instance) == EGAISTickets.EGAISTicket:
            #     pass
    # logger.debug('Загрузка завершена')
