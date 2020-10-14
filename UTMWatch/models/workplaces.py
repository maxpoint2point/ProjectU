from django.db import models
from .ou import OU
from UTMDriver.connector import Connector


class WorkPlace(models.Model):
    """Рабочие места"""
    name = models.CharField('Имя', max_length=70)
    fsrar = models.CharField('ФСРАР ИД', max_length=12)
    kpp = models.CharField('КПП', max_length=12)
    utm_host = models.CharField('Адрес УТМ', max_length=100)
    utm_port = models.PositiveIntegerField('Порт УТМ', )
    delete_requests = models.BooleanField()
    load_ttn = models.BooleanField()
    disabled = models.BooleanField()
    ou = models.ForeignKey(OU, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} <{self.fsrar}>'

    class Meta:
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'

    def save(self, *args, **kwargs):
        if not self.pk:
            utm = Connector(kwargs['utm_host'], kwargs['utm_port'])
            super(WorkPlace, self).save(*args, *kwargs)
