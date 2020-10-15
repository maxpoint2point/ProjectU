# Generated by Django 3.1.1 on 2020-10-14 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=12, verbose_name='ИНН')),
                ('name', models.CharField(max_length=70, verbose_name='Имя')),
                ('disabled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Имя')),
                ('fsrar', models.CharField(max_length=12, verbose_name='ФСРАР ИД')),
                ('kpp', models.CharField(max_length=12, verbose_name='КПП')),
                ('utm_host', models.CharField(max_length=100, verbose_name='Адрес УТМ')),
                ('utm_port', models.PositiveIntegerField(verbose_name='Порт УТМ')),
                ('delete_requests', models.BooleanField()),
                ('load_ttn', models.BooleanField()),
                ('disabled', models.BooleanField()),
                ('ou', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UTMWatch.ou')),
            ],
            options={
                'verbose_name': 'Рабочее место',
                'verbose_name_plural': 'Рабочие места',
            },
        ),
    ]
