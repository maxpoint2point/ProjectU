from django.db import models
from .workplaces import Workplace


class Queue(models.Model):
    """Исходящие запросы в УТМ"""
    reply_id = models.CharField("Идентификатор", max_length=36)
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)
    status = models.BooleanField("Обработан", default=False)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.reply_id} <{self.status}>'
