# Generated by Django 3.1.3 on 2020-11-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTMWatch', '0013_queue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='reply_id',
            field=models.CharField(max_length=36),
        ),
    ]
