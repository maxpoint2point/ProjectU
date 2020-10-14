from django.db import models
from .ou import OU
from UTMDriver.connector import Connector


class WorkPlace(models.Model):
    """Рабочие места"""
    name = models.CharField('Имя', max_length=70)
    fsrar = models.CharField('ФСРАР ИД', max_length=12, blank=True)
    kpp = models.CharField('КПП', max_length=12, null=True, default=None)
    utm_host = models.CharField('Адрес УТМ', max_length=100)
    utm_port = models.PositiveIntegerField('Порт УТМ', )
    delete_requests = models.BooleanField('Удалять обработанные документы')
    load_ttn = models.BooleanField('Загружать накладные')
    disabled = models.BooleanField('Исключить из автоматической обработки')
    ou = models.ForeignKey(OU, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.name} <{self.fsrar}>'

    class Meta:
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'

    def save(self, *args, **kwargs):
        if not self.pk and not self.fsrar:
            utm = Connector(self.utm_host, self.utm_port)
            self.fsrar = utm.FSRAR
        super(WorkPlace, self).save(*args, **kwargs)
