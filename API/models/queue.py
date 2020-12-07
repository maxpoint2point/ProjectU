from django.db import models
from .workplaces import Workplace


class Queue(models.Model):
    """Исходящие запросы в УТМ"""
    reply_id = models.CharField("Идентификатор", max_length=36)
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE, verbose_name='Рабочее место')
    status = models.BooleanField("Обработан", default=False)
    timestamp = models.DateTimeField('Метка времени', auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.reply_id} <{self.status}>'

    class Meta:
        verbose_name = 'Исходящий запрос'
        verbose_name_plural = 'Исходящие запросы'
