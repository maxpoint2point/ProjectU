from django.db import models


class OU(models.Model):
    """Организации"""
    inn = models.CharField('ИНН', max_length=12)
    name = models.CharField('Имя', max_length=70)
    disabled = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return f'{self.name} <{self.inn}>'

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
