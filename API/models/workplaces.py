import json

from django.db import models
from django_celery_beat.utils import now

from .ou import OU
from UTMDriver.connector import Connector
from django_celery_beat.models import PeriodicTask, PeriodicTasks
from django.db.models import signals


class Workplace(models.Model):
    """Рабочие места"""
    name = models.CharField('Имя', max_length=70)
    fsrar = models.CharField('ФСРАР ИД', max_length=12, blank=True)
    kpp = models.CharField('КПП', max_length=12, null=True, default=None, blank=True)
    utm_host = models.CharField('Адрес УТМ', max_length=100)
    utm_port = models.PositiveIntegerField('Порт УТМ', )
    delete_requests = models.BooleanField('Удалять обработанные документы')
    load_ttn = models.BooleanField('Загружать накладные')
    disabled = models.BooleanField('Исключить из автоматической обработки')
    request_rest = models.BooleanField('Запрашивать остатки автоматически')
    ou = models.ForeignKey(OU, on_delete=models.CASCADE, related_name="workplace_ou", verbose_name='Организация')

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
        super(Workplace, self).save(*args, **kwargs)


class Tasks(PeriodicTask):
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.pk:
            PeriodicTasks.update_changed()
        parameters = {"workplace_id": self.workplace.id}
        self.kwargs = json.dumps(parameters)
        super(PeriodicTask, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Задача по расписанию'
        verbose_name_plural = 'Задачи по расписанию'


signals.pre_delete.connect(PeriodicTasks.changed, sender=PeriodicTask)
signals.pre_save.connect(PeriodicTasks.changed, sender=PeriodicTask)
