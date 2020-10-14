from django.db import models
from .producers import Producer


class VCode(models.Model):
    """Виды алкогольной продукции"""
    vcode = models.IntegerField(unique=True)
    name = models.CharField(max_length=200, null=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.name} <{self.vcode}>'


class Alcohol(models.Model):
    """Алкогольная продукция"""
    full_name = models.CharField('Полное наименование', max_length=200)
    short_name = models.CharField('Краткое наименование', max_length=200)
    reg_id = models.CharField('Алкокод', max_length=200, unique=True)
    capacity = models.FloatField('Объем', null=True)
    volume = models.FloatField('Крепость')
    v_code = models.ForeignKey(VCode, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.short_name} <{self.reg_id}>'

    class Meta:
        verbose_name = 'Алкогольная продукция'
        verbose_name_plural = 'Алкогольная продукция'
