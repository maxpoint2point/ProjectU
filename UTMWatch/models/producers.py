from django.db import models


class Producer(models.Model):
    """Контрагенты"""
    reg_id = models.CharField('ФСРАР ИД', max_length=12)
    inn = models.CharField('ИНН', max_length=12)
    kpp = models.CharField('КПП', max_length=12)
    full_name = models.CharField('Полное наименование', max_length=200)
    short_name = models.CharField('Сокращенное наименование', max_length=100)
    country = models.PositiveIntegerField()
    region_code = models.PositiveIntegerField()
    address = models.CharField('Адрес', max_length=200)

    objects = models.Manager()

    def __str__(self):
        return f'{self.short_name} <{self.reg_id}>'

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
