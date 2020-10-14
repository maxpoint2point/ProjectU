# Generated by Django 3.1.1 on 2020-10-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTMWatch', '0003_ticket_workplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workplace',
            name='fsrar',
            field=models.CharField(blank=True, max_length=12, verbose_name='ФСРАР ИД'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='kpp',
            field=models.CharField(default=None, max_length=12, null=True, verbose_name='КПП'),
        ),
    ]
