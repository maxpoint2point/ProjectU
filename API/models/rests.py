from django.db import models
from .alcohols import Alcohol
from .informs import FA, FB
from .workplaces import Workplace
from UTMDriver.connector import Connector
from .queue import Queue


class RestHeader(models.Model):
    """Список документов с остатками"""
    SEND_TO = 'send_to'
    LOADED = 'loaded'
    SEND_AC = 'send_ac'
    ERROR = 'error'

    STATUS_CHOICES = (
        (LOADED, 'Загружены'),
        (SEND_AC, 'Передан в УТМ'),
        (SEND_TO, 'К передаче'),
        (ERROR, 'Ошибка'),
    )

    STOCK = 'stock'
    SHOP = 'shop'

    TYPE = (
        (STOCK, '1 регистр'),
        (SHOP, '2 регистр'),
    )

    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE, verbose_name='Рабочее место')
    request_id = models.CharField('Идентификатор', max_length=36, null=True, blank=True)
    date = models.DateTimeField('Дата из ЕГАИС', null=True, blank=True)
    send_date = models.DateTimeField('Дата отправки', null=True, blank=True)
    type = models.CharField('Тип остатков', max_length=6, choices=TYPE)
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default=SEND_AC)
    message = models.CharField('Сообщение от УТМ', max_length=300, null=True, blank=True, default=None)

    objects = models.Manager()

    def __str__(self):
        return f'{self.workplace} {self.date} ({self.type} [{self.status}])'

    class Meta:
        verbose_name = 'Документ с остатками'
        verbose_name_plural = 'Документы с остатками'

    def save(self, *args, **kwargs):
        if not self.pk:
            utm = Connector(self.workplace.utm_host, self.workplace.utm_port)
            if self.type == self.STOCK:
                try:
                    r = utm.request_document("QueryRests")
                except Exception:
                    r = False
            elif self.type == self.SHOP:
                try:
                    r = utm.request_document("QueryRestsShop_v2")
                except Exception:
                    r = False
            if r:
                self.request_id = r.replyId
                self.status = self.SEND_AC
                d = Queue(
                    reply_id=r.replyId,
                    workplace=self.workplace,
                )
                d.save()
            else:
                self.request_id = None
                self.status = self.ERROR
        super(RestHeader, self).save(*args, **kwargs)


class StockPosition(models.Model):
    """Позиции остатков 1 рег"""
    quantity = models.FloatField('Количество')
    fa = models.ForeignKey(FA, on_delete=models.SET_NULL, null=True, related_name="fa", verbose_name='Справка А')
    fb = models.ForeignKey(FB, on_delete=models.SET_NULL, null=True, related_name='fb', verbose_name='Справка Б')
    alcohol = models.ForeignKey(Alcohol, on_delete=models.SET_NULL, null=True, verbose_name='Алкогольная продукция')
    header = models.ForeignKey(RestHeader, on_delete=models.CASCADE, related_name="restheader_stockposition", verbose_name='Документ')

    def __str__(self):
        return f"{self.alcohol} | {self.quantity}"

    class Meta:
        verbose_name = 'Остатки 1 регистр'
        verbose_name_plural = 'Остатки 1 регистр'


class ShopPosition(models.Model):
    """Позиции остатков 2 рег"""
    quantity = models.FloatField('Количество')
    alcohol = models.ForeignKey(Alcohol, on_delete=models.SET_NULL, null=True, verbose_name='Алкогольная продукция')
    header = models.ForeignKey(RestHeader, on_delete=models.CASCADE, related_name="restheader_shopposition", verbose_name='Запрос')

    def __str__(self):
        return f"{self.alcohol} | {self.quantity}"

    class Meta:
        verbose_name = 'Остатки 2 регистр'
        verbose_name_plural = 'Остатки 2 регистр'
