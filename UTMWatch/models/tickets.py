from django.db import models
from .workplaces import Workplace


class Ticket(models.Model):
    """Тикеты"""
    date = models.DateTimeField()
    identity = models.CharField(max_length=36)
    doc_id = models.CharField(max_length=40)
    doc_type = models.CharField(max_length=40)
    result = models.BooleanField()
    result_date = models.DateTimeField()
    result_comment = models.CharField(max_length=100)
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.result} {self.doc_type}'
