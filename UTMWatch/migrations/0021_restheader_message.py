# Generated by Django 3.1.3 on 2020-11-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTMWatch', '0020_auto_20201127_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='restheader',
            name='message',
            field=models.CharField(blank=True, default=None, max_length=40, null=True, verbose_name='Сообщение от УТМ'),
        ),
    ]
