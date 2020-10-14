from django.db import models
from .producers import Producer
from .workplaces import WorkPlace
from .alcohols import Alcohol
from .informs import FA, FB


class WayBillList(models.Model):
    """Список входящих накладных"""

    LOADED = 'loaded'
    SEND_AC = 'send_ac'
    WAIT_AC = 'wait_ac'
    CONFIRM = 'confirm'
    REJECT = 'reject'
    SEND_REJECT = 'send_reject'
    CANCEL = 'cancel'
    ERROR = 'error'

    STATUS = (
        (LOADED, 'Загружена'),
        (SEND_AC, 'К подтверждению (Передан в УТМ)'),
        (WAIT_AC, 'К подтверждению (Ожидание квитанции о проведении)'),
        (CONFIRM, 'Подтверждена'),
        (REJECT, 'Отменена получателем'),
        (SEND_REJECT, 'К отмене'),
        (CANCEL, 'Отменена отправителем'),
        (ERROR, 'Ошибка'),
    )

    identity = models.CharField(max_length=40)
    number = models.CharField(max_length=40)
    date = models.DateTimeField()
    shipping_date = models.DateTimeField()
    shipper = models.ForeignKey(Producer, on_delete=models.CASCADE)
    ttn = models.CharField(max_length=14)
    status = models.CharField(max_length=11, choices=STATUS, default=LOADED)
    comment = models.CharField(max_length=40, null=True)
    workplace = models.ForeignKey(WorkPlace, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Входящая товаро-транспортная накладная'
        verbose_name_plural = 'Входяще товаро-транспортные накладные'


class WayBillData(models.Model):
    """Позиции накладной"""
    identity = models.PositiveIntegerField()
    alcohol = models.ForeignKey(Alcohol, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    fa = models.ForeignKey(FA, on_delete=models.SET_NULL, null=True)
    fb = models.ForeignKey(FB, on_delete=models.SET_NULL, null=True)
    waybill = models.ForeignKey(WayBillList, on_delete=models.CASCADE)


# class NATTNList(models.Model):
#     """Список запросов о не принятых накладных"""
#     requestID = models.ForeignKey(UTMRequestsIN, on_delete=models.CASCADE)
