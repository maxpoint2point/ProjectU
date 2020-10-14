from django.db import models
from .alcohols import Alcohol
from .informs import FA, FB
from .workplaces import WorkPlace


class RestsList(models.Model):
    """Список документов с остатками"""

    LOADED = 'loaded'
    SEND_AC = 'send_ac'
    ERROR = 'error'

    STATUS_CHOICES = (
        (LOADED, 'Загружены'),
        (SEND_AC, 'Передан в УТМ'),
        (ERROR, 'Ошибка'),
    )

    STOCK = 'stock'
    SHOP = 'shop'

    TYPE = (
        (STOCK, '1 регистр'),
        (SHOP, '2 регистр'),
    )

    workplace = models.ForeignKey(WorkPlace, on_delete=models.CASCADE)
    request_id = models.CharField('Идентификатор', max_length=36)
    date = models.DateTimeField()
    type = models.CharField('Тип остатков', max_length=6, choices=TYPE)
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'Документ с остатками'
        verbose_name_plural = 'Документы с остатками'


class RestsStock(models.Model):
    """Позиции остатков 1 рег"""
    quantity = models.PositiveIntegerField()
    fa = models.ForeignKey(FA, on_delete=models.SET_NULL, null=True)
    fb = models.ForeignKey(FB, on_delete=models.SET_NULL, null=True)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.SET_NULL, null=True)
    rest_list = models.ForeignKey(RestsList, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Остатки 1 регистр'
        verbose_name_plural = 'Остатки 1 регистр'


class RestsShop(models.Model):
    """Позиции остатков 2 рег"""
    quantity = models.PositiveIntegerField()
    alcohol = models.ForeignKey(Alcohol, on_delete=models.SET_NULL, null=True)
    rest_list = models.ForeignKey(RestsList, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Остатки 2 регистр'
        verbose_name_plural = 'Остатки 2 регистр'
