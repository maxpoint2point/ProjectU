from django.db import models


class FA(models.Model):
    """Справки по форме А"""
    reg_id = models.CharField(max_length=18, unique=True)

    objects = models.Manager()

    def __str__(self):
        return self.reg_id

    class Meta:
        verbose_name = 'Справка по форме А'
        verbose_name_plural = 'Справок по форме А'


class FB(models.Model):
    """Справки по форме B"""
    reg_id = models.CharField(max_length=18, unique=True)

    objects = models.Manager()

    def __str__(self):
        return self.reg_id

    class Meta:
        verbose_name = 'Справка по форме Б'
        verbose_name_plural = 'Справок по форме Б'
