# Generated by Django 3.1.3 on 2020-12-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0030_auto_20201208_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workplace',
            name='periodic_task',
        ),
        migrations.AddField(
            model_name='workplace',
            name='request_rest',
            field=models.BooleanField(default=False, verbose_name='Запрашивать остатки автоматически'),
            preserve_default=False,
        ),
    ]
