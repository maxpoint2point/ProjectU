from django.db import models
from .producers import Producer


class VCode(models.Model):
    """Виды алкогольной продукции"""
    vcode = models.IntegerField('Код', unique=True)
    name = models.CharField('Название', max_length=200, null=True, default=None, blank=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.name} <{self.vcode}>'

    class Meta:
        verbose_name = 'Вид продукции'
        verbose_name_plural = 'Виды продукции'


class Alcohol(models.Model):
    """Алкогольная продукция"""
    full_name = models.CharField('Полное наименование', max_length=200)
    short_name = models.CharField('Краткое наименование', max_length=200)
    reg_id = models.CharField('Алкокод', max_length=200, unique=True)
    capacity = models.FloatField('Объем', null=True)
    volume = models.FloatField('Крепость')
    v_code = models.ForeignKey(VCode, on_delete=models.CASCADE, verbose_name='Вид алкогольной продукции')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='Производитель')

    objects = models.Manager()

    def __str__(self):
        return f'{self.short_name} <{self.reg_id}>'

    class Meta:
        verbose_name = 'Алкогольная продукция'
        verbose_name_plural = 'Алкогольная продукция'
